# Source: https://github.com/tensorflow/community/blob/master/rfcs/20190117-tf-module.md

# tf.Module

| Status        | Accepted                                                          |
| :------------ | :---------------------------------------------------------------- |
| **Author(s)** | DeepMind: tomhennigan@google.com, mareynolds@google.com           |
|               | Google: agarwal@google.com, apassos@google.com, dberth@google.com |
| **Sponsor**   | apassos@google.com                                                |
| **Updated**   | 2019-01-16                                                        |
| **Obsoletes** | N/A                                                               |

## Overview

We propose a lightweight base class (`tf.Module`) for stateful containers in
TensorFlow. This base class offers three main features:

-   **Naming** - variables and ops created inside modules are created within a
    name scope so they can easily be tracked back to their creator.
-   **Variable tracking** - variables referenced by a module (directly or via
    dependencies on other modules) can be retrieved via a simple API.
-   **Module tracking** - given a module a simple API exposes all modules that
    this module depends on.

Users are encouraged to subclass `tf.Module` to create their own stateful
components and we expect and encourage an ecosystem of third party modules to
evolve.

## Motivation

When defining neural networks it is convenient to describe the network as a DAG
of connected components (e.g. datasets, layers, optimizers). In Python it is
convenient to represent nodes in this DAG as objects which encapsulate node
state (e.g. `tf.Variable`) and functionality (e.g. forward functions).

We propose a lightweight "module" abstraction that serves as a base class for
all types of node in this DAG (e.g. layers, optimizers, metrics) which is not
tied to a particular higher level framework (e.g. Keras, Estimator or Sonnet).
The module abstraction standardizes naming of variables and ops (to simplify
debugging/visualisation) and dependency tracking (e.g. retrieving `tf.Variable`s
and `tf.Module`s referenced by a given root module).

Having a standard abstraction for stateful TensorFlow components will encourage
users to create loosely coupled components which are easy to reason about in
isolation while providing a standard mechanism for common tasks in a larger
assembly (e.g. finding all trainable variables for a module tree given a root).

We see such a lightweight abstraction as being particularly important for
cutting edge research, where it is not possible for library/framework authors to
reason about what their users will create. We believe that lightweight
abstractions which can be extended or composed to build more complex systems are
the way forward.

## Background

TensorFlow V1 has a number of abstractions for handling TensorFlow state (e.g.
`tf.Variable`s). Broadly you can split them into "collections based" (e.g.
`tf.variable_scope`, `tf.get_collection`, `tf.make_template`, `tf.layers.Layer`)
and "Object Oriented" (e.g. `tf.keras.layers.Layer`).

TensorFlow V2 is standardising on OO and `tf.keras` as the only stateful
abstraction inside the default TensorFlow pip installation.

Outside of TensorFlow there exist a number of third party libraries which also
offer abstractions for managing TensorFlow state. For example the Sonnet library
from DeepMind is built on top of `tf.make_template`.

## Requirements

### Functional

**Naming `tf.Variable`s (and `tf.Operation`s)**

-   Each module instance must have a name scope. This name should include the
    name scope from when the module is constructed.
-   Every method on the module must enter this name scope before calling user
    code (such that variables and operations are correctly named).

**`tf.Variable` creation and reuse**

-   Modules should be able to create and reuse variables.
-   Users should be able to intercept variable creation without changing module
    code (e.g. via `tf.variable_creator_scope`).
-   Users should be able to access and change variables on a module in an
    intuitive way (e.g. being able to copy variables between modules
    `module.w = other_module.w`).

**`tf.Variable` tracking**

-   Variables created, owned or used by a module should be retrievable (e.g.
    mod.variables should provide a collection of variables for mod and all of
    its descendent modules).
-   Which variables are tracked should be obvious (e.g. all object properties)
    and "opt-out" rather than "opt-in" (e.g. the most obvious way to create and
    reuse a variable should automatically be tracked).

**`tf.Module` tracking**

-   Modules should track dependencies (e.g. a sequential should provide access
    to its layers) and support checkpointing as a graph.

**Performance**

-   TensorFlow 2 is eager first meaning Python code is on the critical path.
    tf.Module should have as little runtime overhead as reasonable to avoid
    getting in the way.
-   Additionally tf.Module should be fully compatible with tf.function allowing
    high performance graphs to be extracted when appropriate.

### Non-functional

**Wide adoption**

