# Source: https://cadence-lang.org/docs/language/constants-and-variables

Constants and Variable Declarations | Cadence



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
* Constants and Variable Declarations

# Constants and Variable Declarations

Constants and variables are declarations that bind a value and [type](/docs/language/types-and-type-system/type-safety) to an identifier. Constants are initialized with a value and cannot be reassigned afterwards. Variables are initialized with a value and can be reassigned later. Declarations can be created in any scope, including the global scope.

Constant means that the *identifier's* association is constant, not the *value* itself — the value may still be changed if it is mutable. For example, you can change the values inside of a constant array, but you cannot replace the array assignment with a new array.

Constants are declared using the `let` keyword. Variables are declared using the `var` keyword. The keywords are followed by the identifier, an optional [type annotation](/docs/language/types-and-type-system/type-annotations), an equals sign `=`, and the initial value:

`` _15

// Declare a constant named `a`.

_15

//

_15

let a = 1

_15

_15

// Invalid: re-assigning to a constant.

_15

//

_15

a = 2

_15

_15

// Declare a variable named `b`.

_15

//

_15

var b = 3

_15

_15

// Assign a new value to the variable named `b`.

_15

//

_15

b = 4 ``

Variables and constants **must** be initialized:

`_10

// Invalid: the constant has no initial value.

_10

//

_10

let a`

The names of the variable or constant declarations in each scope must be unique. Declaring another variable or constant with a name that is already declared in the current scope is invalid, regardless of kind or type:

`` _23

// Declare a constant named `a`.

_23

//

_23

let a = 1

_23

_23

// Invalid: cannot re-declare a constant with name `a`,

_23

// as it is already used in this scope.

_23

//

_23

let a = 2

_23

_23

// Declare a variable named `b`.

_23

//

_23

var b = 3

_23

_23

// Invalid: cannot re-declare a variable with name `b`,

_23

// as it is already used in this scope.

_23

//

_23

var b = 4

_23

_23

// Invalid: cannot declare a variable with the name `a`,

_23

// as it is already used in this scope,

_23

// and it is declared as a constant.

_23

//

_23

var a = 5 ``

However, variables can be redeclared in sub-scopes:

`` _13

// Declare a constant named `a`.

_13

//

_13

let a = 1

_13

_13

if true {

_13

// Declare a constant with the same name `a`.

_13

// This is valid because it is in a sub-scope.

_13

// This variable is not visible to the outer scope.

_13

_13

let a = 2

_13

}

_13

_13

// `a` is `1` ``

A variable cannot be used as its own initial value:

`_10

// Invalid: Use of variable in its own initial value.

_10

let a = a`

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/constants-and-variables.md)

[Previous

Syntax](/docs/language/syntax)[Next

Values and Types](/docs/language/values-and-types/)