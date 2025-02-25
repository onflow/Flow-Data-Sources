# Source: https://cadence-lang.org/docs/language/enumerations

Enumerations | Cadence



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Cadence](/img/logo.svg)![Cadence](/img/logo.svg)](/)

[Learn](/learn)[Solidity Guide](/docs/solidity-to-cadence)[Playground](https://play.flow.com/)[Community](/community)[Security](https://flow.com/flow-responsible-disclosure/)[Documentation](/docs/)[1.0](/docs/)

Search

* [Introduction](/docs/)
* [Why Use Cadence?](/docs/why)
* [Tutorial](/docs/tutorial/first-steps)
* [Language Reference](/docs/language/)

  + [Syntax](/docs/language/syntax)
  + [Constants and Variable Declarations](/docs/language/constants-and-variables)
  + [Type Annotations](/docs/language/type-annotations)
  + [Values and Types](/docs/language/values-and-types)
  + [Operators](/docs/language/operators)
  + [Functions](/docs/language/functions)
  + [Control Flow](/docs/language/control-flow)
  + [Scope](/docs/language/scope)
  + [Type Safety](/docs/language/type-safety)
  + [Type Inference](/docs/language/type-inference)
  + [Composite Types](/docs/language/composite-types)
  + [Resources](/docs/language/resources)
  + [Access control](/docs/language/access-control)
  + [Capabilities](/docs/language/capabilities)
  + [Interfaces](/docs/language/interfaces)
  + [Enumerations](/docs/language/enumerations)
  + [Intersection Types](/docs/language/intersection-types)
  + [References](/docs/language/references)
  + [Imports](/docs/language/imports)
  + [Accounts](/docs/language/accounts/)
  + [Attachments](/docs/language/attachments)
  + [Contracts](/docs/language/contracts)
  + [Contract Updatability](/docs/language/contract-updatability)
  + [Transactions](/docs/language/transactions)
  + [Events](/docs/language/events)
  + [Core Events](/docs/language/core-events)
  + [Run-time Types](/docs/language/run-time-types)
  + [Built-in Functions](/docs/language/built-in-functions)
  + [Environment Information](/docs/language/environment-information)
  + [Crypto](/docs/language/crypto)
  + [Type Hierarchy](/docs/language/type-hierarchy)
  + [Glossary](/docs/language/glossary)
* [Cadence 1.0 Migration Guide](/docs/cadence-migration-guide/)
* [Design Patterns](/docs/design-patterns)
* [Anti-Patterns](/docs/anti-patterns)
* [Development Standards](/docs/project-development-tips)
* [Security Best Practices](/docs/security-best-practices)
* [Cadence Guide for Solidity Developers](/docs/solidity-to-cadence)
* [Contract Upgrades with Incompatible Changes](/docs/contract-upgrades)
* [JSON-Cadence format](/docs/json-cadence-spec)
* [Measuring Time](/docs/measuring-time)
* [Testing](/docs/testing-framework)

* [Language Reference](/docs/language/)
* Enumerations

On this page

# Enumerations

Enumerations are sets of symbolic names bound to unique, constant values,
which can be compared by identity.

## Enum Declaration[​](#enum-declaration "Direct link to Enum Declaration")

Enums are declared using the `enum` keyword,
followed by the name of the enum, the raw type after a colon,
and the requirements, which must be enclosed in opening and closing braces.

The raw type must be an integer subtype, e.g. `UInt8` or `Int128`.

Enum cases are declared using the `case` keyword,
followed by the name of the enum case.

Enum cases must be unique.
Each enum case has a raw value, the index of the case in all cases.

The raw value of an enum case can be accessed through the `rawValue` field.

The enum cases can be accessed by using the name as a field on the enum,
or by using the enum constructor,
which requires providing the raw value as an argument.
The enum constructor returns the enum case with the given raw value,
if any, or `nil` if no such case exists.

Enum cases can be compared using the equality operators `==` and `!=`.

`_36

// Declare an enum named `Color` which has the raw value type `UInt8`,

_36

// and declare three enum cases: `red`, `green`, and `blue`

_36

//

_36

access(all)

_36

enum Color: UInt8 {

_36

_36

access(all)

_36

case red

_36

_36

access(all)

_36

case green

_36

_36

access(all)

_36

case blue

_36

}

_36

// Declare a variable which has the enum type `Color` and initialize

_36

// it to the enum case `blue` of the enum

_36

let blue: Color = Color.blue

_36

// Get the raw value of the enum case `blue`.

_36

// As it is the third case, so it has index 2

_36

//

_36

blue.rawValue // is `2`

_36

// Get the `green` enum case of the enum `Color` by using the enum

_36

// constructor and providing the raw value of the enum case `green`, 1,

_36

// as the enum case `green` is the second case, so it has index 1

_36

//

_36

let green: Color? = Color(rawValue: 1) // is `Color.green`

_36

// Get the enum case of the enum `Color` that has the raw value 5.

_36

// As there are only three cases, the maximum raw value / index is 2.

_36

//

_36

let nothing = Color(rawValue: 5) // is `nil`

_36

// Enum cases can be compared

_36

Color.red == Color.red // is `true`

_36

Color(rawValue: 1) == Color.green // is `true`

_36

// Different enum cases are not the same

_36

Color.red != Color.blue // is `true``

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/enumerations.md)

[Previous

Interfaces](/docs/language/interfaces)[Next

Intersection Types](/docs/language/intersection-types)

###### Rate this page

😞😐😊

* [Enum Declaration](#enum-declaration)

Got suggestions for this site?

* [It's open-source!](https://github.com/onflow/cadence-lang.org)

The source code of this site is licensed under the Apache License, Version 2.0.
Content is licensed under the Creative Commons Attribution 4.0 International License.