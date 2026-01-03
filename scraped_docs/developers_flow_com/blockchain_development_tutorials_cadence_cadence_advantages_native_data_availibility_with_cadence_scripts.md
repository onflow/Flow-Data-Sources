# Source: https://developers.flow.com/blockchain-development-tutorials/cadence/cadence-advantages/native-data-availibility-with-cadence-scripts

Native Data Availability With Cadence Scripts | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[DeFi](/defi)[Tutorials](/blockchain-development-tutorials)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Blockchain Development Tutorials](/blockchain-development-tutorials)* [Flow Blockchain 101](/blockchain-development-tutorials/flow-101)* [Forte Network Upgrade](/blockchain-development-tutorials/forte)

      * [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)

        * [Cadence Tutorials](/blockchain-development-tutorials/cadence)

          + [Getting Started with Cadence](/blockchain-development-tutorials/cadence/getting-started)

            + [Cadence Advantages](/blockchain-development-tutorials/cadence/cadence-advantages)

              - [Compose with Cadence Transactions](/blockchain-development-tutorials/cadence/cadence-advantages/compose-with-cadence-transactions)- [Native Data Availability With Cadence Scripts](/blockchain-development-tutorials/cadence/cadence-advantages/native-data-availibility-with-cadence-scripts)- [Upgrading Cadence Contracts](/blockchain-development-tutorials/cadence/cadence-advantages/upgrading-cadence-contracts)+ [Account Linking](/blockchain-development-tutorials/cadence/account-management)

                + [Mobile Development on Flow](/blockchain-development-tutorials/cadence/mobile)

                  + [Fork Testing](/blockchain-development-tutorials/cadence/fork-testing)+ [Emulator Fork Testing](/blockchain-development-tutorials/cadence/emulator-fork-testing)* [Flow EVM Guides](/blockchain-development-tutorials/evm)

            * [Cross-VM Apps](/blockchain-development-tutorials/cross-vm-apps)

              * [Native VRF (Built-in Randomness) Tutorials](/blockchain-development-tutorials/native-vrf)

                * [Token Development and Registration](/blockchain-development-tutorials/tokens)

                  * [Gasless Transactions](/blockchain-development-tutorials/gasless-transactions)

                    * [Third-Party Integrations](/blockchain-development-tutorials/integrations)

* * [Cadence Tutorials](/blockchain-development-tutorials/cadence)* [Cadence Advantages](/blockchain-development-tutorials/cadence/cadence-advantages)* Native Data Availability With Cadence Scripts

On this page

# Native Data Availability With Cadence Scripts

In Solidity, you can only retrieve data from **view** functions that the contract author anticipated and included in the original contract. If the exact query you want isn't exposed, teams typically rely on a *data availability service* such as The Graph, Covalent, Alchemy Enhanced APIs, Reservoir, or NFTScan to compute and serve that view.

In Cadence, **scripts** are general-purpose read programs. They can traverse public account storage, read public capabilities, and compose types from multiple contracts to answer new questions without the need to modify those contracts. You are not limited to the pre-written surface area of a single contract's views.

info

In Cadence, a *script* is a read-only program that can access public data across accounts and contracts in a strongly typed way. It does not require a user signatures not does it incur any fees.

## Objectives[​](#objectives "Direct link to Objectives")

After you complete this guide, you will be able to:

