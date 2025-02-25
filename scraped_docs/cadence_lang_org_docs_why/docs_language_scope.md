# Source: https://cadence-lang.org/docs/language/scope

Scope | Cadence



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
* Scope

# Scope

Every function and block (`{` ... `}`) introduces a new scope for declarations.
Each function and block can refer to declarations in its scope or any of the outer scopes.

`_12

let x = 10

_12

_12

fun f(): Int {

_12

let y = 10

_12

return x + y

_12

}

_12

_12

f() // is `20`

_12

_12

// Invalid: the identifier `y` is not in scope.

_12

//

_12

y`

`_10

fun doubleAndAddOne(_ n: Int): Int {

_10

fun double(_ x: Int) {

_10

return x * 2

_10

}

_10

return double(n) + 1

_10

}

_10

_10

// Invalid: the identifier `double` is not in scope.

_10

//

_10

double(1)`

Each scope can introduce new declarations, i.e., the outer declaration is shadowed.

`_10

let x = 2

_10

_10

fun test(): Int {

_10

let x = 3

_10

return x

_10

}

_10

_10

test() // is `3``

Scope is lexical, not dynamic.

`_12

let x = 10

_12

_12

fun f(): Int {

_12

return x

_12

}

_12

_12

fun g(): Int {

_12

let x = 20

_12

return f()

_12

}

_12

_12

g() // is `10`, not `20``

Declarations are **not** moved to the top of the enclosing function (hoisted).

`_10

let x = 2

_10

_10

fun f(): Int {

_10

if x == 0 {

_10

let x = 3

_10

return x

_10

}

_10

return x

_10

}

_10

f() // is `2``

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/scope.md)

[Previous

Control Flow](/docs/language/control-flow)[Next

Type Safety](/docs/language/type-safety)

Got suggestions for this site?

* [It's open-source!](https://github.com/onflow/cadence-lang.org)

The source code of this site is licensed under the Apache License, Version 2.0.
Content is licensed under the Creative Commons Attribution 4.0 International License.