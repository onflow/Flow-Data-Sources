# Source: https://cadence-lang.org/docs/language/constants-and-variables




Constants and Variable Declarations | Cadence




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
* Constants and Variable Declarations
# Constants and Variable Declarations

Constants and variables are declarations that bind
a value and [type](/docs/language/type-safety) to an identifier.
Constants are initialized with a value and cannot be reassigned afterwards.
Variables are initialized with a value and can be reassigned later.
Declarations can be created in any scope, including the global scope.

Constant means that the *identifier's* association is constant,
not the *value* itself –
the value may still be changed if it is mutable.

Constants are declared using the `let` keyword. Variables are declared
using the `var` keyword.
The keywords are followed by the identifier,
an optional [type annotation](/docs/language/type-annotations), an equals sign `=`,
and the initial value.

 `_15// Declare a constant named `a`._15//_15let a = 1_15_15// Invalid: re-assigning to a constant._15//_15a = 2_15_15// Declare a variable named `b`._15//_15var b = 3_15_15// Assign a new value to the variable named `b`._15//_15b = 4`

Variables and constants **must** be initialized.

 `_10// Invalid: the constant has no initial value._10//_10let a`

The names of the variable or constant
declarations in each scope must be unique.
Declaring another variable or constant with a name that is already
declared in the current scope is invalid, regardless of kind or type.

 `_23// Declare a constant named `a`._23//_23let a = 1_23_23// Invalid: cannot re-declare a constant with name `a`,_23// as it is already used in this scope._23//_23let a = 2_23_23// Declare a variable named `b`._23//_23var b = 3_23_23// Invalid: cannot re-declare a variable with name `b`,_23// as it is already used in this scope._23//_23var b = 4_23_23// Invalid: cannot declare a variable with the name `a`,_23// as it is already used in this scope,_23// and it is declared as a constant._23//_23var a = 5`

However, variables can be redeclared in sub-scopes.

 `_13// Declare a constant named `a`._13//_13let a = 1_13_13if true {_13 // Declare a constant with the same name `a`._13 // This is valid because it is in a sub-scope._13 // This variable is not visible to the outer scope._13_13 let a = 2_13}_13_13// `a` is `1``

A variable cannot be used as its own initial value.

 `_10// Invalid: Use of variable in its own initial value._10let a = a`[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/constants-and-variables.md)[PreviousSyntax](/docs/language/syntax)[NextType Annotations](/docs/language/type-annotations)Got suggestions for this site? 

* [It's open-source!](https://github.com/onflow/cadence-lang.org)
The source code of this site is licensed under the Apache License, Version 2.0.
Content is licensed under the Creative Commons Attribution 4.0 International License.

