# Source: https://cadence-lang.org/docs/language/types-and-type-system/intersection-types

Intersection Types | Cadence



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

    - [Type Annotations](/docs/language/types-and-type-system/type-annotations)
    - [Type Safety](/docs/language/types-and-type-system/type-safety)
    - [Type Inference](/docs/language/types-and-type-system/type-inference)
    - [Composite Types](/docs/language/types-and-type-system/composite-types)
    - [Intersection Types](/docs/language/types-and-type-system/intersection-types)
    - [Run-time Types](/docs/language/types-and-type-system/run-time-types)
    - [Type Hierarchy](/docs/language/types-and-type-system/type-hierarchy)
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
* [Types and Type System](/docs/language/types-and-type-system/)
* Intersection Types

# Intersection Types

Interface types cannot be used in type annotations directly; instead, they must be used as part of intersection types. An intersection type represents a value that conforms to all of the interfaces listed in the intersection.

The syntax of a intersection type is `{U1, U2, ... Un}`, where the types `U1` to `Un` are the interfaces to which the type conforms.

The members and functions of any of the set of interfaces are available.

Intersection types are useful for writing functions that work on a variety of different inputs. For example, by using an intersection type for a parameter's type, the function may accept any concrete value that implements all the interfaces in that intersection. The value is restricted to the functionality of the intersection; if the function accidentally attempts to access other functionality, this is prevented by the static checker.

`` _50

access(all)

_50

struct interface HasID {

_50

access(all)

_50

let id: String

_50

}

_50

_50

access(all)

_50

struct A: HasID {

_50

_50

access(all)

_50

let id: String

_50

_50

init(id: String) {

_50

self.id = id

_50

}

_50

}

_50

_50

access(all)

_50

struct B: HasID {

_50

_50

access(all)

_50

let id: String

_50

_50

init(id: String) {

_50

self.id = id

_50

}

_50

}

_50

_50

// Create two instances, one of type `A`, and one of type `B`.

_50

// Both types conform to interface `HasID`, so the structs can be assigned

_50

// to variables with type `{HasID}`: Some resource type which only allows

_50

// access to the functionality of resource interface `HasID`

_50

_50

let hasID1: {HasID} = A(id: "1")

_50

let hasID2: {HasID} = B(id: "2")

_50

_50

// Declare a function named `getID` which has one parameter with type `{HasID}`.

_50

// The type `{HasID}` is a short-hand for `AnyStruct{HasID}`:

_50

// Some structure which only allows access to the functionality of interface `HasID`.

_50

//

_50

access(all)

_50

fun getID(_ value: {HasID}): String {

_50

return value.id

_50

}

_50

_50

let id1 = getID(hasID1)

_50

// `id1` is "1"

_50

_50

let id2 = getID(hasID2)

_50

// `id2` is "2" ``

If more than two interfaces are present in an intersection type, any concrete value of that type must implement both of them:

`` _31

access(all)

_31

struct interface HasMetadata {

_31

access(all)

_31

var metadata: AnyStruct

_31

}

_31

_31

access(all)

_31

struct C: HasID, HasMetadata {

_31

_31

access(all)

_31

let id: String

_31

_31

access(all)

_31

var metadata: AnyStruct

_31

_31

init(id: String) {

_31

self.id = id

_31

self.metadata = []

_31

}

_31

_31

access(all)

_31

fun setMetadata(_ data: AnyStruct) {

_31

self.metadata = data

_31

}

_31

}

_31

_31

// valid, because `C` implements both `HasID` and `HasMetadata`.

_31

let hasID3: {HasID, HasMetadata} = C(id: "3")

_31

_31

// Invalid, because `A` implements only `HasID`.

_31

let hasID4: {HasID, HasMetadata} = A(id: "4") ``

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/types-and-type-system/intersection-types.md)

[Previous

Composite Types](/docs/language/types-and-type-system/composite-types)[Next

Run-time Types](/docs/language/types-and-type-system/run-time-types)