# Source: https://cadence-lang.org/docs/language/contract-updatability




Contract Updatability | Cadence




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
* Contract Updatability
On this page
# Contract Updatability

## Introduction[​](#introduction "Direct link to Introduction")

A [contract](/docs/language/contracts) is a collection of data (its state) and
code (its functions) that lives in the contract storage area of an account.
When a contract is updated, it is important to make sure that the changes introduced do not lead to runtime
inconsistencies for already stored data.
Cadence maintains this state consistency by validating the contracts and all their components before an update.

## Validation Goals[​](#validation-goals "Direct link to Validation Goals")

The contract update validation ensures that:

* Stored data doesn't change its meaning when a contract is updated.
* Decoding and using stored data does not lead to runtime crashes.
  + For example, it is invalid to add a field because existing stored data won't have the new field.
  + Loading the existing data will result in garbage/missing values for such fields.
  + A static check of the access of the field would be valid, but the interpreter would crash when accessing the field,
    because the field has a missing/garbage value.

However, it **does not** ensure:

* Any program that imports the updated contract stays valid. e.g:
  + Updated contract may remove an existing field or may change a function signature.
  + Then any program that uses that field/function will get semantic errors.

## Updating a Contract[​](#updating-a-contract "Direct link to Updating a Contract")

Changes to contracts can be introduced by adding new contracts, removing existing contracts, or updating existing
contracts. However, some of these changes may lead to data inconsistencies as stated above.

#### Valid Changes[​](#valid-changes "Direct link to Valid Changes")

* Adding a new contract is valid.
* Removing a contract/contract-interface that doesn't have enum declarations is valid.
* Updating a contract is valid, under the restrictions described in the below sections.

#### Invalid Changes[​](#invalid-changes "Direct link to Invalid Changes")

* Removing a contract/contract-interface that contains enum declarations is not valid.
  + Removing a contract allows adding a new contract with the same name.
  + The new contract could potentially have enum declarations with the same names as in the old contract, but with
    different structures.
  + This could change the meaning of the already stored values of those enum types.

A contract may consist of fields and other declarations such as composite types, functions, constructors, etc.
When an existing contract is updated, all its inner declarations are also validated.

### Contract Fields[​](#contract-fields "Direct link to Contract Fields")

When a contract is deployed, the fields of the contract are stored in an account's contract storage.
Changing the fields of a contract only changes the way the program treats the data, but does not change the already
stored data itself, which could potentially result in runtime inconsistencies as mentioned in the previous section.

