# Source: https://developers.flow.com/build/guides/account-linking/parent-accounts

Working With Parent Accounts | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/clients)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)
* [Differences vs. EVM](/build/differences-vs-evm)
* [Getting Started](/build/getting-started/contract-interaction)
* [Flow Protocol](/build/basics/blocks)
* [App Architecture](/build/app-architecture)
* [Writing and Deploying Smart Contracts](/build/learn-cadence)
* [Advanced Concepts](/build/advanced-concepts/account-abstraction)
* [Guides](/build/guides/account-linking)

  + [Account Linking (FLIP 72)](/build/guides/account-linking)

    - [Building Walletless Applications Using Child Accounts](/build/guides/account-linking/child-accounts)
    - [Working With Parent Accounts](/build/guides/account-linking/parent-accounts)
  + [Account Linking With NBA Top Shot](/build/guides/account-linking-with-dapper)
  + [More Guides](/build/guides/more-guides)
  + [Creating an NFT Contract](/build/guides/nft)
  + [Creating a Fungible Token](/build/guides/fungible-token)
  + [Building on Mobile](/build/guides/mobile/overview)
* [Core Smart Contracts](/build/core-contracts)
* [Explore More](/build/explore-more)

* Guides
* [Account Linking (FLIP 72)](/build/guides/account-linking)
* Working With Parent Accounts

On this page

# Working With Parent Accounts

In this doc, we'll continue from the perspective of a wallet or marketplace app seeking to facilitate a unified account
experience, abstracting away the partitioned access between accounts into a single dashboard for user interactions on
all their owned assets.

## Objectives[​](#objectives "Direct link to Objectives")

* Understand the Hybrid Custody account model
* Differentiate between restricted child accounts and unrestricted owned accounts
* Get your app to recognize "parent" accounts along with any associated "child" accounts
* View Fungible and NonFungible Token metadata relating to assets across all of a user's associated accounts - their
  wallet-mediated "parent" account and any hybrid custody model "child" accounts
* Facilitate transactions acting on assets in child accounts

## Design Overview[​](#design-overview "Direct link to Design Overview")

info

