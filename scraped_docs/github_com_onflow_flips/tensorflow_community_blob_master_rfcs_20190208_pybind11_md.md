# Source: https://github.com/tensorflow/community/blob/master/rfcs/20190208-pybind11.md

# Replace SWIG with pybind11

| Status        | Accepted                                             |
:-------------- |:---------------------------------------------------- |
| **Author**    | amitpatankar@google.com                              |
| **Sponsor**   | wicke@google.com, gunan@google.com, jkline@google.com|
| **Updated**   | 2019-02-09                                           |



## Objective

[SWIG](http://www.swig.org/tutorial.html) is an interface compiler that connects code written in C++ with our Python API. Currently we are using SWIG across all of TensorFlow. We would like to deprecate SWIG and transition over to using pybind11. 

This document describes a system to improve:

1.  code readability
2.  build times
3.  binary size
4.  performance of the Python API


## Motivation


### What is pybind11?

[Pybind11](https://github.com/pybind/pybind11) is a header-only library that exposes C++ functions and classes to Python to create Python bindings of existing C++ code. Pybind11 is lightweight, and unlike other libraries that serve a similar purpose, it is purely focussed on binding. Pybind11 is relatively new, but is rapidly growing in contributors and adopters. It's an adaptation of [Boost.Python](https://www.boost.org/doc/libs/1_66_0/libs/python/doc/html/index.html) which is quite reputable, but has a lot of extra libraries. Pybind11 is basically the only the binding generation portions of Boost.Python.


### Cons with SWIG

1. SWIG auto-generated code is not optimal for performance.
2.  SWIG needs the swig toolchain.
3.  SWIG requires .i or .swig files which require knowledge of SWIG directives.
    1.  We've changed .swig to .i files to get around readability issues
4.  SWIG combined with C++ is relatively complicated to understand.


### Why not CLIF?

1.  The CLIF wrapping directives are more complex [[Link](https://github.com/google/clif/blob/master/clif/python/README.md#api-specification-language)]
  1.  Need a separate .cliff file
    2.  Similar to SWIG, adds a toolchain dependency beyond just the C++ compiler (and adds another dependency on a different subset of LLVM)
2.  Most literature is optimized for cmake as opposed to bazel
3.  Fewer developers and adopters in open source
    1.  [No activity](https://github.com/google/clif) for nearly a year


### Pro/Cons with pybind11


| Pros: | Cons: |
|-------|-------|
| No need to link against any additional libraries|Less support|
|Function signatures are precomputed at compile time which leads to smaller binaries|Our cases may be more complicated than their examples|
|No auto-generated code|Heavy reliance on another third party library|
|Much simpler and easier to debug||


## Design Proposal

We should deprecate SWIG and replace the wrapper with pybind11. It would be impractical to create a single cl where we transfer everything so we will do a transition in place. Each [.i file](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/tensorflow.i) is a swig file that has directives to wrap and export various C++ classes and functions. There are 60 files across all of TensorFlow. On average there are roughly 20 symbols per file. We can do a rolling transition where we export certain files twice. We can export some symbols with SWIG and the remaining ones with pybind. 


### Impact

We can get rid of roughly 60 bloated SWIG files by transitioning to pybind11. We can also make documentation and exporting functions much easier. We can save countless hours on adding classes and ops by making exporting them to Python extremely easy. 

1.  Faster build times by decreasing code generation and simply exposing the code directly.
2.  Faster performance by removing the dependence on inefficient auto generated code.
3.  Simpler documentation and API exposure without the reliance on complicated SWIG directives.


### Rollout

We can start with low hanging fruit first. The utils file in [util.cc](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/util/util.cc) and it's corresponding [SWIG file](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/util/util.i) has a bunch of methods we can transition. We plan to roll out a few methods in a cl rather than an entire SWIG file at a time. We have the ability to keep SWIG and pybind together and export different sets of functions from one C++ file. As soon as a swig file is empty we can completely remove it. 


## Detailed Design

### TensorFlow specific example

**_Note: The following source code assumes a familiarity with pybind11. To freshen up please refer to the following [example](https://github.com/av8ramit/pybind_example)._**

**The following example will export a couple of functions from util.cc to nest.py using a pywrap_utils shared object.**

Right now a lot of functions are exposed from C++ using swig. Here is a quick example. The isSequence function is implemented in [util.cc](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/util/util.cc#L789).


```
bool IsSequence(PyObject* o) { return IsSequenceHelper(o) == 1; }
```


We add the pybind export. I've decided to rename the extension to `pywrap_utils_internal` for now.


```
bool IsSequence(PyObject* o) { return IsSequenceHelper(o) == 1; }
PYBIND11_MODULE(pywrap_utils_internal, m) {
  m.doc() = R"pbdoc(
    pywrap_utils_internal
    -----
       IsSequence
  )pbdoc";
  m.def("IsSequence",
    [](py::handle& o) {
      bool output = IsSequence(o.ptr());
      if (PyErr_Occurred()) { throw py::error_already_set(); }
      return output;
    }, R"pbdoc(
      Returns a true if its input is a collections.Sequence (except strings).
      
      Args:
        seq: an input sequence.

      Returns:
        True if the sequence is a not a string and is a collections.Sequence or a
        dict.
    )pbdoc");
}
```


Comment out the method extension in the SWIG file.


```
// %feature("docstring") tensorflow::swig::IsSequence
// """Returns a true if its input is a collections.Sequence (except strings).
//
// Args:
//  seq: an input sequence.
//
// Returns:
//  True if the sequence is a not a string and is a collections.Sequence or a
//  dict.
// """
// %unignore tensorflow::swig::IsSequence;
// %noexception tensorflow::swig::IsSequence;
```

Create a corresponding pybind extension. We keep the original SWIG extension since other functions and classes may use it.

```
tf_pybind_extension(
    name = "pywrap_utils_internal",
    srcs = ["util/util.cc"],
    hdrs = ["util/util.h"],
    copts = [
        "-fexceptions",
        "-fno-strict-aliasing",
    ],
    features = ["-use_header_modules"],
    module_name = "pywrap_utils_internal",
    deps = [
        ":safe_ptr",
        "//third_party/absl/memory",
        "//third_party/pybind11",
        "//third_party/python_runtime:headers",
        "//third_party/tensorflow/core:core_cpu_impl",
        "//third_party/tensorflow/core:framework_internal_impl",
        "//third_party/tensorflow/core:gpu_runtime_impl",
        "//third_party/tensorflow/core:lib",
        "//third_party/tensorflow/core:lib_internal",
        "//third_party/tensorflow/core:lib_internal_impl",
        "//third_party/tensorflow/core/grappler/optimizers:custom_graph_optimizer_registry_
        impl",
        "//third_party/tensorflow/stream_executor:stream_executor_impl",
    ] + tf_additional_binary_deps(),
)

py_library(
    name = "util",
    ...
)
```


Create a corresponding pybind extension. We keep the original SWIG extension since other functions and classes may use it.

### Open Sourcing

Pybind11 is already included in the monolithic repo and we can follow corresponding examples to migrate this to open source. We do not need to install anything on the VMs like we do with SWIG. We just need to add the corresponding bazel workspace dependency.

With bazel you have to create another rule in [tensorflow.bzl](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/tensorflow.bzl) that uses [cc_binary](https://docs.bazel.build/versions/master/be/c-cpp.html#cc_binary).


```
def tf_pybind_extension_opensource(
        name,
        srcs,
        hdrs,
        module_name,
        features = [],
        srcs_version = "PY2AND3",
        data = [],
        copts = None,
        nocopts = None,
        linkopts = [],
        deps = [],
        visibility = None,
        testonly = None,
        licenses = None,
        compatible_with = None,
        restricted_to = None,
        deprecation = None):
    """Builds a Python extension module."""
    _ignore = [module_name]
    p = name.rfind("/")
    if p == -1:
        sname = name
        prefix = ""
    else:
        sname = name[p + 1:]
        prefix = name[:p + 1]
    so_file = "%s%s.so" % (prefix, sname)
    pyd_file = "%s%s.pyd" % (prefix, sname)
    symbol = "init%s" % sname
    symbol2 = "init_%s" % sname
    symbol3 = "PyInit_%s" % sname
    exported_symbols_file = "%s-exported-symbols.lds" % name
    version_script_file = "%s-version-script.lds" % name
    native.genrule(
        name = name + "_exported_symbols",
        outs = [exported_symbols_file],
        cmd = "echo '%s\n%s\n%s' >$@" % (symbol, symbol2, symbol3),
        output_licenses = ["unencumbered"],
        visibility = ["//visibility:private"],
        testonly = testonly,
    )

    native.genrule(
        name = name + "_version_script",
        outs = [version_script_file],
        cmd = "echo '{global:\n %s;\n %s;\n %s;\n local: *;};' >$@" % (symbol, symbol2, symbol3),
        output_licenses = ["unencumbered"],
        visibility = ["//visibility:private"],
        testonly = testonly,
    )
    native.cc_binary(
        name = so_file,
        srcs = srcs + hdrs,
        data = data,
        copts = copts,
        nocopts = nocopts,
        linkopts = linkopts + select({
            "@org_tensorflow//tensorflow:windows": [],
            "@org_tensorflow//tensorflow:darwin": [
                "-Wl,-exported_symbols_list",
                exported_symbols_file,
            ],
            "//conditions:default": [
                "-Wl,--version-script",
                "$(location %s)" % version_script_file,
            ],
        }),
        deps = deps + [
            exported_symbols_file,
            version_script_file,
        ],
        features = features,
        linkshared = 1,
        testonly = testonly,
        licenses = licenses,
        visibility = visibility,
        deprecation = deprecation,
        restricted_to = restricted_to,
        compatible_with = compatible_with,
    )
    native.genrule(
        name = name + "_pyd_copy",
        srcs = [so_file],
        outs = [pyd_file],
        cmd = "cp $< $@",
        output_to_bindir = True,
        visibility = visibility,
        deprecation = deprecation,
        restricted_to = restricted_to,
        compatible_with = compatible_with,
    )
    native.py_library(
        name = name,
        data = select({
            "@org_tensorflow//tensorflow:windows": [pyd_file],
            "//conditions:default": [so_file],
        }),
        srcs_version = srcs_version,
        licenses = licenses,
        testonly = testonly,
        visibility = visibility,
        deprecation = deprecation,
        restricted_to = restricted_to,
        compatible_with = compatible_with,
    )
```

### Issues



1.  PyObject pointers are not inherent to pybind11 and require some minor code modification. [[GitHub Issue Link](https://github.com/pybind/pybind11/issues/1201#issue-278504106)]. As you notice in diagram 2 of the rollout we have to create a small wrapper function around the function. Pybind11 cannot cast a python object to `PyObject*` so you need to provide a `pybind11::handle` reference and cast it internally. We could potentially modify the IsSequence function directly, but that would require additional unnecessary modification in the .cc file. 
2.  Complicated use cases where we export weird classes are not properly documented or seen before. We unfortunately don't know what we don't know when it comes to our migrations. [Other users](https://community.lsst.org/t/using-pybind11-instead-of-swig-to-wrap-c-code/1096) have also complained about the more complicated use cases.
3.  For new ops moving forward should we ask the authors to adopt pybind11 already or SWIG?
    1.  **Tentative plan:** If someone uses SWIG we will have to catch up. The plan is to start by transitioning a few different examples at a time by myself. A class, a method, an attribute, etc. Then afterwards we can write documentation and announce the official start to stop using SWIG when writing new C++ Python-wrapped code. Pybind11 is difficult for some of our more complicated use cases, so I will need to become an expert quite rapidly to field questions.


### Bazel Issues

1.  cc_library does not work easily with bazel. [[GitHub Issue](https://github.com/bazelbuild/bazel/issues/701)]
2.  The bazel workaround for getting through this is to use the cc_binary rule instead and use shared objects.


## Simple sample implementation


### Opensource with bazel

Please see the following [GitHub repository](https://github.com/av8ramit/pybind_example) I've created for an example case where we export a simple math module from C++ to Python using pybind11.


## Work Estimates
This transition is going to take roughly a year to migrate all 60 SWIG files. We can fully deprecate SWIG **by the end of Q1 2020**. 

_Note: Once again we don't know what we don't know. There are hairy edge cases that might affect our transition times._