See the [section about fields below](#fields) for the possible updates that can be done to the fields, and the restrictions
imposed on changing fields of a contract.

### Nested Declarations[​](#nested-declarations "Direct link to Nested Declarations")

Contracts can have nested composite type declarations such as structs, resources, interfaces, and enums.
When a contract is updated, its nested declarations are checked, because:

* They can be used as type annotation for the fields of the same contract, directly or indirectly.
* Any third-party contract can import the types defined in this contract and use them as type annotations.
* Hence, changing the type definition is the same as changing the type annotation of such a field (which is also invalid,
  as described in the [section about fields fields](#fields) below).

Changes that can be done to the nested declarations, and the update restrictions are described in following sections:

* [Structs, resources and interface](#structs-resources-and-interfaces)
* [Enums](#enums)
* [Functions](#functions)
* [Events](#events)
* [Constructors](#constructors)

## Fields[​](#fields "Direct link to Fields")

A field may belong to a contract, struct, resource, or interface.

#### Valid Changes:[​](#valid-changes-1 "Direct link to Valid Changes:")

* Removing a field is valid
  
   `_20// Existing contract_20_20access(all)_20contract Foo {_20 _20 access(all)_20 var a: String_20_20 access(all)_20 var b: Int_20}_20_20_20// Updated contract_20_20access(all)_20contract Foo {_20 access(all)_20 var a: String_20}`
  + It leaves data for the removed field unused at the storage, as it is no longer accessible.
  + However, it does not cause any runtime crashes.
* Changing the order of fields is valid.
  
   `_24// Existing contract_24_24access(all)_24contract Foo {_24_24 access(all)_24 var a: String_24_24 access(all)_24 var b: Int_24}_24_24_24// Updated contract_24_24access(all)_24contract Foo {_24_24 access(all)_24 var b: Int_24_24 access(all)_24 var a: String_24}`
* Changing the access modifier of a field is valid.
  
   `_16// Existing contract_16_16access(all)_16contract Foo {_16 access(all)_16 var a: String_16}_16_16_16// Updated contract_16_16access(all)_16contract Foo {_16 access(self)_16 var a: String // access modifier changed to 'access(self)'_16}`

#### Invalid Changes[​](#invalid-changes-1 "Direct link to Invalid Changes")

* Adding a new field is not valid.
  
   `_20// Existing contract_20_20access(all)_20contract Foo {_20 access(all)_20 var a: String_20}_20_20_20// Updated contract_20_20access(all)_20contract Foo {_20 _20 access(all)_20 var a: String_20_20 access(all)_20 var b: Int // Invalid new field_20}`
  + Initializer of a contract only run once, when the contract is deployed for the first time. It does not rerun
    when the contract is updated. However, it is still required to be present in the updated contract to satisfy type checks.
  + Thus, the stored data won't have the new field, as the initializations for the newly added fields do not get
    executed.
  + Decoding stored data will result in garbage or missing values for such fields.
* Changing the type of existing field is not valid.
  
   `_18// Existing contract_18_18access(all)_18contract Foo {_18_18 access(all)_18 var a: String_18}_18_18_18// Updated contract_18_18access(all)_18contract Foo {_18_18 access(all)_18 var a: Int // Invalid type change_18}`
  + In an already stored contract, the field `a` would have a value of type `String`.
  + Changing the type of the field `a` to `Int`, would make the runtime read the already stored `String`
    value as an `Int`, which will result in deserialization errors.
  + Changing the field type to a subtype/supertype of the existing type is also not valid, as it would also
    potentially cause issues while decoding/encoding.
    - e.g: Changing an `Int64` field to `Int8` - Stored field could have a numeric value`624`, which exceeds the value space
      for `Int8`.
    - However, this is a limitation in the current implementation, and the future versions of Cadence may support
      changing the type of field to a subtype, by providing means to migrate existing fields.

## Structs, Resources and Interfaces[​](#structs-resources-and-interfaces "Direct link to Structs, Resources and Interfaces")

#### Valid Changes:[​](#valid-changes-2 "Direct link to Valid Changes:")

* Adding a new struct, resource, or interface is valid.
* Adding an interface conformance to a struct/resource is valid, since the stored data only
  stores concrete type/value, but doesn't store the conformance info.
   `_12// Existing struct_12_12access(all)_12struct Foo {_12}_12_12_12// Upated struct_12_12access(all)_12struct Foo: T {_12}`
  + However, if adding a conformance also requires changing the existing structure (e.g: adding a new field that is
    enforced by the new conformance), then the other restrictions (such as [restrictions on fields](#fields)) may
    prevent performing such an update.

#### Invalid Changes:[​](#invalid-changes-2 "Direct link to Invalid Changes:")

* Removing an existing declaration is not valid.
  + Removing a declaration allows adding a new declaration with the same name, but with a different structure.
  + Any program that uses stored data belong to that type would face inconsistencies.
* Renaming a declaration is not valid. It can have the same effect as removing an existing declaration and adding
  a new one.
* Changing the type of declaration is not valid. i.e: Changing from a struct to interface, and vise versa.
   `_12// Existing struct_12_12access(all)_12struct Foo {_12}_12_12_12// Changed to a struct interface_12_12access(all)_12struct interface Foo { // Invalid type declaration change_12}`
* Removing an interface conformance of a struct/resource is not valid.
   `_12// Existing struct_12_12access(all)_12struct Foo: T {_12}_12_12_12// Upated struct_12_12access(all)_12struct Foo {_12}`
  + Otherwise, types that used to conform to an interface would no longer conform to that interface, which would lead
    to type safety issues at runtime.

### Updating Members[​](#updating-members "Direct link to Updating Members")

Similar to contracts, these composite declarations: structs, resources, and interfaces also can have fields and
other nested declarations as its member.
Updating such a composite declaration would also include updating all of its members.

Below sections describes the restrictions imposed on updating the members of a struct, resource or an interface.

* [Fields](#fields)
* [Nested structs, resources and interfaces](#structs-resources-and-interfaces)
* [Enums](#enums)
* [Functions](#functions)
* [Constructors](#constructors)

## Enums[​](#enums "Direct link to Enums")

#### Valid Changes:[​](#valid-changes-3 "Direct link to Valid Changes:")

* Adding a new enum declaration is valid.

#### Invalid Changes:[​](#invalid-changes-3 "Direct link to Invalid Changes:")

* Removing an existing enum declaration is invalid.
  + Otherwise, it is possible to remove an existing enum and add a new enum declaration with the same name,
    but with a different structure.
  + The new structure could potentially have incompatible changes (such as changed types, changed enum-cases, etc).
* Changing the name is invalid, as it is equivalent to removing an existing enum and adding a new one.
* Changing the raw type is invalid.
   `_24// Existing enum with `Int` raw type_24_24access(all)_24enum Color: Int {_24_24 access(all)_24 case RED_24_24 access(all)_24 case BLUE_24}_24_24_24// Updated enum with `UInt8` raw type_24_24access(all)_24enum Color: UInt8 { // Invalid change of raw type_24_24 access(all)_24 case RED_24_24 access(all)_24 case BLUE_24}`
  + When the enum value is stored, the raw value associated with the enum-case gets stored.
  + If the type is changed, then deserializing could fail if the already stored values are not in the same value space
    as the updated type.

### Updating Enum Cases[​](#updating-enum-cases "Direct link to Updating Enum Cases")

Enums consist of enum-case declarations, and updating an enum may also include changing the enums cases as well.
Enum cases are represented using their raw-value at the Cadence interpreter and runtime.
Hence, any change that causes an enum-case to change its raw value is not permitted.
Otherwise, a changed raw-value could cause an already stored enum value to have a different meaning than what
it originally was (type confusion).

#### Valid Changes:[​](#valid-changes-4 "Direct link to Valid Changes:")

* Adding an enum-case at the end of the existing enum-cases is valid.
   `_27// Existing enum_27_27access(all)_27enum Color: Int {_27_27 access(all)_27 case RED_27_27 access(all)_27 case BLUE_27}_27_27_27// Updated enum_27_27access(all)_27enum Color: Int {_27_27 access(all)_27 case RED_27_27 access(all)_27 case BLUE_27_27 access(all)_27 case GREEN // valid new enum-case at the bottom_27}`

#### Invalid Changes[​](#invalid-changes-4 "Direct link to Invalid Changes")

* Adding an enum-case at the top or in the middle of the existing enum-cases is invalid.
  
   `_27// Existing enum_27_27access(all)_27enum Color: Int {_27_27 access(all)_27 case RED_27_27 access(all)_27 case BLUE_27}_27_27_27// Updated enum_27_27access(all)_27enum Color: Int {_27_27 access(all)_27 case RED_27_27 access(all)_27 case GREEN // invalid new enum-case in the middle_27_27 access(all)_27 case BLUE_27}`
* Changing the name of an enum-case is invalid.
  
   `_24// Existing enum_24_24access(all)_24enum Color: Int {_24_24 access(all)_24 case RED_24_24 access(all)_24 case BLUE_24}_24_24_24// Updated enum_24_24access(all)_24enum Color: Int {_24_24 access(all)_24 case RED_24_24 access(all)_24 case GREEN // invalid change of names_24}`
  + Previously stored raw values for `Color.BLUE` now represents `Color.GREEN`. i.e: The stored values have changed
    their meaning, and hence not a valid change.
  + Similarly, it is possible to add a new enum with the old name `BLUE`, which gets a new raw value. Then the same
    enum-case `Color.BLUE` may have used two raw-values at runtime, before and after the change, which is also invalid.
* Removing the enum case is invalid. Removing allows one to add and remove an enum-case which has the same effect
  as renaming.
  
   `_23// Existing enum_23_23access(all)_23enum Color: Int {_23_23 access(all)_23 case RED_23_23 access(all)_23 case BLUE_23}_23_23_23// Updated enum_23_23access(all)_23enum Color: Int {_23_23 access(all)_23 case RED_23_23 // invalid removal of `case BLUE`_23}`
* Changing the order of enum-cases is not permitted
  
   `_24// Existing enum_24_24access(all)_24enum Color: Int {_24_24 access(all)_24 case RED_24_24 access(all)_24 case BLUE_24}_24_24_24// Updated enum_24_24access(all)_24enum Color: UInt8 {_24_24 access(all)_24 case BLUE // invalid change of order_24 _24 access(all)_24 case RED_24}`
  + Raw value of an enum is implicit, and corresponds to the defined order.
  + Changing the order of enum-cases has the same effect as changing the raw-value, which could cause storage
    inconsistencies and type-confusions as described earlier.

## Functions[​](#functions "Direct link to Functions")

Adding, changing, and deleting a function definition is always valid, as function definitions are never stored as data
(function definitions are part of the code, but not data).

* Adding a function is valid.
* Deleting a function is valid.
* Changing a function signature (parameters, return types) is valid.
* Changing a function body is valid.
* Changing the access modifiers is valid.

However, changing a *function type* may or may not be valid, depending on where it is used:
If a function type is used in the type annotation of a composite type field (direct or indirect),
then changing the function type signature is the same as changing the type annotation of that field (which is invalid).

## Events[​](#events "Direct link to Events")

Events are not stored on chain. Any changes made to events have no impact on the stored data.
Hence, adding, removing, and modifying events in a contract is valid.

## Constructors[​](#constructors "Direct link to Constructors")

Similar to functions, constructors are also not stored. Hence, any changes to constructors are valid.

## Imports[​](#imports "Direct link to Imports")

A contract may import declarations (types, functions, variables, etc.) from other programs. These imported programs are
already validated at the time of their deployment. Hence, there is no need for validating any declaration every time
they are imported.

## The `#removedType` Pragma[​](#the-removedtype-pragma "Direct link to the-removedtype-pragma")

Under normal circumstances, it is not valid to remove a type declaration, whether a composite or an interface.
However, a special pragma can be used when this is necessary to enable composite declarations to be "tombstoned",
removing them from a contract and preventing any declarations from being re-added with the same name.
This pragma cannot be used with interfaces.

To use this pragma, simply add a `#removedType(T)` line to the contract containing the type `T` you want to remove,
at the same scope as the declaration of `T`. So, for example, to remove a resource definition `R` defined like so:

 `_10access(all) contract Foo {_10_10 access(all) resource R {_10 // definition of R ..._10 }_10_10 // other stuff ... _10}`

change the contract to:

 `_10access(all) contract Foo {_10_10 #removedType(R)_10_10 // other stuff ... _10}`

This will prevent any type named `R` from ever being declared again as a nested declaration in `Foo`,
preventing the security issues normally posed by removing a type.
Specifically, when a `#removedType(T)` pragma is present at a certain scope level in a contract,
no new type named `T` can be added at that scope.
Additionally, once added, a `#removedType` pragma can never be removed,
as this would allow circumventing the above restriction.

Please note that this pragma's behavior is not necessarily final and is subject to change.

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/contract-updatability.md)[PreviousContracts](/docs/language/contracts)[NextTransactions](/docs/language/transactions)
###### Rate this page

😞😐😊

* [Introduction](#introduction)
* [Validation Goals](#validation-goals)
* [Updating a Contract](#updating-a-contract)
  + [Contract Fields](#contract-fields)
  + [Nested Declarations](#nested-declarations)
* [Fields](#fields)
* [Structs, Resources and Interfaces](#structs-resources-and-interfaces)
  + [Updating Members](#updating-members)
* [Enums](#enums)
  + [Updating Enum Cases](#updating-enum-cases)
* [Functions](#functions)
* [Events](#events)
* [Constructors](#constructors)
* [Imports](#imports)
* [The `#removedType` Pragma](#the-removedtype-pragma)
Got suggestions for this site? 

* [It's open-source!](https://github.com/onflow/cadence-lang.org)
The source code of this site is licensed under the Apache License, Version 2.0.
Content is licensed under the Creative Commons Attribution 4.0 International License.

