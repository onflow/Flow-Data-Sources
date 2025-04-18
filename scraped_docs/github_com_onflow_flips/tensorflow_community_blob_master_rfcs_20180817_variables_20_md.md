# Source: https://github.com/tensorflow/community/blob/master/rfcs/20180817-variables-20.md

# Variables in TensorFlow 2.0

| Status        | Accepted       |
:-------------- |:---------------------------------------------------- |
| **Author(s)** | apassos@google.com |
| **Sponsor**   | wicke@google.com, joshl@google.com, ashankar@google.com                 |
| **Updated**   | 2018-08-17                                           |


## Objective

The API for TensorFlow variables has many drawbacks: impossible-to-reason-about semantics, reliance on global scopes, and reliance on global collections. As the TensorFlow API moves to become more pythonic and object oriented, with the Keras layers and models and the object-based serialization, we no longer have a need for much of this global infrastructure around variables.


## Main changes

The API for Variables will then change in the following ways for TF 2.0:



*   tf.Variable will become an abstract base class with a well-defined interface and a scoped factory to construct instances
    *   users will be able to implement their own variable-like objects by subclassing tf.Variable and adding a scoped factory function to use those variables
*   variable_scope and get_variable will be removed
    *   the tf 1.0 version of variable_scope and get_variable will be left in tf.compat.v1
    *   to control variable naming users can use tf.name_scope + tf.Variable
    *   whether a variable is shared across sessions / processes will be controlled by a constructor argument to tf.Variable; no other type of scope reuse will be done in the framework
    *   scoped partitioning will be implemented as a factory function at first
    *   libraries and users are encouraged to reuse variables by reusing their objects, like Keras layers do
    *   custom_getters will have the following API: [variable_creator_scope](https://github.com/tensorflow/tensorflow/blob/567189980f7a1c2aa09a5170bd8d01a6ec37d303/tensorflow/python/ops/variable_scope.py#L2402)
*   the default implementation of the tf.Variable interface will be ResourceVariable
    *   RefVariable will be kept in tf.compat.v1 and will be the default implementation for tf.compat.v1.Variable
    *   tf.compat.v1.Variable will have a use_resource argument to control whether a resource variable or a ref variable will be created
*   symbols like tf.assign* will be removed in favor of methods in tf.Variable
    *   in tf.compat.v1 these symbols will be marked as deprecated and will call the corresponding methods in the Variable object instead


## Detailed changes


### tf.Variable class

The tf.Variable class will be an abstract base class which defines a tf.Variable interface. Initially this interface will have enough abstract methods such that the user-visible API of tf.Variable does not change.

There will be two main implementations of this interface: RefVariable, with the legacy ref edges, available only in tf.compat.v1, and ResourceVariable, which is the default for the v2 API. PartitionedVariable, MirroredVariable, _UnreadVariable, CastVariable, etc, are other implementations which are part of the core library. None of these implementations will be publicly visible, only tf.Variable will be.

Constructing variables is done by calling tf.Variable(*args, **kwargs). Under the hood this will call a hierarchy of scoped constructor functions, similar to what is now done in variable_scope.variable. Each such constructor function can do some combination of:



*   calling a base constructor to actually create a variable
*   returning preexisting variables
*   changing some arguments to the base constructor, and maybe calling it multiple times

This is implemented by having a custom metaclass for tf.Variable which, when asked to construct a tf.Variable directly will call the factory functions, but when asked to construct subclasses of tf.Variable will do nothing and construct the child class.

The tf.Variable interface will make no reference to graph collections, and tf.Variable will not add the Variable to any collections by default. tf.compat.v1.Variable, on the other hand, will have the collections argument and respect the existing semantics for it. Things which currently rely on collections (saving / loading, Optimizer.minimize, etc) will instead be expected to be passed either a list of variables or a CheckpointableBase-inheriting object.


### Variable sharing

Sharing within a model will not be a part of the public API for tf.Variable. Users are strongly encouraged to share variables by sharing a reference to their objects.

That said, the tf.compat.v1.variable_scope library can be made self-contained if we replace the per-graph variable scope stack with a module-global weak key dictionary from graphs to scope objects, and we call the protected methods to access graph collections. This will remain available for users who are not willing to port their libraries to have object-based sharing, as the support burden of maintaining that file in tf.compat.v1 is negligible and the volume of code written to use it is broad.


### Checkpointing

Checkpointing will be done in tf 2.0 via the [object-oriented checkpointing API](https://www.tensorflow.org/api_docs/python/tf/contrib/checkpoint/Checkpointable).


### Optimizers

The Optimizer.minimize method will no longer work if it's passed a Tensor and no list of variables. Users are expected to pass the list of variables to minimize wrt or pass an object which implements the CheckpointableBase interface to let the optimizer find the variables. The behavior of tf.compat.v1.Optimizer will not change.


### Assignment operations

Instead of having free functions which access internal state of variables, reading from and writing to variables will be done via methods. Current tf.assign*(variable, ...) will become variable.assign*(...). tf.compat.v1 will keep the old aliases, but they will call the new methods instead.

This is an easy LSC to make (once the current operations are modified to return a RefVariable object instead of a Ref tensor) and will make the code more homogeneous and pythonic.


### Ref edges versus resources

TensorFlow graphs need to represent state (information which survives calls to session.run, or generally information produced by an op which depends on something other than the content of its input tensors) so most nontrivial programs can be useful. Examples of state are input pipelines, model parameters, queues, mutexes, and random number generators.

There are a number of ways of representing state in TensorFlow directly in the graph, but the most robust and flexible is using resource handles. A **resource handle** is a regular immutable Tensor which represents a name to a shared out-of-graph resource (any C++ class inheriting from ResourceBase can be used as a resource). The resource handle itself doesn't change during the program execution. The resource pointed to by a handle lives on a specific device (so while it's possible to serialize resource handle tensors it's usually not a good idea), and can be accessed by any op which runs on that device and has access to the resource handle tensor. These ops can do things such as reading from the resource, modifying the resource, initializing the resource, and deleting it.

A resource handle is a scalar tensor of dtype DT_RESOURCE (or dtypes.resource in Python), and can be manipulated as any other Tensor: you can concatenate resources, they can go through conditionals, you can slice into them, etc. This means that while it's often possible to determine statically whether two operations can access the same resource some graphs might be structured in ways which make this difficult.

When you can determine statically that two ops touch the same resource you can make inferences about the state of the resource when one op is executing solely by looking at the graph. For example, if there is a path formed of control or data edges connecting a resource-using op O to a resource-using op O', you know that O' is guaranteed to see the effects of O on the resource and, conversely, that O is guaranteed to not see the effects of O' on the resource. If, on the other hand, there is no path in the graph connecting ops O and O' which use the same resource then whether one sees the effects of the other is undefined, and might vary from one execution to another.

Resource variables were the motivating case for introducing the explicit notion of resources to TensorFlow graphs. This was done to avoid complicated issues related to the lack of a memory model for the deprecated ref-edge-based variables  and allow compilation of TensorFlow graphs containing mutable state.

A resource-based variable is the simplest type of resource. What's stored in the device's resource manager is a pair of a Tensor and a mutex. The main operation to read the value of a variable is read_variable_op, and it simply outputs a Tensor which has the same value as the Tensor in the resource handle state. There are many ops which write to the resource (assign_variable_op, assign_add_variable_op, resource_apply_gradient_descent, etc), and the basic properties of the resource edges ensure that it's possible to order reading and writing ops to avoid undefined behavior.

These ops are currently implemented using copy-on-write, but they could also be implemented using copy-on-read or other, more complex, mechanisms, as long as the semantics of the read-before-writes and write-before-read are respected and as long as no mutation is done to the Tensor returned by a read_variable_op after it's been read. Here are two examples of why mutating a Tensor returned by a read_variable_op might be dangerous:



*   tf.cond predicates: a tf.cond takes a boolean tensor as a predicate and conditionally executes ops in the true or false branch of the conditional based on the value of the predicate. The way this is implemented in TensorFlow, to allow for graph pruning and non-strict execution is that there are many "switch" ops in the graph, each of which looks at the value of the predicate and decides which operations downstream from it can execute. If the predicate is a variable and one branch modifies the value of this variable, we would like to ensure that, because the "read" operation happened before the switch ops, only one branch of the conditional will execute. If, instead, writing to a variable could mutate the value of the tensor returned by "read", then a subset of both branches could execute, leading to hard-to-debug errors.
*   gating gradients: when computing the backward pass and training a deep neural network there is by default no in-graph order between the operation to update the parameters of a layer based on its gradients and to use the value of the parameters of the layer to compute the gradient with respect to the previous layer. If the value of a variable was allowed to change after it was read, it would be possible for the value after the update to be used in the backward pass, leading to incorrect gradients for the layers closer to the input of the network.

These are just two examples of how it's much harder to reason about TensorFlow programs when the value of a variable can change after it was read.

Before resource handles TensorFlow variables were represented using a "ref" edge. A ref edge is a pair of pointers, one to a Tensor and one to a mutex, owned by something other than the tf runtime. When an op takes a ref tensor its input has to be a ref tensor, but when an op takes a non-ref tensor but its input is a ref tensor the pointer is silently dereferenced. This means that normal tensor objects in the graph can silently alias a mutable tensor, and hence two ops with the same input can see it having different values. Which value will be seen can depend on execution-specific details such as whether the variables are on a local or remote device, and in general it's not easy to ensure that a read happens before or after a specific write.


### Internal resource variable ops

We will expose the internal ops used to implement ResourceVariable as tf.experimental.variable_operations (name TBD). This way users and libraries can, if they need to, modify the behavior of variables at will.


## Migration plan

The migration plan is roughly as follows. TODO(apassos): flesh out this section with cost estimates.



1.  Implement the abstract base class and factory function scope under the hood
1.  Expose the factory function scope as tf.variable_creator_scope
1.  LSC to change tf.variable_scope / tf.get_variable to tf.compat.v1.*
1.  Removal of tf.variable_scope and tf.get_variable from the tf 2 namespace
1.  Implement the subclass to be returned from tf.assign*
1.  LSC to change tf.assign*(v, …) to v.assign*(...)
1.  Change the implementation of tf.compat.v1.variable_scope to not rely on a per-graph variable scope stack
1.  Remove the get_variable_scope and related public methods from tf.Graph (leaving them on tf.compat.v1.Graph)
1.  Implement PartitionedVariable as a subclass of the tf.Variable interface
1.  Add a partitioner scope to the tf 2.0 API
1.  Add a deprecation warning to the tf.compat.v1 partitioned variable scope with a migration warning
1.  [questionable] Implement a variable creator factory function which calls get_variable under the hood
1.  Make this function active in all tf.compat.v1 endpoints which currently call get_variable (with a decorator, probably)
1.  Change the behavior in tf2 to call tf.Variable (which will redirect to tf.get_variable in tf.compat.v1, keeping the existing behavior but cleaning the codebase)
1.  [WARNING: checkpoint-breaking change] drop calls to variable_scope in parts of our API which use it. Right now they are: feature_column, rnn, canned estimators, optimizer slots, TPU estimator. Most can be replaced with judicious use of name= arguments
1.  [optional] Implement tf v2 make_template which does not rely on variable_scope internally and uses a factory creator function to track and reuse variables


## Questions and Discussion Topics

1. How should we deal with the deprecation of model building APIs?
