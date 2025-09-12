# Source: https://cadence-lang.org/docs/language/types-and-type-system/type-safety

Type Safety | Cadence



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Cadence](/img/logo.svg)![Cadence](/img/logo.svg)](/)

[Learn](/docs)[Playground](https://play.flow.com/)[Community](/community)[Security](https://flow.com/flow-responsible-disclosure/)[Language Reference](/docs/language)

Search

* [Introduction](/docs/)
* [Why Use Cadence?](/docs/why)
* [Cadence Guide for Solidity Developers](/docs/solidity-to-cadence)
* [Tutorial](/docs/tutorial/first-steps)
* [Language Reference](/docs/language/)

  + [Syntax and Glossary](/docs/language/syntax)
  + [Constants and Variable Declarations](/docs/language/constants-and-variables)
  + [Values and Types](/docs/language/values-and-types/)
  + [Types and Type System](/docs/language/types-and-type-system/)

    - [Type Annotations](/docs/language/types-and-type-system/type-annotations)
    - [Type Safety](/docs/language/types-and-type-system/type-safety)
    - [Type Inference](/docs/language/types-and-type-system/type-inference)
    - [Composite Types](/docs/language/types-and-type-system/composite-types)
    - [Intersection Types](/docs/language/types-and-type-system/intersection-types)
    - [Run-time Types](/docs/language/types-and-type-system/run-time-types)
    - [Type Hierarchy](/docs/language/types-and-type-system/type-hierarchy)
  + [Operators](/docs/language/operators/)
  + [Accounts](/docs/language/accounts/)
  + [Functions](/docs/language/functions)
  + [Pre- and Post-Conditions](/docs/language/pre-and-post-conditions)
  + [Built-in Functions](/docs/language/built-in-functions)
  + [Control Flow](/docs/language/control-flow)
  + [Scope](/docs/language/scope)
  + [Resources](/docs/language/resources)
  + [Access Control](/docs/language/access-control)
  + [Capabilities](/docs/language/capabilities)
  + [Interfaces](/docs/language/interfaces)
  + [Enumerations](/docs/language/enumerations)
  + [References](/docs/language/references)
  + [Imports](/docs/language/imports)
  + [Attachments](/docs/language/attachments)
  + [Contracts](/docs/language/contracts)
  + [Contract Updatability](/docs/language/contract-updatability)
  + [Transactions](/docs/language/transactions)
  + [Events](/docs/language/events)
  + [Core Events](/docs/language/core-events)
  + [Environment Information](/docs/language/environment-information)
  + [Crypto](/docs/language/crypto)
* [Cadence 1.0 Migration Guide](/docs/cadence-migration-guide/)
* [Design Patterns](/docs/design-patterns)
* [Anti-Patterns](/docs/anti-patterns)
* [Development Standards](/docs/project-development-tips)
* [Security Best Practices](/docs/security-best-practices)
* [JSON-Cadence Format](/docs/json-cadence-spec)
* [Contract Upgrades with Incompatible Changes](/docs/contract-upgrades)
* [Measuring Time](/docs/measuring-time)
* [Testing](/docs/testing-framework)

* [Language Reference](/docs/language/)
* [Types and Type System](/docs/language/types-and-type-system/)
* Type Safety

On this page

# Type Safety

The Cadence programming language is a *type-safe* language.

### Assigning a new value to a variable[​](#assigning-a-new-value-to-a-variable "Direct link to Assigning a new value to a variable")

When assigning a new value to a variable, the value must be the same type as the variable. For example, if a variable has type `Bool`, it can *only* be assigned a value that has type `Bool`, and not for example a value that has type `Int`:

`` _10

// Declare a variable that has type `Bool`.

_10

var a = true

_10

_10

// Invalid: cannot assign a value that has type `Int` to a variable which has type `Bool`.

_10

//

_10

a = 0 ``

### Passing arguments to a function[​](#passing-arguments-to-a-function "Direct link to Passing arguments to a function")

When passing arguments to a function, the types of the values must match the function parameters' types. For example, if a function expects an argument that has type `Bool`, *only* a value that has type `Bool` can be provided, and not for example a value which has type `Int`:

`` _10

fun nand(_ a: Bool, _ b: Bool): Bool {

_10

return !(a && b)

_10

}

_10

_10

nand(false, false) // is `true`

_10

_10

// Invalid: The arguments of the function calls are integers and have type `Int`,

_10

// but the function expects parameters booleans (type `Bool`).

_10

//

_10

nand(0, 0) ``

### Converting types[​](#converting-types "Direct link to Converting types")

Types are **not** automatically converted. For example, an integer is not automatically converted to a boolean, nor is an `Int32` automatically converted to an `Int8`, nor is an optional integer `Int?` automatically converted to a non-optional integer `Int`, or vice-versa.

`` _16

fun add(_ a: Int8, _ b: Int8): Int8 {

_16

return a + b

_16

}

_16

_16

// The arguments are not declared with a specific type, but they are inferred

_16

// to be `Int8` since the parameter types of the function `add` are `Int8`.

_16

add(1, 2) // is `3`

_16

_16

// Declare two constants which have type `Int32`.

_16

//

_16

let a: Int32 = 3_000_000_000

_16

let b: Int32 = 3_000_000_000

_16

_16

// Invalid: cannot pass arguments which have type `Int32` to parameters which have type `Int8`.

_16

//

_16

add(a, b) ``

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/types-and-type-system/type-safety.md)

[Previous

Type Annotations](/docs/language/types-and-type-system/type-annotations)[Next

Type Inference](/docs/language/types-and-type-system/type-inference)

###### Rate this page

😞😐😊

* [Assigning a new value to a variable](#assigning-a-new-value-to-a-variable)
* [Passing arguments to a function](#passing-arguments-to-a-function)
* [Converting types](#converting-types)