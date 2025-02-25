# Source: https://cadence-lang.org/docs/language/accounts/capabilities

Capabilities | Cadence



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Cadence](/img/logo.svg)![Cadence](/img/logo.svg)](/)

[Learn](/learn)[Solidity Guide](/docs/solidity-to-cadence)[Playground](https://play.flow.com/)[Community](/community)[Security](https://flow.com/flow-responsible-disclosure/)[Documentation](/docs/)[1.0](/docs/)

Search

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

    - [Paths](/docs/language/accounts/paths)
    - [Storage](/docs/language/accounts/storage)
    - [Capabilities](/docs/language/accounts/capabilities)
    - [Keys](/docs/language/accounts/keys)
    - [Contracts](/docs/language/accounts/contracts)
    - [Inbox](/docs/language/accounts/inbox)
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
* [Accounts](/docs/language/accounts/)
* Capabilities

On this page

# Capabilities

Accounts have [capabilities](/docs/language/capabilities) associated with them.

An account exposes its capabilities through the `capabilities` field,
which has the type `Account.Capabilities`.

## `Account.Capabilities`[​](#accountcapabilities "Direct link to accountcapabilities")

`_48

access(all)

_48

struct Capabilities {

_48

_48

/// The storage capabilities of the account.

_48

access(mapping CapabilitiesMapping)

_48

let storage: Account.StorageCapabilities

_48

_48

/// The account capabilities of the account.

_48

access(mapping CapabilitiesMapping)

_48

let account: Account.AccountCapabilities

_48

_48

/// Returns the capability at the given public path.

_48

/// If the capability does not exist,

_48

/// or if the given type is not a supertype of the capability's borrow type,

_48

/// returns an "invalid" capability with ID 0 that will always fail to `check` or `borrow`

_48

access(all)

_48

view fun get<T: &Any>(_ path: PublicPath): Capability<T>

_48

_48

/// Borrows the capability at the given public path.

_48

/// Returns nil if the capability does not exist, or cannot be borrowed using the given type.

_48

/// The function is equivalent to `get(path).borrow()`.

_48

access(all)

_48

view fun borrow<T: &Any>(_ path: PublicPath): T?

_48

_48

/// Returns true if a capability exists at the given public path.

_48

access(all)

_48

view fun exists(_ path: PublicPath): Bool

_48

_48

/// Publish the capability at the given public path.

_48

///

_48

/// If there is already a capability published under the given path, the program aborts.

_48

///

_48

/// The path must be a public path, i.e., only the domain `public` is allowed.

_48

access(Capabilities | PublishCapability)

_48

fun publish(_ capability: Capability, at: PublicPath)

_48

_48

/// Unpublish the capability published at the given path.

_48

///

_48

/// Returns the capability if one was published at the path.

_48

/// Returns nil if no capability was published at the path.

_48

access(Capabilities | UnpublishCapability)

_48

fun unpublish(_ path: PublicPath): Capability?

_48

}

_48

_48

entitlement Capabilities

_48

_48

entitlement PublishCapability

_48

entitlement UnpublishCapability`

## Checking the existence of public capabilities[​](#checking-the-existence-of-public-capabilities "Direct link to Checking the existence of public capabilities")

The function `capabilities.check` determines if a public capability
was [published](#publishing-capabilities) at the given path before.

`_10

access(all)

_10

view fun exists(_ path: PublicPath): Bool`

If the account has a capability published under the given path,
the function returns true, otherwise false.

## Getting public capabilities[​](#getting-public-capabilities "Direct link to Getting public capabilities")

The function `capabilities.get` obtains a public capability
that was [published](#publishing-capabilities) before.

`_10

access(all)

_10

view fun get<T: &Any>(_ path: PublicPath): Capability<T>`

If the account has a capability with the given type published under the given path,
the function returns it.

If the account has no capability published under the given path,
or if the given type is not a supertype of the capability's borrow type,
the function returns an "invalid" capability with ID 0 that will always fail to `check` or `borrow`.

The convenience function `capabilities.borrow` obtains and borrows a public capability
that was [published](#publishing-capabilities) before, in one step.

`_10

access(all)

_10

view fun borrow<T: &Any>(_ path: PublicPath): T?`

If the account has a capability with the given type published under the given path,
the function borrows the capability and returns the resulting reference as an optional.

If the account has no capability published under the given path,
or the requested type, via the type parameter `T`, does not match the published capability,
the function returns `nil`.

## Managing capabilities[​](#managing-capabilities "Direct link to Managing capabilities")

Capabilities can be storage capabilities or account capabilities:

* **Storage capabilities** grant access to [objects in account storage](/docs/language/accounts/storage),
  via [paths](/docs/language/accounts/paths).
  An account allows the management of storage capabilities through the `capabilities.storage` field,
  which has the type `Account.StorageCapabilities`.
* **Account capabilities** grant access to [accounts](/docs/language/accounts/).
  An account allows the management of account capabilities through the `capabilities.account` field,
  which has the type `Account.AccountCapabilities`.

A capability, and all its copies, is managed by a capability controller.

* **Storage capabilities** are controlled by storage capability controllers.
  Storage capability controllers have the type `StorageCapabilityController`.
* **Account capabilities** are controlled by account capability controllers.
  Account capability controllers have the type `AccountCapabilityController`.

### `Account.StorageCapabilities` and `Account.AccountCapabilities`[​](#accountstoragecapabilities-and-accountaccountcapabilities "Direct link to accountstoragecapabilities-and-accountaccountcapabilities")

`_90

access(all)

_90

struct StorageCapabilities {

_90

_90

/// Issue/create a new storage capability.

_90

access(Capabilities | StorageCapabilities | IssueStorageCapabilityController)

_90

fun issue<T: &Any>(_ path: StoragePath): Capability<T>

_90

_90

/// Issue/create a new storage capability.

_90

access(Capabilities | StorageCapabilities | IssueStorageCapabilityController)

_90

fun issueWithType(_ path: StoragePath, type: Type): Capability

_90

_90

/// Get the storage capability controller for the capability with the specified ID.

_90

///

_90

/// Returns nil if the ID does not reference an existing storage capability.

_90

access(Capabilities | StorageCapabilities | GetStorageCapabilityController)

_90

view fun getController(byCapabilityID: UInt64): &StorageCapabilityController?

_90

_90

/// Get all storage capability controllers for capabilities that target this storage path

_90

access(Capabilities | StorageCapabilities | GetStorageCapabilityController)

_90

view fun getControllers(forPath: StoragePath): [&StorageCapabilityController]

_90

_90

/// Iterate over all storage capability controllers for capabilities that target this storage path,

_90

/// passing a reference to each controller to the provided callback function.

_90

///

_90

/// Iteration is stopped early if the callback function returns `false`.

_90

///

_90

/// If a new storage capability controller is issued for the path,

_90

/// an existing storage capability controller for the path is deleted,

_90

/// or a storage capability controller is retargeted from or to the path,

_90

/// then the callback must stop iteration by returning false.

_90

/// Otherwise, iteration aborts.

_90

access(Capabilities | StorageCapabilities | GetStorageCapabilityController)

_90

fun forEachController(

_90

forPath: StoragePath,

_90

_ function: fun(&StorageCapabilityController): Bool

_90

)

_90

}

_90

_90

access(all)

_90

struct AccountCapabilities {

_90

_90

/// Issue/create a new account capability.

_90

access(Capabilities | AccountCapabilities | IssueAccountCapabilityController)

_90

fun issue<T: &Account>(): Capability<T>

_90

_90

/// Issue/create a new account capability.

_90

access(Capabilities | AccountCapabilities | IssueAccountCapabilityController)

_90

fun issueWithType(_ type: Type): Capability

_90

_90

/// Get capability controller for capability with the specified ID.

_90

///

_90

/// Returns nil if the ID does not reference an existing account capability.

_90

access(Capabilities | AccountCapabilities | GetAccountCapabilityController)

_90

view fun getController(byCapabilityID: UInt64): &AccountCapabilityController?

_90

_90

/// Get all capability controllers for all account capabilities.

_90

access(Capabilities | AccountCapabilities | GetAccountCapabilityController)

_90

view fun getControllers(): [&AccountCapabilityController]

_90

_90

/// Iterate over all account capability controllers for all account capabilities,

_90

/// passing a reference to each controller to the provided callback function.

_90

///

_90

/// Iteration is stopped early if the callback function returns `false`.

_90

///

_90

/// If a new account capability controller is issued for the account,

_90

/// or an existing account capability controller for the account is deleted,

_90

/// then the callback must stop iteration by returning false.

_90

/// Otherwise, iteration aborts.

_90

access(Capabilities | AccountCapabilities | GetAccountCapabilityController)

_90

fun forEachController(_ function: fun(&AccountCapabilityController): Bool)

_90

}

_90

_90

entitlement StorageCapabilities

_90

entitlement AccountCapabilities

_90

_90

entitlement GetStorageCapabilityController

_90

entitlement IssueStorageCapabilityController

_90

_90

entitlement GetAccountCapabilityController

_90

entitlement IssueAccountCapabilityController

_90

_90

entitlement mapping CapabilitiesMapping {

_90

include Identity

_90

_90

StorageCapabilities -> GetStorageCapabilityController

_90

StorageCapabilities -> IssueStorageCapabilityController

_90

_90

AccountCapabilities -> GetAccountCapabilityController

_90

AccountCapabilities -> IssueAccountCapabilityController

_90

}`

### `AccountCapabilityController` and `StorageCapabilityController`[​](#accountcapabilitycontroller-and-storagecapabilitycontroller "Direct link to accountcapabilitycontroller-and-storagecapabilitycontroller")

`_40

access(all)

_40

struct AccountCapabilityController {

_40

_40

/// The capability that is controlled by this controller.

_40

access(all)

_40

let capability: Capability

_40

_40

/// An arbitrary "tag" for the controller.

_40

/// For example, it could be used to describe the purpose of the capability.

_40

/// Empty by default.

_40

access(all)

_40

var tag: String

_40

_40

/// Updates this controller's tag to the provided string

_40

access(all)

_40

fun setTag(_ tag: String)

_40

_40

/// The type of the controlled capability, i.e. the T in `Capability<T>`.

_40

access(all)

_40

let borrowType: Type

_40

_40

/// The identifier of the controlled capability.

_40

/// All copies of a capability have the same ID.

_40

access(all)

_40

let capabilityID: UInt64

_40

_40

/// Delete this capability controller,

_40

/// and disable the controlled capability and its copies.

_40

///

_40

/// The controller will be deleted from storage,

_40

/// but the controlled capability and its copies remain.

_40

///

_40

/// Once this function returns, the controller is no longer usable,

_40

/// all further operations on the controller will panic.

_40

///

_40

/// Borrowing from the controlled capability or its copies will return nil.

_40

///

_40

access(all)

_40

fun delete()

_40

}`

`_49

access(all)

_49

struct StorageCapabilityController {

_49

_49

/// The capability that is controlled by this controller.

_49

access(all)

_49

let capability: Capability

_49

_49

/// An arbitrary "tag" for the controller.

_49

/// For example, it could be used to describe the purpose of the capability.

_49

/// Empty by default.

_49

access(all)

_49

var tag: String

_49

_49

/// Updates this controller's tag to the provided string

_49

access(all)

_49

fun setTag(_ tag: String)

_49

_49

/// The type of the controlled capability, i.e. the T in `Capability<T>`.

_49

access(all)

_49

let borrowType: Type

_49

_49

/// The identifier of the controlled capability.

_49

/// All copies of a capability have the same ID.

_49

access(all)

_49

let capabilityID: UInt64

_49

_49

/// Delete this capability controller,

_49

/// and disable the controlled capability and its copies.

_49

///

_49

/// The controller will be deleted from storage,

_49

/// but the controlled capability and its copies remain.

_49

///

_49

/// Once this function returns, the controller is no longer usable,

_49

/// all further operations on the controller will panic.

_49

///

_49

/// Borrowing from the controlled capability or its copies will return nil.

_49

///

_49

access(all)

_49

fun delete()

_49

_49

/// Returns the targeted storage path of the controlled capability.

_49

access(all)

_49

fun target(): StoragePath

_49

_49

/// Retarget the controlled capability to the given storage path.

_49

/// The path may be different or the same as the current path.

_49

access(all)

_49

fun retarget(_ target: StoragePath)

_49

}`

### Issuing capabilities[​](#issuing-capabilities "Direct link to Issuing capabilities")

Capabilities are created by *issuing* them in the target account.

#### Issuing storage capabilities[​](#issuing-storage-capabilities "Direct link to Issuing storage capabilities")

The `capabilities.storage.issue` function issues a new storage capability
that targets the given storage path and can be borrowed with the given type.

`_10

access(Capabilities | StorageCapabilities | IssueStorageCapabilityController)

_10

fun issue<T: &Any>(_ path: StoragePath): Capability<T>`

Calling the `issue` function requires access to an account via a reference which is authorized
with the coarse-grained `Capabilities` or `StorageCapabilities` entitlements
(`auth(Capabilities) &Account` or `auth(StorageCapabilities) &Account`),
or the fine-grained `IssueStorageCapabilityController` entitlement
(`auth(IssueStorageCapabilityController) &Account`).

The path must be a storage path, it must have the domain `storage`.

For example, the following transaction issues a new storage capability,
which grants the ability to withdraw from the stored vault,
by authorizing the capability to be borrowed with the necessary `Withdraw` entitlement.

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

#### Issuing account capabilities[​](#issuing-account-capabilities "Direct link to Issuing account capabilities")

The `capabilities.account.issue` function issues a new account capability
that targets the account and can be borrowed with the given type.

`_10

access(Capabilities | AccountCapabilities | IssueAccountCapabilityController)

_10

fun issue<T: &Account>(): Capability<T>`

Calling the `issue` function requires access to an account via a reference which is authorized
with the coarse-grained `Capabilities` or `AccountCapabilities` entitlements
(`auth(Capabilities) &Account` or `auth(AccountCapabilities) &Account`),
or the fine-grained `IssueAccountCapabilityController` entitlement
(`auth(IssueAccountCapabilityController) &Account`).

For example, the following transaction issues a new account capability,
which grants the ability to save objects into the account,
by authorizing the capability to be borrowed with the necessary [`SaveValue` entitlement](/docs/language/accounts/storage).

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

The `capabilities.publish` function publishes a capability under a given public path.

`_10

access(Capabilities | PublishCapability)

_10

fun publish(_ capability: Capability, at: PublicPath)`

Calling the `publish` function requires access to an account via a reference which is authorized
with the coarse-grained `Capabilities` entitlement (`auth(Capabilities) &Account`),
or the fine-grained `PublishCapability` entitlement (`auth(PublishCapability) &Account`).

For example, the following transaction issues a new storage capability,
and then publishes it under the path `/public/vault`,
allowing anyone to access and borrow the capability and gain access to the stored vault.
Note that the reference type is unauthorized,
so when the capability is borrowed,
only publicly accessible (`access(all)`) fields and functions of the object can be accessed.

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

The `capabilities.unpublish` function unpublishes a capability from a given public path.

`_10

access(Capabilities | UnpublishCapability)

_10

fun unpublish(_ path: PublicPath): Capability?`

Calling the `unpublish` function requires access to an account via a reference which is authorized
with the coarse-grained `Capabilities` entitlement (`auth(Capabilities) &Account`),
or the fine-grained `UnpublishCapability` entitlement (`auth(UnpublishCapability) &Account`).

If there is a capability published under the path, the function removes it from the path and returns it.
If there is no capability published under the path, the function returns `nil`.

For example, the following transaction unpublishes a capability
that was previously published under the path `/public/vault`.

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

Capabilities can be associated with a tag, an arbitrary string.
The tag can be used for various purposes, such as recording the purpose of the capability.
It is empty by default.
The tag is stored in the capability controller.

Both storage capability controllers (`StorageCapabilityController`)
and account capability controllers (`AccountCapabilityController`)
have a `tag` field and `setTag` function, which can be used to get and set the tag.

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

Storage capabilities (`StorageCapabilityController`) can be retargeted
to another storage path after they have been issued.

The `target` function returns the storage path of the controlled capability,
and the `retarget` function sets a new storage path.

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

A capability and all its copies can be revoked by deleting the capability's controller.

The `delete` function deletes a controller
(`StorageCapabilityController` or `AccountCapabilityController`):

`_10

access(all)

_10

fun delete()`

### Getting capability controllers[​](#getting-capability-controllers "Direct link to Getting capability controllers")

The capability management types `StorageCapabilities` and `AccountCapabilities`
allow obtaining the controller for a capability,
as well as iterating over all existing controllers.

#### Getting a storage capability controller[​](#getting-a-storage-capability-controller "Direct link to Getting a storage capability controller")

The `capabilities.storage.getController` function gets the storage capability controller
for the capability with the given capability ID.

`_10

access(Capabilities | StorageCapabilities | GetStorageCapabilityController)

_10

view fun getController(byCapabilityID: UInt64): &StorageCapabilityController?`

Calling the `getController` function requires access to an account via a reference which is authorized
with the coarse-grained `Capabilities` or `StorageCapabilities` entitlements
(`auth(Capabilities) &Account` or `auth(StorageCapabilities) &Account`),
or the fine-grained `GetStorageCapabilityController` entitlement
(`auth(GetStorageCapabilityController) &Account`).

If a storage capability controller for the capability with the given ID exists,
the function returns a reference to it, as an optional.
If there is no storage capability controller with the given capability ID,
the function returns `nil`.

#### Getting an account capability controller[​](#getting-an-account-capability-controller "Direct link to Getting an account capability controller")

The `capabilities.account.getController` function gets the account capability controller
for the capability with the given capability ID.

`_10

access(Capabilities | AccountCapabilities | GetAccountCapabilityController)

_10

view fun getController(byCapabilityID: UInt64): &AccountCapabilityController?`

Calling the `getController` function requires access to an account via a reference which is authorized
with the coarse-grained `Capabilities` or `AccountCapabilities` entitlements
(`auth(Capabilities) &Account` or `auth(AccountCapabilities) &Account`),
or the fine-grained `GetAccountCapabilityController` entitlement
(`auth(GetAccountCapabilityController) &Account`).

If a account capability controller for the capability with the given ID exists,
the function returns a reference to it, as an optional.
If there is no account capability controller with the given capability ID,
the function returns `nil`.

#### Iterating over storage capability controllers[​](#iterating-over-storage-capability-controllers "Direct link to Iterating over storage capability controllers")

The functions `getControllers` and `forEachController` allow iterating
over all storage capability controllers of a storage path.

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

Calling the `getControllers` and `forEachController` function
requires access to an account via a reference which is authorized
with the coarse-grained `Capabilities` or `StorageCapabilities` entitlements
(`auth(Capabilities) &Account` or `auth(StorageCapabilities) &Account`),
or the fine-grained `GetStorageCapabilityController` entitlement
(`auth(GetStorageCapabilityController) &Account`).

The `getControllers` function returns a new array of references
to all storage capability controllers.

The `forEachController` function calls the given callback function
for each storage capability controller and passes a reference to the function.
Iteration stops when the callback function returns `false`.

#### Iterating over account capability controllers[​](#iterating-over-account-capability-controllers "Direct link to Iterating over account capability controllers")

The functions `getControllers` and `forEachController` allow iterating
over all account capability controllers of the account.

`_10

access(Capabilities | AccountCapabilities | GetAccountCapabilityController)

_10

view fun getControllers(): [&AccountCapabilityController]

_10

_10

access(Capabilities | AccountCapabilities | GetAccountCapabilityController)

_10

fun forEachController(_ function: fun(&AccountCapabilityController): Bool)`

Calling the `getControllers` and `forEachController` function
requires access to an account via a reference which is authorized
with the coarse-grained `Capabilities` or `AccountCapabilities` entitlements
(`auth(Capabilities) &Account` or `auth(AccountCapabilities) &Account`),
or the fine-grained `GetAccountCapabilityController` entitlement
(`auth(GetAccountCapabilityController) &Account`).

The `getControllers` function returns a new array of references
to all account capability controllers.

The `forEachController` function calls the given callback function
for each account capability controller and passes a reference to the function.
Iteration stops when the callback function returns `false`.

## Example[​](#example "Direct link to Example")

`_47

entitlement Increment

_47

_47

// Declare a resource named `Counter` that has a field `count`

_47

// and a function `increment`, which requires the `Increment` entitlement.

_47

//

_47

access(all)

_47

resource Counter {

_47

_47

access(all)

_47

var count: UInt

_47

_47

access(all)

_47

init(count: UInt) {

_47

self.count = count

_47

}

_47

_47

access(Increment)

_47

fun increment(by amount: UInt) {

_47

self.count = self.count + amount

_47

}

_47

}

_47

_47

// In this example an account reference is available through the constant `account`,

_47

// which has the type `auth(Storage, Capabilities) &Account`,

_47

// i.e., the reference is authorized to perform storage and capability operations.

_47

_47

// Create a new instance of the resource type `Counter`

_47

// and save it in the storage of the account.

_47

//

_47

// The path `/storage/counter` is used to refer to the stored value.

_47

// Its identifier `counter` was chosen freely and could be something else.

_47

//

_47

account.storage.save(

_47

<-create Counter(count: 42),

_47

to: /storage/counter

_47

)

_47

_47

// Issue a new storage capability that allows access to the stored counter resource

_47

//

_47

let capability = account.capabilities.storage.issue<&Counter>(/storage/counter)

_47

_47

// Publish the capability under the path `/public/counter`,

_47

// so that anyone can access the counter resource.

_47

//

_47

// Its identifier `counter` was chosen freely and could be something else.

_47

//

_47

account.capabilities.publish(capability, at: /public/counter)`

Imagine that the next example is in a different context,
for example a new script or transaction.

`_49

_49

// Get a reference to the account that stores the counter

_49

//

_49

let account = getAccount(0x1)

_49

_49

// Borrow the capability for the counter that is made publicly accessible

_49

// through the path `/public/counter`.

_49

//

_49

// The call of `borrow` returns an optional reference `&Counter?`.

_49

// The borrow succeeds, and the result is not `nil`,

_49

// it is a valid reference, because:

_49

//

_49

// 1. The path `/public/counter` stores a capability.

_49

//

_49

// 2. The capability allows to be borrowed as `&Counter`,

_49

// as it has the type `Capability<&Counter>`.

_49

//

_49

// 3. The target of the storage capability, the *path* `/storage/counter`,

_49

// stores an object and it has a type which is a subtype of the borrowed type

_49

// (type equality is also considered a subtype relationship).

_49

//

_49

// Finally, force-unwrap the optional reference.

_49

// After the call, the declared constant `counterRef` has type `&Counter`.

_49

//

_49

let counterRef = account.capabilities.borrow<&Counter>(/public/counter)!

_49

_49

// Read the field `count` of the `Counter`.

_49

// The field can be accessed, because it has the access modifier `access(all)`.

_49

//

_49

// Even though it is a variable field (`var`),

_49

// it cannot be assigned to from outside of the object.

_49

//

_49

counterRef.count // is `42`

_49

_49

// Invalid: The `increment` function is not accessible for the reference,

_49

// because the reference has the type `&Counter`,

_49

// which does not authorize the entitlement `Increment`,

_49

// which is required by the `increment` function

_49

// (it has the access modifier ` access(Increment)`).

_49

//

_49

counterRef.increment(by: 5)

_49

_49

// Again, attempt to borrow the capability for the counter,

_49

// but use the type `auth(Increment) &Counter` to re-attempt the call to `increment`.

_49

//

_49

// Getting the capability fails, because the capability was issued using the type `&Counter`.

_49

// After the call, `counterRef2` is `nil`.

_49

//

_49

let counterRef2 = account.capabilities.borrow<auth(Increment) &Counter>(/public/counter)`

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/accounts/capabilities.mdx)

[Previous

Storage](/docs/language/accounts/storage)[Next

Keys](/docs/language/accounts/keys)

###### Rate this page

😞😐😊

* [`Account.Capabilities`](#accountcapabilities)
* [Checking the existence of public capabilities](#checking-the-existence-of-public-capabilities)
* [Getting public capabilities](#getting-public-capabilities)
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
* [Example](#example)

Got suggestions for this site?

* [It's open-source!](https://github.com/onflow/cadence-lang.org)

The source code of this site is licensed under the Apache License, Version 2.0.
Content is licensed under the Creative Commons Attribution 4.0 International License.