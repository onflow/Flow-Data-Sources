# Source: https://cadence-lang.org/docs/language/accounts/storage

Storage | Cadence



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
* Storage

On this page

# Storage

Accounts allow storing storable objects, such as resources and structures.

An account exposes its storage through the `storage` field, which has the type `Account.Storage`.

## `Account.Storage`[​](#accountstorage "Direct link to accountstorage")

Here's an example:

`` _134

access(all)

_134

struct Storage {

_134

/// The current amount of storage used by the account in bytes.

_134

access(all)

_134

let used: UInt64

_134

_134

/// The storage capacity of the account in bytes.

_134

access(all)

_134

let capacity: UInt64

_134

_134

/// All public paths of this account.

_134

access(all)

_134

let publicPaths: [PublicPath]

_134

_134

/// All storage paths of this account.

_134

access(all)

_134

let storagePaths: [StoragePath]

_134

_134

/// Saves the given object into the account's storage at the given path.

_134

///

_134

/// Resources are moved into storage, and structures are copied.

_134

///

_134

/// If there is already an object stored under the given path, the program aborts.

_134

///

_134

/// The path must be a storage path, i.e., only the domain `storage` is allowed.

_134

access(Storage | SaveValue)

_134

fun save<T: Storable>(_ value: T, to: StoragePath)

_134

_134

/// Reads the type of an object from the account's storage, which is stored under the given path,

_134

/// or nil if no object is stored under the given path.

_134

///

_134

/// If there is an object stored, the type of the object is returned without modifying the stored object.

_134

///

_134

/// The path must be a storage path, i.e., only the domain `storage` is allowed.

_134

access(all)

_134

view fun type(at path: StoragePath): Type?

_134

_134

/// Loads an object from the account's storage, which is stored under the given path,

_134

/// or nil if no object is stored under the given path.

_134

///

_134

/// If there is an object stored,

_134

/// the stored resource or structure is moved out of storage and returned as an optional.

_134

///

_134

/// When the function returns, the storage no longer contains an object under the given path.

_134

///

_134

/// The given type must be a supertype of the type of the loaded object.

_134

/// If it is not, the function panics.

_134

///

_134

/// The given type must not necessarily be exactly the same as the type of the loaded object.

_134

///

_134

/// The path must be a storage path, i.e., only the domain `storage` is allowed.

_134

access(Storage | LoadValue)

_134

fun load<T: Storable>(from: StoragePath): T?

_134

_134

/// Returns a copy of a structure stored in account storage under the given path,

_134

/// without removing it from storage,

_134

/// or nil if no object is stored under the given path.

_134

///

_134

/// If there is a structure stored, it is copied.

_134

/// The structure stays stored in storage after the function returns.

_134

///

_134

/// The given type must be a supertype of the type of the copied structure.

_134

/// If it is not, the function panics.

_134

///

_134

/// The given type must not necessarily be exactly the same as the type of the copied structure.

_134

///

_134

/// The path must be a storage path, i.e., only the domain `storage` is allowed.

_134

access(Storage | CopyValue)

_134

view fun copy<T: AnyStruct>(from: StoragePath): T?

_134

_134

/// Returns true if the object in account storage under the given path satisfies the given type,

_134

/// i.e. could be borrowed using the given type.

_134

///

_134

/// The given type must not necessarily be exactly the same as the type of the borrowed object.

_134

///

_134

/// The path must be a storage path, i.e., only the domain `storage` is allowed.

_134

access(all)

_134

view fun check<T: Any>(from: StoragePath): Bool

_134

_134

/// Returns a reference to an object in storage without removing it from storage.

_134

///

_134

/// If no object is stored under the given path, the function returns nil.

_134

/// If there is an object stored, a reference is returned as an optional,

_134

/// provided it can be borrowed using the given type.

_134

/// If the stored object cannot be borrowed using the given type, the function panics.

_134

///

_134

/// The given type must not necessarily be exactly the same as the type of the borrowed object.

_134

///

_134

/// The path must be a storage path, i.e., only the domain `storage` is allowed

_134

access(Storage | BorrowValue)

_134

view fun borrow<T: &Any>(from: StoragePath): T?

_134

_134

/// Iterate over all the public paths of an account,

_134

/// passing each path and type in turn to the provided callback function.

_134

///

_134

/// The callback function takes two arguments:

_134

/// 1. The path of the stored object

_134

/// 2. The run-time type of that object

_134

///

_134

/// Iteration is stopped early if the callback function returns `false`.

_134

///

_134

/// The order of iteration is undefined.

_134

///

_134

/// If an object is stored under a new public path,

_134

/// or an existing object is removed from a public path,

_134

/// then the callback must stop iteration by returning false.

_134

/// Otherwise, iteration aborts.

_134

///

_134

access(all)

_134

fun forEachPublic(_ function: fun(PublicPath, Type): Bool)

_134

_134

/// Iterate over all the stored paths of an account,

_134

/// passing each path and type in turn to the provided callback function.

_134

///

_134

/// The callback function takes two arguments:

_134

/// 1. The path of the stored object

_134

/// 2. The run-time type of that object

_134

///

_134

/// Iteration is stopped early if the callback function returns `false`.

_134

///

_134

/// If an object is stored under a new storage path,

_134

/// or an existing object is removed from a storage path,

_134

/// then the callback must stop iteration by returning false.

_134

/// Otherwise, iteration aborts.

_134

access(all)

_134

fun forEachStored(_ function: fun (StoragePath, Type): Bool)

_134

}