-   `tf.Module` (or types derived from it) should be the obvious choice for
    research code and useful in general.
-   It should not favor a specific theme (e.g. supervised learning) vs. another
    (e.g. adversarial training).
-   Having shared abstractions is critical for a research teams to facilitate
    easy collaboration.

**Researcher approved**

-   `tf.Module` should be designed in collaboration with researchers and the API
    should match their preferences.

**Unbloated**

-   `tf.Module` should be a thin abstraction which is trivial to reason about.
-   The implementation should be clean and readable, ideally no more than a few
    100 lines of code.
-   The external API should have very few public methods.

**Tightly specified**

-   The specification for a `tf.Module` should be clear and agreed upon.
-   Future additions to `tf.Module` should be critically evaluated against the
    original design goals and moved elsewhere when they do not align.
-   New features (e.g. supporting mixed precision training) should not require
    changes to `tf.Module`.

**Loosely coupled**

-   Using `tf.Module` should not tie you to a particular framework or mentality.
-   It should be trivial to integrate a subclass of `tf.Module` into any
    codebase.

**Defensive**

-   The design of `tf.Module` should optimize for helping avoid common mistakes
    (e.g. accidentally not tracking variables).
-   If functionality is required (e.g. calling `super(..).__init__()` in
    subclasses) we should error early (e.g. immediately after the module
    constructor returns) to remind users if they forget.

## Detailed Design

### Class structure

We propose a pure Python class `tf.Module` which has a metaclass
`tf.ModuleMetaclass` to wrap all methods in the modules name scope. This design
allows for submodules or variables to created in any method (including
`__init__` and `__call__`). There is more detail on this decision in the
detailed design below.

