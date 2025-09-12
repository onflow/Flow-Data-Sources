# Source: https://cadence-lang.org/docs/language/operators/casting-operators

Casting Operators | Cadence



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
  + [Operators](/docs/language/operators/)

    - [Assignment, Move, Force-Assignment, and Swapping Operators](/docs/language/operators/assign-move-force-swap)
    - [Arithmetic and Logical Operators](/docs/language/operators/arithmetic-logical-operators)
    - [Comparison Operators](/docs/language/operators/comparison-operators)
    - [Bitwise and Ternary Conditional Operators](/docs/language/operators/bitwise-ternary-operators)
    - [Casting Operators](/docs/language/operators/casting-operators)
    - [Optional Operators](/docs/language/operators/optional-operators)
    - [Prescedence and Associativity](/docs/language/operators/prescedence-associativity)
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
* [Operators](/docs/language/operators/)
* Casting Operators

On this page

# Casting Operators

## Static casting operator (`as`)[​](#static-casting-operator-as "Direct link to static-casting-operator-as")

The static casting operator `as` can be used to statically type cast a value to a type.

If the static type of the value is a subtype of the given type (the *target* type), the operator returns the value as the given type.

The cast is performed statically (i.e., when the program is type-checked). Only the static type of the value is considered — not the run-time type of the value.

This means it is not possible to downcast using this operator. Consider using the [conditional downcasting operator `as?`](#conditional-downcasting-operator-as) instead.

`` _22

// Declare a constant named `integer` which has type `Int`.

_22

//

_22

let integer: Int = 1

_22

_22

// Statically cast the value of `integer` to the supertype `Number`.

_22

// The cast succeeds, because the type of the variable `integer`,

_22

// the type `Int`, is a subtype of type `Number`.

_22

// This is an upcast.

_22

//

_22

let number = integer as Number

_22

// `number` is `1` and has type `Number`

_22

_22

// Declare a constant named `something` which has type `AnyStruct`,

_22

// with an initial value which has type `Int`.

_22

//

_22

let something: AnyStruct = 1

_22

_22

// Statically cast the value of `something` to `Int`.

_22

// This is invalid, the cast fails, because the static type of the value is type `AnyStruct`,

_22

// which is not a subtype of type `Int`.

_22

//

_22

let result = something as Int ``

## Conditional downcasting operator (`as?`)[​](#conditional-downcasting-operator-as "Direct link to conditional-downcasting-operator-as")

The conditional downcasting operator `as?` can be used to dynamically type cast a value to a type. The operator returns an optional. If the value has a run-time type that is a subtype of the target type the operator returns the value as the target type; otherwise, the result is `nil`.

The cast is performed at run-time (when the program is executed) and not statically (when the program is checked).

`` _17

// Declare a constant named `something` which has type `AnyStruct`,

_17

// with an initial value which has type `Int`.

_17

//

_17

let something: AnyStruct = 1

_17

_17

// Conditionally downcast the value of `something` to `Int`.

_17

// The cast succeeds, because the value has type `Int`.

_17

//

_17

let number = something as? Int

_17

// `number` is `1` and has type `Int?`

_17

_17

// Conditionally downcast the value of `something` to `Bool`.

_17

// The cast fails, because the value has type `Int`,

_17

// and `Bool` is not a subtype of `Int`.

_17

//

_17

let boolean = something as? Bool

_17

// `boolean` is `nil` and has type `Bool?` ``

Downcasting works for concrete types, but also works for nested types (e.g., arrays), interfaces, optionals, and so on.

`` _10

// Declare a constant named `values` which has type `[AnyStruct]`,

_10

// i.e. an array of arbitrarily typed values.

_10

//

_10

let values: [AnyStruct] = [1, true]

_10

_10

let first = values[0] as? Int

_10

// `first` is `1` and has type `Int?`

_10

_10

let second = values[1] as? Bool

_10

// `second` is `true` and has type `Bool?` ``

## Force-downcasting operator (`as!`)[​](#force-downcasting-operator-as "Direct link to force-downcasting-operator-as")

The force-downcasting operator `as!` behaves like the [conditional downcasting operator `as?`](#conditional-downcasting-operator-as). However, if the cast succeeds, it returns a value of the given type instead of an optional; if the cast fails, it aborts the program instead of returning `nil`:

`` _17

// Declare a constant named `something` which has type `AnyStruct`,

_17

// with an initial value which has type `Int`.

_17

//

_17

let something: AnyStruct = 1

_17

_17

// Force-downcast the value of `something` to `Int`.

_17

// The cast succeeds, because the value has type `Int`.

_17

//

_17

let number = something as! Int

_17

// `number` is `1` and has type `Int`

_17

_17

// Force-downcast the value of `something` to `Bool`.

_17

// The cast fails, because the value has type `Int`,

_17

// and `Bool` is not a subtype of `Int`.

_17

//

_17

let boolean = something as! Bool

_17

// Run-time error ``

## Implicit casting[​](#implicit-casting "Direct link to Implicit casting")

Cadence does not allow implicit casting (coercion).

`_10

let value: UInt8 = 1

_10

_10

// invalid: implicit cast

_10

let intValue: Int = value`

Instead, conversion must be explicitly performed by calling a conversion function.
Cadence provides a conversion function for each number type. The functions have the same name as the type, accept any number, and return the number type.
If the value cannot be converted, the function panics.

For example, for the type `Int`, the conversion function `fun Int(_ number: Number): Int` is provided.

For example, to convert a `UInt8` value to an `Int` value:

`_10

let value: UInt8 = 1

_10

let intValue = Int(value)`

See [Number type casting](/docs/language/values-and-types/fixed-point-nums-ints#number-type-casting) for more information.

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/operators/casting-operators.md)

[Previous

Bitwise and Ternary Conditional Operators](/docs/language/operators/bitwise-ternary-operators)[Next

Optional Operators](/docs/language/operators/optional-operators)

###### Rate this page

😞😐😊

* [Static casting operator (`as`)](#static-casting-operator-as)
* [Conditional downcasting operator (`as?`)](#conditional-downcasting-operator-as)
* [Force-downcasting operator (`as!`)](#force-downcasting-operator-as)
* [Implicit casting](#implicit-casting)