TL;DR: An account's
[`HybridCustody.Manager`](https://github.com/onflow/hybrid-custody/blob/main/contracts/HybridCustody.cdc) is the entry
point for all of a user's associated accounts.

The basic idea in the Hybrid Custody model is relatively simple. A parent account is one that has received delegated
(albeit restricted) access on another account. The account which has delegated authority over itself to the parent
account is the child account.

In the [Hybrid Custody Model](https://forum.onflow.org/t/hybrid-custody/4016), this child account would have shared
access between the app - the entity which created and likely custodies the account - and the linked parent account.

How does this delegation occur? Typically when we think of shared account access in crypto, we think keys. However,
Cadence enables [accounts to link Capabilities on
themselves](https://cadence-lang.org/docs/language/accounts/capabilities#accountcapabilities) and issue those
Capabilities to other parties (more on [capability-based access
here](https://cadence-lang.org/docs/language/capabilities)).

This feature has been leveraged in an ecosystem standard so that apps can implement a hybrid custody model whereby the app
creates an account it controls, then later delegates access on that account to the user once they've authenticated with
their wallet.

All related constructs are used together in the [`HybridCustody`
contract](https://github.com/onflow/hybrid-custody/tree/main) to define the standard.

Parent accounts own a `Manager` resource which stores Capabilities to `ChildAccount` (restricted access) and
`OwnedAccount` (unrestricted access) resources, both of which are stored in any given child account.

Therefore, the presence of a `Manager` in an account implies there are potentially associated accounts for which the
owning account has delegated access. This resource is intended to be configured with a public Capability that enables
querying of an account's child account addresses via `getAccountAddresses()` and `getOwnedAccountAddresses()`. As you can
deduce from these two methods, there is a notion of "owned" accounts which we'll expand on in a bit.

A wallet or marketplace wishing to discover all of a user's accounts and assets within them can do so by first looking
to the user's `Manager`.

### Identifying Account Hierarchy[​](#identifying-account-hierarchy "Direct link to Identifying Account Hierarchy")

To clarify, insofar as the standard is concerned, an account is a parent account if it contains a `Manager` resource,
and an account is a child account if it contains at minimum an `OwnedAccount` or additionally a `ChildAccount` resource.

Within a user's `Manager`, its mapping of `childAccounts` points to the addresses of its child accounts in each key,
with corresponding values giving the `Manager` access to those accounts via corresponding `ChildAccount` Capability.

![HybridCustody Conceptual Overview](/assets/images/hybrid_custody_conceptual_overview-d5155af50fce363671600e0242b4e391.png)

Likewise, the child account's `ChildAccount.parentAddress` (which owns a `Manager`) points to the user's account as its
parent address. This makes it easy to both identify whether an account is a parent, child, or both, and its associated
parent/child account(s).

`OwnedAccount` resources underly all account delegations, so can have multiple parents whereas `ChildAccount`s are 1:1.
This provides more granular revocation as each parent account has its own Capability path on which its access relies.

#### Restricted vs. Owned Accounts[​](#restricted-vs-owned-accounts "Direct link to Restricted vs. Owned Accounts")

It's worth noting here that `ChildAccount` Capabilities enable access to the underlying account according to rules
configured by the child account delegating access. The `ChildAccount` maintains these rules along with an `OwnedAccount`
Capability within which the `&Account` Capability is stored. Anyone with access to the surface level `ChildAccount`
can then access the underlying `Account`, but only according the pre-defined rule set. These rules are fundamentally
a list of Types that can/cannot be retrieved from an account.

The app developer can codify these rule sets on allowable Capability types in a
[`CapabilityFilter`](https://github.com/onflow/hybrid-custody/blob/main/contracts/CapabilityFilter.cdc) along with a
[`CapabilityFactory`](https://github.com/onflow/hybrid-custody/blob/main/contracts/CapabilityFactory.cdc) defining retrieval
patterns for those Capabilities. When delegation occurs, the developer would provide the `CapabilityFilter` and
`CapabilityFactory` Capabilities to an `OwnedAccount` resource which stores them in a `ChildAccount` resource. Then,
capabilities are created for the `OwnedAccount` and `ChildAccount` resource and are given to the specified parent
account.

So, if an app developer wants to enable Hybrid Custody but doesn't want to allow parent accounts to access FungibleToken
Vaults, for example, the app developer can codify rule sets enumerating allowable Capability types in a
`CapabilityFilter` along with a `CapabilityFactory` defining retrieval patterns for those Capabilities.

When delegation occurs, they would provide the `CapabilityFilter` and `CapabilityFactory` Capabilities to an
`OwnedAccount`. This `OwnedAccount` then wraps the given filter & factory Capabilities in a `ChildAccount` along with a
Capability to itself before publishing the new `ChildAccount` Capability for the specified parent account to claim.

info

Note that by enumerating allowable Types in your `CapabilityFilter.Filter` implementation, you're by default excluding
access to anything other than the Types you declare as allowable.

As mentioned earlier, `Manager`s also maintain access to "owned" accounts - accounts which define unrestricted access as
they allow direct retrieval of encapsulated `&Account` Capabilities. These owned accounts, found in `Manager.ownedAccounts`,
are simply `OwnedAccount` Capabilities instead of `ChildAccount` Capabilities.

![HybridCustody Total Overview](/assets/images/hybrid_custody_low_level-d02b49dc41a18f8ca382a968141846a4.png)

### Considerations[​](#considerations "Direct link to Considerations")

Do note that this construction does not prevent an account from having multiple parent accounts or a child account from
being the parent to other accounts. While initial intuition might lead one to believe that account associations are a
tree with the user at the root, the graph of associated accounts among child accounts may lead to cycles of association.

We believe it would be unlikely for a use case to demand a user delegates authority over their main account (in fact
we'd discourage such constructions), but delegating access between child accounts could be useful. As an example,
consider a set of local game clients across mobile and web platforms, each with self-custodied app accounts having
delegated authority to each other while both are child accounts of the user's main account.

Ultimately, it will be up to the implementing wallet/marketplace how far down the graph of account associations they'd
want to traverse and display to the user.

## Implementation[​](#implementation "Direct link to Implementation")

From the perspective of a wallet or marketplace app, some relevant things to know about the user are:

* Does this account have associated linked (child) accounts?
* What are those associated linked accounts, if any?
* What NFTs are owned by this user across all associated accounts?
* What are the balances of all FungibleTokens across all associated accounts?

And with respect to acting on the assets of child accounts and managing child accounts themselves:

* Accessing an NFT from a linked account's Collection
* Removing a linked account

## Examples[​](#examples "Direct link to Examples")

### Query Whether an Address Has Associated Accounts[​](#query-whether-an-address-has-associated-accounts "Direct link to Query Whether an Address Has Associated Accounts")

This script will return `true` if a `HybridCustody.Manager` is stored and `false` otherwise

has\_child\_accounts.cdc

`_10

import "HybridCustody"

_10

_10

access(all) fun main(parent: Address): Bool {

_10

let acct = getAuthAccount<auth(BorrowValue) &Account>(parent)

_10

if let manager = acct.storage.borrow<&HybridCustody.Manager>(from: HybridCustody.ManagerStoragePath) {

_10

return manager.getChildAddresses().length > 0

_10

}

_10

return false

_10

}`

### Query All Accounts Associated with Address[​](#query-all-accounts-associated-with-address "Direct link to Query All Accounts Associated with Address")

The following script will return an array of addresses associated with a given account's address, inclusive of the
provided address. If a `HybridCustody.Manager` is not found, the script will revert.

get\_child\_addresses.cdc

`_10

import "HybridCustody"

_10

_10

access(all) fun main(parent: Address): [Address] {

_10

let acct = getAuthAccount<auth(Storage) &Account>(parent)

_10

let manager = acct.storage.borrow<&HybridCustody.Manager>(from: HybridCustody.ManagerStoragePath)

_10

?? panic("manager not found")

_10

return manager.getChildAddresses()

_10

}`

### Query All Owned NFT Metadata[​](#query-all-owned-nft-metadata "Direct link to Query All Owned NFT Metadata")

While it is possible to iterate over the storage of all associated accounts in a single script, memory limits prevent
this approach from scaling well.

Since some accounts hold thousands of NFTs, we recommend breaking up iteration, utilizing several queries to iterate
over accounts and the storage of each account. Batching queries on individual accounts may even be required based on the
number of NFTs held.

1. Get all associated account addresses (see above)
2. Looping over each associated account address client-side, get each address's owned NFT metadata

For simplicity, we'll show a condensed query, returning NFT display views from all accounts associated with a given
address for a specified NFT Collection path.

get\_nft\_display\_view\_from\_public.cdc

`_59

import "NonFungibleToken"

_59

import "MetadataViews"

_59

import "HybridCustody"

_59

_59

/// Returns resolved Display from given address at specified path for each ID or nil if ResolverCollection is not found

_59

///

_59

access(all)

_59

fun getViews(_ address: Address, _ resolverCollectionPath: PublicPath): {UInt64: MetadataViews.Display} {

_59

_59

let account: PublicAccount = getAccount(address)

_59

let views: {UInt64: MetadataViews.Display} = {}

_59

_59

// Borrow the Collection

_59

if let collection = account.capabilities.borrow<&{NonFungibleToken.Collection}>(resolverCollectionPath) {

_59

// Iterate over IDs & resolve the view

_59

for id in collection.getIDs() {

_59

if let nft = collection.borrowNFT(id) {

_59

if let display = nft.resolveView(Type<MetadataViews.Display>()) as? MetadataViews.Display {

_59

views.insert(key: id, display)

_59

}

_59

}

_59

}

_59

}

_59

_59

return views

_59

}

_59

_59

/// Queries for MetadataViews.Display each NFT across all associated accounts from Collections at the provided

_59

/// PublicPath

_59

///

_59

access(all)

_59

fun main(address: Address, resolverCollectionPath: PublicPath): {Address: {UInt64: MetadataViews.Display}} {

_59

_59

let allViews: {Address: {UInt64: MetadataViews.Display}} = {

_59

address: getViews(address, resolverCollectionPath)

_59

}

_59

_59

/* Iterate over any associated accounts */

_59

//

_59

let seen: [Address] = [address]

_59

if let managerRef = getAuthAccount<auth(BorrowValue) &Account>(address)

_59

.storage

_59

.borrow<&HybridCustody.Manager>(from: HybridCustody.ManagerStoragePath) {

_59

_59

for childAccount in managerRef.getChildAddresses() {

_59

allViews.insert(key: childAccount, getViews(address, resolverCollectionPath))

_59

seen.append(childAccount)

_59

}

_59

_59

for ownedAccount in managerRef.getOwnedAddresses() {

_59

if seen.contains(ownedAccount) == false {

_59

allViews.insert(key: ownedAccount, getViews(address, resolverCollectionPath))

_59

seen.append(ownedAccount)

_59

}

_59

}

_59

}

_59

_59

return allViews

_59

}`

At the end of this query, the caller will have a mapping of `Display` views indexed on the NFT ID and grouped by account
Address. Note that this script does not take batching into consideration and assumes that each NFT resolves the
`MetadataViews.Display` view type.

### Query All Account FungibleToken Balances[​](#query-all-account-fungibletoken-balances "Direct link to Query All Account FungibleToken Balances")

Similar to the previous example, we recommend breaking up this task due to memory limits.

1. Get all linked account addresses (see above)
2. Looping over each associated account address client-side, get each address's owned FungibleToken Vault metadata

However, we'll condense both of these steps down into one script for simplicity:

get\_all\_vault\_bal\_from\_storage.cdc

`_66

import "FungibleToken"

_66

import "MetadataViews"

_66

import "HybridCustody"

_66

_66

/// Returns a mapping of balances indexed on the Type of resource containing the balance

_66

///

_66

access(all)

_66

fun getAllBalancesInStorage(_ address: Address): {Type: UFix64} {

_66

// Get the account

_66

let account = getAuthAccount<auth(BorrowValue) &Account>(address)

_66

// Init for return value

_66

let balances: {Type: UFix64} = {}

_66

// Track seen Types in array

_66

let seen: [Type] = []

_66

// Assign the type we'll need

_66

let balanceType: Type = Type<@{FungibleToken.Balance}>()

_66

// Iterate over all stored items & get the path if the type is what we're looking for

_66

account.forEachStored(fun (path: StoragePath, type: Type): Bool {

_66

if (type.isInstance(balanceType) || type.isSubtype(of: balanceType)) && !type.isRecovered {

_66

// Get a reference to the resource & its balance

_66

let vaultRef = account.borrow<&{FungibleToken.Balance}>(from: path)!

_66

// Insert a new values if it's the first time we've seen the type

_66

if !seen.contains(type) {

_66

balances.insert(key: type, vaultRef.balance)

_66

} else {

_66

// Otherwise just update the balance of the vault (unlikely we'll see the same type twice in

_66

// the same account, but we want to cover the case)

_66

balances[type] = balances[type]! + vaultRef.balance

_66

}

_66

}

_66

return true

_66

})

_66

return balances

_66

}

_66

_66

/// Queries for FT.Vault balance of all FT.Vaults in the specified account and all of its associated accounts

_66

///

_66

access(all)

_66

fun main(address: Address): {Address: {Type: UFix64}} {

_66

_66

// Get the balance for the given address

_66

let balances: {Address: {Type: UFix64}} = { address: getAllBalancesInStorage(address) }

_66

// Tracking Addresses we've come across to prevent overwriting balances (more efficient than checking dict entries (?))

_66

let seen: [Address] = [address]

_66

_66

/* Iterate over any associated accounts */

_66

//

_66

if let managerRef = getAuthAccount<auth(BorrowValue) &Account>(address)

_66

.storage

_66

.borrow<&HybridCustody.Manager>(from: HybridCustody.ManagerStoragePath) {

_66

_66

for childAccount in managerRef.getChildAddresses() {

_66

balances.insert(key: childAccount, getAllBalancesInStorage(address))

_66

seen.append(childAccount)

_66

}

_66

_66

for ownedAccount in managerRef.getOwnedAddresses() {

_66

if seen.contains(ownedAccount) == false {

_66

balances.insert(key: ownedAccount, getAllBalancesInStorage(address))

_66

seen.append(ownedAccount)

_66

}

_66

}

_66

}

_66

_66

return balances

_66

}`

The above script returns a dictionary of balances indexed on the type and further grouped by account Address.

The returned data at the end of address iteration should be sufficient to achieve a unified balance of all Vaults of
similar types across all of a user's associated account as well as a more granular per account view.

You might consider resolving
[`FungibleTokenMetadataViews`](https://github.com/onflow/flow-ft/blob/master/contracts/FungibleTokenMetadataViews.cdc)
to aggregate more information about the underlying Vaults.

### Access NFT in Child Account from Parent Account[​](#access-nft-in-child-account-from-parent-account "Direct link to Access NFT in Child Account from Parent Account")

A user with NFTs in their child accounts will likely want to utilize said NFTs. In this example, the user will sign a
transaction with their authenticated account that retrieves a reference to a child account's
`NonFungibleToken.Provider`, enabling withdrawal from the child account having signed as the parent account.

withdraw\_nft\_from\_child.cdc

`_52

import "NonFungibleToken"

_52

import "FlowToken"

_52

import "HybridCustody"

_52

_52

transaction(

_52

childAddress: Address, // Address of the child account

_52

storagePath: StoragePath, // Path to the Collection in the child account

_52

collectionType: Type, // Type of the requested Collection from which to withdraw

_52

withdrawID: UInt64 // ID of the NFT to withdraw

_52

) {

_52

_52

let providerRef: auth(NonFungibleToken.Withdraw) &{NonFungibleToken.Provider}

_52

_52

prepare(signer: auth(BorrowValue) &Account) {

_52

// Get a reference to the signer's HybridCustody.Manager from storage

_52

let managerRef = signer.storage.borrow<auth(HybridCustody.Manage) &HybridCustody.Manager>(

_52

from: HybridCustody.ManagerStoragePath

_52

) ?? panic("Could not borrow reference to HybridCustody.Manager in signer's account at expected path!")

_52

_52

// Borrow a reference to the signer's specified child account

_52

let account = managerRef

_52

.borrowAccount(addr: childAddress)

_52

?? panic("Signer does not have access to specified child account")

_52

_52

// Get the Capability Controller ID for the requested collection type

_52

let controllerID = account.getControllerIDForType(

_52

type: collectionType,

_52

forPath: storagePath

_52

) ?? panic("Could not find Capability controller ID for collection type ".concat(collectionType.identifier)

_52

.concat(" at path ").concat(storagePath.toString()))

_52

_52

// Get a reference to the child NFT Provider and assign to the transaction scope variable

_52

let cap = account.getCapability(

_52

controllerID: controllerID,

_52

type: Type<auth(NonFungibleToken.Withdraw) &{NonFungibleToken.Provider}>()

_52

) ?? panic("Cannot access NonFungibleToken.Provider from this child account")

_52

_52

// We'll need to cast the Capability - this is possible thanks to CapabilityFactory, though we'll rely on the relevant

_52

// Factory having been configured for this Type or it won't be castable

_52

let providerCap = cap as! Capability<auth(NonFungibleToken.Withdraw) &{NonFungibleToken.Provider}>

_52

self.providerRef = providerCap.borrow() ?? panic("Provider capability is invalid - cannot borrow reference")

_52

}

_52

_52

execute {

_52

// Withdraw the NFT from the Collection

_52

let nft <- self.providerRef.withdraw(withdrawID: withdrawID)

_52

// Do stuff with the NFT

_52

// NOTE: Without storing or burning the NFT before scope closure, this transaction will fail. You'll want to

_52

// fill in the rest of the transaction with the necessary logic to handle the NFT

_52

// ...

_52

}

_52

}`

At the end of this transaction, you withdrew an NFT from the specified account using an NFT `Provider` Capability. A
similar approach could get you any allowable Capabilities from a signer's child account.

### Revoking Secondary Access on a Linked Account[​](#revoking-secondary-access-on-a-linked-account "Direct link to Revoking Secondary Access on a Linked Account")

The expected uses of child accounts for progressive onboarding implies that they will be accounts with shared access. A
user may decide that they no longer want secondary parties to have access to the child account.

There are two ways a party can have delegated access to an account - keys and `&Account` Capability. With
`ChildAccount` mediated access, a user wouldn't be able to revoke anyone's access except for their own. With
unrestricted access via `OwnedAccount`, one could remove parents (`OwnedAccount.removeParent(parent: Address)`) thereby
unlinking relevant Capabilities and further destroying their `ChildAccount` and `CapabilityDelegator` resources.

For now, we recommend that if users want to revoke secondary access, they transfer any assets from the relevant child
account and remove it from their `Manager` altogether.

### Remove a Child Account[​](#remove-a-child-account "Direct link to Remove a Child Account")

As mentioned above, if a user no longer wishes to share access with another party, it's recommended that desired assets
be transferred from that account to either their main account or other linked accounts and the linked account be removed
from their `HybridCustody.Manager`. Let's see how to complete that removal.

remove\_child\_account.cdc

`_10

import "HybridCustody"

_10

_10

transaction(child: Address) {

_10

prepare (acct: auth(BorrowValue) &Account) {

_10

let manager = acct.storage.borrow<auth(HybridCustody.Manage) &HybridCustody.Manager>(

_10

from: HybridCustody.ManagerStoragePath

_10

) ?? panic("manager not found")

_10

manager.removeChild(addr: child)

_10

}

_10

}`

After removal, the signer no longer has delegated access to the removed account via their `Manager` and the caller is
removed as a parent of the removed child.

Note also that it's possible for a child account to remove a parent. This is necessary to give application developers
and ultimately the owners of these child accounts the ability to revoke secondary access on owned accounts.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/guides/account-linking/parent-accounts.md)

Last updated on **Mar 28, 2025** by **Brian Doyle**

[Previous

Building Walletless Applications Using Child Accounts](/build/guides/account-linking/child-accounts)[Next

Account Linking With NBA Top Shot](/build/guides/account-linking-with-dapper)

###### Rate this page

😞😐😊

* [Objectives](#objectives)
* [Design Overview](#design-overview)
  + [Identifying Account Hierarchy](#identifying-account-hierarchy)
  + [Considerations](#considerations)
* [Implementation](#implementation)
* [Examples](#examples)
  + [Query Whether an Address Has Associated Accounts](#query-whether-an-address-has-associated-accounts)
  + [Query All Accounts Associated with Address](#query-all-accounts-associated-with-address)
  + [Query All Owned NFT Metadata](#query-all-owned-nft-metadata)
  + [Query All Account FungibleToken Balances](#query-all-account-fungibletoken-balances)
  + [Access NFT in Child Account from Parent Account](#access-nft-in-child-account-from-parent-account)
  + [Revoking Secondary Access on a Linked Account](#revoking-secondary-access-on-a-linked-account)
  + [Remove a Child Account](#remove-a-child-account)

Documentation

* [Getting Started](/build/getting-started/contract-interaction)
* [SDK's & Tools](/tools)
* [Cadence](https://cadence-lang.org/docs/)
* [Mobile](/build/guides/mobile/overview)
* [FCL](/tools/clients/fcl-js)
* [Testing](/build/smart-contracts/testing)
* [CLI](/tools/flow-cli)
* [Emulator](/tools/emulator)
* [Dev Wallet](https://github.com/onflow/fcl-dev-wallet)
* [VS Code Extension](/tools/vscode-extension)

Community

* [Ecosystem](/ecosystem)
* [Flow Port](https://port.onflow.org/)
* [Developer Grants](https://github.com/onflow/developer-grants)
* [Responsible Disclosure](https://flow.com/flow-responsible-disclosure)
* [Flowverse](https://www.flowverse.co/)
* [Emerald Academy](https://academy.ecdao.org/)
* [FLOATs (Attendance NFTs)](https://floats.city/)

Start Building

* [Flow Playground](https://play.flow.com/)
* [Cadence Tutorials](https://cadence-lang.org/docs/tutorial/first-steps)
* [Cadence Cookbook](https://open-cadence.onflow.org)
* [Core Contracts & Standards](/build/core-contracts)
* [EVM](/evm/about)

Network

* [Network Status](https://status.onflow.org/)
* [Flowscan Mainnet](https://flowdscan.io/)
* [Flowscan Testnet](https://testnet.flowscan.io/)
* [Past Sporks](/networks/node-ops/node-operation/past-sporks)
* [Upcoming Sporks](/networks/node-ops/node-operation/upcoming-sporks)
* [Node Operation](/networks/node-ops)
* [Spork Information](/networks/node-ops/node-operation/spork)

More

* [GitHub](https://github.com/onflow)
* [Discord](https://discord.gg/flow)
* [Forum](https://forum.onflow.org/)
* [OnFlow](https://onflow.org/)
* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.