# Source: https://cadence-lang.org/docs/language/accounts




Accounts | Cadence




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
* [Guide for Solidity Developers](/docs/solidity-to-cadence)
* [Contract Upgrades with Incompatible Changes](/docs/contract-upgrades)
* [JSON-Cadence format](/docs/json-cadence-spec)
* [Measuring Time](/docs/measuring-time)
* [Testing](/docs/testing-framework)


* [Language Reference](/docs/language/)
* Accounts
On this page
# Accounts

The type `Account` provides access to accounts,
Accounts are only accessed through [references](/docs/language/references),
which might be [authorized](/docs/language/references#authorized-references).

Account objects provide information about and allow the management of
different aspects of the account, such as [account storage](/docs/language/accounts/storage),
[keys](/docs/language/accounts/keys), [contracts](/docs/language/accounts/contracts),
and [capabilities](/docs/language/accounts/capabilities).

 `_58access(all)_58struct Account {_58_58 /// The address of the account._58 access(all)_58 let address: Address_58_58 /// The FLOW balance of the default vault of this account._58 access(all)_58 let balance: UFix64_58_58 /// The FLOW balance of the default vault of this account that is available to be moved._58 access(all)_58 let availableBalance: UFix64_58_58 /// The storage of the account._58 access(mapping AccountMapping)_58 let storage: Account.Storage_58_58 /// The contracts deployed to the account._58 access(mapping AccountMapping)_58 let contracts: Account.Contracts_58_58 /// The keys assigned to the account._58 access(mapping AccountMapping)_58 let keys: Account.Keys_58_58 /// The inbox allows bootstrapping (sending and receiving) capabilities._58 access(mapping AccountMapping)_58 let inbox: Account.Inbox_58_58 /// The capabilities of the account._58 access(mapping AccountMapping)_58 let capabilities: Account.Capabilities_58}_58_58entitlement mapping AccountMapping {_58 include Identity_58_58 Storage -> SaveValue_58 Storage -> LoadValue_58 Storage -> CopyValue_58 Storage -> BorrowValue_58_58 Contracts -> AddContract_58 Contracts -> UpdateContract_58 Contracts -> RemoveContract_58_58 Keys -> AddKey_58 Keys -> RevokeKey_58_58 Inbox -> PublishInboxCapability_58 Inbox -> UnpublishInboxCapability_58 Inbox -> ClaimInboxCapability_58_58 Capabilities -> StorageCapabilities_58 Capabilities -> AccountCapabilities_58}`
## Account access[​](#account-access "Direct link to Account access")

### Performing read operations[​](#performing-read-operations "Direct link to Performing read operations")

Access to an `&Account` means having "read access" to it.
For example, the `address` and `balance` fields have the `access(all)` modifier,
so are always accessible, which is safe because this information is public,
and the fields are read-only.

Any code can get a "read-only" reference to an account (`&Account`)
at a given address by using the built-in `getAccount` function:

 `_10view fun getAccount(_ address: Address): &Account`
### Performing write operations[​](#performing-write-operations "Direct link to Performing write operations")

Access to an authorized account reference (`auth(...) &Account`)
means having certain "write access" to it.

[Entitlements](/docs/language/access-control#entitlements) authorize access to accounts.
Cadence provides both coarse-grained and fine-grained entitlements,
which decide what management functions are accessible on the account.

For example, the coarse-grained entitlement `Storage` grants access to all
storage related functions, such as `save` and `load`, which save a value to storage,
and load a value from storage respectively.

The fine-grained entitlement `AddKey` for instance,
grants access to only the `add` function of the `Account.Keys` value,
that is, it grants access to adding a key to the account.

An authorized account reference like `auth(Storage, AddKey) &Account`
therefore provides read access, as well as write access to storage,
and the ability to add a new key to that account.

[Signed transactions](/docs/language/transactions) can get authorized account references
for each signer of the transaction that signs as an authorizer.
The `prepare` phase of the transaction can specify exactly which entitlements
it needs to perform its work.

For example, a transaction that deploys a contract to an account can be written as follows:

 `_10transaction {_10 prepare(signer: auth(AddContract) &Account) {_10 signer.contracts.add(name: "MyContract", code: [/* code */])_10 }_10}`

Here, the transaction requests an authorized reference with the `AddContract` entitlement.
That means that the transaction is entitled to add a contract to the account,
but is not able to add another key to the account, for example.

Script can get any kind of access to any account, using the built-in `getAuthAccount` function:

 `_10view fun getAuthAccount<T: &Account>(_ address: Address): T`

This function is only available in scripts.
Though scripts can perform write operations,
they discard their changes upon completion.
Attempting to use this function outside of a script,
for example in a transaction,
causes a type error.

## Creating an account[​](#creating-an-account "Direct link to Creating an account")

The `Account` constructor allows creating new accounts.
The function requires a reference to a *payer* account,
which should pay for the account creation.

The payer account must have enough funds to be able to create an account.
If the account does not have the required funds, the program aborts.

The constructor returns a reference to the new account
which has all coarse-grained account entitlements
(it has the type `auth(Storage, Contracts, Keys, Inbox, Capabilities) &Account`).
This provides write access to all parts fo the new account,
for example, storage, contracts, and keys.

 `_10fun Account(payer: auth(BorrowValue | Storage) &Account):_10 auth(Storage, Contracts, Keys, Inbox, Capabilities) &Account`

For example, the following transaction creates a new account
and has the signer of the transaction pay for it:

 `_10transaction {_10 prepare(signer: auth(BorrowValue) &Account) {_10 let account = Account(payer: signer)_10 }_10}`[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/accounts/index.mdx)[PreviousImports](/docs/language/imports)[NextPaths](/docs/language/accounts/paths)
###### Rate this page

😞😐😊

* [Account access](#account-access)
  + [Performing read operations](#performing-read-operations)
  + [Performing write operations](#performing-write-operations)
* [Creating an account](#creating-an-account)
Got suggestions for this site? 

* [It's open-source!](https://github.com/onflow/cadence-lang.org)
The source code of this site is licensed under the Apache License, Version 2.0.
Content is licensed under the Creative Commons Attribution 4.0 International License.

