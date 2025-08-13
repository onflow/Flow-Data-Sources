# Source: https://cadence-lang.org/docs/language/types-and-type-system/type-annotations

Type Annotations | Cadence



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
* [Types and Type System](/docs/language/types-and-type-system/)
* Type Annotations

# Type Annotations

When declaring a constant or variable, an optional *type annotation* can be provided, to make it explicit what type the declaration has.

If no type annotation is provided, the type of the declaration is [inferred from the initial value](/docs/language/types-and-type-system/type-inference).

For function parameters, a type annotation must be provided:

`` _20

// Declare a variable named `boolVarWithAnnotation`, which has an explicit type annotation.

_20

//

_20

// `Bool` is the type of booleans.

_20

//

_20

var boolVarWithAnnotation: Bool = false

_20

_20

// Declare a constant named `integerWithoutAnnotation`, which has no type annotation

_20

// and for which the type is inferred to be `Int`, the type of arbitrary-precision integers.

_20

//

_20

// This is based on the initial value which is an integer literal.

_20

// Integer literals are always inferred to be of type `Int`.

_20

//

_20

let integerWithoutAnnotation = 1

_20

_20

// Declare a constant named `smallIntegerWithAnnotation`, which has an explicit type annotation.

_20

// Because of the explicit type annotation, the type is not inferred.

_20

// This declaration is valid because the integer literal `1` fits into the range of the type `Int8`,

_20

// the type of 8-bit signed integers.

_20

//

_20

let smallIntegerWithAnnotation: Int8 = 1 ``

If a type annotation is provided, the initial value must be of this type. All new values assigned to variables must match their type. This type safety is explained in more detail in [this article](/docs/language/types-and-type-system/type-safety):

`` _12

// Invalid: declare a variable with an explicit type `Bool`,

_12

// but the initial value has type `Int`.

_12

//

_12

let booleanConstant: Bool = 1

_12

_12

// Declare a variable that has the inferred type `Bool`.

_12

//

_12

var booleanVariable = false

_12

_12

// Invalid: assign a value with type `Int` to a variable which has the inferred type `Bool`.

_12

//

_12

booleanVariable = 1 ``

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/types-and-type-system/type-annotations.md)

[Previous

Types and Type System](/docs/language/types-and-type-system/)[Next

Type Safety](/docs/language/types-and-type-system/type-safety)