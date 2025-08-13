# Source: https://cadence-lang.org/docs/language/accounts/paths

Paths | Cadence



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

    - [Paths](/docs/language/accounts/paths)
    - [Storage](/docs/language/accounts/storage)
    - [Capabilities](/docs/language/accounts/capabilities)
    - [Keys](/docs/language/accounts/keys)
    - [Contracts](/docs/language/accounts/contracts)
    - [Inbox](/docs/language/accounts/inbox)
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
* [Accounts](/docs/language/accounts/)
* Paths

On this page

# Paths

Account storage stores objects under paths. Paths consist of a domain and an identifier.

Paths start with the character `/`, followed by the domain, the path separator `/`, and finally the identifier. The identifier must start with a letter and can only be followed by letters, numbers, or the underscore `_`. For example, the path `/storage/test` has the domain `storage` and the identifier `test`.

There are two valid domains: `storage` and `public`.

Paths in the storage domain have type `StoragePath`, and paths in the public domain have the type `PublicPath`. Both `StoragePath` and `PublicPath` are subtypes of `Path`.

The `storage` domain stores storable objects, such as resources and structs. Objects stored under the `storage` domain are only accessible through account references, which are authorized with a storage entitlement.

The `public` domain stores capabilities, which are accessible by anyone.

## Path functions[​](#path-functions "Direct link to Path functions")

`_10

fun toString(): String`

Returns the string representation of the path.

`_10

let storagePath = /storage/path

_10

_10

storagePath.toString() // is "/storage/path"`

There are also utilities to produce paths from strings:

`_10

fun PublicPath(identifier: string): PublicPath?

_10

fun StoragePath(identifier: string): StoragePath?`

Each of these functions take an identifier and produce a path of the appropriate domain:

`_10

let pathID = "foo"

_10

let path = PublicPath(identifier: pathID) // is /public/foo`

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/accounts/paths.mdx)

[Previous

Accounts](/docs/language/accounts/)[Next

Storage](/docs/language/accounts/storage)

###### Rate this page

😞😐😊

* [Path functions](#path-functions)