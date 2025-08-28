# Source: https://developers.flow.com/cadence/language/capabilities

Capabilities | Cadence



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
* Capabilities

On this page

# Capabilities

Cadence supports [capability-based security](https://en.wikipedia.org/wiki/Capability-based_security) through the [object-capability model](https://en.wikipedia.org/wiki/Object-capability_model).

A capability in Cadence is a value that represents the right to access an object and perform certain operations on it. A capability specifies *what* can be accessed, and *how* it can be accessed.

Capabilities are unforgeable, transferable, and revocable.

Capabilities can be storage capabilities or account capabilities:

* **Storage capabilities** grant access to [objects in account storage](/docs/language/accounts/storage) via [paths](/docs/language/accounts/paths).
* **Account capabilities** grant access to [accounts](/docs/language/accounts/).

Capabilities can be borrowed to get a [reference](/docs/language/references) to the stored object or the account it refers to.

Capabilities have the type `Capability<T: &Any>`. The type parameter specifies the kind of reference that can be obtained when borrowing the capability. The type specifies the associated set of access rights through [entitlements](/docs/language/access-control): the reference type of the capability can be authorized, which grants the owner of the capability the ability to access the fields and functions of the target that require the given entitlements.

For example, a capability that has type `Capability<auth(SaveValue) &Account>` grants access to an account, and allows saving a value into the account.

Each capability has an ID, and the ID is unique **per account/address**.

Capabilities are created and managed through [capability controllers](#capabilities-in-accounts).

Capabilities are structs, so they are copyable. They can be used (i.e., borrowed) arbitrarily many times, as long as the target capability controller has not been deleted.

## `Capability`[​](#capability "Direct link to capability")

General syntax:

`_32

access(all)

_32

struct Capability<T: &Any> {

_32

_32

/// The address of the account that the capability targets:

_32

access(all)

_32

let address: Address

_32

_32

/// The ID of the capability:

_32

access(all)

_32

let id: UInt64

_32

_32

/// Returns a reference to the targeted object.

_32

///

_32

/// If the capability is revoked, the function returns nil.

_32

///

_32

/// If the capability targets an object in account storage,

_32

/// and no object is stored at the target storage path,

_32

/// the function returns nil.

_32

///

_32

/// If the targeted object cannot be borrowed using the given type,

_32

/// the function panics.

_32

///

_32

access(all)

_32

view fun borrow(): T?

_32

_32

/// Returns true if the capability currently targets an object

_32

/// that satisfies the given type (i.e., could be borrowed using

_32

/// the given type).

_32

///

_32

access(all)

_32

view fun check(): Bool

_32

}`

## Capabilities in accounts[​](#capabilities-in-accounts "Direct link to Capabilities in accounts")

An [account](/docs/language/accounts/) exposes its capabilities through the `capabilities` field, which has the type `Account.Capabilities`.

`` _52

access(all)

_52

struct Capabilities {

_52

_52

/// The storage capabilities of the account:

_52

access(mapping CapabilitiesMapping)

_52

let storage: Account.StorageCapabilities

_52

_52

/// The account capabilities of the account:

_52

access(mapping CapabilitiesMapping)

_52

let account: Account.AccountCapabilities

_52

_52

/// Returns the capability at the given public path.

_52

/// If the capability does not exist,

_52

/// or if the given type is not a supertype of the capability's

_52

/// borrow type, returns an "invalid" capability with ID 0 that

_52

/// will always fail to `check` or `borrow`:

_52

access(all)

_52

view fun get<T: &Any>(_ path: PublicPath): Capability<T>

_52

_52

/// Borrows the capability at the given public path.

_52

/// Returns nil if the capability does not exist, or cannot be

_52

/// borrowed using the given type. The function is equivalent

_52

/// to `get(path).borrow()`:

_52

access(all)

_52

view fun borrow<T: &Any>(_ path: PublicPath): T?

_52

_52

/// Returns true if a capability exists at the given public path:

_52

access(all)

_52

view fun exists(_ path: PublicPath): Bool

_52

_52

/// Publish the capability at the given public path.

_52

///

_52

/// If there is already a capability published under the given path,

_52

/// the program aborts.

_52

///

_52

/// The path must be a public path (i.e., only the domain `public`

_52

/// is allowed):

_52

access(Capabilities | PublishCapability)

_52

fun publish(_ capability: Capability, at: PublicPath)

_52

_52

/// Unpublish the capability published at the given path.

_52

///

_52

/// Returns the capability if one was published at the path.

_52

/// Returns nil if no capability was published at the path:

_52

access(Capabilities | UnpublishCapability)

_52

fun unpublish(_ path: PublicPath): Capability?

_52

}

_52

_52

entitlement Capabilities

_52

_52

entitlement PublishCapability

_52

entitlement UnpublishCapability ``

## Checking the existence of public capabilities with `.exists()`[​](#checking-the-existence-of-public-capabilities-with-exists "Direct link to checking-the-existence-of-public-capabilities-with-exists")

The function `capabilities.exists` determines if a public capability was [published](#publishing-capabilities) at the given path before:

`_10

access(all)

_10

view fun exists(_ path: PublicPath): Bool`

If the account has a capability published under the given path, the function returns true; otherwise, it returns false.

## Getting public capabilities with `.get()`[​](#getting-public-capabilities-with-get "Direct link to getting-public-capabilities-with-get")

The function `capabilities.get` obtains a public capability that was [published](#publishing-capabilities) before:

`_10

access(all)

_10

view fun get<T: &Any>(_ path: PublicPath): Capability<T>`

If the account has a capability with the given type published under the given path, the function returns it.

If the account has no capability published under the given path, or if the given type is not a supertype of the capability's borrow type, the function returns an "invalid" capability with ID 0 that will always fail to `check` or `borrow`.

## Borrowing public capabilities with `.borrow()`[​](#borrowing-public-capabilities-with-borrow "Direct link to borrowing-public-capabilities-with-borrow")

The convenience function `capabilities.borrow` obtains and borrows a public capability that was [published](#publishing-capabilities) before, in one step:

`_10

access(all)

_10

view fun borrow<T: &Any>(_ path: PublicPath): T?`

If the account has a capability with the given type published under the given path, the function borrows the capability and returns the resulting reference as an optional.

If the account has no capability published under the given path, or the requested type, via the type parameter `T`, and does not match the published capability, the function returns `nil`.

## Managing capabilities[​](#managing-capabilities "Direct link to Managing capabilities")

Capabilities can be storage capabilities or account capabilities:

* **Storage capabilities** grant access to [objects in account storage](/docs/language/accounts/storage) via [paths](/docs/language/accounts/paths). An account allows the management of storage capabilities through the `capabilities.storage` field, which has the type `Account.StorageCapabilities`.
* **Account capabilities** grant access to [accounts](/docs/language/accounts/). An account allows the management of account capabilities through the `capabilities.account` field, which has the type `Account.AccountCapabilities`.

A capability, and all its copies, is managed by a capability controller:

* **Storage capabilities** are controlled by storage capability controllers. Storage capability controllers have the type `StorageCapabilityController`.
* **Account capabilities** are controlled by account capability controllers. Account capability controllers have the type `AccountCapabilityController`.

### `Account.StorageCapabilities` and `Account.AccountCapabilities`[​](#accountstoragecapabilities-and-accountaccountcapabilities "Direct link to accountstoragecapabilities-and-accountaccountcapabilities")

`` _96

access(all)

_96

struct StorageCapabilities {

_96

_96

/// Issue/create a new storage capability:

_96

access(Capabilities | StorageCapabilities | IssueStorageCapabilityController)

_96

fun issue<T: &Any>(_ path: StoragePath): Capability<T>

_96

_96

/// Issue/create a new storage capability:

_96

access(Capabilities | StorageCapabilities | IssueStorageCapabilityController)

_96

fun issueWithType(_ path: StoragePath, type: Type): Capability

_96

_96

/// Get the storage capability controller for the capability with the

_96

/// specified ID.

_96

///

_96

/// Returns nil if the ID does not reference an existing storage

_96

/// capability:

_96

access(Capabilities | StorageCapabilities | GetStorageCapabilityController)

_96

view fun getController(byCapabilityID: UInt64): &StorageCapabilityController?

_96

_96

/// Get all storage capability controllers for capabilities that target

_96

/// this storage path:

_96

access(Capabilities | StorageCapabilities | GetStorageCapabilityController)

_96

view fun getControllers(forPath: StoragePath): [&StorageCapabilityController]

_96

_96

/// Iterate over all storage capability controllers for capabilities

_96

/// that target this storage path, passing a reference to each

_96

/// controller to the provided callback function.

_96

///

_96

/// Iteration is stopped early if the callback function returns `false`.

_96

///

_96

/// If a new storage capability controller is issued for the path,

_96

/// an existing storage capability controller for the path is deleted,

_96

/// or a storage capability controller is retargeted from or to the

_96

/// path, then the callback must stop iteration by returning false.

_96

/// Otherwise, iteration aborts:

_96

access(Capabilities | StorageCapabilities | GetStorageCapabilityController)

_96

fun forEachController(

_96

forPath: StoragePath,

_96

_ function: fun(&StorageCapabilityController): Bool

_96

)

_96

}

_96

_96

access(all)

_96

struct AccountCapabilities {

_96

_96

/// Issue/create a new account capability:

_96

access(Capabilities | AccountCapabilities | IssueAccountCapabilityController)

_96

fun issue<T: &Account>(): Capability<T>

_96

_96

/// Issue/create a new account capability:

_96

access(Capabilities | AccountCapabilities | IssueAccountCapabilityController)

_96

fun issueWithType(_ type: Type): Capability

_96

_96

/// Get capability controller for capability with the specified ID.

_96

///

_96

/// Returns nil if the ID does not reference an existing account

_96

/// capability:

_96

access(Capabilities | AccountCapabilities | GetAccountCapabilityController)

_96

view fun getController(byCapabilityID: UInt64): &AccountCapabilityController?

_96

_96

/// Get all capability controllers for all account capabilities:

_96

access(Capabilities | AccountCapabilities | GetAccountCapabilityController)

_96

view fun getControllers(): [&AccountCapabilityController]

_96

_96

/// Iterate over all account capability controllers for all account

_96

/// capabilities, passing a reference to each controller to the provided

_96

/// callback function.

_96

///

_96

/// Iteration is stopped early if the callback function returns `false`.

_96

///

_96

/// If a new account capability controller is issued for the account,

_96

/// or an existing account capability controller for the account is

_96

/// deleted, then the callback must stop iteration by returning false.

_96

/// Otherwise, iteration aborts:

_96

access(Capabilities | AccountCapabilities | GetAccountCapabilityController)

_96

fun forEachController(_ function: fun(&AccountCapabilityController): Bool)

_96

}

_96

_96

entitlement StorageCapabilities

_96

entitlement AccountCapabilities

_96

_96

entitlement GetStorageCapabilityController

_96

entitlement IssueStorageCapabilityController

_96

_96

entitlement GetAccountCapabilityController

_96

entitlement IssueAccountCapabilityController

_96

_96

entitlement mapping CapabilitiesMapping {

_96

include Identity

_96

_96

StorageCapabilities -> GetStorageCapabilityController

_96

StorageCapabilities -> IssueStorageCapabilityController

_96

_96

AccountCapabilities -> GetAccountCapabilityController

_96

AccountCapabilities -> IssueAccountCapabilityController

_96

} ``

### `AccountCapabilityController` and `StorageCapabilityController`[​](#accountcapabilitycontroller-and-storagecapabilitycontroller "Direct link to accountcapabilitycontroller-and-storagecapabilitycontroller")

`` _43

access(all)

_43

struct AccountCapabilityController {

_43

_43

/// The capability that is controlled by this controller:

_43

access(all)

_43

let capability: Capability

_43

_43

/// An arbitrary "tag" for the controller.

_43

/// For example, it could be used to describe the purpose of

_43

/// the capability.

_43

/// Empty by default:

_43

access(all)

_43

var tag: String

_43

_43

/// Updates this controller's tag to the provided string:

_43

access(all)

_43

fun setTag(_ tag: String)

_43

_43

/// The type of the controlled capability (i.e., the T

_43

/// in `Capability<T>`):

_43

access(all)

_43

let borrowType: Type

_43

_43

/// The identifier of the controlled capability.

_43

/// All copies of a capability have the same ID:

_43

access(all)

_43

let capabilityID: UInt64

_43

_43

/// Delete this capability controller,

_43

/// and disable the controlled capability and its copies.

_43

///

_43

/// The controller will be deleted from storage,

_43

/// but the controlled capability and its copies remain.

_43

///

_43

/// Once this function returns, the controller is no longer usable,

_43

/// all further operations on the controller will panic.

_43

///

_43

/// Borrowing from the controlled capability or its copies will

_43

/// return nil:

_43

///

_43

access(all)

_43

fun delete()

_43

} ``

`` _52

access(all)

_52

struct StorageCapabilityController {

_52

_52

/// The capability that is controlled by this controller:

_52

access(all)

_52

let capability: Capability

_52

_52

/// An arbitrary "tag" for the controller.

_52

/// For example, it could be used to describe the purpose of

_52

/// the capability.

_52

/// Empty by default:

_52

access(all)

_52

var tag: String

_52

_52

/// Updates this controller's tag to the provided string:

_52

access(all)

_52

fun setTag(_ tag: String)

_52

_52

/// The type of the controlled capability (i.e., the T

_52

/// in `Capability<T>`):

_52

access(all)

_52

let borrowType: Type

_52

_52

/// The identifier of the controlled capability.

_52

/// All copies of a capability have the same ID.

_52

access(all)

_52

let capabilityID: UInt64

_52

_52

/// Delete this capability controller,

_52

/// and disable the controlled capability and its copies.

_52

///

_52

/// The controller will be deleted from storage,

_52

/// but the controlled capability and its copies remain.

_52

///

_52

/// Once this function returns, the controller is no longer usable,

_52

/// all further operations on the controller will panic.

_52

///

_52

/// Borrowing from the controlled capability or its copies

_52

/// will return nil:

_52

///

_52

access(all)

_52

fun delete()

_52

_52

/// Returns the targeted storage path of the controlled capability:

_52

access(all)

_52

fun target(): StoragePath

_52

_52

/// Retarget the controlled capability to the given storage path.

_52

/// The path may be different or the same as the current path:

_52

access(all)

_52

fun retarget(_ target: StoragePath)

_52

} ``

### Issuing capabilities[​](#issuing-capabilities "Direct link to Issuing capabilities")

Capabilities are created by *issuing* them in the target account.

**Issuing storage capabilities**

The `capabilities.storage.issue` function issues a new storage capability that targets the given storage path and can be borrowed with the given type:

`_10

access(Capabilities | StorageCapabilities | IssueStorageCapabilityController)

_10

fun issue<T: &Any>(_ path: StoragePath): Capability<T>`

Calling the `issue` function requires access to an account via a reference, which is authorized with the coarse-grained `Capabilities` or `StorageCapabilities` entitlements (`aut (Capabilities) &Account` or `auth(StorageCapabilities) &Account`), or the fine-grained `IssueStorageCapabilityController` entitlement (`auth(IssueStorageCapabilityController) &Account`).

The path must be a storage path, and it must have the domain `storage`.

For example, the following transaction issues a new storage capability, which grants the ability to withdraw from the stored vault by authorizing the capability to be borrowed with the necessary `Withdraw` entitlement:

`_10

transaction {

_10

prepare(signer: auth(IssueStorageCapabilityController) &Account) {

_10

let capability = signer.capabilities.storage.issue<auth(Withdraw) &Vault>(/storage/vault)

_10

// ...

_10

}

_10

}`

**Issuing account capabilities**

The `capabilities.account.issue` function issues a new account capability that targets the account and can be borrowed with the given type:

`_10

access(Capabilities | AccountCapabilities | IssueAccountCapabilityController)

_10

fun issue<T: &Account>(): Capability<T>`

Calling the `issue` function requires access to an account via a reference, which is authorized with the coarse-grained `Capabilities` or `AccountCapabilities` entitlements (`auth(Capabilities) &Account` or `auth(AccountCapabilities) &Account`), or the fine-grained `IssueAccountCapabilityController` entitlement (`auth(IssueAccountCapabilityController) &Account`).

For example, the following transaction issues a new account capability, which grants the ability to save objects into the account by authorizing the capability to be borrowed with the necessary [`SaveValue` entitlement](/docs/language/accounts/storage#saving-objects):

`_10

transaction {

_10

prepare(signer: auth(IssueAccountCapabilityController) &Account) {

_10

let capability = signer.capabilities.account.issue<auth(SaveValue) &Account>()

_10

// ...

_10

}

_10

}`

### Publishing capabilities[​](#publishing-capabilities "Direct link to Publishing capabilities")

Capabilities can be made available publicly by *publishing* them.

The `capabilities.publish` function publishes a capability under a given public path:

`_10

access(Capabilities | PublishCapability)

_10

fun publish(_ capability: Capability, at: PublicPath)`

Calling the `publish` function requires access to an account via a reference that is authorized with the coarse-grained `Capabilities` entitlement (`auth(Capabilities) Account`), or the fine-grained `PublishCapability` entitlement (`auth(PublishCapability) &Account`).

For example, the following transaction issues a new storage capability and then publishes it under the path `/public/vault`, allowing anyone to access and borrow the capability and gain access to the stored vault. Note that the reference type is unauthorized, so when the capability is borrowed, only publicly accessible (`access(all)`) fields and functions of the object can be accessed:

`_10

transaction {

_10

prepare(signer: auth(Capabilities) &Account) {

_10

let capability = signer.capabilities.storage.issue<&Vault>(/storage/vault)

_10

signer.capabilities.publish(capability, at: /public/vault)

_10

}

_10

}`

### Unpublishing capabilities[​](#unpublishing-capabilities "Direct link to Unpublishing capabilities")

The `capabilities.unpublish` function unpublishes a capability from a given public path:

`_10

access(Capabilities | UnpublishCapability)

_10

fun unpublish(_ path: PublicPath): Capability?`

Calling the `unpublish` function requires access to an account via a reference, which is authorized with the coarse-grained `Capabilities` entitlement (`auth(Capabilities) Account`), or the fine-grained `UnpublishCapability` entitlement (`auth(UnpublishCapability) &Account`).

If there is a capability published under the path, the function removes it from the path and returns it. If there is no capability published under the path, the function returns `nil`.

For example, the following transaction unpublishes a capability that was previously published under the path `/public/vault`:

`_10

transaction {

_10

prepare(signer: auth(Capabilities) &Account) {

_10

signer.capabilities.unpublish(/public/vault)

_10

}

_10

}`

### Tagging capabilities[​](#tagging-capabilities "Direct link to Tagging capabilities")

Capabilities can be associated with a tag, which is an arbitrary string. The tag can be used for various purposes, such as recording the purpose of the capability. It is empty by default and is stored in the capability controller.

Both storage capability controllers (`StorageCapabilityController`) and account capability controllers (`AccountCapabilityController`) have a `tag` field and a `setTag` function, which can be used to get and set the tag:

`_10

access(all)

_10

var tag: String

_10

_10

access(all)

_10

fun setTag(_ tag: String)`

### Retargeting storage capabilities[​](#retargeting-storage-capabilities "Direct link to Retargeting storage capabilities")

Storage capabilities (`StorageCapabilityController`) can be retargeted to another storage path after they have been issued.

The `target` function returns the storage path of the controlled capability, and the `retarget` function sets a new storage path:

`_10

access(all)

_10

fun target(): StoragePath

_10

_10

access(all)

_10

fun retarget(_ target: StoragePath)`

### Revoking capabilities[​](#revoking-capabilities "Direct link to Revoking capabilities")

A capability and all of its copies can be revoked by deleting the capability's controller.

The `delete` function deletes a controller (`StorageCapabilityController` or `AccountCapabilityController`):

`_10

access(all)

_10

fun delete()`

### Getting capability controllers[​](#getting-capability-controllers "Direct link to Getting capability controllers")

The capability management types `StorageCapabilities` and `AccountCapabilities` allow obtaining the controller for a capability, as well as iterating over all existing controllers.

**Getting a storage capability controller**

The `capabilities.storage.getController` function gets the storage capability controller for the capability with the given capability ID:

`_10

access(Capabilities | StorageCapabilities | GetStorageCapabilityController)

_10

view fun getController(byCapabilityID: UInt64): &StorageCapabilityController?`

Calling the `getController` function requires access to an account via a reference, which is authorized with the coarse-grained `Capabilities` or `StorageCapabilities` entitlements (`auth(Capabilities) &Account` or `auth(StorageCapabilities) &Account`), or the fine-grained `GetStorageCapabilityController` entitlement (`auth(GetStorageCapabilityController) &Account`).

If a storage capability controller for the capability with the given ID exists, the function returns a reference to it, as an optional. If there is no storage capability controller with the given capability ID, the function returns `nil`.

**Getting an account capability controller**

The `capabilities.account.getController` function gets the account capability controller for the capability with the given capability ID:

`_10

access(Capabilities | AccountCapabilities | GetAccountCapabilityController)

_10

view fun getController(byCapabilityID: UInt64): &AccountCapabilityController?`

Calling the `getController` function requires access to an account via a reference, which is authorized with the coarse-grained `Capabilities` or `AccountCapabilities` entitlements (`auth(Capabilities) &Account` or `auth(AccountCapabilities) &Account`), or the fine-grained `GetAccountCapabilityController` entitlement (`auth(GetAccountCapabilityController) &Account`).

If an account capability controller for the capability with the given ID exists, the function returns a reference to it, as an optional. If there is no account capability controller with the given capability ID, the function returns `nil`.

**Iterating over storage capability controllers**

The functions `getControllers` and `forEachController` allow iterating over all storage capability controllers of a storage path:

`_10

access(Capabilities | StorageCapabilities | GetStorageCapabilityController)

_10

view fun getControllers(forPath: StoragePath): [&StorageCapabilityController]

_10

_10

access(Capabilities | StorageCapabilities | GetStorageCapabilityController)

_10

fun forEachController(

_10

forPath: StoragePath,

_10

_ function: fun(&StorageCapabilityController): Bool

_10

)`

Calling the `getControllers` and `forEachController` function requires access to an account via a reference, which is authorized with the coarse-grained `Capabilities` or `StorageCapabilities` entitlements (`auth(Capabilities) &Account` or `auth(StorageCapabilities) &Account`), or the fine-grained `GetStorageCapabilityController` entitlement (`auth(GetStorageCapabilityController) &Account`).

The `getControllers` function returns a new array of references to all storage capability controllers.

The `forEachController` function calls the given callback function for each storage capability controller and passes a reference to the function. Iteration stops when the callback function returns `false`.

**Iterating over account capability controllers**

The functions `getControllers` and `forEachController` allow iterating over all account capability controllers of the account:

`_10

access(Capabilities | AccountCapabilities | GetAccountCapabilityController)

_10

view fun getControllers(): [&AccountCapabilityController]

_10

_10

access(Capabilities | AccountCapabilities | GetAccountCapabilityController)

_10

fun forEachController(_ function: fun(&AccountCapabilityController): Bool)`

Calling the `getControllers` and `forEachController` function requires access to an account via a reference, which is authorized with the coarse-grained `Capabilities` or `AccountCapabilities` entitlements (`auth(Capabilities) &Account` or `auth(AccountCapabilities) &Account`), or the fine-grained `GetAccountCapabilityController` entitlement (`auth(GetAccountCapabilityController) &Account`).

The `getControllers` function returns a new array of references to all account capability controllers.

The `forEachController` function calls the given callback function for each account capability controller and passes a reference to the function. Iteration stops when the callback function returns `false`.

## Examples[​](#examples "Direct link to Examples")

**Entitlement Increment**

1. Declare a resource named `Counter` that has a field `count` and a function `increment`, which requires the `Increment` entitlement:

   `_16

   access(all)

   _16

   resource Counter {

   _16

   _16

   access(all)

   _16

   var count: UInt

   _16

   _16

   access(all)

   _16

   init(count: UInt) {

   _16

   self.count = count

   _16

   }

   _16

   _16

   access(Increment)

   _16

   fun increment(by amount: UInt) {

   _16

   self.count = self.count + amount

   _16

   }

   _16

   }`

   In this example, an account reference is available through the constant `account`, which has the type `auth(Storage, Capabilities) &Account` (i.e., the reference is authorized to perform storage and capability operations).
2. Create a new instance of the resource type `Counter` and save it in the storage of the account. The path `/storage/counter` is used to refer to the stored value. Its identifier `counter` was chosen freely and could be something else:

   `_10

   account.storage.save(

   _10

   <-create Counter(count: 42),

   _10

   to: /storage/counter

   _10

   )`
3. Issue a new storage capability that allows access to the stored counter resource:

   `_10

   let capability = account.capabilities.storage.issue<&Counter>(/storage/counter)`
4. Publish the capability under the path `/public/counter`, so that anyone can access the counter resource. Its identifier `counter` was chosen freely and could be something else:

   `_10

   account.capabilities.publish(capability, at: /public/counter)`

Imagine that the next example is in a different context, such as a new script or transaction:

1. Get a reference to the account that stores the counter:

   `_10

   let account = getAccount(0x1)`
2. Borrow the capability for the counter that is made publicly accessible through the path `/public/counter`. The `borrow` call returns an optional reference `&Counter?`. The borrow succeeds, and the result is not `nil`; it is a valid reference because:

   * The path `/public/counter` stores a capability.
   * The capability allows it to be borrowed as `&Counter`, as it has the type `Capability<&Counter>`.
   * The target of the storage capability, the *path* `/storage/counter`, stores an object and it has a type that is a subtype of the borrowed type (type equality is also considered a subtype relationship).
3. Force-unwrap the optional reference. After the call, the declared constant `counterRef` has type `&Counter`:

   `_10

   let counterRef = account.capabilities.borrow<&Counter>(/public/counter)!`
4. Read the field `count` of the `Counter`. The field can be accessed because it has the access modifier `access(all)`.

   Even though it is a variable field (`var`), it cannot be assigned to from outside of the object.

   `` _10

   counterRef.count // is `42`

   _10

   _10

   // Invalid: The `increment` function is not accessible for the

   _10

   // reference, because the reference has the type `&Counter`,

   _10

   // which does not authorize the entitlement `Increment`,

   _10

   // which is required by the `increment` function

   _10

   // (it has the access modifier ` access(Increment)`).

   _10

   _10

   counterRef.increment(by: 5) ``
5. Attempt to borrow the capability again for the counter, but use the type `auth(Increment) &Counter` to re-attempt the call to `increment`.

   Getting the capability fails, because the capability was issued using the type `&Counter`. After the call, `counterRef2` is `nil`.

   `_10

   let counterRef2 = account.capabilities.borrow<auth(Increment) &Counter>(/public/counter)`

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/capabilities.md)

[Previous

Access Control](/docs/language/access-control)[Next

Interfaces](/docs/language/interfaces)

###### Rate this page

😞😐😊

* [`Capability`](#capability)
* [Capabilities in accounts](#capabilities-in-accounts)
* [Checking the existence of public capabilities with `.exists()`](#checking-the-existence-of-public-capabilities-with-exists)
* [Getting public capabilities with `.get()`](#getting-public-capabilities-with-get)
* [Borrowing public capabilities with `.borrow()`](#borrowing-public-capabilities-with-borrow)
* [Managing capabilities](#managing-capabilities)
  + [`Account.StorageCapabilities` and `Account.AccountCapabilities`](#accountstoragecapabilities-and-accountaccountcapabilities)
  + [`AccountCapabilityController` and `StorageCapabilityController`](#accountcapabilitycontroller-and-storagecapabilitycontroller)
  + [Issuing capabilities](#issuing-capabilities)
  + [Publishing capabilities](#publishing-capabilities)
  + [Unpublishing capabilities](#unpublishing-capabilities)
  + [Tagging capabilities](#tagging-capabilities)
  + [Retargeting storage capabilities](#retargeting-storage-capabilities)
  + [Revoking capabilities](#revoking-capabilities)
  + [Getting capability controllers](#getting-capability-controllers)
* [Examples](#examples)