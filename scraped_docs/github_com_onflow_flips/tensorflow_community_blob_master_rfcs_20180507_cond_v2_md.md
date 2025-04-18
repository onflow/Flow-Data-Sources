# Source: https://github.com/tensorflow/community/blob/master/rfcs/20180507-cond-v2.md

# **"Functional"** **cond design doc**

| Status        | Approved       |
:-------------- |:---------------------------------------------------- |
| **Author(s)** | Skye Wanderman-Milne (skyewm@gmail.com)  |
| **Created**   | 2018-05-07                                           |
| **Updated**   | 2019-02-26                                           |
| **Implementation** | [cond_v2.py](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/ops/cond_v2.py) |

## Objective

**Switch tf.cond to emit a single If op.**

Benefits:
* Higher-order derivatives
* Better XLA/TPU integration
* Better error messages
* Fewer bugs

Note that cond will still support side-effecting ops (e.g. variable updates).


## Background material

Related tf.while_loop RFC: https://github.com/tensorflow/community/blob/master/rfcs/20180821-differentiable-functional-while.md

tf.cond API: https://www.tensorflow.org/api_docs/python/tf/cond

If op: https://github.com/tensorflow/tensorflow/blob/master/tensorflow/core/ops/functional_ops.cc#L104

Overview of current control flow implementation: [Implementation of Control Flow in TensorFlow](http://download.tensorflow.org/paper/white_paper_tf_control_flow_implementation_2017_11_1.pdf)


## Design overview


### Functional tf.cond

The signature of `tf.cond` will stay the same: boolean predicate Tensor, and Python callables for the two branches. The two callables each take no arguments (they instead close over any input tensors), and are required to return the same number and type of tensors.

We need to convert this to the If op signature, which is a boolean predicate, and FunctionDefs for the two branches. The FunctionDefs are required to have the same number and type of inputs and outputs. Luckily, tf.function already gives us the machinery to convert the Python callables into FunctionDefs, including converting closures to inputs and adding extra inputs to make the branch signatures match. This is done via an overloaded Graph subclass, [FuncGraph](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/framework/func_graph.py#L117), which gives us the full flexibility of graphs while creating the branch functions.

This conversion results in a single If op representing the `tf.cond`.


### Gradients

The gradient of an If op is another If op. The predicate is the same as the forward op's, and each branch function is the gradient function of the corresponding forward branch.

This requires the gradient branch functions to access intermediate tensors of the forward branch functions. Internal tensors in a function can't be directly accessed, so we need to add the necessary intermediates as outputs to the forward If op (how to do this is discussed in the "Implementation challenges" section).


### Execution

There are two choices for running the resulting If ops:



1.  Use the `IfOp` kernel as-is, which runs the functions using `FunctionLibraryRuntime`.
1.  "Lower" the If ops to the current `tf.cond` implementation (i.e. `Switch` and `Merge` nodes).

(1) is simpler at a high level, but (2) will avoid some of the implementation challenges below.

The lowering can be implemented as an early (pre-placement) optimization pass, in order for the lowered control flow to be placed, pruned, partitioned, etc. as usual. There are already a few examples of similar passes: ParallelConcatRemovePass, AccumulateNV2RemovePass

**Update**: this is done: [LowerIfOpPass](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/core/common_runtime/lower_if_op.h)

We don't want to lower If ops that will eventually be consumed by the [XLA encapsulation pass](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/compiler/jit/jit_compilation_pass_registration.cc#L35), so the TF-XLA bridge can take advantage of the easy-to-convert functional representation. This can be achieved by setting an attribute on the If op indicating whether it should be lowered, determined by e.g. if the If op is in an `XLAContext`. This may prove useful for other future use cases as well, such as transitioning to using the functional representation in the main TF runtime.


## Implementation challenges


### Exposing intermediate tensors to gradient functions

See the "Gradients" section. We somehow need to add intermediate tensors as outputs to the already-created forward-pass If op and its branch functions. Options:

Solution:\
Modify the existing If op in-place. We do this by replacing the branch functions, and changing the outputs of the op (tricky but doable).

Since this is mutating an existing graph element, if the graph has already been run by a Session, this theoretically invalidates the session! In practice the Session appears to still be usable though.

This is the same method that tf.function and [while_v2](https://github.com/tensorflow/community/blob/master/rfcs/20180821-differentiable-functional-while.md) use for intermediate gradients, making all of them compose nicely.

Alternatives considered:
1.  Output every possible intermediate and rely on pruning to clean it up. The original implementation did this, but we changed it to match tf.function.
1.  Create a new If op with the required outputs. To prevent running both the original and new ops, we need to rewire the outputs of the original op to use the new op (and ideally modify any existing Tensor objects as well). This also requires a Session-invalidating graph mutation.
1.  Use placeholders for intermediates during construction, then use a C++ rewrite (Grappler or GraphOptimizationPass) to rewire the graph. This is effectively creating an alternative representation of the dataflow graph, which is undesireable (e.g. all graph traversal code would need to know about these special placeholders).


### Making branch function outputs match

After adding the intermediate outputs to the forward If op's branch functions, it's likely the two functions don't have the same output signature anymore. For each new output of each branch, we need to add an extra output tensor to the other branch to mirror it (since the If op requires the two outputs signatures match).

Note that the "mirror" tensors never need to be read. The original output is only consumed by the corresponding gradient function, which is only executed if the original output's branch is taken. Thus, if the mirror tensor is produced, no consumer of it will be run. However, without pruning and/or non-strict execution, the If op must still produce some value for the mirror tensor.

Solution:\
Wrap all intermediate outputs in optionals. Optionals are like maybe or [optional types](https://en.wikipedia.org/wiki/Option_type) in TensorFlow. They are variant-type tensors that may or may not contain a value tensor, which are created and introspected by [these ops](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/core/ops/dataset_ops.cc#L629).

In the branch where the intermediate is actually produced, the intermediate tensor is wrapped in an optional via the [`OptionalFromValue` op](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/core/ops/dataset_ops.cc#L629), meaning the output optional will contain the intermediate if that branch is taken. In the other branch, the "mirror" tensor is produced via the [`OptionalNone` op](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/core/ops/dataset_ops.cc#L635), meaning the output optional will have no value if the other branch is taken.

Each gradient branch then only unwraps the optionals from its corresponding forward branch to pass to the gradient computation.

Alternatives considered:
1. Output dead tensors as the "mirror" tensors, similar to the current tf.cond implementation. This requires changes to the executor to make it not mark If ops, While ops, functions ops, and possibly other special cases as dead if they have dead inputs, and prevents us from someday simplifying the excutor by removing the dead tensor logic.
1. Introduce a special op to output mirror tensors. This op's shape inference function will claim to output the same shape and type of the mirrored output, but since the tensor isn't actually needed the kernel will produce some small value to avoid producing large unnecessary values.


### Taking the gradient of deserialized If ops

We need a graph representing the branch function of an If op in order to take its gradient. We already have a graph as part of creating the function, but if the graph was loaded from a GraphDef, we no longer have this graph. Options:

Solution:\
[function_def_to_graph method](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/framework/function_def_to_graph.py)


### Variable initialization
**TODO: this section needs updating**

Variables created in the `cond` input callables must be created in the main graph, not in the temporary `FuncGraphs`. Luckily this is already handled by [init_scope](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/framework/ops.py#L5230), which should already be used as necessary to handle creating variables in Defuns, etc.


### Collections
**TODO: this section needs updating**

We must support reading and writing to collections in the `cond` input callables.

Reading from collections in eager-mode defuns already works by copying the collections into the `FuncGraphs`, which should presumably work here as well.

For writing, we'll have to forward or copy the values back to the original collections. This is tricky and poorly-defined for Tensor and Operation values, and possibly intractable for data structures containing graph elements (e.g. `WhileContext`). Options:



1.  Collections are supposed to go away in TF 2.0
1.  Somehow turn Tensors into function outputs
1.  Can some tensors/operations be pulled out of the function?
1.  Expose "legacy cond" in contrib, eventually deprecate.

**Writing to collections requires more investigation.**

For example, how are people using collections within `cond` branches? How do they avoid dead Tensors?


### Name/device/colocation scope
**TODO: this section needs updating**

Similar to reading collections, any graph-wide stacks and other state can be copied into the `FuncGraphs`. New scopes can then be added within the FuncGraph, and the semantics prevent any added state from persisting beyond the input callable.

For colocation, we can possibly use external tensor names as-is, since they'll either be lowered into the main graph or compiled by XLA.


### Control dependencies
**TODO: this section needs updating**

If the `tf.cond` call occurs inside a control_dependencies block, the control inputs will be added directly to the resulting If op.

If the `cond` input callables contain control_dependencies blocks referring external tensors, we can create Identity nodes of the external tensors inside the function definition, and then create internal control edges (functions only have data inputs).

_The following concerns are avoided by lowering If ops before execution (see "Execution" section):_


### Devices
**TODO: this section needs updating**

Akshay is working on allowing functions to run across multiple devices. My understanding is that it's mostly working, with a few limitations (e.g. all arguments to the function must go through the caller device, colocation with external tensors doesn't work).


### Partial evaluation

TF graphs are pruned before execution, meaning only the subgraph needed to compute the requested output tensors is run (this doesn't work completely for ops in a conditional branch, but some pruning still occurs). This is not currently possible with TF functions; the entire function is run regardless of which outputs are needed. This would need to be supported for parity with the current `cond` implementation.


### Non-strict execution

The current `cond` implementation allows each op in the taken branch to be run as soon as its inputs are ready, even if other ops in the branch aren't ready yet ("non-strict" execution). However, each TF op kernel will only begin running once it's inputs are all ready ("strict" execution), with `Merge` nodes being the only exception. If we replace the current `cond` construct with a single op, this will switch `cond` to strict execution. We would need to support non-strict execution of If ops and their branch functions.


## Future work

**C API support.** Ideally other language bindings support conditional execution as well. The C API already includes the primitives for other bindings to implement something similar to `tf.cond` that produces an `If` op, but the C API `TF_AddGradients` method would need to support `If` ops in order for other bindings to (easily) allow autodiff of conditionals.

## Update log

2019-02-26: Updated some sections to reflect what was built and added link to implementation. Marked other sections as still needing update; many of these concerns are common to cond_v2, while_v2, and functions, so we may wanna include these as part of a function design doc.
