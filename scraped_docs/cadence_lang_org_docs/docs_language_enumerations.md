# Source: https://cadence-lang.org/docs/language/enumerations

Enumerations | Cadence



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
* Enumerations

On this page

# Enumerations

Enumerations are sets of symbolic names bound to unique, constant values, which can be compared by identity.

## Enum declaration[​](#enum-declaration "Direct link to Enum declaration")

Enums are declared using the `enum` keyword, followed by the name of the enum, the raw type after a colon, and the requirements, which must be enclosed in opening and closing braces.

The raw type must be an integer subtype (e.g., `UInt8` or `Int128`).

Enum cases are declared using the `case` keyword, followed by the name of the enum case.

Enum cases must be unique. Each enum case has a raw value, which is the index of the case among all cases.

The raw value of an enum case can be accessed through the `rawValue` field.

The enum cases can be accessed by using the name as a field on the enum or by using the enum constructor, which requires providing the raw value as an argument. The enum constructor returns the enum case with the given raw value, if any, or `nil` if no such case exists.

Enum cases can be compared using the equality operators `==` and `!=`.

## Working with an enum declaration[​](#working-with-an-enum-declaration "Direct link to Working with an enum declaration")

1. Declare an enum named `Color`, which has the raw value type `UInt8`, and declare three enum cases (`red`, `green`, and `blue`):

   `_12

   access(all)

   _12

   enum Color: UInt8 {

   _12

   _12

   access(all)

   _12

   case red

   _12

   _12

   access(all)

   _12

   case green

   _12

   _12

   access(all)

   _12

   case blue

   _12

   }`
2. Declare a variable that has the enum type `Color` and initialize it to the enum case `blue` of the enum:

   `_10

   let blue: Color = Color.blue`
3. Get the raw value of the enum case `blue`. Since it is the third case, it has an index of 2:

   `` _10

   blue.rawValue // is `2` ``
4. Get the `green` enum case of the enum `Color` by using the enum constructor and providing the raw value of the enum case `green`, 1. Since the enum case `green` is the second case, it has an index of 1:

   `` _10

   let green: Color? = Color(rawValue: 1) // is `Color.green` ``
5. Get the enum case of the enum `Color` with the raw value 5. As there are only three cases, the maximum raw value/index is 2:

   `` _10

   let nothing = Color(rawValue: 5) // is `nil` ``

   Enum cases can be compared:

   `` _10

   Color.red == Color.red // is `true`

   _10

   Color(rawValue: 1) == Color.green // is `true` ``

   Different enum cases are not the same:

   `` _10

   Color.red != Color.blue // is `true` ``
6. Use an enum as part of a control flow statement.

   `_13

   fun applyPaint(_ paint: Color): String {

   _13

   // Directly test the value of the enum paint

   _13

   switch paint {

   _13

   case Color.red:

   _13

   return "red"

   _13

   case Color.blue:

   _13

   return "blue"

   _13

   case Color.green:

   _13

   return "green"

   _13

   default

   _13

   return "unsupported color"

   _13

   }

   _13

   }`

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/enumerations.md)

[Previous

Interfaces](/docs/language/interfaces)[Next

References](/docs/language/references)

###### Rate this page

😞😐😊

* [Enum declaration](#enum-declaration)
* [Working with an enum declaration](#working-with-an-enum-declaration)