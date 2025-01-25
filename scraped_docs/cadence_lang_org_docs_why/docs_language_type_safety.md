# Source: https://cadence-lang.org/docs/language/type-safety




Type Safety | Cadence




[Skip to main content](#__docusaurus_skipToContent_fallback)[![Cadence](/img/logo.svg)![Cadence](/img/logo.svg)](/)[Learn](/learn)[Solidity Guide](/docs/solidity-to-cadence)[Playground](https://play.flow.com/)[Community](/community)[Security](https://flow.com/flow-responsible-disclosure/)[Documentation](/docs/)[1.0](/docs/)Search

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
* Type Safety
# Type Safety

The Cadence programming language is a *type-safe* language.

When assigning a new value to a variable, the value must be the same type as the variable.
For example, if a variable has type `Bool`,
it can *only* be assigned a value that has type `Bool`,
and not for example a value that has type `Int`.

 `_10// Declare a variable that has type `Bool`._10var a = true_10_10// Invalid: cannot assign a value that has type `Int` to a variable which has type `Bool`._10//_10a = 0`

When passing arguments to a function,
the types of the values must match the function parameters' types.
For example, if a function expects an argument that has type `Bool`,
*only* a value that has type `Bool` can be provided,
and not for example a value which has type `Int`.

 `_10fun nand(_ a: Bool, _ b: Bool): Bool {_10 return !(a && b)_10}_10_10nand(false, false) // is `true`_10_10// Invalid: The arguments of the function calls are integers and have type `Int`,_10// but the function expects parameters booleans (type `Bool`)._10//_10nand(0, 0)`

Types are **not** automatically converted.
For example, an integer is not automatically converted to a boolean,
nor is an `Int32` automatically converted to an `Int8`,
nor is an optional integer `Int?`
automatically converted to a non-optional integer `Int`,
or vice-versa.

 `_16fun add(_ a: Int8, _ b: Int8): Int8 {_16 return a + b_16}_16_16// The arguments are not declared with a specific type, but they are inferred_16// to be `Int8` since the parameter types of the function `add` are `Int8`._16add(1, 2) // is `3`_16_16// Declare two constants which have type `Int32`._16//_16let a: Int32 = 3_000_000_000_16let b: Int32 = 3_000_000_000_16_16// Invalid: cannot pass arguments which have type `Int32` to parameters which have type `Int8`._16//_16add(a, b)`[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/type-safety.md)[PreviousScope](/docs/language/scope)[NextType Inference](/docs/language/type-inference)Got suggestions for this site? 

* [It's open-source!](https://github.com/onflow/cadence-lang.org)
The source code of this site is licensed under the Apache License, Version 2.0.
Content is licensed under the Creative Commons Attribution 4.0 International License.

