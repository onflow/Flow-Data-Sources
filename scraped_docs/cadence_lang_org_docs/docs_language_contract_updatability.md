# Source: https://cadence-lang.org/docs/language/contract-updatability

Contract Updatability | Cadence



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

* [Language Reference](/docs/language/)
* Contract Updatability

On this page

# Contract Updatability

A [contract](/docs/language/contracts) is a collection of data (its state) and code (its functions) that lives in the contract storage area of an account. When a contract is *updated*, it is important to make sure that the changes introduced do not lead to runtime inconsistencies for already stored data.

Cadence maintains this state consistency by validating the contracts and all their components before an update.

## Threat model and scope[​](#threat-model-and-scope "Direct link to Threat model and scope")

The contract update validator has a **narrow, deliberate scope: storage compatibility**. Its purpose is to ensure that already-stored on-chain data remains deserializable after an update. It is a storage compatibility check, not a general-purpose interface freeze.

**What the validator enforces** (storage compatibility):

* Field types cannot change — serialized data is type-bound; a mismatch corrupts storage.
* Nested composite/interface declarations cannot be removed — orphaned stored data would have no matching type at deserialization time.
* Interface conformances cannot be removed — removing a conformance would invalidate type assumptions baked into stored collections (e.g. `[{I}]` containing `{T: I}` values).
* Enum cases cannot be removed or reordered — enum values are stored as ordinals; any reordering silently changes their meaning.

**What the validator intentionally does NOT enforce** (deployer discretion):

* Access modifiers on fields (e.g. `access(self)` → `access(all)`) — access control is not a storage property. The runtime enforces the access rules present in the current chain-state code at execution time. If a deployer chooses to widen access, that is a deliberate decision they make as the contract owner. Users who rely on a contract's access guarantees must trust the deployer, as they would on any upgradeable platform.
* Field mutability (`let` → `var`) — the `let`/`var` distinction is a Cadence semantic constraint enforced at compile time against the current code; it is not encoded in the storage layout and does not affect deserialization.
* Function signatures, event definitions, code logic — none of these affect storage layout.

## Validation goals[​](#validation-goals "Direct link to Validation goals")

The contract update validation ensures that:

* Stored data doesn't change its meaning when a contract is updated.
* Decoding and using stored data does not lead to runtime crashes.
  + For example, it is invalid to add a field because the existing stored data won't have the new field.
  + Loading the existing data will result in garbage/missing values for such fields.
  + A static check of the access of the field would be valid, but the interpreter would crash when accessing the field because the field has a missing/garbage value.

However, it does **not** ensure any program that imports the updated contract stays valid. For example, an updated contract may remove an existing field or may change a function signature. In this case, any program that uses that field/function will get semantic errors.

## Updating a contract[​](#updating-a-contract "Direct link to Updating a contract")

Changes to contracts can be introduced by adding new contracts, removing existing contracts, or updating existing contracts. However, some of these changes may lead to data inconsistencies as stated above.

**Valid changes**

* Adding a new contract is valid.
* Removing a contract/contract-interface that doesn't have enum declarations is valid.
* Updating a contract is valid under the restrictions described in the following sections.

**Invalid changes**

* Removing a contract/contract-interface that contains enum declarations is not valid.
  + Removing a contract allows adding a new contract with the same name.
  + The new contract could potentially have enum declarations with the same names as in the old contract, but with different structures.
  + This could change the meaning of the already stored values of those enum types.

A contract may consist of fields and other declarations such as composite types, functions, constructors, and so on. When an existing contract is updated, all of its inner declarations are also validated.

### Contract fields[​](#contract-fields "Direct link to Contract fields")

When a contract is deployed, the fields of the contract are stored in an account's contract storage. Changing the fields of a contract only changes the way the program treats the data, but does not change the already-stored data itself, which could potentially result in runtime inconsistencies as mentioned in the previous section.

