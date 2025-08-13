# Source: https://cadence-lang.org/docs/language/values-and-types/min-max-saturation-floating-pt-nums

Minimum and Maximum Values, Saturation Arithmetic, and Floating-Point Numbers | Cadence



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Cadence](/img/logo.svg)![Cadence](/img/logo.svg)](/)

[Learn](/docs)[Playground](https://play.flow.com/)[Community](/community)[Security](https://flow.com/flow-responsible-disclosure/)[Language Reference](/docs/language)

Search

* [Introduction](/docs/)
* [Why Use Cadence?](/docs/why)
* [Cadence Guide for Solidity Developers](/docs/solidity-to-cadence)
* [Tutorial](/docs/tutorial/first-steps)
* [Language Reference](/docs/language/)

  + [Syntax](/docs/language/syntax)
  + [Constants and Variable Declarations](/docs/language/constants-and-variables)
  + [Values and Types](/docs/language/values-and-types/)

    - [Booleans, Numeric Literals, and Integers](/docs/language/values-and-types/booleans-numlits-ints)
    - [Fixed-Point Numbers and Functions](/docs/language/values-and-types/fixed-point-nums-ints)
    - [Minimum and Maximum Values, Saturation Arithmetic, and Floating-Point Numbers](/docs/language/values-and-types/min-max-saturation-floating-pt-nums)
    - [Addresses and Address Functions](/docs/language/values-and-types/addresses-functions)
    - [AnyStruct, AnyResource, Optionals, and Never](/docs/language/values-and-types/anystruct-anyresource-opts-never)
    - [Strings and Characters](/docs/language/values-and-types/strings-and-characters)
    - [Arrays](/docs/language/values-and-types/arrays)
    - [Dictionaries](/docs/language/values-and-types/dictionaries)
    - [InclusiveRange](/docs/language/values-and-types/inclusive-range)
  + [Types and Type System](/docs/language/types-and-type-system/)
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
  + [Glossary](/docs/language/glossary)
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
* [Values and Types](/docs/language/values-and-types/)
* Minimum and Maximum Values, Saturation Arithmetic, and Floating-Point Numbers

On this page

# Minimum and Maximum Values, Saturation Arithmetic, and Floating-Point Numbers

## Minimum and maximum values[​](#minimum-and-maximum-values "Direct link to Minimum and maximum values")

The minimum and maximum values for all integer and fixed-point number types are available through the fields `min` and `max`.

For example:

`` _10

let max = UInt8.max

_10

// `max` is 255, the maximum value of the type `UInt8` ``

`` _10

let max = UFix64.max

_10

// `max` is 184467440737.09551615, the maximum value of the type `UFix64` ``

## Saturation arithmetic[​](#saturation-arithmetic "Direct link to Saturation arithmetic")

Integers and fixed-point numbers support saturation arithmetic, which means that arithmetic operations, such as addition or multiplications, are saturating at the numeric bounds instead of overflowing.

* If the result of an operation is greater than the maximum value of the operands' type, the maximum is returned.
* If the result is lower than the minimum of the operands' type, the minimum is returned.

Saturating addition, subtraction, multiplication, and division are provided as functions with the prefix `saturating`:

* `Int8`, `Int16`, `Int32`, `Int64`, `Int128`, `Int256`, `Fix64`:

  + `saturatingAdd`
  + `saturatingSubtract`
  + `saturatingMultiply`
  + `saturatingDivide`
* `Int`:

  + none
* `UInt8`, `UInt16`, `UInt32`, `UInt64`, `UInt128`, `UInt256`, `UFix64`:

  + `saturatingAdd`
  + `saturatingSubtract`
  + `saturatingMultiply`
* `UInt`:

  + `saturatingSubtract`

`` _10

let a: UInt8 = 200

_10

let b: UInt8 = 100

_10

let result = a.saturatingAdd(b)

_10

// `result` is 255, the maximum value of the type `UInt8` ``

## Floating-point numbers[​](#floating-point-numbers "Direct link to Floating-point numbers")

There is **no** support for floating point numbers.

Smart Contracts are not intended to work with values that include error margins and therefore floating point arithmetic is not appropriate here.

Instead, consider using [fixed point numbers](/docs/language/values-and-types/fixed-point-nums-ints).

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/values-and-types/min-max-saturation-floating-pt-nums.md)

[Previous

Fixed-Point Numbers and Functions](/docs/language/values-and-types/fixed-point-nums-ints)[Next

Addresses and Address Functions](/docs/language/values-and-types/addresses-functions)

###### Rate this page

😞😐😊

* [Minimum and maximum values](#minimum-and-maximum-values)
* [Saturation arithmetic](#saturation-arithmetic)
* [Floating-point numbers](#floating-point-numbers)