_134

_134

entitlement Storage

_134

_134

entitlement SaveValue

_134

entitlement LoadValue

_134

entitlement CopyValue

_134

entitlement BorrowValue ``

## Saving objects[​](#saving-objects "Direct link to Saving objects")

`_10

access(Storage | SaveValue)

_10

fun save<T: Storable>(_ value: T, to: StoragePath)`

The `save` function saves an object to account storage. The function moves resources and copies structures. If there is already an object stored under the given path, the program aborts. The path must be a storage path, and it must have the domain `storage`.

`T` is the type parameter for the object type. Cadence can infer this type parameter from the argument's type.

## Getting object type information[​](#getting-object-type-information "Direct link to Getting object type information")

`_10

access(all)

_10

view fun type(at path: StoragePath): Type?`

The `type` function returns the type of the object stored under the given path, or `nil` if the account does not store an object under the given path.

The function does not change the stored object.

The path must be a storage path, and it must have the domain `storage`.

## Loading (removing) objects[​](#loading-removing-objects "Direct link to Loading (removing) objects")

`_10

access(Storage | LoadValue)

_10

fun load<T: Storable>(from: StoragePath): T?`

The `load` function loads an object from account storage. If there is an object stored under the given path, the function moves the stored resource or structure out of storage and returns it as an optional. If there is no object stored under the given path, the function returns `nil`. When the function returns with an object, the storage no longer stores an object under the given path.

`T` is the type parameter for the object type. Programs must explicitly provide a type argument for the parameter.

The type `T` must be a supertype of the type of the loaded object. If it is not, the program aborts. The given type does not necessarily need to be exactly the same as the type of the loaded object.

The path must be a storage path, and it must have the domain `storage`.

## Copying objects[​](#copying-objects "Direct link to Copying objects")

`_10

access(Storage | CopyValue)

_10

view fun copy<T: AnyStruct>(from: StoragePath): T?`

The `copy` function returns a copy of a structure stored in account storage, without removing it from storage. If there is a structure stored under the given path, the function copies the stored structure and returns it as an optional. If there is no structure stored under the given path, the function returns `nil`. When the function returns with an object, the structure stays stored in storage after the function returns.

`T` is the type parameter for the structure type. Programs must explicitly provide a type argument for the parameter.

The type `T` must be a supertype of the type of the copied structure. If it is not, the program aborts. The given type does not necessarily have to be exactly the same as the type of the copied structure.

The path must be a storage path, and it must have the domain `storage`.

## Borrowing objects[​](#borrowing-objects "Direct link to Borrowing objects")

`_10

access(Storage | BorrowValue)

_10

view fun borrow<T: &Any>(from: StoragePath): T?`

The `borrow` function returns a reference to an objects stored in storage, without removing the object from storage. The function makes it convenient to work with objects in storage without having to move them out of storage.

If there is a structure stored under the given path, the function creates a reference to the object and returns the reference as an optional. If there is no structure stored under the given path, the function returns `nil`.

`T` is the type parameter for the object type. Programs must explicitly provide a type argument for the parameter.

The type argument must be a reference to any type, `&Any` (`Any` is the supertype of all types). The type `T` must be a supertype of the type of the borrowed object. If it is not, the program aborts. The given type does not necessarily have to be exactly the same as the type of the borrowed object.