See [Fields](#fields) for any possible updates that can be made to the fields, and the restrictions imposed on changing the fields of a contract.

### Nested declarations[​](#nested-declarations "Direct link to Nested declarations")

Contracts can have nested composite type declarations such as structs, resources, interfaces, and enums. When a contract is updated, its nested declarations are checked because:

* They can be used as type annotations for the fields of the same contract, directly or indirectly.
* Any third-party contract can import the types defined in this contract and use them as type annotations.
* Hence, changing the type definition is the same as changing the type annotation of such a field (which is also invalid, as described in the [Fields](#fields) section below).

Changes that can be performed on the nested declarations and the update restrictions are described in the following sections:

* [Structs, resources, and interfaces](#structs-resources-and-interfaces)
* [Enums](#enums)
* [Functions](#functions)
* [Events](#events)
* [Constructors](#constructors)

## Fields[​](#fields "Direct link to Fields")

A field may belong to a contract, struct, resource, or interface:

**Valid changes**

* Removing a field is valid

  `_19

  // Existing contract

  _19

  _19

  access(all)

  _19

  contract Foo {

  _19

  _19

  access(all)

  _19

  var a: String

  _19

  _19

  access(all)

  _19

  var b: Int

  _19

  }

  _19

  _19

  // Updated contract

  _19

  _19

  access(all)

  _19

  contract Foo {

  _19

  access(all)

  _19

  var a: String

  _19

  }`

  + It leaves data for the removed field unused at the storage, as it is no longer accessible.
  + However, it does not cause any runtime crashes.
* Changing the order of fields is valid.

  `_23

  // Existing contract

  _23

  _23

  access(all)

  _23

  contract Foo {

  _23

  _23

  access(all)

  _23

  var a: String

  _23

  _23

  access(all)

  _23

  var b: Int

  _23

  }

  _23

  _23

  // Updated contract

  _23

  _23

  access(all)

  _23

  contract Foo {

  _23

  _23

  access(all)

  _23

  var b: Int

  _23

  _23

  access(all)

  _23

  var a: String

  _23

  }`
* Changing the access modifier of a field is valid.

  `_15

  // Existing contract

  _15

  _15

  access(all)

  _15

  contract Foo {

  _15

  access(all)

  _15

  var a: String

  _15

  }

  _15

  _15

  // Updated contract

  _15

  _15

  access(all)

  _15

  contract Foo {

  _15

  access(self)

  _15

  var a: String // access modifier changed to 'access(self)'

  _15

  }`

**Invalid changes**

* Adding a new field is not valid:

  `_19

  // Existing contract

  _19

  _19

  access(all)

  _19

  contract Foo {

  _19

  access(all)

  _19

  var a: String

  _19

  }

  _19

  _19

  // Updated contract

  _19

  _19

  access(all)

  _19

  contract Foo {

  _19

  _19

  access(all)

  _19

  var a: String

  _19

  _19

  access(all)

  _19

  var b: Int // Invalid new field

  _19

  }`

  + The initializer of a contract only runs once, when the contract is deployed for the first time. It does not rerun when the contract is updated. However, it is still required to be present in the updated contract to satisfy type checks.
  + Thus, the stored data won't have the new field, as the initializations for the newly added fields do not get executed.
  + Decoding stored data will result in garbage or missing values for such fields.
* Changing the type of an existing field is not valid.

  `_17

  // Existing contract

  _17

  _17

  access(all)

  _17

  contract Foo {

  _17

  _17

  access(all)

  _17

  var a: String

  _17

  }

  _17

  _17

  // Updated contract

  _17

  _17

  access(all)

  _17

  contract Foo {

  _17

  _17

  access(all)

  _17

  var a: Int // Invalid type change

  _17

  }`

  + In an already stored contract, the field `a` would have a value of type `String`.
  + Changing the type of the field `a` to `Int` would make the runtime read the already stored `String` value as an `Int`, which will result in deserialization errors.
  + Changing the field type to a subtype/supertype of the existing type is also not valid, as it would also potentially cause issues while decoding/encoding.
    - For example: changing an `Int64` field to `Int8` — Stored field could have a numeric value`624`, which exceeds the value space for `Int8`.
    - However, this is a limitation in the current implementation; future versions of Cadence may support changing the type of field to a subtype by providing means to migrate existing fields.

## Structs, resources, and interfaces[​](#structs-resources-and-interfaces "Direct link to Structs, resources, and interfaces")

**Valid changes**

* Adding a new struct, resource, or interface is valid.
* Adding an interface conformance to a struct/resource is valid, since the stored data only stores concrete type/value, but doesn't store the conformance info:

  `_11

  // Existing struct

  _11

  _11

  access(all)

  _11

  struct Foo {

  _11

  }

  _11

  _11

  // Updated struct

  _11

  _11

  access(all)

  _11

  struct Foo: T {

  _11

  }`

  + However, if adding a conformance also requires changing the existing structure (e.g., adding a new field that is enforced by the new conformance), then the other restriction(such as [restrictions on fields](#fields)) may prevent performing such an update.

**Invalid changes**

* Removing an existing declaration is not valid.
  + Removing a declaration allows adding a new declaration with the same name, but with a different structure.
  + Any program that uses stored data belonging to that type would face inconsistencies.
* Renaming a declaration is not valid. It can have the same effect as removing an existing declaration and adding a new one.
* Changing the type of declaration is not valid (i.e., changing from a struct to an interface, and vise versa).

  `_11

  // Existing struct

  _11

  _11

  access(all)

  _11

  struct Foo {

  _11

  }

  _11

  _11

  // Changed to a struct interface

  _11

  _11

  access(all)

  _11

  struct interface Foo { // Invalid type declaration change

  _11

  }`
* Removing an interface conformance of a struct/resource is not valid.

  `_11

  // Existing struct

  _11

  _11

  access(all)

  _11

  struct Foo: T {

  _11

  }

  _11

  _11

  // Updated struct

  _11

  _11

  access(all)

  _11

  struct Foo {

  _11

  }`

  + Otherwise, types that used to conform to an interface would no longer conform to that interface, which would lead to [type safety](/docs/language/types-and-type-system/type-safety) issues at runtime.

### Updating members[​](#updating-members "Direct link to Updating members")

Similar to contracts, the composite declarations structs, resources, and interfaces can also have fields and other nested declarations as its member. Updating such a composite declaration would also include updating all of its members.

The following sections describe the restrictions imposed on updating the members of a struct, resource, or interface:

* [Fields](#fields)
* [Enums](#enums)
* [Functions](#functions)
* [Constructors](#constructors)

## Enums[​](#enums "Direct link to Enums")

**Valid changes**

* Adding a new enum declaration is valid.

**Invalid changes**

* Removing an existing enum declaration is invalid.
  + Otherwise, it is possible to remove an existing enum and add a new enum declaration with the same name, but with a different structure.
  + The new structure could potentially have incompatible changes (such as changed types, changed enum-cases, and so on).
* Changing the name is invalid, as it is equivalent to removing an existing enum and adding a new one.
* Changing the raw type is invalid:

  `` _23

  // Existing enum with `Int` raw type

  _23

  _23

  access(all)

  _23

  enum Color: Int {

  _23

  _23

  access(all)

  _23

  case RED

  _23

  _23

  access(all)

  _23

  case BLUE

  _23

  }

  _23

  _23

  // Updated enum with `UInt8` raw type

  _23

  _23

  access(all)

  _23

  enum Color: UInt8 { // Invalid change of raw type

  _23

  _23

  access(all)

  _23

  case RED

  _23

  _23

  access(all)

  _23

  case BLUE

  _23

  } ``

  + When the enum value is stored, the raw value associated with the enum case gets stored.
  + If the type is changed, then deserializing could fail if the already stored values are not in the same value space as the updated type.

### Updating enum cases[​](#updating-enum-cases "Direct link to Updating enum cases")

Enums consist of enum-case declarations, and updating an enum may also include changing the enum's cases as well. Enum cases are represented using their raw value at the Cadence interpreter and runtime. Hence, any change that causes an enum case to change its raw value is not permitted. Otherwise, a changed raw value could cause an already stored enum value to have a different meaning than what it originally was (type confusion).

**Valid changes**

* Adding an enum case at the end of the existing enum cases is valid:

  `_26

  // Existing enum

  _26

  _26

  access(all)

  _26

  enum Color: Int {

  _26

  _26

  access(all)

  _26

  case RED

  _26

  _26

  access(all)

  _26

  case BLUE

  _26

  }

  _26

  _26

  // Updated enum

  _26

  _26

  access(all)

  _26

  enum Color: Int {

  _26

  _26

  access(all)

  _26

  case RED

  _26

  _26

  access(all)

  _26

  case BLUE

  _26

  _26

  access(all)

  _26

  case GREEN // valid new enum-case at the bottom

  _26

  }`

**Invalid changes**

* Adding an enum-case at the top or in the middle of the existing enum cases is invalid:

  `_26

  // Existing enum

  _26

  _26

  access(all)

  _26

  enum Color: Int {

  _26

  _26

  access(all)

  _26

  case RED

  _26

  _26

  access(all)

  _26

  case BLUE

  _26

  }

  _26

  _26

  // Updated enum

  _26

  _26

  access(all)

  _26

  enum Color: Int {

  _26

  _26

  access(all)

  _26

  case RED

  _26

  _26

  access(all)

  _26

  case GREEN // invalid new enum-case in the middle

  _26

  _26

  access(all)

  _26

  case BLUE

  _26

  }`
* Changing the name of an enum case is invalid.

  `_23

  // Existing enum

  _23

  _23

  access(all)

  _23

  enum Color: Int {

  _23

  _23

  access(all)

  _23

  case RED

  _23

  _23

  access(all)

  _23

  case BLUE

  _23

  }

  _23

  _23

  // Updated enum

  _23

  _23

  access(all)

  _23

  enum Color: Int {

  _23

  _23

  access(all)

  _23

  case RED

  _23

  _23

  access(all)

  _23

  case GREEN // invalid change of names

  _23

  }`

  + Previously stored raw values for `Color.BLUE` now represents `Color.GREEN` (i.e., the stored values have changed their meaning, and hence not a valid change).
  + Similarly, it is possible to add a new enum with the old name `BLUE`, which gets a new raw value. Then, the same enum case `Color.BLUE` may have used two raw values at runtime, before and after the change, which is also invalid.
* Removing the enum case is invalid. Removing allows one to add and remove an enum case, which has the same effect as renaming:

  `` _22

  // Existing enum

  _22

  _22

  access(all)

  _22

  enum Color: Int {

  _22

  _22

  access(all)

  _22

  case RED

  _22

  _22

  access(all)

  _22

  case BLUE

  _22

  }

  _22

  _22

  // Updated enum

  _22

  _22

  access(all)

  _22

  enum Color: Int {

  _22

  _22

  access(all)

  _22

  case RED

  _22

  _22

  // invalid removal of `case BLUE`

  _22

  } ``
* Changing the order of enum cases is not permitted.

  `_23

  // Existing enum

  _23

  _23

  access(all)

  _23

  enum Color: Int {

  _23

  _23

  access(all)

  _23

  case RED

  _23

  _23

  access(all)

  _23

  case BLUE

  _23

  }

  _23

  _23

  // Updated enum

  _23

  _23

  access(all)

  _23

  enum Color: UInt8 {

  _23

  _23

  access(all)

  _23

  case BLUE // invalid change of order

  _23

  _23

  access(all)

  _23

  case RED

  _23

  }`

  + The raw value of an enum is implicit and corresponds to the defined order.
  + Changing the order of enum-cases has the same effect as changing the raw value, which could cause storage inconsistencies and type-confusions as described earlier.

## Functions[​](#functions "Direct link to Functions")

Adding, changing, and deleting a function definition is always valid, as function definitions are never stored as data (function definitions are part of the code, but not data).

* Adding a function is valid.
* Deleting a function is valid.
* Changing a function signature (parameters, return types) is valid.
* Changing a function body is valid.
* Changing the access modifiers is valid.

However, changing a *function type* may or may not be valid, depending on where it is used: if a function type is used in the type annotation of a composite type field (direct or indirect), then changing the function type signature is the same as changing the type annotation of that field (which is invalid).

## Events[​](#events "Direct link to Events")

Events are not stored onchain. Any changes made to events have no impact on the stored data. Hence, adding, removing, and modifying events in a contract is valid.

## Constructors[​](#constructors "Direct link to Constructors")

Similar to functions, constructors are also not stored. Hence, any changes to constructors are valid.

## Imports[​](#imports "Direct link to Imports")

A contract may import declarations (types, functions, variables, and so on) from other programs. These imported programs are already validated at the time of their deployment. Hence, there is no need to validate any declaration every time they are imported.

## The `#removedType` pragma[​](#the-removedtype-pragma "Direct link to the-removedtype-pragma")

Under normal circumstances, it is not valid to remove a type declaration, whether a composite or an interface. However, a special pragma can be used when this is necessary to enable composite declarations to be *tombstoned*, removing them from a contract and preventing any declarations from being re-added with the same name. This pragma cannot be used with interfaces.

To use this pragma, simply add a `#removedType(T)` line to the contract containing the type `T` you want to remove, at the same scope as the declaration of `T`.

For example, to remove a resource definition `R` defined like so:

`_10

access(all) contract Foo {

_10

_10

access(all) resource R {

_10

// definition of R ...

_10

}

_10

_10

// other stuff ...

_10

}`

change the contract to:

`_10

access(all) contract Foo {

_10

_10

#removedType(R)

_10

_10

// other stuff ...

_10

}`

This prevents any type named `R` from ever being declared again as a nested declaration in `Foo`, preventing the security issues normally posed by removing a type. Specifically, when a `#removedType(T)` pragma is present at a certain scope level in a contract, no new type named `T` can be added at that scope. Additionally, once added, a `#removedType` pragma can never be removed, as this would allow circumventing the above restriction.

Please note that this pragma's behavior is not necessarily final and is subject to change.

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/contract-updatability.md)

[Previous

Contracts](/docs/language/contracts)[Next

Transactions](/docs/language/transactions)

###### Rate this page

😞😐😊

* [Threat model and scope](#threat-model-and-scope)
* [Validation goals](#validation-goals)
* [Updating a contract](#updating-a-contract)
  + [Contract fields](#contract-fields)
  + [Nested declarations](#nested-declarations)
* [Fields](#fields)
* [Structs, resources, and interfaces](#structs-resources-and-interfaces)
  + [Updating members](#updating-members)
* [Enums](#enums)
  + [Updating enum cases](#updating-enum-cases)
* [Functions](#functions)
* [Events](#events)
* [Constructors](#constructors)
* [Imports](#imports)
* [The `#removedType` pragma](#the-removedtype-pragma)