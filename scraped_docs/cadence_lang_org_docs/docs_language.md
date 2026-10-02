# Source: https://cadence-lang.org/docs/language

The Cadence Programming Language | Cadence



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

* Language Reference

On this page

# The Cadence Programming Language

## Introduction[​](#introduction "Direct link to Introduction")

The Cadence Programming Language is a new high-level programming language intended for smart contract development.

The language's goals are, in order of importance:

* **Safety and security** — Provide a strong static type system, design by contract (preconditions and postconditions), and resources (inspired by linear types).
* **Auditability** — Focus on readability: Make it easy to verify what the code is doing, and make intentions explicit, at a small cost of verbosity.
* **Simplicity** — Focus on developer productivity and usability: Make it easy to write code and provide good tooling.

## Terminology[​](#terminology "Direct link to Terminology")

In this document, the following terminology is used to describe syntax or behavior that is not allowed in the language:

* `Invalid` means that the invalid program will not even be allowed to run. The program error is detected and reported statically by the type checker.
* `Run-time error` means that the erroneous program will run, but bad behavior will result in the execution of the program being aborted.

## Syntax and behavior[​](#syntax-and-behavior "Direct link to Syntax and behavior")

Much of the language's syntax is inspired by Swift, Kotlin, and TypeScript.

* Much of the syntax, types, and standard library is inspired by Swift, which popularized features including optionals and argument labels, and provides safe handling of integers and strings.
* Resources are based on linear types which were popularized by Rust.
* Events are inspired by Solidity.

info

In real Cadence code, all type definitions and code must be declared and contained in [contracts](/docs/language/contracts) or [transactions](/docs/language/transactions), but we omit these containers in examples for simplicity.

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/index.md)

[Previous

Voting Contract](/docs/tutorial/voting)[Next

Syntax and Glossary](/docs/language/syntax)

###### Rate this page

😞😐😊

* [Introduction](#introduction)
* [Terminology](#terminology)
* [Syntax and behavior](#syntax-and-behavior)