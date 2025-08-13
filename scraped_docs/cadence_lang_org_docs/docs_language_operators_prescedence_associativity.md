# Source: https://cadence-lang.org/docs/language/operators/prescedence-associativity

Prescedence and Associativity | Cadence



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
* Prescedence and Associativity

# Prescedence and Associativity

Operators have the following precedences, from highest to lowest:

* Unary precedence: `-`, `!`, `<-`
* Cast precedence: `as`, `as?`, `as!`
* Multiplication precedence: `*`, `/`, `%`
* Addition precedence: `+`, `-`
* Bitwise shift precedence: `<<`, `>>`
* Bitwise conjunction precedence: `&`
* Bitwise exclusive disjunction precedence: `^`
* Bitwise disjunction precedence: `|`
* Nil-coalescing precedence: `??`
* Relational precedence: `<`, `<=`, `>`, `>=`
* Equality precedence: `==`, `!=`
* Logical conjunction precedence: `&&`
* Logical disjunction precedence: `||`
* Ternary precedence: `? :`

All operators are left-associative, except for the following operators, which are right-associative:

* Ternary operator
* Nil-coalescing operator

Expressions can be wrapped in parentheses to override precedence conventions (i.e., an alternate order should be indicated), or when the default order should be emphasized (e.g., to avoid confusion). For example, `(2 + 3) * 4` forces addition to precede multiplication, and `5 + (6 * 7)` reinforces the default order.

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/operators/prescedence-associativity.md)

[Previous

Optional Operators](/docs/language/operators/optional-operators)[Next

Accounts](/docs/language/accounts/)