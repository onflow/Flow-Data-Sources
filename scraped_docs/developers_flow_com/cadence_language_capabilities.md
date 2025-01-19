# Source: https://developers.flow.com/cadence/language/capabilities




Capabilities | Cadence




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
* Capabilities
On this page
# Capabilities

Cadence supports [capability-based security](https://en.wikipedia.org/wiki/Capability-based_security)
through the [object-capability model](https://en.wikipedia.org/wiki/Object-capability_model).

A capability in Cadence is a value that represents the right
to access an object and perform certain operations on it.
A capability specifies *what* can be accessed, and *how* it can be accessed.

Capabilities are unforgeable, transferable, and revocable.

Capabilities can be storage capabilities or account capabilities:

* **Storage capabilities** grant access to [objects in account storage](/docs/language/accounts/storage),
  via [paths](/docs/language/accounts/paths)
* **Account capabilities** grant access to [accounts](/docs/language/accounts/)

Capabilities can be borrowed to get a [reference](/docs/language/references) to the stored object or the account it refers to.

Capabilities have the type `Capability<T: &Any>`.
The type parameter specifies the kind of reference that can be obtained when borrowing the capability.
The type specifies the associated set of access rights through [entitlements](/docs/language/access-control):
the reference type of the capability can be authorized,
which grants the owner of the capability the ability to access the fields and functions of the target
which require the given entitlements.

For example, a capability which has type `Capability<auth(SaveValue) &Account>`
grants access to an account, and allows saving a value into the account.

Each capability has an ID.
The ID is unique **per account/address**.

Capabilities are created and managed through [capability controllers](/docs/language/accounts/capabilities).

Capabilities are structs, so they are copyable.
They can be used (e.g. borrowed) arbitrarily many times, as long as the target capability controller has not been deleted.

## `Capability`[​](#capability "Direct link to capability")

 `_31access(all)_31struct Capability<T: &Any> {_31 _31 /// The address of the account which the capability targets._31 access(all)_31 let address: Address_31_31 /// The ID of the capability._31 access(all)_31 let id: UInt64_31_31 /// Returns a reference to the targeted object._31 ///_31 /// If the capability is revoked, the function returns nil._31 ///_31 /// If the capability targets an object in account storage,_31 /// and and no object is stored at the target storage path,_31 /// the function returns nil._31 ///_31 /// If the targeted object cannot be borrowed using the given type,_31 /// the function panics._31 ///_31 access(all)_31 view fun borrow(): T?_31_31 /// Returns true if the capability currently targets an object_31 /// that satisfies the given type, i.e. could be borrowed using the given type._31 ///_31 access(all)_31 view fun check(): Bool_31}`[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/capabilities.md)[PreviousAccess control](/docs/language/access-control)[NextInterfaces](/docs/language/interfaces)
###### Rate this page

😞😐😊

* [`Capability`](#capability)
Got suggestions for this site? 

* [It's open-source!](https://github.com/onflow/cadence-lang.org)
The source code of this site is licensed under the Apache License, Version 2.0.
Content is licensed under the Creative Commons Attribution 4.0 International License.