```python
class Module(six.with_metaclass(ModuleMetaclass, tf.checkpoint.Checkpointable)):
  """Base neural network module class.

  A module is a named container for `tf.Variable`s, other `tf.Module`s and
  functions which apply to user input. For example a dense layer in a neural
  network might be implemented as a `tf.Module`:

  >>> class Dense(tf.Module):
  ...   def __init__(self, in_features, output_features):
  ...     super(Dense, self).__init__()
  ...     # NOTE: We're creating variables in the ctor, but you can actually
  ...     #       create them in any method (including __call__) you like.
  ...     self.w = tf.Variable(
  ...         tf.random.normal([input_features, output_features]), name='w')
  ...     self.b = tf.Variable(tf.zeros([output_features]), name='b')
  ...
  ...   def __call__(self, x):
  ...     y = tf.matmul(x, self.w) + self.b
  ...     return tf.nn.relu(y)

  You can use the layer as you would expect:

  >>> d = Dense(input_features=64, output_features=10)
  >>> d(tf.ones([100, 64]))
  <tf.Tensor: ...>

  By subclassing `tf.Module` instead of `object` any variables created inside
  the module are automatically created within the modules name scope:

  >> d.w.name
  "dense/w:0"

  In eager mode this is useful for debugging, and when used with `@tf.function`
  the use of name scopes gives operations (e.g. matmul) useful names as well.

  As well as automatic naming, the Dense module inherits methods for tracking
  its variables:

  >>> d.variables
  (<tf.Variable 'dense/b:0' ...>, <tf.Variable 'dense/w:0' ...>)
  """

  @property
  def name(self):
    """Returns the name of this module as passed or determined in the ctor.

    NOTE: This is not the same as the `self.name_scope.name` which includes
    parent module names.
    """

  @property
  def name_scope(self):
    """Returns a `tf.name_scope` instance for this class.

    NOTE: The module name scope includes all parent modules as determined
    when this module was created.
    """

  @property
  def variables(self):
    """Returns a collection of variables owned by this module and it's submodules.

    Returns:
      A collection of variables for the current module (sorted by attribute name)
      followed by variables from all submodules recursively (depth first).
    """

  @property
  def trainable_variables(self):
    """Returns a collection of variables owned by this module and it's submodules.

    Returns:
      A collection of variables for the current module (sorted by attribute name)
      followed by variables from all submodules recursively (depth first).
    """

  @property
  def submodules(self):
    """Returns an iterator of all submodules recursively.

    Submodules are modules which are properties of this module, or found as
    properties of modules which are properties of this module (and so on).

    >>> a = tf.Module()
    >>> b = tf.Module()
    >>> c = tf.Module()
    >>> a.b = b
    >>> b.c = c
    >>> assert list(a.submodules) == [b, c]
    >>> assert list(b.submodules) == [c]
    >>> assert list(c.submodules) == []

    Returns:
      A generator over all submodules.
    """

  def _flatten(self,
               recursive=True,
               predicate=None,
               attribute_traversal_key=None,
               with_path=False):
    """Flattened attribute values in sorted order by attribute name.

    Modules are flattened by first walking their attributes in name order.
    Each attribute value is then flattened to find leaf values. If flatten is
    to be applied `recursive`ly then if the leaf is a `Module` it will also be
    flattened to find leaves. Finally every leaf value is optionally tested
    against the given `predicate` and finally yielded.

    >>> class Foo(tf.Module):
    ...   def __init__(self):
    ...     super(Foo, self).__init__()
    ...     self.x = [tf.constant('a'), tf.constant('b')]
    ...     self.y = {'i': tf.constant('c'), 'j': tf.constant('d')}
    ...     self.z = tf.constant('e')
    ...
    ...   @property
    ...   def tensors(self):
    ...     return tuple(self._flatten(predicate=is_tensor, with_path=True))

    >>> foo = Foo()
    >>> foo.tensors
    ((('x', 0),   <tf.Tensor: ...'a'>),
     (('x', 1),   <tf.Tensor: ...'b'>),
     (('y', 'i'), <tf.Tensor: ...'c'>),
     (('y', 'j'), <tf.Tensor: ...'d'>),
     (('z',),     <tf.Tensor: ...'e'>))

    `attribute_traversal_key` controls the order object properties are visited.
    If not set objects are visited in ascending order by name.

    Args:
      recursive: Whether to recurse into child modules or not.
      predicate: (Optional) If set then only values matching predicate are
        yielded. A value of `None` (the default) means no items will be
        filtered.
      attribute_traversal_key: (Optional) Method to rekey object attributes
        before they are sorted. Contract is the same as `key` argument to
        builtin `sorted` and only applies to object properties.
      with_path: (Optional) Whether to include the path to the object as well
        as the object itself. If `with_path` is `True` then leaves will not be
        de-duplicated (e.g. if the same leaf instance is reachable via multiple
        modules then it will be yielded multiple times with different paths).

    Returns:
      Flat generator for leaves of the current module and optionally all
      submodules.
    """


class ModuleMetaclass(type):
  def __new__(mcs, name, bases, clsdict):
    """Modifies module subclasses when they are defined.

    Wraps all methods and properties in clsdict such that enter the modules
    name scope before evaluation.

    >>> class MyModule(tf.Module):
    ...   def __call__(self, x):
    ...     if not hasattr(self, 'w'):
    ...       self.w = tf.Variable(tf.zeros([x.shape[1], 64]), name='w')
    ...     return tf.matmul(x, w)

    Without any user intervention __call__ will enter the modules name scope,
    allowing variables and submodules to be created. In some cases this is not
    desirable, so there exists an opt out annotation(`@no_auto_name_scope`)
    which instructs the metaclass to not wrap these functions.
    """

  def __call__(cls, *args, **kwargs):
    """Creates new module instances.

    To allow other modules/variables to be created in the constructor of a
    module (and be named appropriately) we enter the module name scope inside
    the base (Module) constructor. We close the name scope in the metaclass
    before returning the new instance.

    >>> class MyModule(tf.Module):
    ...   def __init__(self):
    ...     super(MyModule, self).__init__()
    ...     # ^ Enters the module name scope but does not exit.
    ...
    ...     self.v = tf.Variable(1., name='v')
    ...     # ^ Will be named "my_module/v"
    ...
    ...     self.m = MyOtherModule()
    ...     # ^ Will be named "my_module/my_other_module"

    >>> m = MyModule()
    >>> # ^ Name scope will be closed thanks to metaclass.
    """
```

### Naming

Having human readable names for ops and variables is essential for debugging.
Each `tf.Module` will have a name scope which is determined in the constructor.
By default this will be a `lower_camel_case` version of the `ClassName`:

```python
class MyModule(tf.Module):
  def __init__(self, name=None):
    super(MyModule, self).__init__(name=name)
    self.v = tf.Variable(1., name='v')

>>> m = MyModule()
>>> m.name
'my_module'
>>> m.name_scope.name
'my_module/'
>>> m.v.name
'my_module/v:0'

>>> m = MyModule(name='custom_name')
>>> m.name
'custom_name'
>>> m.name_scope.name
'custom_name/'
>>> m.v.name
'custom_name/v:0'
```

