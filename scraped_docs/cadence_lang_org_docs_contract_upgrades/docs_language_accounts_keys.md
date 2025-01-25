# Source: https://cadence-lang.org/docs/language/accounts/keys




Keys | Cadence




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
* [Cadence Guide for Solidity Developers](/docs/solidity-to-cadence)
* [Contract Upgrades with Incompatible Changes](/docs/contract-upgrades)
* [JSON-Cadence format](/docs/json-cadence-spec)
* [Measuring Time](/docs/measuring-time)
* [Testing](/docs/testing-framework)


* [Language Reference](/docs/language/)
* [Accounts](/docs/language/accounts/)
* Keys
On this page
# Keys

Accounts have keys associated with them.
When a key is added to an account,
the key can be used to sign a [transaction](/docs/language/transactions),
which in turn gets access the account
and can [perform write operations](/docs/language/accounts/#performing-write-operations) on it.

An account exposes its keys through the `keys` field,
which has the type `Account.Keys`.

## `Account.Keys`[​](#accountkeys "Direct link to accountkeys")

 `_43access(all)_43struct Keys {_43_43 /// The total number of unrevoked keys in this account._43 access(all)_43 let count: UInt64_43_43 /// Returns the key at the given index, if it exists, or nil otherwise._43 ///_43 /// Revoked keys are always returned, but they have `isRevoked` field set to true._43 access(all)_43 view fun get(keyIndex: Int): AccountKey?_43_43 /// Iterate over all unrevoked keys in this account,_43 /// passing each key in turn to the provided function._43 ///_43 /// Iteration is stopped early if the function returns `false`._43 ///_43 /// The order of iteration is undefined._43 access(all)_43 fun forEach(_ function: fun(AccountKey): Bool)_43_43 /// Adds a new key with the given hashing algorithm and a weight._43 ///_43 /// Returns the added key._43 access(Keys | AddKey)_43 fun add(_43 publicKey: PublicKey,_43 hashAlgorithm: HashAlgorithm,_43 weight: UFix64_43 ): AccountKey_43_43 /// Marks the key at the given index revoked, but does not delete it._43 ///_43 /// Returns the revoked key if it exists, or nil otherwise._43 access(Keys | RevokeKey)_43 fun revoke(keyIndex: Int): AccountKey?_43}_43_43entitlement Keys_43_43entitlement AddKey_43entitlement RevokeKey`
## Account key[​](#account-key "Direct link to Account key")

An account key has the following structure:

 `_24access(all)_24struct AccountKey {_24_24 const accountKeyHashAlgorithmFieldDocString = ``_24 const accountKeyWeightFieldDocString = ``_24 const accountKeyIsRevokedFieldDocString = ``_24_24 /// The index of the account key._24 access(all)_24 let keyIndex: Int_24_24 /// The public key of the account key._24 let publicKey: PublicKey_24_24 /// The hash algorithm used by the public key._24 let hashAlgorithm: HashAlgorithm_24_24 /// The weight assigned to the account key,_24 /// with a maximum of 1000.0_24 let weight: UFix64_24_24 /// The flag indicating whether the key is revoked._24 let isRevoked: Bool_24}`

A valid account key's `publicKey` field is a `PublicKey` of either the
`ECDSA_P256` or `ECDSA_secp256k1` signature algorithm.
Public keys of other signature algorithms supported by Cadence are
not valid account public keys.

Refer to the [public keys section](/docs/language/crypto#public-keys)
for more details on the creation and validity of public keys.

A valid account key's `hashAlgorithm` field is either `SHA2_256` or `SHA3_256`.  

All other hash algorithms supported by Cadence are
not valid for hashing with an account key.

Refer to the the [hash algorithms section](/docs/language/crypto#hash-algorithms)
for more details on hash algorithms.

## Getting an account key[​](#getting-an-account-key "Direct link to Getting an account key")

The functions `keys.get` and `keys.forEach` allow retrieving the keys of an account.

The `get` function allows retrieving a key with a specific index.
The function returns the key if it exists, and `nil` otherwise.

 `_10access(all)_10view fun get(keyIndex: Int): AccountKey?`

The `forEach` function allows iterating over all keys of an account.

 `_10access(all)_10fun forEach(_ function: fun(AccountKey): Bool)`

For each key of the account, the `forEach` function calls the given callback, passing the key to it.
When the callback function returns `true` the iteration continues,
and when it returns `false`, iteration stops.

warning

The `keys.get` and `keys.forEach` functions include revoked keys,
which have the `isRevoked` field set to `true`.


 `_14access(all)_14fun main() {_14 let account = getAccount(0x42)_14_14 // Get the third key from the account._14 let thirdKey = account.keys.get(keyIndex: 2)_14 // ..._14_14 // Iterate over all keys of the account._14 account.keys.forEach(fun (key: AccountKey): Bool {_14 // ..._14 return true_14 })_14}`
## Adding an account key[​](#adding-an-account-key "Direct link to Adding an account key")

The function `keys.add` allows a key to access an account.

 `_10access(Keys | AddKey)_10fun add(_10 publicKey: PublicKey,_10 hashAlgorithm: HashAlgorithm,_10 weight: UFix64_10): AccountKey`

Calling the `add` function requires access to an account via a reference which is authorized
with the coarse-grained `Keys` entitlement (`auth(Keys) &Account`),
or the fine-grained `AddKey` entitlement (`auth(AddKey) &Account`).

For example, to add a public key to an existing account,
which signed the transaction:

 `_14transaction(publicKey: [UInt8]) {_14 prepare(signer: auth(AddKey) &Account) {_14 let key = PublicKey(_14 publicKey: publicKey,_14 signatureAlgorithm: SignatureAlgorithm.ECDSA_P256_14 )_14_14 signer.keys.add(_14 publicKey: key,_14 hashAlgorithm: HashAlgorithm.SHA3_256,_14 weight: 10.0_14 )_14 }_14}`

A more complex transaction, which creates an account,
has the signer of the transaction pay for the account creation,
and authorizes one key to access the account,
could look like:

 `_16transaction(publicKey: [UInt8]) {_16 prepare(signer: auth(BorrowValue) &Account) {_16 let key = PublicKey(_16 publicKey: publicKey,_16 signatureAlgorithm: SignatureAlgorithm.ECDSA_P256_16 )_16_16 let account = Account(payer: signer)_16_16 account.keys.add(_16 publicKey: key,_16 hashAlgorithm: HashAlgorithm.SHA3_256,_16 weight: 10.0_16 )_16 }_16}`
## Revoking an account key[​](#revoking-an-account-key "Direct link to Revoking an account key")

The `revoke` function revokes a key from accessing an account.
The function only marks the key at the given index as revoked, but never deletes it.

 `_10access(Keys | RevokeKey)_10fun revoke(keyIndex: Int): AccountKey?`

Calling the `revoke` function requires access to an account via a reference which is authorized
with the coarse-grained `Keys` entitlement (`auth(Keys) &Account`),
or the fine-grained `RevokeKey` entitlement (`auth(RevokeKey) &Account`).

For example, to revoke the third key of the account which signed the transaction:

 `_10transaction {_10 prepare(signer: auth(RevokeKey) &Account) {_10 let revokedKey = signer.keys.revoke(keyIndex: 2)_10 // ..._10 }_10}`[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/language/accounts/keys.mdx)[PreviousCapabilities](/docs/language/accounts/capabilities)[NextContracts](/docs/language/accounts/contracts)
###### Rate this page

😞😐😊

* [`Account.Keys`](#accountkeys)
* [Account key](#account-key)
* [Getting an account key](#getting-an-account-key)
* [Adding an account key](#adding-an-account-key)
* [Revoking an account key](#revoking-an-account-key)
Got suggestions for this site? 

* [It's open-source!](https://github.com/onflow/cadence-lang.org)
The source code of this site is licensed under the Apache License, Version 2.0.
Content is licensed under the Creative Commons Attribution 4.0 International License.

