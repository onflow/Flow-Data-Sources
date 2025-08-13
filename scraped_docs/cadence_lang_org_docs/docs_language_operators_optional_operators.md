# Source: https://cadence-lang.org/docs/language/operators/optional-operators

Optional Operators | Cadence



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
* [Operators](/docs/language/operators/)
* Optional Operators

On this page

# Optional Operators

## Nil-coalescing operator (`??`)[​](#nil-coalescing-operator- "Direct link to nil-coalescing-operator-")

The nil-coalescing operator `??` returns the value inside an optional if it contains a value, or returns an alternative value if the optional has no value (i.e., the optional value is `nil`).

If the left-hand side is non-nil, the right-hand side is not evaluated:

`` _10

// Declare a constant which has an optional integer type

_10

//

_10

let a: Int? = nil

_10

_10

// Declare a constant with a non-optional integer type,

_10

// which is initialized to `a` if it is non-nil, or 42 otherwise.

_10

//

_10

let b: Int = a ?? 42

_10

// `b` is 42, as `a` is nil ``

The nil-coalescing operator can only be applied to values that have an optional type:

`` _10

// Declare a constant with a non-optional integer type.

_10

//

_10

let a = 1

_10

_10

// Invalid: nil-coalescing operator is applied to a value which has a non-optional type

_10

// (a has the non-optional type `Int`).

_10

//

_10

let b = a ?? 2 ``

`` _10

// Invalid: nil-coalescing operator is applied to a value which has a non-optional type

_10

// (the integer literal is of type `Int`).

_10

//

_10

let c = 1 ?? 2 ``

The type of the right-hand side of the operator (the alternative value) must be a subtype of the type of left-hand side. This means that the right-hand side of the operator must be the non-optional or optional type matching the type of the left-hand side:

`` _11

// Declare a constant with an optional integer type.

_11

//

_11

let a: Int? = nil

_11

let b: Int? = 1

_11

let c = a ?? b

_11

// `c` is `1` and has type `Int?`

_11

_11

// Invalid: nil-coalescing operator is applied to a value of type `Int?`,

_11

// but the alternative has type `Bool`.

_11

//

_11

let d = a ?? false ``

## Force unwrap operator (`!`)[​](#force-unwrap-operator- "Direct link to force-unwrap-operator-")

The force-unwrap operator (`!`) returns the value inside an optional if it contains a value, or panics and aborts the execution if the optional has no value (i.e., the optional value is `nil`):

`` _19

// Declare a constant which has an optional integer type

_19

//

_19

let a: Int? = nil

_19

_19

// Declare a constant with a non-optional integer type,

_19

// which is initialized to `a` if `a` is non-nil.

_19

// If `a` is nil, the program aborts.

_19

//

_19

let b: Int = a!

_19

// The program aborts because `a` is nil.

_19

_19

// Declare another optional integer constant

_19

let c: Int? = 3

_19

_19

// Declare a non-optional integer

_19

// which is initialized to `c` if `c` is non-nil.

_19

// If `c` is nil, the program aborts.

_19

let d: Int = c!

_19

// `d` is initialized to 3 because c isn't nil. ``

The force-unwrap operator can only be applied to values that have an optional type:

`` _10

// Declare a constant with a non-optional integer type.

_10

//

_10

let a = 1

_10

_10

// Invalid: force-unwrap operator is applied to a value which has a

_10

// non-optional type (`a` has the non-optional type `Int`).

_10

//

_10

let b = a! ``

`` _10

// Invalid: The force-unwrap operator is applied

_10

// to a value which has a non-optional type

_10

// (the integer literal is of type `Int`).

_10

//

_10

let c = 1! ``

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/operators/optional-operators.md)

[Previous

Casting Operators](/docs/language/operators/casting-operators)[Next

Prescedence and Associativity](/docs/language/operators/prescedence-associativity)

###### Rate this page

😞😐😊

* [Nil-coalescing operator (`??`)](#nil-coalescing-operator-)
* [Force unwrap operator (`!`)](#force-unwrap-operator-)