The path must be a storage path, and it must have the domain `storage`.

## Example[​](#example "Direct link to Example")

The following steps show you how to declare a resource, create a new instance, and save it in the storage of the account:

1. Declare a resource interface named `HasCount` that has a field `count`:

   `_10

   resource interface HasCount {

   _10

   count: Int

   _10

   }`
2. Declare a resource named `Counter` that conforms to `HasCount`:

   `_10

   resource Counter: HasCount {

   _10

   access(all)

   _10

   var count: Int

   _10

   _10

   access(all)

   _10

   init(count: Int) {

   _10

   self.count = count

   _10

   }

   _10

   }`

   In this example, an authorized reference to an account is available through the constant `account`.
3. Create a new instance of the resource type `Counter` and save it in the storage of the account.

   * The path `/storage/counter` is used to refer to the stored value.
   * Its identifier `counter` was chosen freely and could be something else.

   `` _11

   account.storage.save(

   _11

   <-create Counter(count: 42),

   _11

   to: /storage/counter

   _11

   )

   _11

   _11

   // Run-time error: Storage already contains an object under path `/storage/counter`

   _11

   //

   _11

   account.storage.save(

   _11

   <-create Counter(count: 123),

   _11

   to: /storage/counter

   _11

   ) ``
4. Load the `Counter` resource from storage path `/storage/counter`.

   The new constant `counter` has the type `Counter?` (i.e., it is an optional), and its value is the counter resource that was saved at the beginning of the example:

   `_10

   let counter <- account.storage.load<@Counter>(from: /storage/counter)`

   The storage is now empty, there is no longer an object stored under the path `/storage/counter`.
5. Load the `Counter` resource again from storage path `/storage/counter`.

   The new constant `counter2` has the type `Counter?` and is `nil`, as nothing is stored under the path `/storage/counter` anymore because the previous load moved the counter out of storage:

   `_10

   let counter2 <- account.storage.load<@Counter>(from: /storage/counter)`
6. Create another new instance of the resource type `Counter` and save it in the storage of the account.

   The path `/storage/otherCounter` is used to refer to the stored value:

   `_10

   account.storage.save(

   _10

   <-create Counter(count: 123),

   _10

   to: /storage/otherCounter

   _10

   )`
7. Load the `Vault` resource from storage path `/storage/otherCounter`.

   The new constant `vault` has the type `Vault?` and its value is `nil` as there is a resource with type `Counter` stored under the path, which is not a subtype of the requested type `Vault`:

   `_10

   let vault <- account.storage.load<@Vault>(from: /storage/otherCounter)`

   The storage still stores a `Counter` resource under the path `/storage/otherCounter`.
8. Save the string "Hello, World" in storage under the path `/storage/helloWorldMessage`:

   `_10

   account.storage.save(

   _10

   "Hello, world!",

   _10

   to: /storage/helloWorldMessage

   _10

   )`
9. Copy the stored message from storage.

   After the copy, the storage still stores the string under the path. Unlike `load`, `copy` does not remove the object from storage:

   `_10

   let message = account.storage.copy<String>(from: /storage/helloWorldMessage)`
10. Create a new instance of the resource type `Vault` and save it in the storage of the account:

    `_10

    account.storage.save(

    _10

    <-createEmptyVault(),

    _10

    to: /storage/vault

    _10

    )

    _10

    _10

    // Invalid: Cannot copy a resource, as this would allow arbitrary duplication.

    _10

    //

    _10

    let vault <- account.storage.copy<@Vault>(from: /storage/vault)`
11. Create a reference to the object stored under path `/storage/counter`, typed as `&Counter`.

    * `counterRef` has type `&Counter?` and is a valid reference (i.e., non-`nil`) because the borrow succeeded.
    * There is an object stored under path `/storage/otherCounter` and it has type `Counter`, so it can be borrowed as `&Counter`:

    `` _10

    let counterRef = account.storage.borrow<&Counter>(from: /storage/otherCounter)

    _10

    _10

    counterRef?.count // is `42` ``
12. Create a reference to the object stored under path `/storage/otherCounter`, typed as `&{HasCount}`.

    `hasCountRef` is non-`nil` as there is an object stored under path `/storage/otherCounter`, and the stored value of type `Counter` conforms to the requested type `{HasCount}` — the type `Counter` implements the intersection type's interface `HasCount`:

    `_10

    let hasCountRef = account.storage.borrow<&{HasCount}>(from: /storage/otherCounter)`
