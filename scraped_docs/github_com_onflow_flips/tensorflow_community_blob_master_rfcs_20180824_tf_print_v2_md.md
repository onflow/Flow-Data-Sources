# Source: https://github.com/tensorflow/community/blob/master/rfcs/20180824-tf-print-v2.md

# New tf.print

Status        | Accepted
:------------ | :---------------------------------
**Author(s)** | Tomer Kaftan (Google)
**Sponsor**   | Asim Shankar (Google)
**Updated**   | 2018-08-24

## Background

Printing is a core component of any language or system. From their first hello
world application to in-depth debugging of complex workloads, developers rely on
printing and logging as some of their most important tools. Unfortunately,
setting up printing of Tensors when building TensorFlow graphs doesn't align
with the natural usage of print primitives most programmers are used to. This
has led to various bugs, questions on online forums, and entire blog posts
explaining tf.Print (e.g.
[blog post 1](https://towardsdatascience.com/using-tf-print-in-tensorflow-aa26e1cff11e),
[blog post 2](http://www.heyuhang.com/blog/2018/01/31/the-secret-of-tf-dot-print-in-tensorflow/),
[Github question](https://github.com/tensorflow/tensorflow/issues/1988),
[Quora question](https://www.quora.com/How-does-the-tf-Print-statement-work-for-TensorFlow),
[Stack Overflow question](https://stackoverflow.com/questions/33633370/how-to-print-the-value-of-a-tensor-object-in-tensorflow),
...). Much of the confusion comes from the existing `tf.Print` operator being an
identity operator with a side effect of printing. This is a very non-standard
API for printing, and the operator graph must be carefully set up to ensure the
operator gets executed. This is at odds with printing/logging users are used to
from elsewhere, where a print method produces no outputs and immediately prints
the desired value.

Eager execution promises a more interactive, easier to debug experience that
works with Python's `print` method. However, even with eager execution enabled,
there is need to wrap parts of execution and optimized graph functions
(currently `tf.contrib.eager.defun`). The Python `print` method placed in these
graph function will run at graph construction time, not graph execution time,
creating confusion.

This doc proposes a new `tf.print` TensorFlow printing approach that is very
similar to the standard python `print` API whether or not executing eagerly. It
also provides long-requested functionality for both eager and session-based
execution, such as a more meaningful Tensor summarization, support for printing
nested data structures that contain tensors, and controllable logging levels.

## Overview

We introduce two methods to the public Python API: `tf.strings.format` and
`tf.print`. (We may have to use `tf.strings.Format` or `tf.strings.fmt` instead
of `tf.strings.format` if the built-in python `format` method causes issues with
the naming.) These are internally backed by two C++ operators: `StringFormat`
and `PrintV2`. The method headers & docstrings are as follows:

### Python Public API Methods

````python
@tf_export("print")
def print_v2(*inputs, **kwargs):
  """Print the specified inputs.
  Returns an operator that prints the specified inputs to a desired
  output stream or logging level. The inputs may be dense or sparse Tensors,
  primitive python objects, data structures that contain Tensors, and printable
  python objects. Printed tensors will recursively show the first and last
  `summarize` elements of each dimension.

  With eager execution enabled and/or inside a `tf.contrib.eager.defun` this
  operator will automatically execute, and users only need to call `tf.print`
  without using the return value. When constructing graphs outside of a
  `tf.contrib.eager.defun`, one must either include the returned op
  in the input to `session.run`, or use the operator as a control dependency for
  executed ops by specifying `with tf.control_dependencies([print_op])`.

  @compatibility(python2)
  In python 2.7, make sure to import the following:
  `from __future__ import print_function`
  @end_compatibility

  Example:
    Single-input usage:
    ```python
    tf.enable_eager_execution()
    tensor = tf.range(10)
    tf.print(tensor, output_stream=sys.stderr)
    ```
    (This prints "[0 1 2 ... 7 8 9]" to sys.stderr)

    Multi-input usage:
    ```python
    tf.enable_eager_execution()
    tensor = tf.range(10)
    tf.print("tensors:", tensor, {2: tensor * 2}, output_stream=sys.stdout)
    ```
    (This prints "tensors: [0 1 2 ... 7 8 9] {2: [0 2 4 ... 14 16 18]}" to sys.stdout)

    Usage when constructing graphs:
    ```python
    sess = tf.Session()
    with sess.as_default():
        tensor = tf.range(10)
        print_op = tf.print("tensors:", tensor, {2: tensor * 2},
                            output_stream=sys.stdout)
        with tf.control_dependencies([print_op]):
          doubled_tensor = tensor * 2
        sess.run(doubled_tensor)

    ```
    (This prints "tensors: [0 1 2 ... 7 8 9] {2: [0 2 4 ... 14 16 18]}" to
    sys.stdout)

  Note: This op is only partially compatible with Jupyter notebooks and colabs.
    Because it prints to the C++ standard out / standard error, this will go
    in the notebook kernel's console output, not in the notebook cell output.

  Args:
    *inputs: Positional arguments that are the inputs to print. Inputs in the
      printed output will be separated by spaces. Inputs may be python
      primitives, tensors, data structures such as dicts and lists that
      may contain tensors (with the data structures possibly nested in
      arbitrary ways), and printable python objects.

    output_stream: The output stream or logging level to print to. Defaults to
      sys.stderr, but sys.stdout, tf.logging.info, tf.logging.warning,
      tf.logging.error, and tf.logging.fatal are also supported.

    summarize: The first and last `summarize` elements within each dimension are
      recursively printed per Tensor. If None, then the first 3 and last 3
      elements of each dimension are printed for each tensor. If set to -1, it
      will print all elements of every tensor.

    name: A name for the operation (optional).

  Returns:
    A print operator that prints the specified inputs in the specified output
    stream or logging level.

  Raises:
    ValueError: If an unsupported output stream is specified.
  """
````

````python
@tf_export("strings.format")
def string_format(template, inputs, placeholder="{}", summarize=3, name=None):
  r"""Formats a string template using a list of tensors.
  Formats a string template using a list of tensors, abbreviating tensors by
  only printing the first and last `summarize` elements of each dimension
  (recursively). If formatting only one tensor into a template, the tensor does
  not have to be wrapped in a list.

  Example:
    Formatting a single-tensor template:
    ```python
    sess = tf.Session()
    with sess.as_default():
        tensor = tf.range(10)
        formatted = tf.strings.format("tensor: %s, suffix", tensor)
        out = sess.run(formatted)
        expected = "tensor: [0 1 2 ... 7 8 9], suffix"
        assert(out.decode() == expected)
    ```

    Formatting a multi-tensor template:
    ```python
    sess = tf.Session()
    with sess.as_default():
        tensor_one = tf.reshape(tf.range(100), [10, 10])
        tensor_two = tf.range(10)
        formatted = tf.strings.format("first: %s, second: %s, suffix",
          (tensor_one, tensor_two))

        out = sess.run(formatted)
        expected = ("first: [[0 1 2 ... 7 8 9]\n"
              " [10 11 12 ... 17 18 19]\n"
              " [20 21 22 ... 27 28 29]\n"
              " ...\n"
              " [70 71 72 ... 77 78 79]\n"
              " [80 81 82 ... 87 88 89]\n"
              " [90 91 92 ... 97 98 99]], second: [0 1 2 ... 7 8 9], suffix")
        assert(out.decode() == expected)
    ```

  Args:
    template: A string template to format tensor values into.

    inputs: A list of `Tensor` objects, or a single Tensor.
      The list of tensors to format into the template string. If a solitary
      tensor is passed in, the input tensor will automatically be wrapped as a
      list.

    placeholder: An optional `string`. Defaults to `"{}"`.
      At each placeholder occurring in the template, a subsequent tensor
      will be inserted.

    summarize: An optional `int`. Defaults to `3`.
      When formatting the tensors, show the first and last `summarize`
      entries of each tensor dimension (recursively). If set to -1, all
      elements of the tensor will be shown.

    name: A name for the operation (optional).

  Returns:
    A scalar `Tensor` of type `string`.

  Raises:
    ValueError: if the number of placeholders does not match the number of
      inputs.
  """
````

### C++ Ops & Implementation Overview

These two python methods are backed by two new C++ operators: `StringFormat` and
`PrintV2`.

StringFormat takes a template string attr, a placeholder string attr, a list of
tensor inputs, and nicely formats the tensor summarizations inside of the
template string where the placeholders are. It outputs a string scalar tensor.

```
REGISTER_OP("StringFormat")
    .Input("inputs: T")
    .Output("output: string")
    .Attr("T: list(type) >= 0")
    .Attr("template: string = '%s'")
    .Attr("placeholder: string = '%s'")
    .Attr("summarize: int = 3")
    .SetShapeFn(...)
```

PrintV2 takes an input string scalar tensor, and a string constant specifying an
output stream/logging level, and produces no outputs. When it executes, it
prints the string scalar to the specified output stream / logging level. It is
marked as stateful to ensure it gets executed in graph functions without being
pruned, and to ensure prints get executed in program order in eager mode and
graph functions.

```
REGISTER_OP("PrintV2")
    .Input("input: string")
    .SetIsStateful()
    .Attr("output_stream: string")
    .SetShapeFn(...)
```

The `tf.strings.format` method calls directly into the StringFormat operator
with a bit of extra syntactic sugar to wrap a single tensor input as a list
automatically.

The `tf.print` method maps python logging level strings or logging methods or
standard out/err streams to the appropriate output stream string constant. If
there is only one string scalar tensor as the input, it directly calls into
`PrintV2`. Otherwise, it:

1.  Uses the TensorFlow `nest` utilities to build a placeholder-less template
    for the inputs to print and to extract a flattened list of tensors.
    *   Also detects sparse tensors and extracts their components / sets up the
        template appropriately
1.  Generates a placeholder that won't conflict with the template
1.  Rebuilds the template with the placeholder inserted where the tensors should
    go
1.  Creates a StringFormat op to convert the tensor inputs into an appropriate
    string scalar
1.  Passes the output of the StringFormat op to a PrintV2 op (that it returns).

## Major Design alternatives:

### Device Locations

The location at which tensors actually get printed (& where formatting of large
tensors happens) plays a major role in the user experience.

In the current approach, printing and formatting will happen on whatever machine
is currently specified in the device scope when entering `tf.print` /
`tf.strings.format`.

UPDATE: Following the design review we have decided to *not* specify cpu:0 by default.
Outdated: Because the new operators only have C++ kernels, we nest
`with tf.device('/CPU:0'):` inside of `tf.print` and `tf.strings.format` to
avoid crashes when the device scope is referring to a non-CPU device.


Alternatives to this are:

*   Don't automatically specify cpu:0 for tf.print and tf.strings.format
    *   This provides full user control over devices & which cpu device prints
        (if they want different cpu devices to be printing different things).
    *   Will cause potentially hard-to-interpret errors if users try printing in
        non-cpu device scopes as-is (w/o explicitly changing the device scope
        before printing).
*   Automatically specify a client device for print & format according to
    context parameters
    *   Users may want all printing & logging to happen on a single client
        device, without having to muck with device scopes around each `tf.print`
        call.
    *   This would most closely match behavior programmers are used to with
        printing & logging
    *   Lowers user flexibility if they want printing to happen on other devices
    *   Would somehow have to either automatically detect the client device, or
        require users to specify it in configuration when starting TensorFlow
        (which increases the required user effort).
*   Wrap each input tensor to print in a separate `tf.strings.format` before
    formatting tensors into the main template, then co-locate the formatting
    device locations w/ the tensors.
    *   This would add extra formatting ops to execute, but it would have the
        benefit of never transferring tensors over the network to print. It
        would only ever transfer formatted strings.
    *   This would still have to force a cpu:0 device for formatting ops, just
        on the worker machines that the tensors appear on
    *   If there are risky subtleties to ops.colocate_with and ops.device, they
        could pose issues w/ this approach.

### Functionality to Operator Breakdown

We use two public python methods and two C++ ops (StringFormat & PrintV2). Some
alternatives to how we break down this functionality are:

*   Use a single c++ op / a single public api method for both formatting and
    printing
    *   However, it's good to have a separation of functionality, and having one
        op would cause issues if users want to format colocated with a giant
        tensor, and print on a different machine.
*   In the StringFormat op do not take a template and only format one tensor
    nicely. Then, make tf.print build a separate format op for each extracted
    input tensor, and construct the final printed string using a TensorFlow
    string join/concat operator.
    *   This would encourage writing the `tf.print` op in a way that co-locates
        tensor formatting with the tensor locations. (not necessary for doing
        that though)
    *   However, it may be nice for users to be able to format using explicit
        string templates instead of having to rely on the print method.
*   Allow the tf.strings.format python method to support formatting python
    objects & data structures (that may contain tensors) as opposed to just
    formatting tensors. tf.print would then feed almost straight into
    tf.strings.format.
    *   This would move a lot of the complexity into the tf.strings.format
        method, and force the format method to have to re-generate a different
        template for the StringFormat op than the user-input template. (seems
        somewhat unnatural).

### Update legacy `tf.Print` or Not

We are specifically choosing to make no changes to the legacy `tf.Print`, and to
deprecate it for removal in TF 2.0. Although we could apply some of this
improved functionality to `tf.Print` (or even make `tf.Print` call into the new
print/format operators), it comes with many backwards & compatibility concerns.
This is especially the case if people were already relying on the exact print
format of `tf.Print`. We also want to encourage people to move over to the
newer, more natural print methods, so that we don't have to maintain two going
forward.

## Caveats & Open User Experience Risks

1.  To use the lower-case name `tf.print` in python 2.7, users have to import
    `from __future__ import print_function`
    *   Because Python 2 is on the way out, this might not be a major issue.
    *   Alternatively, we could provide an additional python2-safe alias.
1.  Relative order of prints will not be guaranteed inside of session-based
    graph mode (Ordering should be correct during eager execution / inside
    `tf.contrib.eager.defun` graph functions).
    *   When session-based graphs are compiled/executed, execution order may be
        changed / is not guaranteed
1.  When using the various logging levels, the logged line will capture the
    PrintV2 Op Kernel call-site in the C++ code, not the python line at which
    `tf.print` actually appeared.
    *   We could solve this by capturing the python call-site in the `tf.print`
        when the various `tf.logging` streams are used, and include it as part
        of the template passed to the format string.
1.  In Colab/Jupyter notebooks, printing to the C++/OS standard out & standard
    error goes to the notebook kernel's console output, not the notebook cell
    output. (This is an issue w/ the legacy tf.Print as well)
    *   This is a known issue with python notebooks.
    *   Requires complex capturing logic to send output to notebook cells, and
        the solutions are often not totally portable across operating systems /
        C++ runtimes.
    *   If we want to do something about this, a possible approach could be to
        have the PrintV2 kernel execute a python print if we detect a
        jupyter/colab notebook environment and that the current device has a
        python runtime, rather than using the C++ logging/printing methods.
    *   Alternatively, we could provide utilities to capture the C++
        stdout/stderr in Jupyter notebook outputs as a part of TensorFlow.
    *   We would have to be very careful w/ device placement in distributed
        multi-machine/multi-device settings to ensure that the print device is
        the notebook kernel CPU.
1.  Users might get too comfortable w/ support for python data structure
    printing, then run into various nest utility quirks like OrderedDicts being
    re-ordered, or tensors not being extracted correctly from sets. (See
    Supported Input Types in Extra Details for more info)
1.  In graph functions & session-based run mode the python values printed won't
    change w/ subsequent executions of that PrintV2 (See Supported Input Types
    in Extra Details for more info)
1.  Because printing & formatting follows the current device context, printing
    may happen on a different machine than users intend, and then they have a
    hard time finding the printed data. Or, it may unintentionally transfer a
    large tensor over the network before formatting it.
    *   Developers may be more inclined to have printing/logging happening in
        their client as opposed to on various machines in a distributed system.
1.  To format & print on different devices, users must explicitly call both
    `tf.strings.format` and `tf.print`
1.  Someone using normal python print in eager mode python notebooks or repl
    might get used to it working, and not realize that there's a separate
    `tf.print`. They may then try using the standard python `print` in a Graph Function and have their
    printing not work. Alternatively, in a colab they might switch to tf.print then suddenly be
    confused why nothing is printing.
    *   It may make sense for eager graph functions to automatically hook the
        python print method to replace it with calls to `tf.Print`. This would
        still be problematic in python notebooks though (for above reasons).
1.  Various user code could still end up calling EagerTensor `__str__`
    unintentionally, which calls .numpy() on the tensor then prints it. This
    will copy the full tensor over then format it w/ numpy, which will have
    similar but slightly mismatched formatting from tf.print.
    *   For consistency, maybe make `__str__` and `__repr__` in EagerTensors use
        the tf.strings.format op on whatever device the tensor is on? This could
        avoid transferring giant tensors over the network unintentionally.
1.  The `tf.print` functionality to deal w/ arbitrary nested structures will be
    python-specific. Other language bindings will have to manually chain format
    & print.

## Extra Details

### Supported Input Types

Any Python object can be passed as input to `tf.print`, and it will be printed.

Tensors will automatically be extracted from python lists, dicts, and other data
structures supported by the TensorFlow `nest` utilities. These extracted tensors
will print with their summarization format whenever `tf.print` executes.
TensorFlow variables also work correctly inside of `tf.print` (even when nested
inside data structures).

However, there are the following caveats!

*   In session mode and inside graph functions (and possibly in eager loops as
    well), the printed value of non-tensor python objects will always match what
    it was the very first time that a given `tf.print` is executed. It will not
    update when that specific `tf.print` is called again.
*   The TensorFlow nest utilities do not support *all* standard python data
    structures. For example, tensors nested inside of python sets will not be
    properly and their values will not be shown/formatted when the `tf.print`
    kernels run.
*   Tensors also can't be extracted from arbitrary python objects, even ones
    that define a __str__ or __repr__ method that tries to print the contained
    tensor with the normal python `str`/`print` methods.

### Summarization Format

The strategy StringFormat uses to format tensors is heavily inspired by numpy.
The first and last `summarize` entries in each tensor dimension will recursively
be printed, separated by a separator string (in this case `...`).

Each dimension is bordered by open and close square brackets `[` and `]`. The
inner-most dimension will separate entries using just spaces, and other
dimensions will separate entries using new-lines (with the number of new-lines
matching the number of nested dimensions the current dimension has). Spaces will
be used to match indentation after new-lines.

Example of how a 2d tensor may be printed:

```
[[0 1 2 ... 7 8 9]
 [10 11 12 ... 17 18 19]
 [20 21 22 ... 27 28 29]
 ...
 [70 71 72 ... 77 78 79]
 [80 81 82 ... 87 88 89]
 [90 91 92 ... 97 98 99]]

```

Example of how a 3d tensor may be printed:

```
[[[0 1]
  [2 3]]

 [[4 5]
  [6 7]]]
```

### Sparse Tensor Printing

The `tf.print` method will detect when SparseTensors are provided as inputs or
are nested inside of lists/dicts, and convert them to the template
appropriately. The following is an eager example:

```
ind = [[0, 0], [1, 0], [1, 3], [4, 1], [1, 4], [3, 2], [3, 3]]
val = [0, 10, 13, 4, 14, 32, 33]
shape = [5, 6]
sparse = tf.SparseTensor(
    tf.constant(ind, dtypes.int64),
    tf.constant(val, dtypes.int64),
    tf.constant(shape, dtypes.int64))

tf.print(sparse)
```

This will print:

```
SparseTensor(indices=[[0 0]
 [1 0]
 [1 3]
 ...
 [1 4]
 [3 2]
 [3 3]], values=[0 10 13 ... 14 32 33], shape=[5 6])
```

### Output Streams & Logging Levels

The output streams passed into `tf.print` are converted to string constants
supported by the C++ PrintV2 op as follows:

```python
{
      sys.stdout: "stdout",
      sys.stderr: "stderr",
      tf.logging.INFO: "log(info)",
      tf.logging.info: "log(info)",
      tf.logging.WARN: "log(warning)",
      tf.logging.warning: "log(warning)",
      tf.logging.warn: "log(warning)",
      tf.logging.ERROR: "log(error)",
      tf.logging.error: "log(error)",
      tf.logging.FATAL: "log(fatal)",
      tf.logging.fatal: "log(fatal)",
  }

```

### Device Locations

The new C++ operators only have CPU kernels. So, `tf.print` and
`tf.strings.format` will place the operators wherever the current device scope
is set to, but also nesting `with tf.device('/CPU:0'):` inside of the scope.
This leaves it on the current specified device machine/worker, but avoids
crashes when the device context is a non-CPU device such as a GPU. It may cause
issues if users want to print on different CPU devices, or if the current worker
machine has no available CPUs.

## Minor Design Alternatives / Possible Extra Features

*   Print to single line (as opposed to multi-line output), or make it
    configurable
*   Make print a context manager for extra syntactic sugar in session-based
    graph mode.
*   Change the default output stream / logging level choices
*   Support writing to arbitrary file descriptors?
*   Don't have defaults for template or placeholder for the c++ StringFormat op
*   Support a debug flag to include shape & device & type in the printed format
*   In format op: make template and placeholder inputs as opposed to attributes
*   In format op: Support more complex absl-type templates (e.g. positional
    substitutes)

