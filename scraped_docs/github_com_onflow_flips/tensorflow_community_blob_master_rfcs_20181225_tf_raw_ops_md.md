# Source: https://github.com/tensorflow/community/blob/master/rfcs/20181225-tf-raw-ops.md

# `tf.raw_ops`

| Status | Accepted |
| :------------ | :------------------------------------------------------ |
| **Author**    | apassos@google.com 								  |
| **Sponsor**   | wicke@google.com                                        |
 | **Updated**   | 2018-12-21                                              |

## Objective

Expose a `tf.raw_ops` namespace containing all raw operations in TensorFlow.

## Motivation

Some parts of the TensorFlow Python API, such as variables, optimizers, and
control flow, are currently not implementable by third parties. Moreover, with
the tf.contrib deprecation, there is now no valid Python endpoint from which to
use many TF operations.

## Design Proposal

We'll add a `tf.raw_ops` namespace to TensorFlow with Python bindings to all
non-deprecated TensorFlow ops which is usable in a backwards-compatible
way. This is designed to be consumed by downstream library writers and not end
users.

## Detailed Design

The namespace will be automatically populated with generated bindings for every
operation in TensorFlow. These generated bindings will be similar to the ones
currently used for the python API, with the following differences:

* All arguments are keyword arguments.
 - This allows us to add new attributes to existing ops without breaking users
   who call by positional arguments (given that there is an always-last `name`
   argument added by the tf op binding generator).
 - This also prevents users from assuming that calling conventions from the
   existing python bindings apply to the raw versions (we often do argument
   reordering in our python bindings, for example).
* Any op marked as deprecated will be in the namespace but will raise an
  exception when used.
 - This includes ops which take or produce ref tensors.
 - This allows us to deprecate ops eventually and to be less strict with the API
   here than with the main API.
 - This is mostly OK since only library writers are supposed to use these
   symbols, and the deprecation messages should include upgrading instructions.


## Questions and Discussion Topics

* Naming: tf.raw_ops is the name
* Backward compatibility policy: we'll document on tf.org
* Flat namespace vs nested? flat
* Will not include protocol buffers
