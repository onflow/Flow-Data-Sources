# Source: https://cadence-lang.org/docs/language/intersection-types




Intersection Types | Cadence




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
* Intersection Types
# Intersection Types

Interface types cannot be used in type annotations directly;
instead they must be used as part of intersection types.
An intersection type represents a value that conforms to all of the interfaces listed in the intersection.

The syntax of a intersection type is `{U1, U2, ... Un}`,
where the types `U1` to `Un` are the interfaces that the type conforms to.

The members and functions of any of the set of interfaces are available.

Intersection types are useful for writing functions that work on a variety of different inputs.
For example, by using an intersection type for a parameter's type,
the function may accept any concrete value that implements all the interfaces in that intersection.
The value is restricted to the functionality of the intersection;
if the function accidentally attempts to access other functionality,
this is prevented by the static checker.

 `_50access(all)_50struct interface HasID {_50 access(all)_50 let id: String_50}_50_50access(all)_50struct A: HasID {_50_50 access(all)_50 let id: String_50_50 init(id: String) {_50 self.id = id_50 }_50}_50_50access(all)_50struct B: HasID {_50_50 access(all)_50 let id: String_50_50 init(id: String) {_50 self.id = id_50 }_50}_50_50// Create two instances, one of type `A`, and one of type `B`._50// Both types conform to interface `HasID`, so the structs can be assigned_50// to variables with type `{HasID}`: Some resource type which only allows_50// access to the functionality of resource interface `HasID`_50_50let hasID1: {HasID} = A(id: "1")_50let hasID2: {HasID} = B(id: "2")_50_50// Declare a function named `getID` which has one parameter with type `{HasID}`._50// The type `{HasID}` is a short-hand for `AnyStruct{HasID}`:_50// Some structure which only allows access to the functionality of interface `HasID`._50//_50access(all)_50fun getID(_ value: {HasID}): String {_50 return value.id_50}_50_50let id1 = getID(hasID1)_50// `id1` is "1"_50_50let id2 = getID(hasID2)_50// `id2` is "2"`

If more than two interfaces are present in an intersection type,
any concrete value of that type must implement both of them:

 `_31access(all)_31struct interface HasMetadata {_31 access(all)_31 var metadata: AnyStruct_31}_31_31access(all)_31struct C: HasID, HasMetadata {_31_31 access(all)_31 let id: String_31 _31 access(all)_31 var metadata: AnyStruct_31_31 init(id: String) {_31 self.id = id_31 self.metadata = []_31 }_31_31 access(all)_31 fun setMetadata(_ data: AnyStruct) {_31 self.metadata = data_31 }_31}_31_31// valid, because `C` implements both `HasID` and `HasMetadata`._31let hasID3: {HasID, HasMetadata} = C(id: "3")_31_31// Invalid, because `A` implements only `HasID`._31let hasID4: {HasID, HasMetadata} = A(id: "4")`[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/intersection-types.md)[PreviousEnumerations](/docs/language/enumerations)[NextReferences](/docs/language/references)Got suggestions for this site? 

* [It's open-source!](https://github.com/onflow/cadence-lang.org)
The source code of this site is licensed under the Apache License, Version 2.0.
Content is licensed under the Creative Commons Attribution 4.0 International License.

