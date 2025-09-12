# Source: https://cadence-lang.org/docs/language/accounts/

Accounts | Cadence



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
* Accounts

On this page

# Accounts

The type `Account` provides access to accounts. Accounts are only accessed through [references](/docs/language/references), which might be [authorized](/docs/language/references#authorized-references).

Account objects provide information about and allow the management of different aspects of the account, such as [account storage](/docs/language/accounts/storage),
[keys](/docs/language/accounts/keys), [contracts](/docs/language/contracts), and [capabilities](/docs/language/capabilities).

`_58

access(all)

_58

struct Account {

_58

_58

/// The address of the account.

_58

access(all)

_58

let address: Address

_58

_58

/// The FLOW balance of the default vault of this account.

_58

access(all)

_58

let balance: UFix64

_58

_58

/// The FLOW balance of the default vault of this account that is available to be moved.

_58

access(all)

_58

let availableBalance: UFix64

_58

_58

/// The storage of the account.

_58

access(mapping AccountMapping)

_58

let storage: Account.Storage

_58

_58

/// The contracts deployed to the account.

_58

access(mapping AccountMapping)

_58

let contracts: Account.Contracts

_58

_58

/// The keys assigned to the account.

_58

access(mapping AccountMapping)

_58

let keys: Account.Keys

_58

_58

/// The inbox allows bootstrapping (sending and receiving) capabilities.

_58

access(mapping AccountMapping)

_58

let inbox: Account.Inbox

_58

_58

/// The capabilities of the account.

_58

access(mapping AccountMapping)

_58

let capabilities: Account.Capabilities

_58

}

_58

_58

entitlement mapping AccountMapping {

_58

include Identity

_58

_58

Storage -> SaveValue

_58

Storage -> LoadValue

_58

Storage -> CopyValue

_58

Storage -> BorrowValue

_58

_58

Contracts -> AddContract

_58

Contracts -> UpdateContract

_58

Contracts -> RemoveContract

_58

_58

Keys -> AddKey

_58

Keys -> RevokeKey

_58

_58

Inbox -> PublishInboxCapability

_58

Inbox -> UnpublishInboxCapability

_58

Inbox -> ClaimInboxCapability

_58

_58

Capabilities -> StorageCapabilities

_58

Capabilities -> AccountCapabilities

_58

}`

## Accessing an account[​](#accessing-an-account "Direct link to Accessing an account")

The following sections describe how to perform read and write operation to view account details.

### Read operations[​](#read-operations "Direct link to Read operations")

Access to an `&Account` means having *read access* to it. For example, the `address` and `balance` fields have the `access(all)` modifier, so they are always accessible, which is safe because this information is public, and the fields are read-only.

Any code can get a read-only reference to an account (`&Account`) at a given address by using the built-in `getAccount` function:

`_10

view fun getAccount(_ address: Address): &Account`

### Write operations[​](#write-operations "Direct link to Write operations")

Access to an authorized account reference (`auth(...) &Account`) means having a certain **write access** to it.

[Entitlements](/docs/language/access-control#entitlements) authorize access to accounts. Cadence provides both coarse-grained and fine-grained entitlements, which decide what management functions are accessible on the account.

For example, the coarse-grained entitlement `Storage` grants access to all storage related functions, such as `save` and `load`, which save a value to storage, and load a value from storage respectively.

The fine-grained entitlement `AddKey`, for instance, grants access to only the `add` function of the `Account.Keys` value — that is, it grants access to adding a key to the account.

An authorized account reference like `auth(Storage, AddKey) &Account` therefore provides read access, as well as write access to storage, and the ability to add a new key to that account.

[Signed transactions](/docs/language/transactions) can get authorized account references for each signer of the transaction that signs as an authorizer. The `prepare` phase of the transaction can specify exactly which entitlements it needs to perform its work.

For example, a transaction that deploys a contract to an account can be written as follows:

`_10

transaction {

_10

prepare(signer: auth(AddContract) &Account) {

_10

signer.contracts.add(name: "MyContract", code: [/* code */])

_10

}

_10

}`

In this example, the transaction requests an authorized reference with the `AddContract` entitlement. That means that the transaction is entitled to add a contract to the account, but is not able to add another key to the account, for example.

The following Script can get any kind of access to any account, using the built-in `getAuthAccount` function:

`_10

view fun getAuthAccount<T: &Account>(_ address: Address): T`

This function is only available in scripts. Though scripts can perform write operations, they discard their changes upon completion. Attempting to use this function outside of a script (e.g., in a transaction) causes a type error.

## Creating an account[​](#creating-an-account "Direct link to Creating an account")

The `Account` constructor allows the creation of new accounts. The function requires a reference to a *payer* account, which should pay for the account creation.

The payer account must have enough funds to be able to create an account. If the account does not have the required funds, the program aborts.

The constructor returns a reference to the new account, which has all coarse-grained account entitlements (it has the type `auth(Storage, Contracts, Keys, Inbox, Capabilities) Account`). This provides write access to all parts fo the new account (e.g., storage, contracts, and keys):

`_10

fun Account(payer: auth(BorrowValue | Storage) &Account):

_10

auth(Storage, Contracts, Keys, Inbox, Capabilities) &Account`

For example, the following transaction creates a new account and has the signer of the transaction pay for it:

`_10

transaction {

_10

prepare(signer: auth(BorrowValue) &Account) {

_10

let account = Account(payer: signer)

_10

}

_10

}`

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/accounts/index.mdx)

[Previous

Prescedence and Associativity](/docs/language/operators/prescedence-associativity)[Next

Paths](/docs/language/accounts/paths)

###### Rate this page

😞😐😊

* [Accessing an account](#accessing-an-account)
  + [Read operations](#read-operations)
  + [Write operations](#write-operations)
* [Creating an account](#creating-an-account)