# Source: https://cadence-lang.org/docs/language/operators/arithmetic-logical-operators

Arithmetic and Logical Operators | Cadence



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
* Arithmetic and Logical Operators

On this page

# Arithmetic and Logical Operators

## Arithmetic operators[​](#arithmetic-operators "Direct link to Arithmetic operators")

The unary pefix operator `-` negates an integer:

`` _10

let a = 1

_10

-a // is `-1` ``

There are four binary arithmetic operators:

* Addition: `+`
* Subtraction: `-`
* Multiplication: `*`
* Division: `/`
* Remainder: `%`

`` _10

let a = 1 + 2

_10

// `a` is `3` ``

The arguments for the operators need to be of the same type. The result is always the same type as the arguments.

The division and remainder operators abort the program when the divisor is zero.

Arithmetic operations on the signed integer types `Int8`, `Int16`, `Int32`, `Int64`, `Int128`, `Int256`, and on the unsigned integer types `UInt8`, `UInt16`, `UInt32`, `UInt64`, `UInt128`, and `UInt256` do not cause values to overflow or underflow - the program will abort with a fatal overflow error.

`` _10

let a: UInt8 = 255

_10

_10

// Run-time error: The result `256` does not fit in the range of `UInt8`,

_10

// thus a fatal overflow error is raised and the program aborts

_10

//

_10

let b = a + 1 ``

`` _10

let a: Int8 = 100

_10

let b: Int8 = 100

_10

_10

// Run-time error: The result `10000` does not fit in the range of `Int8`,

_10

// thus a fatal overflow error is raised and the program aborts

_10

//

_10

let c = a * b ``

`` _10

let a: Int8 = -128

_10

_10

// Run-time error: The result `128` does not fit in the range of `Int8`,

_10

// thus a fatal overflow error is raised and the program aborts

_10

//

_10

let b = -a ``

Arithmetic operations on the unsigned integer types `Word8`, `Word16`, `Word32`, and `Word64` **can cause values to overflow or underflow**.

For example, the maximum value of an unsigned 8-bit integer is 255 (binary 11111111). Adding 1 results in an overflow, truncation to 8 bits, and the value 0:

`_10

// 11111111 = 255

_10

// + 1

_10

// = 100000000 = 0`

`` _10

let a: Word8 = 255

_10

a + 1 // is `0` ``

Similarly, for the minimum value 0, subtracting 1 wraps around and results in the maximum value 255:

`_10

// 00000000

_10

// - 1

_10

// = 11111111 = 255`

`` _10

let b: Word8 = 0

_10

b - 1 // is `255` ``

### Arithmetics on number super-types[​](#arithmetics-on-number-super-types "Direct link to Arithmetics on number super-types")

Arithmetic operators are not supported for number supertypes (`Number`, `SignedNumber`, `FixedPoint`, `SignedFixedPoint`, `Integer`, and `SignedInteger`), as they may or may not succeed at run-time:

`_10

let x: Integer = 3 as Int8

_10

let y: Integer = 4 as Int8

_10

_10

let z: Integer = x + y // Static error`

Values of these types must be cast to the desired type before performing the arithmetic operation:

`_10

let z: Integer = (x as! Int8) + (y as! Int8)`

## Logical operators[​](#logical-operators "Direct link to Logical operators")

Logical operators work with the boolean values `true` and `false`.

* Logical NOT: `!a`

  This unary prefix operator logically negates a boolean:

  `` _10

  let a = true

  _10

  !a // is `false` ``
* Logical AND: `a && b`

  `` _10

  true && true // is `true`

  _10

  _10

  true && false // is `false`

  _10

  _10

  false && true // is `false`

  _10

  _10

  false && false // is `false` ``

  If the left-hand side is false, the right-hand side is not evaluated.
* Logical OR: `a || b`

  `` _10

  true || true // is `true`

  _10

  _10

  true || false // is `true`

  _10

  _10

  false || true // is `true`

  _10

  _10

  false || false // is `false` ``

  If the left-hand side is true, the right-hand side is not evaluated.

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/operators/arithmetic-logical-operators.md)

[Previous

Assignment, Move, Force-Assignment, and Swapping Operators](/docs/language/operators/assign-move-force-swap)[Next

Comparison Operators](/docs/language/operators/comparison-operators)

###### Rate this page

😞😐😊

* [Arithmetic operators](#arithmetic-operators)
  + [Arithmetics on number super-types](#arithmetics-on-number-super-types)
* [Logical operators](#logical-operators)