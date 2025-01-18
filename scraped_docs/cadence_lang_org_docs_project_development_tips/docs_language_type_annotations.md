# Source: https://cadence-lang.org/docs/language/type-annotations




Type Annotations | Cadence




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
* [Guide for Solidity Developers](/docs/solidity-to-cadence)
* [Contract Upgrades with Incompatible Changes](/docs/contract-upgrades)
* [JSON-Cadence format](/docs/json-cadence-spec)
* [Measuring Time](/docs/measuring-time)
* [Testing](/docs/testing-framework)


* [Language Reference](/docs/language/)
* Type Annotations
# Type Annotations

When declaring a constant or variable,
an optional *type annotation* can be provided,
to make it explicit what type the declaration has.

If no type annotation is provided, the type of the declaration is
[inferred from the initial value](/docs/language/type-inference).

For function parameters a type annotation must be provided.

 `_20// Declare a variable named `boolVarWithAnnotation`, which has an explicit type annotation._20//_20// `Bool` is the type of booleans._20//_20var boolVarWithAnnotation: Bool = false_20_20// Declare a constant named `integerWithoutAnnotation`, which has no type annotation_20// and for which the type is inferred to be `Int`, the type of arbitrary-precision integers._20//_20// This is based on the initial value which is an integer literal._20// Integer literals are always inferred to be of type `Int`._20//_20let integerWithoutAnnotation = 1_20_20// Declare a constant named `smallIntegerWithAnnotation`, which has an explicit type annotation._20// Because of the explicit type annotation, the type is not inferred._20// This declaration is valid because the integer literal `1` fits into the range of the type `Int8`,_20// the type of 8-bit signed integers._20//_20let smallIntegerWithAnnotation: Int8 = 1`

If a type annotation is provided, the initial value must be of this type.
All new values assigned to variables must match its type.
This type safety is explained in more detail in a [separate section](/docs/language/type-safety).

 `_12// Invalid: declare a variable with an explicit type `Bool`,_12// but the initial value has type `Int`._12//_12let booleanConstant: Bool = 1_12_12// Declare a variable that has the inferred type `Bool`._12//_12var booleanVariable = false_12_12// Invalid: assign a value with type `Int` to a variable which has the inferred type `Bool`._12//_12booleanVariable = 1`[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/type-annotations.md)[PreviousConstants and Variable Declarations](/docs/language/constants-and-variables)[NextValues and Types](/docs/language/values-and-types)Got suggestions for this site? 

* [It's open-source!](https://github.com/onflow/cadence-lang.org)
The source code of this site is licensed under the Apache License, Version 2.0.
Content is licensed under the Creative Commons Attribution 4.0 International License.

