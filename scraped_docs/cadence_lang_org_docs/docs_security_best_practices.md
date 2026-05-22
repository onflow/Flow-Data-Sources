# Source: https://cadence-lang.org/docs/security-best-practices

Cadence Security Best Practices | Cadence



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Cadence](/img/logo.svg)![Cadence](/img/logo.svg)](/)

[Learn](/docs)[Playground](https://play.flow.com/)[Community](/community)[Security](https://flow.com/flow-responsible-disclosure/)[Language Reference](/docs/language)

Search

* [Introduction](/docs/)
* [Why Use Cadence?](/docs/why)
* [Cadence Guide for Solidity Developers](/docs/solidity-to-cadence)
* [Tutorial](/docs/tutorial/first-steps)
* [Language Reference](/docs/language/)
* [Cadence 1.0 Migration Guide](/docs/cadence-migration-guide/)
* [Design Patterns](/docs/design-patterns)
* [Anti-Patterns](/docs/anti-patterns)
* [Development Standards](/docs/project-development-tips)
* [Security Best Practices](/docs/security-best-practices)
* [JSON-Cadence Format](/docs/json-cadence-spec)
* [Contract Upgrades with Incompatible Changes](/docs/contract-upgrades)
* [Measuring Time](/docs/measuring-time)
* [Testing](/docs/testing-framework)

* Security Best Practices

On this page

# Cadence Security Best Practices

This is an opinionated list of best practices that Cadence developers should follow to write more secure Cadence code.

Some practices listed below might overlap with advice in the [Cadence Anti-Patterns](/docs/anti-patterns) article, which is a recommended read as well.

## Access Control[​](#access-control "Direct link to Access Control")

Do not use the `access(all)` modifier on fields and functions unless absolutely necessary. Prefer `access(self)`, `access(contract)`, `access(account)`, or `access(SomeEntitlement)`. Unintentionally declaring fields or functions as `access(all)` can expose vulnerabilities in your code.

When writing definitions for contracts, structs, or resources, start by declaring all your fields and functions as `access(self)`. If there is a function that needs to be accessible by external code, only declare it as `access(all)` if it is a `view` function or if you definitely want it to be accessible by anyone in the network.

`_13

/// Simplified Bank Account implementation

_13

access(all) resource BankAccount {

_13

_13

/// Fields should default to access(self) to be safe

_13

/// and be readable through view functions

_13

access(self) var balance: UFix64

_13

_13

/// It is okay to make this function access(all) because it is a view function

_13

/// and all blockchain data is public

_13

access(all) view fun getBalance(): UFix64 {

_13

return self.balance

_13

}

_13

}`

If there are any functions that modify privileged state that also need to be callable from external code, use [entitlements](/docs/language/access-control) for the access modifiers for those functions:

`` _32

/// Declare Entitlements at the contract level — entitlements are

_32

/// namespaced to their contract and referenced by access modifiers

_32

/// on the contract's resources, structs, and functions.

_32

access(all) entitlement Owner

_32

_32

/// Simplified Bank Account implementation

_32

access(all) resource BankAccount {

_32

_32

/// Fields should default to access(self) just to be safe

_32

access(self) var balance: UFix64

_32

_32

/// All non-view functions should be something other than access(all),

_32

_32

/// This is only callable by other functions in the type, so it is `access(self)`

_32

access(self) fun updateBalance(_ new: UFix64) {

_32

self.balance = new

_32

}

_32

_32

/// This function is external, but should only be called by the owner

_32

/// so we use the `Owner` entitlement

_32

access(Owner) fun withdrawFromAccount(_ amount: UFix64): @BankAccount {

_32

self.updateBalance(self.balance - amount)

_32

return <-create BankAccount(balance: amount)

_32

}

_32

_32

/// This is also state-modifying, but we intend for it to be callable by anyone

_32

/// so we can make it access(all)

_32

access(all) fun depositToAccount(_ from: @BankAccount) {

_32

self.updateBalance(self.balance + from.getBalance())

_32

destroy from

_32

}

_32

} ``

## Access Control for Composite-typed Fields[​](#access-control-for-composite-typed-fields "Direct link to Access Control for Composite-typed Fields")

Declaring a field as [`access(all)`](/docs/language/access-control) only protects from replacing the field's value, but the value itself can still be mutated if it is mutable. Remember that containers, like dictionaries and arrays, are mutable and composite fields like structs and resources are still mutable through their own functions.

danger

This means that if you ever have a field that is a resource, struct, or capability, it should ALWAYS be `access(self)`! If it is `access(all)`, anyone could access it and call its functions, which could be a major vulnerability.

You can still allow external code to access that field, but only through functions that you have defined with `access(SomeEntitlement)`. This way, you can explicitly define how external code can access these fields.

# Capabilities

## Issuing Capabilities[​](#issuing-capabilities "Direct link to Issuing Capabilities")

Don't issue and publish capabilities unless absolutely necessary. Anyone can access capabilities that are published. If public access is needed, follow the [principle of least privilege/authority](https://en.wikipedia.org/wiki/Principle_of_least_privilege): make sure that the capability type only grants access to the fields and functions that should be exposed, and nothing else. Ideally, create a capability with a reference type that is unauthorized.

When issuing a capability, a capability of the same type might already be present. It is a good practice to check if a capability already exists with `getControllers()` before creating it. If it already exists, you can reuse it instead of issuing a new one. This prevents you from overloading your account storage and overpaying because of redundant capabilities.

`_20

// Capability to find or issue

_20

var flowTokenVaultCap: Capability<auth(FungibleToken.Withdraw) &FlowToken.Vault>? = nil

_20

_20

// Get all the capabilities that have already been issued for the desired storage path

_20

let flowTokenVaultCaps = signer.capabilities.storage.getControllers(forPath: /storage/flowTokenVault)

_20

_20

// Iterate through them to see if there is already one of the needed type

_20

for cap in flowTokenVaultCaps {

_20

if let cap = cap as? Capability<auth(FungibleToken.Withdraw) &FlowToken.Vault> {

_20

flowTokenVaultCap = cap

_20

break

_20

}

_20

}

_20

_20

// If no capabilities of the needed type are already present,

_20

// issue a new one

_20

if flowTokenVaultCap == nil {

_20

// issue a new entitled capability to the flow token vault

_20

flowTokenVaultCap = signer.capabilities.storage.issue<auth(FungibleToken.Withdraw) &FlowToken.Vault>(/storage/flowTokenVault)

_20

}`

## Publishing Capabilities[​](#publishing-capabilities "Direct link to Publishing Capabilities")

When publishing a capability, a published capability might already be present. It is a good practice to check if a capability already exists with `borrow` before creating it. This function will return `nil` if the capability does not exist.

`_10

// Check if the published capability already exists

_10

if signer.capabilities.borrow<&FlowToken.Vault>(/public/flowTokenReceiver) == nil {

_10

// since it doesn't exist yet, we should publish a new one that we created earlier

_10

signer.capabilities.publish(

_10

receiverCapability,

_10

at: /public/flowTokenReceiver

_10

)

_10

}`

## Checking Capabilities[​](#checking-capabilities "Direct link to Checking Capabilities")

If it is necessary to handle the case where borrowing a capability might fail, the `account.check` function can be used to verify that the target exists and has a valid type:

`_10

// check if the capability is valid

_10

if capability.check() {

_10

let reference = capability.borrow()

_10

} else {

_10

// do something else if the capability isn't valid

_10

}`

## Capability Access[​](#capability-access "Direct link to Capability Access")

Ensure capabilities cannot be accessed by unauthorized parties. For example, capabilities should not be accessible through a public field, including public dictionaries or arrays. Exposing a capability in such a way allows anyone to borrow it and to perform all actions that the capability allows, including `access(all)` fields and functions that aren't even in the restricted type of the capability.

## References[​](#references "Direct link to References")

[References](/docs/language/references) are ephemeral values and cannot be stored. If persistence is required, store a capability and borrow it when needed.

When exposing functionality in an account, struct, or resource, provide the least access necessary. When creating an authorized reference with [entitlements](/docs/language/access-control), create it with only the minimal set of [entitlements](/docs/language/access-control) required to achieve the desired functionality.

# Accounts

## Account storage[​](#account-storage "Direct link to Account storage")

Don't trust a user's [account storage](/docs/language/accounts/storage). Users have full control over their data and may reorganize it as they see fit. Users may store values in any path, so paths may store values of *unexpected* types. These values may be instances of types in contracts that the user deployed.

Always [borrow](/docs/language/capabilities#capabilities-in-accounts) with the specific type that is expected. Or, check if the value is an instance of the expected type.

## Authorized account references[​](#authorized-account-references "Direct link to Authorized account references")

Access to an authorized account reference (`auth(...) &Account`) gives access to entitled operations (e.g., the account's storage, keys, and contracts).

Therefore, avoid passing an entitled account reference to a function, and when defining a function, only specify an account reference parameter with the fine-grained entitlements required to perform the necessary operations.

It is preferable to use capabilities over direct account storage access when exposing account data. Using capabilities allows the revocation of access and limits the access to a single value with a certain set of functionality.

## Transactions[​](#transactions "Direct link to Transactions")

Audits of Cadence code should also include [transactions](/docs/language/transactions), as they may contain arbitrary code, just like in contracts. In addition, they are given full access to the accounts of the transaction's signers (i.e., the transaction is allowed to manipulate the signer's account storage, contracts, and keys).

Signing a transaction gives access to the operations accessible by the entitlements specified in the parameter types of the `prepare` block.

For example, the account reference type `auth(Storage) &Auth` is authorized to perform any storage operation.

When signing a transaction, audit which entitlements are requested.

When authoring a transaction, follow the [principle of least privilege/authority](https://en.wikipedia.org/wiki/Principle_of_least_privilege), and only request the least and most fine-grained account entitlements necessary to perform the operations of the transactions.

## Types[​](#types "Direct link to Types")

Use [intersection types and interfaces](/docs/language/types-and-type-system/intersection-types). Always use the most specific type possible, following the principle of least privilege. Types should always be as restrictive as possible, especially for resource types.

If given a less-specific type, cast to the more specific type that is expected. For example, when implementing the fungible token standard, a user may deposit any fungible token, so the implementation should cast to the expected concrete fungible token type.

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/security-best-practices.md)

[Previous

Development Standards](/docs/project-development-tips)[Next

JSON-Cadence Format](/docs/json-cadence-spec)

###### Rate this page

😞😐😊

* [Access Control](#access-control)
* [Access Control for Composite-typed Fields](#access-control-for-composite-typed-fields)
* [Issuing Capabilities](#issuing-capabilities)
* [Publishing Capabilities](#publishing-capabilities)
* [Checking Capabilities](#checking-capabilities)
* [Capability Access](#capability-access)
* [References](#references)
* [Account storage](#account-storage)
* [Authorized account references](#authorized-account-references)
* [Transactions](#transactions)
* [Types](#types)