Modules created inside methods of other modules inherit their parent module
name:

```python
class ParentModule(tf.Module):
  def __init__(self):
    super(ParentModule, self).__init__()
    self.child_module = MyModule(name='child')
    self.v = tf.Variable(1., name='v')

>>> p = ParentModule()

>>> p.name
'parent_module'
>>> p.name_scope.name
'parent_module/'
>>> p.v.name
'parent_module/v:0'

>>> p.child_module.name
'child'
>>> p.child_module.name_scope.name
'parent_module/child/'
>>> p.child_module.v.name
'parent_module/child/v:0'
```

In TensorFlow 2 string matching of variable names is not required for
distributed training (you can create remote variables eagerly, also see
[DistributionStrategy](https://github.com/tensorflow/community/blob/master/rfcs/20181016-replicator.md))
or checkpointing (this is done based on Python object structure) so the naming
of variables and ops is just to aid with usability and visualisation.

### Variables

Users are free to create `tf.Variable` instances in any method at any time (as
long as the super constructor has run).

Variable reuse should be achieved using standard object oriented programming
(e.g. assigning to object properties). `tf.Module` doesn't do anything behind the
scenes to help (or hinder) variable reuse.

We considered including a default implementation of `__call__` since lazy
building is extremely common (e.g. constructing model parameters the first time
an input is observed), however we backtracked on this for a number of reasons:

-   Even among the authors there existed different preferences for how to enable
    this pattern, it seemed unlikely we could make a choice which would satisfy
    the community.
-   Not all modules want a `__call__` method (e.g. an `Optimizer`) and we got
    strong feedback that it is annoying to ignore unused methods inherited from
    your base class.
-   Encouraging a lazy pattern might make it harder to create modules with
    multiple forward methods (e.g. a VAE module might be implemented with an
    `encode` and `decode` method with no `__call__`).

As such we leave the problem of how to enable lazy parameter construction to
library authors who build on `tf.Module`s.

### Checkpointing

`tf.Module` will extend `tf.checkpoint.AutoCheckpointable` which automatically
tracks variables which are object properties and enables restore on create etc.
Users who want to learn more about checkpointing should look into this type.

It is worth noting that object structure (e.g. the names of object parameters)
are encoded into checkpoints, so library authors should take care to lay out
their objects in a consistent way and defend their structure. `tf.Module` is
careful to not add any load to the user here by not imposing any requirements on
how you lay out your internal state.

We considered imposing a constraint that all `tf.Variable`s were created with some
utility (e.g. `self.create_variable(name, shape)`) and storing these in a
dictionary of variable name to instance. While this would simplify the checkpointing
story (since the structure of TensorFlow state would only depend on variable
names) internal users felt that it was overly restrictive. Additionally we would
require functions to query this storage (e.g. `get_variable('name')` and remove
items from it). Library authors may want to consider this pattern if it makes
sense for their users.

### `tf.Variable` tracking

It is very convenient to be able to collect all the variables for a given module
and all of its dependencies. We achieve this in `tf.Module` using reflection to
walk object properties. When walking if we encounter a nested structure (e.g. a
`list`, `dict` etc) we will flatten it using `nest.flatten(value)` and evaluate
each leaf. This means variables nested in properties will be found (e.g.
variables in `list`s or `tuple`s on the module).

This "walk" function is used to provide the following properties:

-   `module.variables` - All variables from this module and all of its child
    modules (recursively).
-   `module.trainable_variables` - All trainable variables from this module and
    all of its child modules (recursively).

We considered alternative tracking mechanisms, for example wrapping all methods
in a `tf.variable_creator_scope` and associating created variables with the
module that created them. Ultimately we felt this had too much magic and was not
flexible enough for some use cases. For example users wanted to be able to
create temporary variables and discard them after some time period, we would
need to allow them to opt these variables out of tracking or to remove them from
the store.

### tf.Module tracking

Module tracking is implemented in the same way as variable tracking. We expose:

-   `module.submodules` - All submodules from this module and submodules of its
    immediate child modules (recursively).

We considered adding tracking from children to parents (e.g. `assert
mlp.layers[0].parent is mlp`) however we were concerned that enabling this might
cause modules to become less composable (e.g. a child relying on `self.parent`
would presumably be harder to integrate into a different parent module).
Ultimately we felt that thinking of modules as a tree rather than a cyclic graph
was conceptually simpler.

### Performance

There are two main areas where `tf.Module` might affect performance (in eager
code):

1.  How will automatic name scopes affect method call performance?
2.  How performant will the reflection mechanism be for collecting variables?

Re (1) on my (fairly beefy) workstation calling an empty method on a `tf.Module`
takes ~15µs, creating + entering a name_scope (e.g. `with
tf.name_scope('some_name'): pass`) takes ~6µs. We would like to optimize the
per-method overhead, but feel like it is unlikely to be a blocker in the short
term. For reference stepping an empty `@tf.function` currently takes ~40µs.

Re (2) it takes ~2ms to collect variables for a `Sequential` with 100 `Linear`
layers (e.g. 200 variables). This scales linearly (as expected) based on the
number of layers. Users can pay this cost once in their training loop by
memoizing the result of mod.variables (e.g. `variables = mod.variables`).

### Integration in TensorFlow

A good rule of thumb is that anything currently using `Checkpointable` should
consider using `Module` instead (an obvious counter example is `tf.Variable`).
For example, stateful components in `tf.keras` (like layers, networks and
models) could extend `tf.Module` instead of `Checkpointable`.

We avoid suggesting specific integrations as part of this proposal, and leave
this up to the authors of libraries and frameworks built on top of TensorFlow to
decide.

### Examples

To be clear these examples are not going to become part of TensorFlow. They are
simply an example of the types of modules users or higher level libraries can
express using the `tf.Module` abstraction.

**Layers**

```python
class Sequential(tf.Module):
  def __init__(self, layers, name=None):
    super(Sequential, self).__init__(name=name)
    self.layers = list(layers)

  def __call__(self, x):
    for layer in self.layers:
      x = layer(x)
    return x

class Linear(tf.Module):
  def __init__(self, output_size, name=None):
    super(Linear, self).__init__(name=name)
    self.output_size = output_size

  def __call__(self, x):
    if not hasattr(self, 'w'):
      input_size = x.shape[1]
      initial_w = tf.random.truncated_normal(shape=[input_size, self.output_size],
                                             stddev=(1 / math.sqrt(input_size)))
      self.w = tf.Variable(initial_w, name='w')
      self.b = tf.Variable(tf.zeros([self.output_size]), name='b')

    return tf.matmul(x, self.w) + self.b

mlp = Sequential([
  Linear(1024),
  tf.nn.relu,
  Linear(10),
])

# Calling the module produces the result. In the above example variables
# are created lazily the first time the module is called.
y = mlp(tf.ones([10, 100]))

assert set(mlp.variables) == {mlp.layers[0].w, mlp.layers[0].b,
                              mlp.layers[2].w, mlp.layers[2].b}

# Variable names include module names.
assert mlp.layers[0].w.name == 'linear/w:0'
assert mlp.layers[2].w.name == 'linear/w:0'  # NOTE: in graph mode this is linear_1

# The full submodule graph only includes the two linear layers.
assert set(mlp.submodules) == {mlp.layers[0], mlp.layers[2]}
```

**Metrics**

```python
class Mean(tf.Module):
  def __init__(self, dtype=tf.float32, name=None):
    super(Mean, self).__init__(name=name)
    self.count = tf.Variable(0., dtype=dtype, name='count')
    self.sum = tf.Variable(0., dtype=dtype, name='sum')

  def reset(self):
    self.count.assign(0)
    self.sum.assign(0)

  def update(self, sample):
    self.sum.assign_add(sample)
    self.count.assign_add(1)

  def result(self):
    return self.sum / self.count
```

**Optimizers**

```python
class GradientDescent(tf.Module):
  def __init__(self, learning_rate=0.01, name=None):
    super(GradientDescent, self).__init__(name=name)
    self.learning_rate = tf.Variable(learning_rate, name='learning_rate')

  def minimize(self, loss_fn, variables=None):
    with tf.GradientTape() as tape:
      loss = loss_fn()
    if variables is None:
      variables = tape.watched_variables()
    self.apply_gradients(zip(variables, tape.gradients(loss, variables)))
    return loss

  def apply_gradients(self, vars_and_grads):
    for variable, grad in vars_and_grads:
      variable.assign_sub(grad * self.learning_rate)
```