* Explain why Cadence **scripts** are more powerful than Solidity **view** functions.
* Use the [Flow CLI Commands](/build/tools/flow-cli/commands) to execute a Cadence script against mainnet.
* Analyze an account for [NBA Top Shot](https://nbatopshot.com/) NFTs held by the account or its child accounts.
* Build the script incrementally to:
  + Query a parent account for child accounts via [*Hybrid Custody*](/blockchain-development-tutorials/cadence/account-management).
  + Inspect each child account's storage paths.
  + Detect NFT collections the parent can control.
  + List only NBA Top Shot NFTs with display metadata.
  + Update the script to also list NFL All Day NFT metadata.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

* Basic familiarity with [Cadence](https://cadence-lang.org/docs/tutorial/first-steps) and [Flow accounts](/build/cadence/basics/accounts).
* Flow command line interface (CLI) installed and authenticated for mainnet (see [Flow CLI Commands](/build/tools/flow-cli/commands)).
* The target parent account uses *Hybrid Custody* and controls at least one child account that holds NBA Top Shot NFTs.
  + If you don't have an account that owns NBA Top Shots, you can use `0xfeb88a0fcc175a3d` for this tutorial.

tip

If you are new to [*Hybrid Custody*](/blockchain-development-tutorials/cadence/account-management), the high-level idea is that in Cadence, a parent account can manage one or more child accounts through managed capabilities. This guide uses those capabilities to enumerate NFT collections the parent can control.

## Get started[​](#get-started "Direct link to Get started")

Create a new Flow project and generate a script file:

`_10

# Create a new Flow project

_10

flow init cadence-scripts-tutorial

_10

_10

# Navigate to the project directory

_10

cd cadence-scripts-tutorial

_10

_10

# Generate a new script file

_10

flow generate script TopShotQuery`

This creates a proper Flow project structure with `flow.json` configuration and generates a script template at `cadence/scripts/TopShotQuery.cdc`.

We will **revise one script file** in four passes, and run it after each step. This mirrors how you would build and verify a script from scratch.

---

## Query the account to find child accounts[​](#query-the-account-to-find-child-accounts "Direct link to Query the account to find child accounts")

To start, write a script that borrows the parent's *Hybrid Custody* manager and returns the child addresses it controls. This verifies that imports resolve and that the parent account is configured as expected.

First, you'll need to install the `HybridCustody` contract from mainnet.

info

In Cadence, you can import a file from a path as you'd expect. You can also **import an already deployed contract** into your project.

Use the [dependency manager](/build/tools/flow-cli/dependency-manager) to install the contract with:

`_10

flow dependencies install mainnet://0xd8a7e05a7ac670c0.HybridCustody`

This will install the contract and its own dependencies. You don't need to deploy these contracts again, so pick `none` for the account to deploy. You also don't need an alias.

warning

The language server treats dependency installations in this way similar to package installations in other platforms. You'll need to close and reopen the file or type something to trigger a refresh.

Open `scripts/TopShotQuery.cdc` Replace the file contents with:

`_13

import "HybridCustody"

_13

_13

// Return the child account addresses managed by the given parent.

_13

access(all) fun main(addr: Address): [Address] {

_13

let parent = getAuthAccount<auth(Storage) &Account>(addr)

_13

_13

let manager =

_13

parent.storage.borrow<auth(HybridCustody.Manage) &HybridCustody.Manager>(

_13

from: HybridCustody.ManagerStoragePath

_13

) ?? panic("manager does not exist")

_13

_13

return manager.getChildAddresses()

_13

}`

Run it:

`_10

flow scripts execute cadence/scripts/TopShotQuery.cdc --network mainnet 0xfeb88a0fcc175a3d`

You will see a list of child addresses. If you do not, confirm the parent actually stores a manager at `HybridCustody.ManagerStoragePath`.

`_10

Result: [0xa16b948ba2c9a858]`

---

## Listing the storage paths found in each child account[​](#listing-the-storage-paths-found-in-each-child-account "Direct link to Listing the storage paths found in each child account")

Next, for each child, enumerate storage paths. This helps us understand what each account stores before we try to detect NFTs.

info

In Cadence, data is stored in a users account in [storage paths](https://cadence-lang.org/docs/tutorial/resources#storage-paths).

Update the query to iterate through the child addresses in the `manager` and collect their storage paths and return those paths:

`_24

import "HybridCustody"

_24

_24

// Map child address -> array of storage path strings (e.g. "storage/SomePath").

_24

access(all) fun main(addr: Address): {Address: [String]} {

_24

let parent = getAuthAccount<auth(Storage) &Account>(addr)

_24

_24

let manager =

_24

parent.storage.borrow<auth(HybridCustody.Manage) &HybridCustody.Manager>(

_24

from: HybridCustody.ManagerStoragePath

_24

) ?? panic("manager does not exist")

_24

_24

var pathsByChild: {Address: [String]} = {}

_24

_24

for child in manager.getChildAddresses() {

_24

let acct = getAuthAccount<auth(Storage) &Account>(child)

_24

var paths: [String] = []

_24

for sp in acct.storage.storagePaths {

_24

paths.append(sp.toString())

_24

}

_24

pathsByChild[child] = paths

_24

}

_24

_24

return pathsByChild

_24

}`

Run it again:

`_10

flow scripts execute cadence/scripts/TopShotQuery.cdc --network mainnet 0xfeb88a0fcc175a3d`

You'll see a map from each child address to its storage paths. This tells us where to look for potential collections.

`_10

Result: {0xa16b948ba2c9a858: ["/storage/flowTokenVault", "/storage/PinnacleNFTCollectionProviderForNFTStorefront", "/storage/BackpackCollection", "/storage/PackNFTCollection", "/storage/HybridCustodyChild_0xd8a7e05a7ac670c0", "/storage/ChildAccount_0xfeb88a0fcc175a3d", "/storage/privateForwardingStorage", "/storage/PinnacleCollection", "/storage/AllDayNFTCollection", "/storage/NFTStorefrontV2", "/storage/PinnaclePackNFTCollection", "/storage/ChildAccount_0x0f566b3217c33c4a", "/storage/dapperUtilityCoinReceiver", "/storage/CapFilterParent0xfeb88a0fcc175a3d", "/storage/ChildCapabilityDelegator_0x0f566b3217c33c4a", "/storage/CapFilterParent0x0f566b3217c33c4a", "/storage/flowUtilityTokenReceiver", "/storage/MomentCollection", "/storage/ChildCapabilityDelegator_0xfeb88a0fcc175a3d", "/storage/NFTStorefrontV20x3cdbb3d569211ff3"]}`

---

## Detecting NFT collections the parent can control[​](#detecting-nft-collections-the-parent-can-control "Direct link to Detecting NFT collections the parent can control")

Now you can identify which stored items are NFT collections that the **parent** can act on. In Cadence, a [*capability*](https://cadence-lang.org/docs/language/capabilities) exposes specific interfaces on a stored value. We look for a capability whose type includes [`{NonFungibleToken.Provider}`](https://github.com/onflow/flow-nft/blob/21c5e18a0985528b53931dc14c55332b3b47939e/contracts/NonFungibleToken.cdc#L154) and confirm the parent has access via *Hybrid Custody*.

Update the script to iterate through storage paths found in child accounts to search for providers of the `NonFungibleToken.Provider` type:

`_51

import "HybridCustody"

_51

import "NonFungibleToken"

_51

_51

// Map child address -> array of type identifiers for NFT collections

_51

// that the parent can control (i.e. has a Provider capability for).

_51

access(all) fun main(addr: Address): {Address: [String]} {

_51

let parent = getAuthAccount<auth(Storage) &Account>(addr)

_51

_51

let manager =

_51

parent.storage.borrow<auth(HybridCustody.Manage) &HybridCustody.Manager>(

_51

from: HybridCustody.ManagerStoragePath

_51

) ?? panic("manager does not exist")

_51

_51

let providerType = Type<auth(NonFungibleToken.Withdraw) &{NonFungibleToken.Provider}>()

_51

var controllableTypes: {Address: [String]} = {}

_51

_51

for child in manager.getChildAddresses() {

_51

let acct = getAuthAccount<auth(Storage, Capabilities) &Account>(child)

_51

let childAcct = manager.borrowAccount(addr: child) ?? panic("child account not found")

_51

var found: [String] = []

_51

_51

// For each storage path, inspect its controllers (capability controllers).

_51

for sp in acct.storage.storagePaths {

_51

for ctrl in acct.capabilities.storage.getControllers(forPath: sp) {

_51

// If the controller's borrow type does not include Provider, skip.

_51

if !ctrl.borrowType.isSubtype(of: providerType) {

_51

continue

_51

}

_51

_51

// Verify the parent has an accessible capability through Hybrid Custody.

_51

if let cap: Capability = childAcct.getCapability(

_51

controllerID: ctrl.capabilityID,

_51

type: providerType

_51

) {

_51

let providerCap = cap as! Capability<&{NonFungibleToken.Provider}>

_51

if providerCap.check() {

_51

// Record the concrete type identifier behind this capability.

_51

let typeId = cap.borrow<&AnyResource>()!.getType().identifier

_51

found.append(typeId)

_51

// One confirmation per path is sufficient.

_51

break

_51

}

_51

}

_51

}

_51

}

_51

_51

controllableTypes[child] = found

_51

}

_51

_51

return controllableTypes

_51

}`

Run it:

`_10

flow scripts execute cadence/scripts/TopShotQuery.cdc --network mainnet 0xfeb88a0fcc175a3d`

You will now see type identifiers such as `A.<address>.<Contract>.<Type>` for collections the parent can control. We will use these identifiers to filter for Top Shot.

`_10

Result: {0xa16b948ba2c9a858: ["A.807c3d470888cc48.Backpack.Collection", "A.e4cf4bdc1751c65d.AllDay.Collection", "A.0b2a3299cc857e29.TopShot.Collection"]}`

---

## Filter NFT collection to find and return Top Shots[​](#filter-nft-collection-to-find-and-return-top-shots "Direct link to Filter NFT collection to find and return Top Shots")

Finally, for each detected collection, [borrow](https://cadence-lang.org/docs/language/capabilities#borrowing-public-capabilities-with-borrow) the collection `{NonFungibleToken.CollectionPublic}`, iterate IDs, resolve `MetadataViews.Display`, and return only Top Shot items. We add a small `isTopShot` predicate that you can customize to your deployment.

info

The [borrow](https://cadence-lang.org/docs/language/capabilities#borrowing-public-capabilities-with-borrow) function is how you use a published [*capability*](https://cadence-lang.org/docs/language/capabilities) in your code. In this case, you borrow the **public** functionality of Cadence NFTs, which includes [`MetadataViews`] that return a view of the **fully-onchain metadata** for the NFT.

Update the query to borrow a reference to each public collection and return metadata for those that are NBA Top Shots:

`_87

import "HybridCustody"

_87

import "NonFungibleToken"

_87

import "MetadataViews"

_87

_87

// Map child address -> { tokenId : MetadataViews.Display } for Top Shot NFTs only.

_87

access(all) fun main(addr: Address): {Address: {UInt64: MetadataViews.Display}} {

_87

let parent = getAuthAccount<auth(Storage) &Account>(addr)

_87

_87

let manager =

_87

parent.storage.borrow<auth(HybridCustody.Manage) &HybridCustody.Manager>(

_87

from: HybridCustody.ManagerStoragePath

_87

) ?? panic("manager does not exist")

_87

_87

let providerType = Type<auth(NonFungibleToken.Withdraw) &{NonFungibleToken.Provider}>()

_87

let collectionIface: Type = Type<@{NonFungibleToken.CollectionPublic}>()

_87

_87

// Customize this to match other collections found in the previous step!

_87

fun isTopShot(_ typeId: String): Bool {

_87

// Common pattern: typeId.contains("TopShot")

_87

return typeId.contains("TopShot")

_87

}

_87

_87

var result: {Address: {UInt64: MetadataViews.Display}} = {}

_87

_87

for child in manager.getChildAddresses() {

_87

let acct = getAuthAccount<auth(Storage, Capabilities) &Account>(child)

_87

let childAcct = manager.borrowAccount(addr: child) ?? panic("child account not found")

_87

_87

// First, collect controllable type identifiers for this child.

_87

var typesWithProvider: [String] = []

_87

_87

for sp in acct.storage.storagePaths {

_87

for ctrl in acct.capabilities.storage.getControllers(forPath: sp) {

_87

if !ctrl.borrowType.isSubtype(of: providerType) {

_87

continue

_87

}

_87

if let cap: Capability = childAcct.getCapability(

_87

controllerID: ctrl.capabilityID,

_87

type: providerType

_87

) {

_87

let providerCap = cap as! Capability<&{NonFungibleToken.Provider}>

_87

if providerCap.check() {

_87

let typeId = cap.borrow<&AnyResource>()!.getType().identifier

_87

typesWithProvider.append(typeId)

_87

break

_87

}

_87

}

_87

}

_87

}

_87

_87

var displays: {UInt64: MetadataViews.Display} = {}

_87

_87

// Walk storage again to borrow the matching collections and read their items.

_87

acct.storage.forEachStored(fun (path: StoragePath, t: Type): Bool {

_87

// Only consider types we know are controllable and that match Top Shot.

_87

var match = false

_87

for tid in typesWithProvider {

_87

if tid == t.identifier && isTopShot(tid) {

_87

match = true

_87

break

_87

}

_87

}

_87

if !match {

_87

return true

_87

}

_87

_87

// Skip the concrete resource type token; we want the collection interface.

_87

if t.isInstance(collectionIface) {

_87

return true

_87

}

_87

_87

if let col = acct.storage.borrow<&{NonFungibleToken.CollectionPublic}>(from: path) {

_87

for id in col.getIDs() {

_87

let nft = col.borrowNFT(id)!

_87

if let display = nft.resolveView(Type<MetadataViews.Display>())! as? MetadataViews.Display {

_87

displays[id] = display

_87

}

_87

}

_87

}

_87

return true

_87

})

_87

_87

result[child] = displays

_87

}

_87

_87

return result

_87

}`

Run it:

`_10

flow scripts execute cadence/scripts/TopShotQuery.cdc --network mainnet 0xfeb88a0fcc175a3d`

The output is a Cadence representation of:

`_10

{ Address: { UInt64: MetadataViews.Display } }`

which maps each child account address to a map of NFT IDs to their display metadata (name, description, thumbnail).

`_10

Result: {0xa16b948ba2c9a858: {44311697: A.1d7e57aa55817448.MetadataViews.Display(name: "Immanuel Quickley 3 Pointer", description: "", thumbnail: A.1d7e57aa55817448.MetadataViews.HTTPFile(url: "https://assets.nbatopshot.com/media/44311697?width=256")), 44274843: A.1d7e57aa55817448.MetadataViews.Display(name: "Rudy Gobert Rim", description: "", thumbnail: A.1d7e57aa55817448.MetadataViews.HTTPFile(url: "https://assets.nbatopshot.com/media/44274843?width=256")), 44219960: A.1d7e57aa55817448.MetadataViews.Display(name: "Sasha Vezenkov 3 Pointer", description: "", thumbnail: A.1d7e57aa55817448.MetadataViews.HTTPFile(url: "https://assets.nbatopshot.com/media/44219960?width=256")), 44300175: A.1d7e57aa55817448.MetadataViews.Display(name: "Malik Monk Assist", description: "", thumbnail: A.1d7e57aa55817448.MetadataViews.HTTPFile(url: "https://assets.nbatopshot.com/media/44300175?width=256")), 43995280: A.1d7e57aa55817448.MetadataViews.Display(name: "Kelly Olynyk 3 Pointer", description: "Regardless of the stakes, regardless of the stage, Kelly Olynyk is calm and collected beyond the arc. Trailing in the fourth quarter of a tight contest, the Utah Jazz big gets to his spot in the corner and buries a triple to claw within one. After a defensive stop on the next possession Olynyk doubles down on the momentum and drains a transition three to give his team the lead. Olynyk finished with 15 points on 5 of 6 shooting in the October 27, 2023 matchup and the Jazz held on for the W at the hands of the LA Clippers.", thumbnail: A.1d7e57aa55817448.MetadataViews.HTTPFile(url: "https://assets.nbatopshot.com/media/43995280?width=256"))}}`

---

## Extend the script to include AllDay NFTs[​](#extend-the-script-to-include-allday-nfts "Direct link to Extend the script to include AllDay NFTs")

Now that you have a working script for Top Shot NFTs, let's extend it to also return NFL All Day NFTs. This demonstrates the flexibility of Cadence scripts - you can easily modify them to answer new questions without the need to change any contracts.

Update the `isTopShot` function to also include AllDay NFTs:

`_10

// Customize this to match other collections found in the previous step!

_10

fun isTopShot(_ typeId: String): Bool {

_10

// Include both TopShot and AllDay NFTs

_10

return typeId.contains("TopShot") || typeId.contains("AllDay")

_10

}`

Run the updated script:

`_10

flow scripts execute cadence/scripts/TopShotQuery.cdc --network mainnet 0xfeb88a0fcc175a3d`

You will see both Top Shot and AllDay NFTs in the results (truncated for space):

`_10

Result: {0xa16b948ba2c9a858: {44311697: A.1d7e57aa55817448.MetadataViews.Display(name: "Immanuel Quickley 3 Pointer", description: "", thumbnail: A.1d7e57aa55817448.MetadataViews.HTTPFile(url: "https://assets.nbatopshot.com/media/44311697?width=256")), 8220605: A.1d7e57aa55817448.MetadataViews.Display(name: "Zach Ertz Reception", description: "Normally used to overwhelming his NFC East foes in a different, midnight-green attire, Zach Ertz, in his most productive yardage-based game since 2022, showed in Week 2 that productivity remains well within reach. Challenged to a \u{201c}who wants it more\u{201d}-type battle during a corner route, Ertz adjusted to a floated ball, using both a 6-foot-5 frame and pure strength to rip away a potential interception, turning it into a 21-yard catch for himself. The 12-year veteran helped the Washington Commanders \u{2014} whose seven field goals offset the New York Giants\u{2019} three touchdowns \u{2014} survive for a unique 21-18 win, with Ertz providing four catches (on four targets) and 62 yards on Sept. 15, 2024.", thumbnail: A.1d7e57aa55817448.MetadataViews.HTTPFile(url: "https://media.nflallday.com/editions/3304/media/image?format=jpeg&width=256"))}}`

This demonstrates how you can easily modify Cadence scripts to answer different questions about the same data, unlike Solidity, where you'd need to deploy new contracts or rely on external indexers.

---

## Troubleshoot[​](#troubleshoot "Direct link to Troubleshoot")

* If you see `manager does not exist`, confirm the parent address actually stores a `HybridCustody.Manager` at `HybridCustody.ManagerStoragePath`.
* If you see empty arrays in Step 3, the parent may not have *provider* access to any collections in those child accounts.
* If you see empty results in Step 4, confirm `isTopShot` matches the identifiers you observed in Step 3.
* If you are not using *Hybrid Custody*, you can adapt Steps 2-4 to use `getAccount(child)` and scan **publicly exposed** `{NonFungibleToken.CollectionPublic}` capabilities, but you will not be able to assert provider access.

## How this compares to Solidity[​](#how-this-compares-to-solidity "Direct link to How this compares to Solidity")

* **Solidity views are fixed**: You can only retrieve what the contract author exposed via `view` or `pure` functions. If you need a different aggregation or cross-contract traversal, you typically rely on a *data availability service* or write a new contract to expose that view.
* **Cadence scripts are flexible**: You compose types across modules, traverse account storage, and read public capabilities at query time. You do not need to redeploy contracts to answer new questions.

Common *data availability service* examples used in EVM ecosystems:

* The Graph (subgraphs)
* Covalent (unified API)
* Alchemy Enhanced APIs
* Reservoir (NFT market APIs)
* NFTScan (NFT inventory APIs)

## Conclusion[​](#conclusion "Direct link to Conclusion")

In this tutorial, you learned how to use Cadence scripts to query onchain data directly from Flow's state, without the need to rely on external indexers or APIs. You built a script that can discover and query NFT collections across multiple child accounts with Hybrid Custody, and then extended it to include both NBA Top Shot and NFL All Day NFTs, which demonstrates the power and flexibility of Cadence's native data availability.

Now that you have completed the tutorial, you should be able to:

* Query onchain data directly with Cadence scripts without external dependencies
* Use Hybrid Custody to access child account data from parent accounts
* Filter and process NFT collections to extract specific metadata
* Modify scripts to answer different questions about the same onchain data
* Compare Cadence's native data availability with Solidity's limitations
* Build applications that can access any onchain data in real-time

This approach gives you the freedom to build applications that can access any onchain data in real-time, which makes Flow's native data availability a powerful tool for developers who build on Flow.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/cadence/cadence-advantages/native-data-availibility-with-cadence-scripts.md)

Last updated on **Dec 2, 2025** by **Brian Doyle**

[Previous

Compose with Cadence Transactions](/blockchain-development-tutorials/cadence/cadence-advantages/compose-with-cadence-transactions)[Next

Upgrading Cadence Contracts](/blockchain-development-tutorials/cadence/cadence-advantages/upgrading-cadence-contracts)

###### Rate this page

😞😐😊

Copy as Markdown

* [Objectives](#objectives)* [Prerequisites](#prerequisites)* [Get started](#get-started)* [Query the account to find child accounts](#query-the-account-to-find-child-accounts)* [Listing the storage paths found in each child account](#listing-the-storage-paths-found-in-each-child-account)* [Detecting NFT collections the parent can control](#detecting-nft-collections-the-parent-can-control)* [Filter NFT collection to find and return Top Shots](#filter-nft-collection-to-find-and-return-top-shots)* [Extend the script to include AllDay NFTs](#extend-the-script-to-include-allday-nfts)* [Troubleshoot](#troubleshoot)* [How this compares to Solidity](#how-this-compares-to-solidity)* [Conclusion](#conclusion)

Flow

* [Build with AI](/blockchain-development-tutorials/use-AI-to-build-on-flow)* [Why Flow](/blockchain-development-tutorials/flow-101)* [Tools](/build/tools)* [Faucet](/ecosystem/faucets)* [Builder Toolkit](/ecosystem/developer-support-hub)

Cadence

* [Quickstart](/blockchain-development-tutorials/cadence/getting-started)* [Build with Forte](/blockchain-development-tutorials/forte)* [Cadence Advantages](/blockchain-development-tutorials/cadence/cadence-advantages)* [React SDK](/build/tools/react-sdk)* [Language Reference](https://cadence-lang.org/)

Solidity (EVM)

* [Quickstart](/build/evm/quickstart)* [Native VRF](/blockchain-development-tutorials/native-vrf)* [Batched Transactions](/blockchain-development-tutorials/cross-vm-apps)* [Network Information](/build/evm/networks)

Community & Support

* [Dev Office Hours](https://calendar.google.com/calendar/u/0/embed?src=c_47978f5cd9da636cadc6b8473102b5092c1a865dd010558393ecb7f9fd0c9ad0@group.calendar.google.com)* [Hackathons and Events](/ecosystem/hackathons-and-events)* [Discord](https://discord.gg/flow)* [GitHub](https://github.com/onflow)* [Careers](https://flow.com/careers)

Network & Resources

* [Network Status](https://status.flow.com/)* [Block Explorer](https://flowscan.io/)* [Flow Port](https://port.flow.com/)* [Flow Website](https://flow.com/)* [Flow Blog](https://flow.com/blog)

Copyright © 2026 Flow Foundation. All Rights Reserved.