13. Create a reference to the object stored under path `/storage/otherCounter`, typed as `&{SomethingElse}`.

    `otherRef` is `nil` as there is an object stored under path `/storage/otherCounter`, but the stored value of type `Counter` does not conform to the requested type `{SomethingElse}` — the type `Counter` does not implement the intersection type's interface `SomethingElse`:

    `_10

    let otherRef = account.storage.borrow<&{SomethingElse}>(from: /storage/otherCounter)`
14. Create a reference to the object stored under path `/storage/nonExistent`, typed as `&{HasCount}`.

    `nonExistentRef` is `nil`, as there is nothing stored under path `/storage/nonExistent`:

    `_10

    let nonExistentRef = account.storage.borrow<&{HasCount}>(from: /storage/nonExistent)`

## Iterating over stored objects[​](#iterating-over-stored-objects "Direct link to Iterating over stored objects")

The following functions allow iterating over an account's storage:

`_10

fun forEachPublic(_ function: fun(PublicPath, Type): Bool)

_10

fun forEachStored(_ function: fun(StoragePath, Type): Bool)`

The functions iterate over all stored objects in the particular domain, by calling the callback function for each stored object, and passing the path and the run-time type of the stored object.

The `Bool` value returned from the callback function determines whether iteration continues. If the callback function returns `true`, iteration proceeds to the next stored object. If the callback function returns `false`, the iteration function stops. The specific order in which the objects are iterated over is undefined, as is the behavior when a path is added or removed from storage.

warning

The iteration functions skip broken objects.

An object could be broken due to invalid types associated with the stored value. For example, the contract for the stored object might have syntactic or semantic errors.

warning

The order of iteration is undefined. Do not rely on any particular behavior.

Saving an object to a path or loading an object from storage during iteration can cause the order in which values are stored to change arbitrarily.

When a program continues to iterate after such an operation, the program aborts.

To avoid such errors, do not save objects to storage or load objects from storage during iteration. If you do perform such an operation, return `false` from the iteration callback to cause the iteration to end after the mutation like so:

`_17

account.storage.save(1, to: /storage/foo1)

_17

account.storage.save(2, to: /storage/foo2)

_17

account.storage.save(3, to: /storage/foo3)

_17

account.storage.save("qux", to: /storage/foo4)

_17

_17

account.storage.forEachStored(fun (path: StoragePath, type: Type): Bool {

_17

if type == Type<String>() {

_17

// Save a value to storage while iterating

_17

account.storage.save("bar", to: /storage/foo5)

_17

_17

// Returning false here ends iteration after storage is modified,

_17

// preventing the program from aborting

_17

return false

_17

}

_17

_17

return true

_17

})`

## Storage limit[​](#storage-limit "Direct link to Storage limit")

An account's storage is limited by its storage capacity.

An account's storage used is the sum of the size of all the data that the account stores, in MB. An account's storage capacity is a value that is calculated from the amount of $FLOW that is stored in the account's main $FLOW token vault.

At the end of every transaction, the storage used is compared to the storage capacity. For all accounts involved in the transaction, if the account's storage used is greater than its storage capacity, the transaction fails.

An account exposes its storage used through the `storage.used` field, and its storage capacity through the `storage.capacity` field.

The fields represent current values:

`_13

// Query the storage used before saving an object

_13

let storageUsedBefore = account.storage.used

_13

_13

// Save a resource into storage

_13

account.storage.save(

_13

<-create Counter(count: 123),

_13

to: /storage/counter

_13

)

_13

_13

// Query the storage used again after saving

_13

let storageUsedAfter = account.storage.used

_13

_13

let storageUsedChanged = storageUsedAfter > storageUsedBefore // is true`

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/accounts/storage.mdx)

[Previous

Paths](/docs/language/accounts/paths)[Next

Capabilities](/docs/language/accounts/capabilities)

###### Rate this page

😞😐😊

* [`Account.Storage`](#accountstorage)
* [Saving objects](#saving-objects)
* [Getting object type information](#getting-object-type-information)
* [Loading (removing) objects](#loading-removing-objects)
* [Copying objects](#copying-objects)
* [Borrowing objects](#borrowing-objects)
* [Example](#example)
* [Iterating over stored objects](#iterating-over-stored-objects)
* [Storage limit](#storage-limit)