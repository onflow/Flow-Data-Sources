# Source: https://developers.flow.com/build/guides/account-linking/child-accounts

Building Walletless Applications Using Child Accounts | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

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
* Building Walletless Applications Using Child Accounts

On this page

# Building Walletless Applications Using Child Accounts

In this doc, we'll dive into a progressive onboarding flow, including the Cadence scripts & transactions that go into
its implementation in your app. These components will enable any implementing app to create a custodial account, mediate
the user's onchain actions on their behalf, and later delegate access of that app-created account to the user's wallet.
We'll refer to this custodial pattern as the Hybrid Custody Model and the process of delegating control of the app
account as Account Linking.

## Objectives[​](#objectives "Direct link to Objectives")

* Create a [walletless onboarding](https://flow.com/post/flow-blockchain-mainstream-adoption-easy-onboarding-wallets)
  transaction
* Link an existing app account as a child to a newly authenticated parent account
* Get your app to recognize "parent" accounts along with any associated "child" accounts
* Put it all together to create a blockchain-native onboarding transaction
* View fungible and non-fungible Token metadata relating to assets across all of a user's associated accounts - their
  wallet-mediated "parent" account and any "child" accounts
* Facilitate transactions acting on assets in child accounts

## Point of Clarity[​](#point-of-clarity "Direct link to Point of Clarity")

Before diving in, let's make a distinction between "account linking" and "linking accounts".

### Account Linking[​](#account-linking "Direct link to Account Linking")

info

Note that since account linking is a sensitive action, transactions where an account may be linked are designated by a
topline pragma `#allowAccountLinking`. This lets wallet providers inform users that their account may be linked in the
signed transaction.

Very simply, account linking is a [feature in Cadence](https://github.com/onflow/flips/pull/53) that let's an
[Account](https://cadence-lang.org/docs/language/accounts#authaccount) create a
[Capability](https://cadence-lang.org/docs/language/capabilities) on itself.

Below is an example demonstrating how to issue an `&Account` Capability from a signing account

transaction:

link\_account.cdc

`_10

#allowAccountLinking

_10

_10

transaction(linkPathSuffix: String) {

_10

prepare(signer: auth(IssueAccountCapabilityController) &Account) {

_10

// Issues a fully-entitled Account Capability

_10

let accountCapability = signer.capabilities

_10

.account

_10

.issue<auth(Storage, Contracts, Keys, Inbox, Capabilities) &Account>()

_10

}

_10

}`

From there, the signing account can retrieve the privately linked `&Account` Capability and delegate it to another
account, revoking the Capability if they wish to revoke delegated access.

Note that in order to link an account, a transaction must state the `#allowAccountLinking` pragma in the top line of the
transaction. This is an interim safety measure so that wallet providers can notify users they're about to sign a
transaction that may create a Capability on their `Account`.

### Linking Accounts[​](#linking-accounts "Direct link to Linking Accounts")

Linking accounts leverages this account link, otherwise known as an **`&Account` Capability**, and encapsulates it. The
[components and actions](https://github.com/onflow/flips/pull/72) involved in this process - what the Capability is
encapsulated in, the collection that holds those encapsulations, etc. is what we'll dive into in this doc.

## Terminology[​](#terminology "Direct link to Terminology")

**Parent-Child accounts** - For the moment, we'll call the account created by the app the "child" account and the
account receiving its `&Account` Capability the "parent" account. Existing methods of account access & delegation (i.e.
keys) still imply ownership over the account, but insofar as linked accounts are concerned, the account to which both
the user and the app share access via `&Account` Capability will be considered the "child" account.

**Walletless onboarding** - An onboarding flow whereby an app creates a custodial account for a user, onboarding them to
the app, obviating the need for user wallet authentication.

**Blockchain-native onboarding** - Similar to the already familiar Web3 onboarding flow where a user authenticates with
their existing wallet, an app onboards a user via wallet authentication while additionally creating a custodial app
account and linking it with the authenticated account, resulting in a "hybrid custody" model.

**Hybrid Custody Model** - A custodial pattern in which an app and a user maintain access to an app created account and
user access to that account has been mediated via account linking.

**Account Linking** - Technically speaking, account linking in our context consists of giving some other account an
`&Account` Capability from the granting account. This Capability is maintained in standardized resource called a
`HybridCustody.Manager`, providing its owning user access to any and all of their linked accounts.

**Progressive Onboarding** - An onboarding flow that walks a user up to self-custodial ownership, starting with
walletless onboarding and later linking the app account with the user's authenticated wallet once the user chooses to do
so.

**Restricted Child Account** - An account delegation where the access on the delegating account is restricted according
to rules set by the linking child account. The distinctions between this and the subsequent term ("owned" account) will
be expanding on later.

**Owned Account** - An account delegation where the delegatee has unrestricted access on the delegating child account,
thereby giving the delegatee presiding authority superseding any other "restricted" parent accounts.

## Account Linking[​](#account-linking-1 "Direct link to Account Linking")

Linking an account is the process of delegating account access via `&Account` Capability. Of course, we want to do this
in a way that allows the receiving account to maintain that Capability and allows easy identification of the accounts on
either end of the linkage - the user's main "parent" account and the linked "child" account. This is accomplished in the
`HybridCustody` contract which we'll continue to use in this guidance.

### Prerequisites[​](#prerequisites "Direct link to Prerequisites")

Since account delegation is mediated by developer-defined rules, you should make sure to first configure the resources
that contain those rules. Contracts involved in defining and enforcing this ruleset are
[`CapabilityFilter`](https://github.com/onflow/hybrid-custody/blob/main/contracts/CapabilityFilter.cdc) and
[`CapabilityFactory`](https://github.com/onflow/hybrid-custody/blob/main/contracts/CapabilityFactory.cdc). The former
enumerates those types that are and are not accessible from a child account while the latter enables the access of those
allowable Capabilities such that the returned values can be properly typed - e.g. retrieving a Capability that can be
cast to `Capability<&NonFungibleToken.Collection>` for example.

Here's how you would configure an `AllowlistFilter` and add allowed types to it:

setup\_allow\_all\_filter.cdc

`_31

import "CapabilityFilter"

_31

_31

transaction(identifiers: [String]) {

_31

prepare(acct: auth(BorrowValue, SaveValue, StorageCapabilities, PublishCapability, UnpublishCapability) &Account) {

_31

// Setup the AllowlistFilter

_31

if acct.storage.borrow<&AnyResource>(from: CapabilityFilter.StoragePath) == nil {

_31

acct.storage.save(

_31

<-CapabilityFilter.createFilter(Type<@CapabilityFilter.AllowlistFilter>()),

_31

to: CapabilityFilter.StoragePath)

_31

}

_31

_31

// Ensure the AllowlistFilter is linked to the expected PublicPath

_31

acct.capabilities.unpublish(CapabilityFilter.PublicPath)

_31

acct.capabilities.publish(

_31

acct.capabilities.storage.issue<&{CapabilityFilter.Filter}>(CapabilityFilter.StoragePath),

_31

at: CapabilityFilter.PublicPath

_31

)

_31

_31

// Get a reference to the filter

_31

let filter = acct.storage.borrow<auth(CapabilityFilter.Add) &CapabilityFilter.AllowlistFilter>(

_31

from: CapabilityFilter.StoragePath

_31

) ?? panic("filter does not exist")

_31

_31

// Add the given type identifiers to the AllowlistFilter

_31

// **Note:** the whole transaction fails if any of the given identifiers are malformed

_31

for identifier in identifiers {

_31

let c = CompositeType(identifier)!

_31

filter.addType(c)

_31

}

_31

}

_31

}`

And the following transaction configures a `CapabilityFactory.Manager`, adding NFT-related `Factory` objects:

info

Note that the Manager configured here enables retrieval of castable Capabilities. It's recommended that you implement
Factory resource definitions to support any NFT Collections related with the use of your application so that users can
retrieve Typed Capabilities from accounts linked from your app.

setup\_factory.cdc

`_39

import "NonFungibleToken"

_39

_39

import "CapabilityFactory"

_39

import "NFTCollectionPublicFactory"

_39

import "NFTProviderAndCollectionFactory"

_39

import "NFTProviderFactory"

_39

import "NFTCollectionFactory"

_39

_39

transaction {

_39

prepare(acct: auth(BorrowValue, SaveValue, StorageCapabilities, PublishCapability, UnpublishCapability) &Account) {

_39

// Check for a stored Manager, saving if not found

_39

if acct.storage.borrow<&AnyResource>(from: CapabilityFactory.StoragePath) == nil {

_39

let f <- CapabilityFactory.createFactoryManager()

_39

acct.storage.save(<-f, to: CapabilityFactory.StoragePath)

_39

}

_39

_39

// Check for Capabilities where expected, linking if not found

_39

acct.capabilities.unpublish(CapabilityFactory.PublicPath)

_39

acct.capabilities.publish(

_39

acct.capabilities.storage.issue<&CapabilityFactory.Manager>(CapabilityFactory.StoragePath),

_39

at: CapabilityFactory.PublicPath

_39

)

_39

_39

assert(

_39

acct.capabilities.get<&CapabilityFactory.Manager>(CapabilityFactory.PublicPath).check(),

_39

message: "CapabilityFactory is not setup properly"

_39

)

_39

_39

let manager = acct.storage.borrow<auth(CapabilityFactory.Add) &CapabilityFactory.Manager>(from: CapabilityFactory.StoragePath)

_39

?? panic("manager not found")

_39

_39

/// Add generic NFT-related Factory implementations to enable castable Capabilities from this Manager

_39

manager.updateFactory(Type<&{NonFungibleToken.CollectionPublic}>(), NFTCollectionPublicFactory.Factory())

_39

manager.updateFactory(Type<auth(NonFungibleToken.Withdraw) &{NonFungibleToken.Provider, NonFungibleToken.CollectionPublic}>(), NFTProviderAndCollectionFactory.Factory())

_39

manager.updateFactory(Type<auth(NonFungibleToken.Withdraw) &{NonFungibleToken.Provider}>(), NFTProviderFactory.Factory())

_39

manager.updateFactory(Type<auth(NonFungibleToken.Withdraw) &{NonFungibleToken.Collection}>(), NFTCollectionFactory.WithdrawFactory())

_39

manager.updateFactory(Type<&{NonFungibleToken.Collection}>(), NFTCollectionFactory.Factory())

_39

}

_39

}`

![resources/hybrid_custody_high_level](/assets/images/hybrid_custody_high_level-0fdf5d00b8b4545c3c587ba78a817fd9.png)

*In this scenario, a user custodies a key for their main account which maintains access to a wrapped `Account`
Capability, providing the user restricted access on the app account. The app maintains custodial access to the account
and regulates the access restrictions to delegatee "parent" accounts.*

Linking accounts can be done in one of two ways. Put simply, the child account needs to get the parent an `Account`
Capability, and the parent needs to save that Capability so they can retain access. This delegation must be done manner
that represents each side of the link while safeguarding the integrity of any access restrictions an application puts in
place on delegated access.

We can achieve issuance from the child account and claim from the parent account pattern by either:

1. Leveraging [Cadence's `Account.Inbox`](https://cadence-lang.org/docs/language/accounts#account-inbox) to publish the
   Capability from the child account & have the parent claim the Capability in a subsequent transaction.
2. Executing a multi-party signed transaction, signed by both the child and parent accounts.

Let's take a look at both.

info

You'll want to consider whether you would like the parent account to be configured with some app-specific resources or
Capabilities and compose you multisig or claim transactions to include such configurations.

For example, if your app deals with specific NFTs, you may want to configure the parent account with Collections for
those NFTs so the user can easily transfer them between their linked accounts.

### Publish & Claim[​](#publish--claim "Direct link to Publish & Claim")

#### Publish[​](#publish "Direct link to Publish")

Here, the account delegating access to itself links its `&Account` Capability, and publishes it to be claimed by the
designated parent account.

publish\_to\_parent.cdc

`_32

import "HybridCustody"

_32

import "CapabilityFactory"

_32

import "CapabilityFilter"

_32

import "CapabilityDelegator"

_32

_32

transaction(parent: Address, factoryAddress: Address, filterAddress: Address) {

_32

prepare(acct: auth(BorrowValue) &Account) {

_32

// NOTE: The resources and Capabilities needed for this transaction are assumed to have be pre-configured

_32

_32

// Borrow the OwnedAccount resource

_32

let owned = acct.storage.borrow<auth(HybridCustody.Owner) &HybridCustody.OwnedAccount>(

_32

from: HybridCustody.OwnedAccountStoragePath

_32

) ?? panic("owned account not found")

_32

_32

// Get a CapabilityFactory.Manager Capability

_32

let factory = getAccount(factoryAddress).capabilities

_32

.get<&CapabilityFactory.Manager>(

_32

CapabilityFactory.PublicPath

_32

)

_32

assert(factory.check(), message: "factory address is not configured properly")

_32

_32

// Get a CapabilityFilter.Filter Capability

_32

let filter = getAccount(filterAddress).capabilities

_32

.get<&{CapabilityFilter.Filter}>(

_32

CapabilityFilter.PublicPath

_32

)

_32

assert(filter.check(), message: "capability filter is not configured properly")

_32

_32

// Publish the OwnedAccount to the designated parent account

_32

owned.publishToParent(parentAddress: parent, factory: factory, filter: filter)

_32

}

_32

}`

#### Claim[​](#claim "Direct link to Claim")

On the other side, the receiving account claims the published `ChildAccount` Capability, adding it to the signer's
`HybridCustody.Manager.childAccounts` indexed on the child account's Address.

redeem\_account.cdc

`_53

import "MetadataViews"

_53

import "ViewResolver"

_53

_53

import "HybridCustody"

_53

import "CapabilityFilter"

_53

_53

transaction(childAddress: Address, filterAddress: Address?, filterPath: PublicPath?) {

_53

prepare(acct: auth(Storage, Capabilities, Inbox) &Account) {

_53

// Get a Manager filter if a path is provided

_53

var filter: Capability<&{CapabilityFilter.Filter}>? = nil

_53

if filterAddress != nil && filterPath != nil {

_53

filter = getAccount(filterAddress!).capabilities

_53

.get<&{CapabilityFilter.Filter}>(

_53

filterPath!

_53

)

_53

}

_53

_53

// Configure a Manager if not already configured

_53

if acct.storage.borrow<&HybridCustody.Manager>(from: HybridCustody.ManagerStoragePath) == nil {

_53

let m <- HybridCustody.createManager(filter: filter)

_53

acct.storage.save(<- m, to: HybridCustody.ManagerStoragePath)

_53

_53

for c in acct.capabilities.storage.getControllers(forPath: HybridCustody.ManagerStoragePath) {

_53

c.delete()

_53

}

_53

_53

acct.capabilities.unpublish(HybridCustody.ManagerPublicPath)

_53

_53

acct.capabilities.publish(

_53

acct.capabilities.storage.issue<&{HybridCustody.ManagerPublic}>(

_53

HybridCustody.ManagerStoragePath

_53

),

_53

at: HybridCustody.ManagerPublicPath

_53

)

_53

_53

acct.capabilities

_53

.storage

_53

.issue<auth(HybridCustody.Manage) &{HybridCustody.ManagerPrivate, HybridCustody.ManagerPublic}>(

_53

HybridCustody.ManagerStoragePath

_53

)

_53

}

_53

_53

// Claim the published ChildAccount Capability

_53

let inboxName = HybridCustody.getChildAccountIdentifier(acct.address)

_53

let cap = acct.inbox.claim<auth(HybridCustody.Child) &{HybridCustody.AccountPrivate, HybridCustody.AccountPublic, ViewResolver.Resolver}>(inboxName, provider: childAddress)

_53

?? panic("child account cap not found")

_53

_53

// Get a reference to the Manager and add the account & add the child account

_53

let manager = acct.storage.borrow<auth(HybridCustody.Manage) &HybridCustody.Manager>(from: HybridCustody.ManagerStoragePath)

_53

?? panic("manager no found")

_53

manager.addAccount(cap: cap)

_53

}

_53

}`

### Multi-Signed Transaction[​](#multi-signed-transaction "Direct link to Multi-Signed Transaction")

We can combine the two transactions in [Publish](#publish) and [Claim](#claim) into a single multi-signed transaction to
achieve Hybrid Custody in a single step.

info

Note that while the following code links both accounts in a single transaction, in practicality you may find it easier
to execute publish and claim transactions separately depending on your custodial infrastructure.

setup\_multi\_sig.cdc

`_92

#allowAccountLinking

_92

_92

import "HybridCustody"

_92

_92

import "CapabilityFactory"

_92

import "CapabilityDelegator"

_92

import "CapabilityFilter"

_92

_92

import "MetadataViews"

_92

import "ViewResolver"

_92

_92

transaction(parentFilterAddress: Address?, childAccountFactoryAddress: Address, childAccountFilterAddress: Address) {

_92

prepare(childAcct: auth(Storage, Capabilities) &Account, parentAcct: auth(Storage, Capabilities, Inbox) &Account) {

_92

// --------------------- Begin setup of child account ---------------------

_92

var optCap: Capability<auth(Storage, Contracts, Keys, Inbox, Capabilities) &Account>? = nil

_92

let t = Type<auth(Storage, Contracts, Keys, Inbox, Capabilities) &Account>()

_92

for c in childAcct.capabilities.account.getControllers() {

_92

if c.borrowType.isSubtype(of: t) {

_92

optCap = c.capability as! Capability<auth(Storage, Contracts, Keys, Inbox, Capabilities) &Account>

_92

break

_92

}

_92

}

_92

_92

if optCap == nil {

_92

optCap = childAcct.capabilities.account.issue<auth(Storage, Contracts, Keys, Inbox, Capabilities) &Account>()

_92

}

_92

let acctCap = optCap ?? panic("failed to get account capability")

_92

_92

if childAcct.storage.borrow<&HybridCustody.OwnedAccount>(from: HybridCustody.OwnedAccountStoragePath) == nil {

_92

let ownedAccount <- HybridCustody.createOwnedAccount(acct: acctCap)

_92

childAcct.storage.save(<-ownedAccount, to: HybridCustody.OwnedAccountStoragePath)

_92

}

_92

_92

for c in childAcct.capabilities.storage.getControllers(forPath: HybridCustody.OwnedAccountStoragePath) {

_92

c.delete()

_92

}

_92

_92

// configure capabilities

_92

childAcct.capabilities.storage.issue<&{HybridCustody.BorrowableAccount, HybridCustody.OwnedAccountPublic, ViewResolver.Resolver}>(HybridCustody.OwnedAccountStoragePath)

_92

childAcct.capabilities.publish(

_92

childAcct.capabilities.storage.issue<&{HybridCustody.OwnedAccountPublic, ViewResolver.Resolver}>(HybridCustody.OwnedAccountStoragePath),

_92

at: HybridCustody.OwnedAccountPublicPath

_92

)

_92

_92

// --------------------- End setup of child account ---------------------

_92

_92

// --------------------- Begin setup of parent account ---------------------

_92

var filter: Capability<&{CapabilityFilter.Filter}>? = nil

_92

if parentFilterAddress != nil {

_92

filter = getAccount(parentFilterAddress!).capabilities.get<&{CapabilityFilter.Filter}>(CapabilityFilter.PublicPath)

_92

}

_92

_92

if parentAcct.storage.borrow<&HybridCustody.Manager>(from: HybridCustody.ManagerStoragePath) == nil {

_92

let m <- HybridCustody.createManager(filter: filter)

_92

parentAcct.storage.save(<- m, to: HybridCustody.ManagerStoragePath)

_92

}

_92

_92

for c in parentAcct.capabilities.storage.getControllers(forPath: HybridCustody.ManagerStoragePath) {

_92

c.delete()

_92

}

_92

_92

parentAcct.capabilities.publish(

_92

parentAcct.capabilities.storage.issue<&{HybridCustody.ManagerPublic}>(HybridCustody.ManagerStoragePath),

_92

at: HybridCustody.ManagerPublicPath

_92

)

_92

parentAcct.capabilities.storage.issue<auth(HybridCustody.Manage) &{HybridCustody.ManagerPrivate, HybridCustody.ManagerPublic}>(HybridCustody.ManagerStoragePath)

_92

_92

// --------------------- End setup of parent account ---------------------

_92

_92

// Publish account to parent

_92

let owned = childAcct.storage.borrow<auth(HybridCustody.Owner) &HybridCustody.OwnedAccount>(from: HybridCustody.OwnedAccountStoragePath)

_92

?? panic("owned account not found")

_92

_92

let factory = getAccount(childAccountFactoryAddress).capabilities.get<&CapabilityFactory.Manager>(CapabilityFactory.PublicPath)

_92

assert(factory.check(), message: "factory address is not configured properly")

_92

_92

let filterForChild = getAccount(childAccountFilterAddress).capabilities.get<&{CapabilityFilter.Filter}>(CapabilityFilter.PublicPath)

_92

assert(filterForChild.check(), message: "capability filter is not configured properly")

_92

_92

owned.publishToParent(parentAddress: parentAcct.address, factory: factory, filter: filterForChild)

_92

_92

// claim the account on the parent

_92

let inboxName = HybridCustody.getChildAccountIdentifier(parentAcct.address)

_92

let cap = parentAcct.inbox.claim<auth(HybridCustody.Child) &{HybridCustody.AccountPrivate, HybridCustody.AccountPublic, ViewResolver.Resolver}>(inboxName, provider: childAcct.address)

_92

?? panic("child account cap not found")

_92

_92

let manager = parentAcct.storage.borrow<auth(HybridCustody.Manage) &HybridCustody.Manager>(from: HybridCustody.ManagerStoragePath)

_92

?? panic("manager no found")

_92

_92

manager.addAccount(cap: cap)

_92

}

_92

}`

## Onboarding Flows[​](#onboarding-flows "Direct link to Onboarding Flows")

Given the ability to establish an account and later delegate access to a user, apps are freed from the constraints of
dichotomous custodial & self-custodial paradigms. A developer can choose to onboard a user via traditional Web2 identity
and later delegate access to the user's wallet account. Alternatively, an app can enable wallet authentication at the
outset, creating an app-specific account & linking with the user's wallet account. As specified above, these two flows
are known as "walletless" and "blockchain-native" onboarding respectively. Developers can choose to implement one for
simplicity or both for maximum flexibility.

### Walletless Onboarding[​](#walletless-onboarding "Direct link to Walletless Onboarding")

The following transaction creates an account, funding creation via the signer and adding the provided public key. You'll
notice this transaction is pretty much your standard account creation. The magic for you will be how you custody the key
for this account (locally, KMS, wallet service, etc.) in a manner that allows your app to mediate onchain interactions
on behalf of your user.

walletless\_onboarding

`_51

import "FungibleToken"

_51

import "FlowToken"

_51

_51

transaction(pubKey: String, initialFundingAmt: UFix64) {

_51

_51

prepare(signer: auth(BorrowValue) &Account) {

_51

_51

/* --- Account Creation --- */

_51

// **NOTE:** your app may choose to separate creation depending on your custodial model)

_51

//

_51

// Create the child account, funding via the signer

_51

let newAccount = Account(payer: signer)

_51

// Create a public key for the new account from string value in the provided arg

_51

// **NOTE:** You may want to specify a different signature algo for your use case

_51

let key = PublicKey(

_51

publicKey: pubKey.decodeHex(),

_51

signatureAlgorithm: SignatureAlgorithm.ECDSA_P256

_51

)

_51

// Add the key to the new account

_51

// **NOTE:** You may want to specify a different hash algo & weight best for your use case

_51

newAccount.keys.add(

_51

publicKey: key,

_51

hashAlgorithm: HashAlgorithm.SHA3_256,

_51

weight: 1000.0

_51

)

_51

_51

/* --- (Optional) Additional Account Funding --- */

_51

//

_51

// Fund the new account if specified

_51

if initialFundingAmt > 0.0 {

_51

// Get a vault to fund the new account

_51

let fundingProvider = signer.storage.borrow<auth(FungibleToken.Withdraw) &FlowToken.Vault>(

_51

from: /storage/flowTokenVault

_51

)!

_51

// Fund the new account with the initialFundingAmount specified

_51

let receiver = newAccount.capabilities.get<&FlowToken.Vault>(

_51

/public/flowTokenReceiver

_51

).borrow()!

_51

let fundingVault <-fundingProvider.withdraw(

_51

amount: initialFundingAmt

_51

)

_51

receiver.deposit(from: <-fundingVault)

_51

}

_51

_51

/* --- Continue with use case specific setup --- */

_51

//

_51

// At this point, the newAccount can further be configured as suitable for

_51

// use in your app (e.g. Setup a Collection, Mint NFT, Configure Vault, etc.)

_51

// ...

_51

}

_51

}`

### Blockchain-Native Onboarding[​](#blockchain-native-onboarding "Direct link to Blockchain-Native Onboarding")

This onboarding flow is really a single-transaction composition of the steps covered above. This is a testament to the
power of the complex transactions you can compose on Flow with Cadence!

info

Recall the [prerequisites](#prerequisites) needed to be satisfied before linking an account:

1. CapabilityFilter Filter saved and linked
2. CapabilityFactory Manager saved and linked as well as Factory implementations supporting the Capability Types you'll
   want accessible from linked child accounts as Typed Capabilities.

#### Account Creation & Linking[​](#account-creation--linking "Direct link to Account Creation & Linking")

Compared to walletless onboarding where a user does not have a Flow account, blockchain-native onboarding assumes a user
already has a wallet configured and immediately links it with a newly created app account. This enables the app to sign
transactions on the user's behalf via the new child account while immediately delegating control of that account to the
onboarding user's main account.

After this transaction, both the custodial party (presumably the client/app) and the signing parent account will have
access to the newly created account - the custodial party via key access and the parent account via their
`HybridCustody.Manager` maintaining the new account's `ChildAccount` Capability.

blockchain\_native\_onboarding.cdc

`_123

#allowAccountLinking

_123

_123

import "FungibleToken"

_123

import "FlowToken"

_123

import "MetadataViews"

_123

import "ViewResolver"

_123

_123

import "HybridCustody"

_123

import "CapabilityFactory"

_123

import "CapabilityFilter"

_123

import "CapabilityDelegator"

_123

_123

transaction(

_123

pubKey: String,

_123

initialFundingAmt: UFix64,

_123

factoryAddress: Address,

_123

filterAddress: Address

_123

) {

_123

_123

prepare(parent: auth(Storage, Capabilities, Inbox) &Account, app: auth(Storage, Capabilities) &Account) {

_123

/* --- Account Creation --- */

_123

//

_123

// Create the child account, funding via the signing app account

_123

let newAccount = Account(payer: app)

_123

// Create a public key for the child account from string value in the provided arg

_123

// **NOTE:** You may want to specify a different signature algo for your use case

_123

let key = PublicKey(

_123

publicKey: pubKey.decodeHex(),

_123

signatureAlgorithm: SignatureAlgorithm.ECDSA_P256

_123

)

_123

// Add the key to the new account

_123

// **NOTE:** You may want to specify a different hash algo & weight best for your use case

_123

newAccount.keys.add(

_123

publicKey: key,

_123

hashAlgorithm: HashAlgorithm.SHA3_256,

_123

weight: 1000.0

_123

)

_123

_123

/* --- (Optional) Additional Account Funding --- */

_123

//

_123

// Fund the new account if specified

_123

if initialFundingAmt > 0.0 {

_123

// Get a vault to fund the new account

_123

let fundingProvider = app.storage.borrow<auth(FungibleToken.Withdraw) &{FungibleToken.Provider}>(from: /storage/flowTokenVault)!

_123

// Fund the new account with the initialFundingAmount specified

_123

newAccount.capabilities.get<&{FungibleToken.Receiver}>(/public/flowTokenReceiver)!

_123

.borrow()!

_123

.deposit(

_123

from: <-fundingProvider.withdraw(

_123

amount: initialFundingAmt

_123

)

_123

)

_123

}

_123

_123

/* Continue with use case specific setup */

_123

//

_123

// At this point, the newAccount can further be configured as suitable for

_123

// use in your dapp (e.g. Setup a Collection, Mint NFT, Configure Vault, etc.)

_123

// ...

_123

_123

/* --- Link the AuthAccount Capability --- */

_123

//

_123

let acctCap = newAccount.capabilities.account.issue<auth(Storage, Contracts, Keys, Inbox, Capabilities) &Account>()

_123

_123

// Create a OwnedAccount & link Capabilities

_123

let ownedAccount <- HybridCustody.createOwnedAccount(acct: acctCap)

_123

newAccount.storage.save(<-ownedAccount, to: HybridCustody.OwnedAccountStoragePath)

_123

_123

newAccount.capabilities.storage.issue<&{HybridCustody.BorrowableAccount, HybridCustody.OwnedAccountPublic, ViewResolver.Resolver}>(HybridCustody.OwnedAccountStoragePath)

_123

newAccount.capabilities.publish(

_123

newAccount.capabilities.storage.issue<&{HybridCustody.OwnedAccountPublic, ViewResolver.Resolver}>(HybridCustody.OwnedAccountStoragePath),

_123

at: HybridCustody.OwnedAccountPublicPath

_123

)

_123

_123

// Get a reference to the OwnedAccount resource

_123

let owned = newAccount.storage.borrow<auth(HybridCustody.Owner) &HybridCustody.OwnedAccount>(from: HybridCustody.OwnedAccountStoragePath)!

_123

_123

// Get the CapabilityFactory.Manager Capability

_123

let factory = getAccount(factoryAddress).capabilities.get<&CapabilityFactory.Manager>(CapabilityFactory.PublicPath)

_123

assert(factory.check(), message: "factory address is not configured properly")

_123

_123

// Get the CapabilityFilter.Filter Capability

_123

let filter = getAccount(filterAddress).capabilities.get<&{CapabilityFilter.Filter}>(CapabilityFilter.PublicPath)

_123

assert(filter.check(), message: "capability filter is not configured properly")

_123

_123

// Configure access for the delegatee parent account

_123

owned.publishToParent(parentAddress: parent.address, factory: factory, filter: filter)

_123

_123

/* --- Add delegation to parent account --- */

_123

//

_123

// Configure HybridCustody.Manager if needed

_123

if parent.storage.borrow<&AnyResource>(from: HybridCustody.ManagerStoragePath) == nil {

_123

let m <- HybridCustody.createManager(filter: filter)

_123

parent.storage.save(<- m, to: HybridCustody.ManagerStoragePath)

_123

_123

for c in parent.capabilities.storage.getControllers(forPath: HybridCustody.ManagerStoragePath) {

_123

c.delete()

_123

}

_123

_123

// configure Capabilities

_123

parent.capabilities.storage.issue<&{HybridCustody.ManagerPrivate, HybridCustody.ManagerPublic}>(HybridCustody.ManagerStoragePath)

_123

parent.capabilities.publish(

_123

parent.capabilities.storage.issue<&{HybridCustody.ManagerPublic}>(HybridCustody.ManagerStoragePath),

_123

at: HybridCustody.ManagerPublicPath

_123

)

_123

}

_123

_123

_123

// Claim the ChildAccount Capability

_123

let inboxName = HybridCustody.getChildAccountIdentifier(parent.address)

_123

let cap = parent

_123

.inbox

_123

.claim<auth(HybridCustody.Child) &{HybridCustody.AccountPrivate, HybridCustody.AccountPublic, ViewResolver.Resolver}>(

_123

inboxName,

_123

provider: newAccount.address

_123

) ?? panic("child account cap not found")

_123

_123

// Get a reference to the Manager and add the account

_123

let managerRef = parent.storage.borrow<auth(HybridCustody.Manage) &HybridCustody.Manager>(from: HybridCustody.ManagerStoragePath)

_123

?? panic("manager not found")

_123

managerRef.addAccount(cap: cap)

_123

}

_123

}`

## Funding & Custody Patterns[​](#funding--custody-patterns "Direct link to Funding & Custody Patterns")

Aside from implementing onboarding flows & account linking, you'll want to also consider the account funding & custodial
pattern appropriate for the app you're building. The only pattern compatible with walletless onboarding (and therefore
the only one showcased above) is one in which the app custodies the child account's key and funds account creation.

In general, the funding pattern for account creation will determine to some extent the backend infrastructure needed to
support your app and the onboarding flow your app can support. For example, if you want to to create a service-less
client (a totally local app without backend infrastructure), you could forego walletless onboarding in favor of a
user-funded blockchain-native onboarding to achieve a hybrid custody model. Your app maintains the keys to the app
account locally to sign on behalf of the user, and the user funds the creation of the the account, linking to their main
account on account creation. This would be a **user-funded, app custodied** pattern.

Again, custody may deserve some regulatory insight depending on your jurisdiction. If building for production, you'll
likely want to consider these non-technical implications in your technical decision-making. Such is the nature of
building in crypto.

Here are the patterns you might consider:

### App-Funded, App-Custodied[​](#app-funded-app-custodied "Direct link to App-Funded, App-Custodied")

If you want to implement walletless onboarding, you can stop here as this is the only compatible pattern. In this
scenario, a backend app account funds the creation of a new account and the app custodies the key for said account
either on the user's device or some backend KMS.

### App-Funded, User-Custodied[​](#app-funded-user-custodied "Direct link to App-Funded, User-Custodied")

In this case, the backend app account funds account creation, but adds a key to the account which the user custodies. In
order for the app to act on the user's behalf, it has to be delegated access via `&Account` Capability which the backend
app account would maintain in a `HybridCustody.Manager`. This means that the new account would have two parent accounts

* the user's and the app.

While this pattern provides the user maximum ownership and authority over the child account, it may present unique
considerations and edge cases for you as a builder depending on your app's access to the child account. Also note that
this and the following patterns are incompatible with walletless onboarding in that the user must have a wallet
pre-configured before onboarding.

### User-Funded, App-Custodied[​](#user-funded-app-custodied "Direct link to User-Funded, App-Custodied")

As mentioned above, this pattern unlocks totally service-less architectures - just a local client & smart contracts. An
authenticated user signs a transaction creating an account, adding the key provided by the client, and linking the
account as a child account. At the end of the transaction, hybrid custody is achieved and the app can sign with the
custodied key on the user's behalf using the newly created account.

### User-Funded, User-Custodied[​](#user-funded-user-custodied "Direct link to User-Funded, User-Custodied")

While perhaps not useful for most apps, this pattern may be desirable for advanced users who wish to create a shared
access account themselves. The user funds account creation, adding keys they custody, and delegates secondary access to
some other account.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/guides/account-linking/child-accounts.md)

Last updated on **Feb 24, 2025** by **j pimmel**

[Previous

Account Linking (FLIP 72)](/build/guides/account-linking)[Next

Working With Parent Accounts](/build/guides/account-linking/parent-accounts)

###### Rate this page

😞😐😊

* [Objectives](#objectives)
* [Point of Clarity](#point-of-clarity)
  + [Account Linking](#account-linking)
  + [Linking Accounts](#linking-accounts)
* [Terminology](#terminology)
* [Account Linking](#account-linking-1)
  + [Prerequisites](#prerequisites)
  + [Publish & Claim](#publish--claim)
  + [Multi-Signed Transaction](#multi-signed-transaction)
* [Onboarding Flows](#onboarding-flows)
  + [Walletless Onboarding](#walletless-onboarding)
  + [Blockchain-Native Onboarding](#blockchain-native-onboarding)
* [Funding & Custody Patterns](#funding--custody-patterns)
  + [App-Funded, App-Custodied](#app-funded-app-custodied)
  + [App-Funded, User-Custodied](#app-funded-user-custodied)
  + [User-Funded, App-Custodied](#user-funded-app-custodied)
  + [User-Funded, User-Custodied](#user-funded-user-custodied)

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