# Source: https://cadence-lang.org/docs/language/operators/bitwise-ternary-operators

Bitwise and Ternary Conditional Operators | Cadence



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
* Bitwise and Ternary Conditional Operators

On this page

# Bitwise and Ternary Conditional Operators

## Bitwise operators[​](#bitwise-operators "Direct link to Bitwise operators")

Bitwise operators enable the manipulation of individual bits of unsigned and signed integers. They're often used in low-level programming.

* Bitwise AND: `a & b`

  Returns a new integer whose bits are 1 only if the bits were 1 in *both* input integers:

  `_10

  let firstFiveBits = 0b11111000

  _10

  let lastFiveBits = 0b00011111

  _10

  let middleTwoBits = firstFiveBits & lastFiveBits // is 0b00011000`
* Bitwise OR: `a | b`

  Returns a new integer whose bits are 1 only if the bits were 1 in *either* input integers:

  `_10

  let someBits = 0b10110010

  _10

  let moreBits = 0b01011110

  _10

  let combinedbits = someBits | moreBits // is 0b11111110`
* Bitwise XOR: `a ^ b`

  Returns a new integer whose bits are 1 where the input bits are different, and are 0 where the input bits are the same:

  `_10

  let firstBits = 0b00010100

  _10

  let otherBits = 0b00000101

  _10

  let outputBits = firstBits ^ otherBits // is 0b00010001`

### Bitwise shifting operators[​](#bitwise-shifting-operators "Direct link to Bitwise shifting operators")

* Bitwise LEFT SHIFT: `a << b`

  Returns a new integer with all bits moved to the left by a certain number of places:

  `_10

  let someBits = 4 // is 0b00000100

  _10

  let shiftedBits = someBits << 2 // is 0b00010000`
* Bitwise RIGHT SHIFT: `a >> b`

  Returns a new integer with all bits moved to the right by a certain number of places:

  `_10

  let someBits = 8 // is 0b00001000

  _10

  let shiftedBits = someBits >> 2 // is 0b00000010`

For unsigned integers, the bitwise shifting operators perform [logical shifting](https://en.wikipedia.org/wiki/Logical_shift); for signed integers, they perform [arithmetic shifting](https://en.wikipedia.org/wiki/Arithmetic_shift). Also note that for `a << b` or `a >> b`, `b` must fit into a 64-bit integer.

## Ternary conditional operator[​](#ternary-conditional-operator "Direct link to Ternary conditional operator")

There is only one ternary conditional operator (e.g., `a ? b : c`).

It behaves like an if-statement, but is an expression: if the first operator value is true, the second operator value is returned. If the first operator value is false, the third value is returned.

The first value must be a boolean, or resolve to one (and must have the type `Bool`). The second value and third value can be of any type. The result type is the least common supertype of the second and third value.

`` _10

let x = 1 > 2 ? 3 : 4

_10

// `x` is `4` and has type `Int`

_10

_10

let y = 1 > 2 ? nil : 3

_10

// `y` is `3` and has type `Int?` ``

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/operators/bitwise-ternary-operators.md)

[Previous

Comparison Operators](/docs/language/operators/comparison-operators)[Next

Casting Operators](/docs/language/operators/casting-operators)

###### Rate this page

😞😐😊

* [Bitwise operators](#bitwise-operators)
  + [Bitwise shifting operators](#bitwise-shifting-operators)
* [Ternary conditional operator](#ternary-conditional-operator)