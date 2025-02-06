# Source: https://developers.flow.com/build/guides/nft




Creating an NFT Contract | Flow Developer Portal





[Skip to main content](#__docusaurus_skipToContent_fallback)[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build With Cadence](/build/flow)[Build With EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)Connect[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)Search

* [Why Flow](/build/flow)
* [Differences vs. EVM](/build/differences-vs-evm)
* [Getting Started](/build/getting-started/contract-interaction)
* [Flow Protocol](/build/basics/blocks)
* [App Architecture](/build/app-architecture)
* [Writing and Deploying Smart Contracts](/build/learn-cadence)
* [Advanced Concepts](/build/advanced-concepts/account-abstraction)
* [Guides](/build/guides/account-linking)
  + [Account Linking (FLIP 72)](/build/guides/account-linking)
  + [Account Linking With NBA Top Shot](/build/guides/account-linking-with-dapper)
  + [More Guides](/build/guides/more-guides)
  + [Creating an NFT Contract](/build/guides/nft)
  + [Creating a Fungible Token](/build/guides/fungible-token)
  + [Building on Mobile](/build/guides/mobile/overview)
* [Core Smart Contracts](/build/core-contracts)
* [Explore More](/build/explore-more)


* Guides
* Creating an NFT Contract
On this page
# Creating an NFT Contract


info

This guide is an in-depth tutorial on launching NFT contracts from scratch.
To launch in 2 minutes using a tool check out [Touchstone](https://www.touchstone.city/)

## What are NFTs[​](#what-are-nfts "Direct link to What are NFTs")

NFTs, or Non-Fungible Tokens, represent a unique digital asset verified
using blockchain technology. Unlike cryptocurrencies such as Bitcoin,
which are fungible and can be exchanged on a one-for-one basis,
NFTs are distinct and cannot be exchanged on a like-for-like basis.
This uniqueness and indivisibility make them ideal for representing
rare and valuable items like art, collectibles, tickets and even real estate.
Their blockchain-backed nature ensures the authenticity and ownership of these digital assets.

## Setting Up a Project[​](#setting-up-a-project "Direct link to Setting Up a Project")

To start creating an NFT on the Flow blockchain, you'll first need some tools and configurations in place.

### Installing Flow CLI[​](#installing-flow-cli "Direct link to Installing Flow CLI")

The **Flow CLI** (Command Line Interface) provides a suite of tools
that allow developers to interact seamlessly with the Flow blockchain.

If you haven't installed the Flow CLI yet and have [Homebrew](https://brew.sh/) installed,
you can run `brew install flow-cli`. If you don't have Homebrew,
please follow [the installation guide here](/tools/flow-cli/install).

### Initializing a New Project[​](#initializing-a-new-project "Direct link to Initializing a New Project")

> 💡 Note: Here is [a link to the completed code](https://github.com/chasefleming/foobar-nft) if you want to skip ahead or reference as you follow along.

Once you have the Flow CLI installed, you can set up a new project using the `flow init` command. This command initializes the necessary directory structure and a `flow.json` configuration file (a way to configure your project for contract sources, deployments, accounts, and more):

 `_10flow init foobar-nft`
> Note: Select "No" when it asks you to install core contracts for the purposes of this tutorial.

Upon execution, the command will generate the following directory structure:

 `_10/cadence_10 /contracts_10 /scripts_10 /transactions_10 /tests_10flow.json`

Now, navigate into the project directory:

 `_10cd foobar-nft`

To begin, let's create a contract file named `FooBar` for the `FooBar` token,
which will be the focus of this tutorial. To do this, we can use the boilerplate `generate` command from the Flow CLI:

 `_10flow generate contract FooBar`

This will create a new file at `cadence/contracts/FooBar.cdc` with the following contents:

 `_10access(all) contract FooBar {_10 init() {}_10}`

Now, add these contracts to your `flow.json`.
These are important contracts that your contract will import that
are pre-deployed to the emulator.

 `_17"contracts": {_17 "NonFungibleToken": {_17 "aliases": {_17 "emulator": "f8d6e0586b0a20c7"_17 }_17 },_17 "ViewResolver": {_17 "aliases": {_17 "emulator": "0xf8d6e0586b0a20c7"_17 }_17 },_17 "MetadataViews": {_17 "aliases": {_17 "emulator": "0xf8d6e0586b0a20c7"_17 }_17 }_17}`
## Setting Up Our NFT on the Contract[​](#setting-up-our-nft-on-the-contract "Direct link to Setting Up Our NFT on the Contract")

### Understanding Resources[​](#understanding-resources "Direct link to Understanding Resources")

On the Flow blockchain, "[Resources](https://cadence-lang.org/docs/tutorial/resources-compose)"
are a key feature of the Cadence programming language.
They represent unique, non-duplicable assets, ensuring that they can only exist
in one place at a time. This concept is crucial for representing NFTs on Flow,
as it guarantees their uniqueness.

To begin, let's define a basic `NFT` resource.
This resource requires an `init` method, which is invoked when the resource is instantiated:

 `_10access(all) contract FooBar {_10_10 access(all) resource NFT {_10 init() {}_10 }_10_10 init() {}_10}`

Every resource in Cadence has a unique identifier assigned to it.
We can use it to set an ID for our NFT. Here's how you can do that:

 `_12access(all) contract FooBar {_12_12 access(all) resource NFT {_12 access(all) let id: UInt64_12_12 init() {_12 self.id = self.uuid_12 }_12 }_12_12 init() {}_12}`

To control the creation of NFTs, it's essential to have a mechanism
that restricts their minting. This ensures that not just anyone can create an NFT and inflate its supply.
To achieve this, you can introduce an `NFTMinter` resource that contains a `createNFT` function:

 `_14access(all) contract FooBar {_14_14 // ...[previous code]..._14_14 access(all) resource NFTMinter {_14 access(all) fun createNFT(): @NFT {_14 return <-create NFT()_14 }_14_14 init() {}_14 }_14_14 init() {}_14}`

In this example, the `NFTMinter` resource will be stored on the contract account's storage.
This means that only the contract account will have the ability to mint new NFTs.
To set this up, add the following line to the contract's `init` function:

 `_10access(all) contract FooBar {_10_10 // ...[previous code]..._10_10 init() {_10 self.account.storage.save(<- create NFTMinter(), to: /storage/fooBarNFTMinter)_10 }_10}`
### Setting Up an NFT Collection[​](#setting-up-an-nft-collection "Direct link to Setting Up an NFT Collection")

Storing individual NFTs directly in an account's storage can cause issues,
especially if you want to store multiple NFTs.
Instead, it's required to create a collection that can hold multiple NFTs.
This collection can then be stored in the account's storage.

Start by creating a new resource named `Collection`.
This resource will act as a container for your NFTs, storing them in a dictionary indexed by their IDs.

 `_16access(all) contract FooBar {_16_16 // ...[NFT resource code]..._16_16 access(all) resource Collection {_16_16 access(all) var ownedNFTs: @{UInt64: NFT}_16_16 init() {_16 self.ownedNFTs <- {}_16 }_16_16 }_16_16 // ...[NFTMinter code]..._16}`
## Fitting the Flow NFT Standard[​](#fitting-the-flow-nft-standard "Direct link to Fitting the Flow NFT Standard")

To ensure compatibility and interoperability within the Flow ecosystem,
it's crucial that your NFT contract adheres to the [Flow NFT standard](https://github.com/onflow/flow-nft).
This standard defines the events, functions, resources, metadata and other elements that a contract should have.
By following this standard, your NFTs will be compatible with various marketplaces, apps, and other services within the Flow ecosystem.

### Applying the Standard[​](#applying-the-standard "Direct link to Applying the Standard")

To start, you need to inform the Flow blockchain that your contract will implement the `NonFungibleToken` standard.
Since it's a standard, there's no need for deployment.
It's already available on the Emulator, Testnet, and Mainnet for the community's benefit.

Begin by importing the token standard into your contract
and adding the correct interface conformances to FooBar, NFT, and Collection:

 `_36import "NonFungibleToken"_36_36access(all) contract FooBar: NonFungibleToken {_36_36 /// Standard Paths_36 access(all) let CollectionStoragePath: StoragePath_36 access(all) let CollectionPublicPath: PublicPath_36_36 /// Path where the minter should be stored_36 /// The standard paths for the collection are stored in the collection resource type_36 access(all) let MinterStoragePath: StoragePath_36_36 // ...contract code_36_36 access(all) resource NFT: NonFungibleToken.NFT {_36 // ...NFT code_36 }_36_36 access(all) resource Collection: NonFungibleToken.Collection {_36_36 // Make sure to update this field!_36 access(all) var ownedNFTs: @{UInt64: {NonFungibleToken.NFT}}_36_36 // ...Collection Code_36 }_36_36 // ...rest of the contract code_36_36 init() {_36 // Set the named paths_36 self.CollectionStoragePath = /storage/fooBarNFTCollection_36 self.CollectionPublicPath = /public/fooBarNFTCollection_36 self.MinterStoragePath = /storage/fooBarNFTMinter_36 self.account.storage.save(<- create NFTMinter(), to: self.MinterStoragePath)_36 }_36}`

As you can see, we also added standard paths for the Collection and Minter

These interface conformances for [NFT](https://github.com/onflow/flow-nft/blob/master/contracts/NonFungibleToken.cdc#L98)
and [Collection](https://github.com/onflow/flow-nft/blob/master/contracts/NonFungibleToken.cdc#L190)
inherit from other interfaces that provide important functionality and restrictions
for your NFT and Collection types.

To allow accounts to create their own collections, add a function
in the main contract that creates a new `Collection` and returns it.
This function takes a `nftType: Type` argument that allows the caller
to specify which type of `Collection` they want to create.
Contracts that implement multiple `NFT` and/or `Collection` types can use this argument,
but since your contract is only implementing one `NFT` and `Collection` type,
it can ignore the argument.
You'll also want to add a simpler one directly
to the `NFT` and `Collection` definitions
so users can directly create a collection from an existing collection:

 `_35access(all) contract FooBar: NonFungibleToken {_35_35 // ...other FooBar contract code_35_35 access(all) resource NFT: NonFungibleToken.NFT {_35 // ...NFT code_35_35 access(all) fun createEmptyCollection(): @{NonFungibleToken.Collection} {_35 return <-FooBar.createEmptyCollection(nftType: Type<@FooBar.NFT>())_35 }_35 }_35_35_35 access(all) resource Collection: NonFungibleToken.Collection {_35_35 // ...other Collection code_35_35 /// createEmptyCollection creates an empty Collection of the same type_35 /// and returns it to the caller_35 /// @return A an empty collection of the same type_35 access(all) fun createEmptyCollection(): @{NonFungibleToken.Collection} {_35 return <-FooBar.createEmptyCollection(nftType: Type<@FooBar.NFT>())_35 }_35 }_35_35 // ...other FooBar contract code_35_35 /// createEmptyCollection creates an empty Collection for the specified NFT type_35 /// and returns it to the caller so that they can own NFTs_35 access(all) fun createEmptyCollection(nftType: Type): @{NonFungibleToken.Collection} {_35 return <- create Collection()_35 }_35_35 // ...FooBar minter and init code_35}`

To manage the NFTs within a collection, you'll need functions to deposit and withdraw NFTs. Here's how you can add a `deposit` function:

 `_18access(all) resource Collection: NonFungibleToken.Collection {_18_18 access(all) var ownedNFTs: @{UInt64: {NonFungibleToken.NFT}}_18_18 /// deposit takes a NFT and adds it to the collections dictionary_18 /// and adds the ID to the id array_18 access(all) fun deposit(token: @{NonFungibleToken.NFT}) {_18 let token <- token as! @FooBar.NFT_18 let id = token.id_18_18 // add the new token to the dictionary which removes the old one_18 let oldToken <- self.ownedNFTs[token.id] <- token_18_18 destroy oldToken_18 }_18_18 // ...[following code]..._18}`

Similarly, you can add a `withdraw` function to remove an NFT from the collection:

 `_15access(all) resource Collection: NonFungibleToken.Collection {_15 // ...[deposit code]..._15_15 /// withdraw removes an NFT from the collection and moves it to the caller_15 access(NonFungibleToken.Withdraw) fun withdraw(withdrawID: UInt64): @{NonFungibleToken.NFT} {_15 let token <- self.ownedNFTs.remove(key: withdrawID)_15 ?? panic("FooBar.Collection.withdraw: Could not withdraw an NFT with ID "_15 .concat(withdrawID.toString())_15 .concat(". Check the submitted ID to make sure it is one that this collection owns."))_15_15 return <-token_15 }_15_15 // ...[createEmptyCollection code]..._15}`

As you can see, this function has an `access(NonFungibleToken.Withdraw)` access modifier.
This is an example of entitlements in Cadence.
[Entitlements](https://cadence-lang.org/docs/language/access-control#entitlements)
are a way for developers to restrict access to privileged fields and functions
in a composite type like a resource when a reference is created for it.
In this example, the `withdraw()` function is always accessible to code that
controls the full `Collection` object, but if a reference is created for it,
the `withdraw()` function can only be called if the reference
is authorized by the owner with `NonFungibleToken.Withdraw`,
which is [a standard entitlement](https://github.com/onflow/flow-nft/blob/master/contracts/NonFungibleToken.cdc#L58)
defined by the `NonFungibleToken` contract:

 `_10// Example of an authorized entitled reference to a NonFungibleToken.Collection_10<auth(NonFungibleToken.Withdraw) &{NonFungibleToken.Collection}>`

Entitlements are important to understand because they are what protects
privileged functionality in your resource objects from being accessed by third-parties.
It is recommended to read the [entitlements documentation](https://cadence-lang.org/docs/language/access-control#entitlements)
to understand how to use the feature properly.

[References](https://cadence-lang.org/docs/language/references) can be freely up-casted and down-casted in Cadence, so it is important
for privileged functionality to be protected by an entitlement so that it can
only be accessed if it is authorized.

### Standard NFT Events[​](#standard-nft-events "Direct link to Standard NFT Events")

Many projects rely on events the signal when withdrawals or deposits happen.
Luckily, the `NonFungibleToken` standard handles the definition and emission
of events for projects, so there is no need for you to add any events
to your implementation for withdraw and deposit.

Here are the `FungibleToken` event definitions:

 `_15 /// Event that is emitted when a token is withdrawn,_15 /// indicating the type, id, uuid, the owner of the collection that it was withdrawn from,_15 /// and the UUID of the resource it was withdrawn from, usually a collection._15 ///_15 /// If the collection is not in an account's storage, `from` will be `nil`._15 ///_15 access(all) event Withdrawn(type: String, id: UInt64, uuid: UInt64, from: Address?, providerUUID: UInt64)_15_15 /// Event that emitted when a token is deposited to a collection._15 /// Indicates the type, id, uuid, the owner of the collection that it was deposited to,_15 /// and the UUID of the collection it was deposited to_15 ///_15 /// If the collection is not in an account's storage, `from`, will be `nil`._15 ///_15 access(all) event Deposited(type: String, id: UInt64, uuid: UInt64, to: Address?, collectionUUID: UInt64)`

These events are [emitted by the `Collection` interface](https://github.com/onflow/flow-nft/blob/master/contracts/NonFungibleToken.cdc#L202)
in the `NonFungibleToken` contract whenever the relevant function is called on any implementation.

There is also a [standard `NonFungibleToken.Updated` event](https://github.com/onflow/flow-nft/blob/master/contracts/NonFungibleToken.cdc#L63-L77)
that your contract can emit if the NFT is updated in any way.
This is optional though, so no need to include support for it in your implementation.

To facilitate querying, you'll also want a function to retrieve
important information from the collection, like what types it supports
and all the NFT IDs within a collection:

 `_23access(all) resource Collection: NonFungibleToken.Collection {_23 // ...[withdraw code]..._23_23 /// getIDs returns an array of the IDs that are in the collection_23 access(all) view fun getIDs(): [UInt64] {_23 return self.ownedNFTs.keys_23 }_23_23 /// getSupportedNFTTypes returns a list of NFT types that this receiver accepts_23 access(all) view fun getSupportedNFTTypes(): {Type: Bool} {_23 let supportedTypes: {Type: Bool} = {}_23 supportedTypes[Type<@FooBar.NFT>()] = true_23 return supportedTypes_23 }_23_23 /// Returns whether or not the given type is accepted by the collection_23 /// A collection that can accept any type should just return true by default_23 access(all) view fun isSupportedNFTType(type: Type): Bool {_23 return type == Type<@FooBar.NFT>()_23 }_23_23 // ...[createEmptyCollection code]..._23}`
### Supporting NFT Metadata[​](#supporting-nft-metadata "Direct link to Supporting NFT Metadata")

The Non-Fungible Token standard also enforces that implementations
provide functionality to return a set of standard views about the tokens
via the [ViewResolver](https://github.com/onflow/flow-nft/blob/master/contracts/ViewResolver.cdc)
and [MetadataViews](https://github.com/onflow/flow-nft/blob/master/contracts/MetadataViews.cdc) definitions.
(You will need to add these imports to your contract)
These provide developers with standard ways of representing metadata
about a given token such as token symbols, images, royalties, editions,
website links, and standard account paths and types that third-parties can access in a standard way.
You can see the [metadata views documentation](/build/advanced-concepts/metadata-views)
for a more thorough guide using a NFT contract as an example.

For now, you can add this code to your contract to support the important metadata:

 `_110// Add this import!_110import "MetadataViews"_110_110access(all) contract FooBar: NonFungibleToken {_110_110 // ...other FooBar contract code_110_110 access(all) resource NFT: NonFungibleToken.NFT {_110_110 // ...other NFT code_110_110 /// Gets a list of views specific to the individual NFT_110 access(all) view fun getViews(): [Type] {_110 return [_110 Type<MetadataViews.Display>(),_110 Type<MetadataViews.Editions>(),_110 Type<MetadataViews.NFTCollectionData>(),_110 Type<MetadataViews.NFTCollectionDisplay>(),_110 Type<MetadataViews.Serial>()_110 ]_110 }_110_110 /// Resolves a view for this specific NFT_110 access(all) fun resolveView(_ view: Type): AnyStruct? {_110 switch view {_110 case Type<MetadataViews.Display>():_110 return MetadataViews.Display(_110 name: "FooBar Example Token",_110 description: "An Example NFT Contract from the Flow NFT Guide",_110 thumbnail: MetadataViews.HTTPFile(_110 url: "Fill this in with a URL to a thumbnail of the NFT"_110 )_110 )_110 case Type<MetadataViews.Editions>():_110 // There is no max number of NFTs that can be minted from this contract_110 // so the max edition field value is set to nil_110 let editionInfo = MetadataViews.Edition(name: "FooBar Edition", number: self.id, max: nil)_110 let editionList: [MetadataViews.Edition] = [editionInfo]_110 return MetadataViews.Editions(_110 editionList_110 )_110 case Type<MetadataViews.Serial>():_110 return MetadataViews.Serial(_110 self.id_110 )_110 case Type<MetadataViews.NFTCollectionData>():_110 return FooBar.resolveContractView(resourceType: Type<@FooBar.NFT>(), viewType: Type<MetadataViews.NFTCollectionData>())_110 case Type<MetadataViews.NFTCollectionDisplay>():_110 return FooBar.resolveContractView(resourceType: Type<@FooBar.NFT>(), viewType: Type<MetadataViews.NFTCollectionDisplay>())_110 }_110 return nil_110 }_110 }_110_110 access(all) resource Collection: NonFungibleToken.Vault {_110_110 // ...[getIDs code]..._110_110 /// Allows a caller to borrow a reference to a specific NFT_110 /// so that they can get the metadata views for the specific NFT_110 access(all) view fun borrowNFT(_ id: UInt64): &{NonFungibleToken.NFT}? {_110 return &self.ownedNFTs[id]_110 }_110_110 // ...[rest of code]..._110 }_110_110 /// Gets a list of views for all the NFTs defined by this contract_110 access(all) view fun getContractViews(resourceType: Type?): [Type] {_110 return [_110 Type<MetadataViews.NFTCollectionData>(),_110 Type<MetadataViews.NFTCollectionDisplay>()_110 ]_110 }_110_110 /// Resolves a view that applies to all the NFTs defined by this contract_110 access(all) fun resolveContractView(resourceType: Type?, viewType: Type): AnyStruct? {_110 switch viewType {_110 case Type<MetadataViews.NFTCollectionData>():_110 let collectionData = MetadataViews.NFTCollectionData(_110 storagePath: self.CollectionStoragePath,_110 publicPath: self.CollectionPublicPath,_110 publicCollection: Type<&FooBar.Collection>(),_110 publicLinkedType: Type<&FooBar.Collection>(),_110 createEmptyCollectionFunction: (fun(): @{NonFungibleToken.Collection} {_110 return <-FooBar.createEmptyCollection(nftType: Type<@FooBar.NFT>())_110 })_110 )_110 return collectionData_110 case Type<MetadataViews.NFTCollectionDisplay>():_110 let media = MetadataViews.Media(_110 file: MetadataViews.HTTPFile(_110 url: "Add your own SVG+XML link here"_110 ),_110 mediaType: "image/svg+xml"_110 )_110 return MetadataViews.NFTCollectionDisplay(_110 name: "The FooBar Example Collection",_110 description: "This collection is used as an example to help you develop your next Flow NFT.",_110 externalURL: MetadataViews.ExternalURL("Add your own link here"),_110 squareImage: media,_110 bannerImage: media,_110 socials: {_110 "twitter": MetadataViews.ExternalURL("Add a link to your project's twitter")_110 }_110 )_110 }_110 return nil_110 }_110}`

If you ever plan on making your NFTs more complex, you should look into
adding views for `Edition`, `EVMBridgedMetadata`, `Traits`, and `Royalties`.
These views make it much easier for third-party sites like marketplaces
and NFT information aggregators to clearly display information
about your projects on their apps and websites and are critical
for every project to include if we want to have a vibrant and interoperable
ecosystem.

## Deploying the Contract[​](#deploying-the-contract "Direct link to Deploying the Contract")

With your contract ready, it's time to deploy it.
First, add the `FooBar` contract to the `flow.json` configuration file:

 `_10flow config add contract`

When prompted, enter the following name and location (press `Enter` to skip alias questions):

 `_10Enter name: FooBar_10Enter contract file location: cadence/contracts/FooBar.cdc`

Next, configure the deployment settings by running the following command:

 `_10flow config add deployment`

Choose the `emulator` for the network and `emulator-account`
for the account to deploy to.
Then, select the `FooBar` contract (you may need to scroll down).
This will update your `flow.json` configuration.
After that, you can select `No` when asked to deploy another contract.

To start the Flow emulator, run (you may need to approve a prompt to allow connection the first time):

 `_10flow emulator start`

In a separate terminal or command prompt, deploy the contract:

 `_10flow project deploy`

You'll then see a message that says `All contracts deployed successfully`.

## Creating an NFTCollection[​](#creating-an-nftcollection "Direct link to Creating an NFTCollection")

To manage multiple NFTs, you'll need an NFT collection.
Start by creating a transaction file for this purpose (we can use the `generate` command again):

 `_10flow generate transaction setup_foobar_collection`

This creates a transaction file at `cadence/transactions/setup_foobar_collection.cdc`.

Transactions, on the other hand, are pieces of Cadence code
that can mutate the state of the blockchain.
Transactions need to be signed by one or more accounts,
and they can have multiple phases, represented by different blocks of code.

In this file, import the necessary contracts and define a transaction
to create a new collection, storing it in the account's storage.
Additionally, the transaction creates a capability that allows others
to get a public reference to the collection to read from its methods.

This capability ensures secure, restricted access to specific functionalities or information within a resource.

 `_22import "FooBar"_22import "NonFungibleToken"_22_22transaction {_22_22 prepare(signer: auth(BorrowValue, IssueStorageCapabilityController, PublishCapability, SaveValue, UnpublishCapability) &Account) {_22_22 // Return early if the account already has a collection_22 if signer.storage.borrow<&FooBar.Collection>(from: FooBar.CollectionStoragePath) != nil {_22 return_22 }_22_22 // Create a new empty collection_22 let collection <- FooBar.createEmptyCollection(nftType: Type<@FooBar.NFT>())_22_22 // save it to the account_22 signer.storage.save(<-collection, to: FooBar.CollectionStoragePath)_22_22 let collectionCap = signer.capabilities.storage.issue<&FooBar.Collection>(FooBar.CollectionStoragePath)_22 signer.capabilities.publish(collectionCap, at: FooBar.CollectionPublicPath)_22 }_22}`

There are also examples of [generic transactions](https://github.com/onflow/flow-nft/blob/master/transactions/setup_account_from_address.cdc)
that you can use to setup an account for ANY non-fungible token using metadata views!
You should check those out and try to use generic transactions whenever it is possible.

To store this new NFT collection, create a new account:

 `_10flow accounts create`

Name it `test-acct` and select `emulator` as the network. Then, using the Flow CLI, run the transaction:

 `_10flow transactions send cadence/transactions/setup_foobar_collection.cdc --signer test-acct --network emulator`

Congratulations! You've successfully created an NFT collection for the `test-acct`.

## Get an Account's NFTs[​](#get-an-accounts-nfts "Direct link to Get an Account's NFTs")

To retrieve the NFTs associated with an account, you'll need a script.
Scripts are read-only operations that allow you to query the blockchain.
They don't modify the blockchain's state, and therefore,
they don't require gas fees or signatures (read more about scripts here).

Start by creating a script file using the `generate` command again:

 `_10flow generate script get_foobar_ids`

In this script, import the necessary contracts and define a function that retrieves the NFT IDs associated with a given account:

 `_14import "NonFungibleToken"_14import "FooBar"_14_14access(all) fun main(address: Address): [UInt64] {_14 let account = getAccount(address)_14_14 let collectionRef = account.capabilities.borrow<&{NonFungibleToken.Collection}>(_14 FooBar.CollectionPublicPath_14 ) ?? panic("The account ".concat(address.toString()).concat(" does not have a NonFungibleToken Collection at ")_14 .concat(FooBar.CollectionPublicPath.toString())_14 .concat(". The account must initialize their account with this collection first!"))_14_14 return collectionRef.getIDs()_14}`

To check the NFTs associated with the `test-acct`, run the script (note: replace `0x123` with the address for `test-acct` from `flow.json`):

 `_10flow scripts execute cadence/scripts/get_foobar_ids.cdc 0x123`

Since you haven't added any NFTs to the collection yet, the result will be an empty array.

## Minting and Depositing an NFT to a Collection[​](#minting-and-depositing-an-nft-to-a-collection "Direct link to Minting and Depositing an NFT to a Collection")

To mint and deposit an NFT into a collection, create a new transaction file:

 `_10flow generate transaction mint_foobar_nft`

In this file, define a transaction that takes a recipient's address as an argument.
This transaction will borrow the minting capability from the contract account,
borrow the recipient's collection capability, create a new NFT using the minter,
and deposit it into the recipient's collection:

 `_35import "NonFungibleToken"_35import "FooBar"_35_35transaction(_35 recipient: Address_35) {_35_35 /// local variable for storing the minter reference_35 let minter: &FooBar.NFTMinter_35_35 /// Reference to the receiver's collection_35 let recipientCollectionRef: &{NonFungibleToken.Receiver}_35_35 prepare(signer: auth(BorrowValue) &Account) {_35_35 // borrow a reference to the NFTMinter resource in storage_35 self.minter = signer.storage.borrow<&FooBar.NFTMinter>(from: FooBar.MinterStoragePath)_35 ?? panic("The signer does not store a FooBar Collection object at the path "_35 .concat(FooBar.CollectionStoragePath.toString())_35 .concat("The signer must initialize their account with this collection first!"))_35_35 // Borrow the recipient's public NFT collection reference_35 self.recipientCollectionRef = getAccount(recipient).capabilities.borrow<&{NonFungibleToken.Receiver}>(_35 FooBar.CollectionPublicPath_35 ) ?? panic("The account ".concat(recipient.toString()).concat(" does not have a NonFungibleToken Receiver at ")_35 .concat(FooBar.CollectionPublicPath.toString())_35 .concat(". The account must initialize their account with this collection first!"))_35 }_35_35 execute {_35 // Mint the NFT and deposit it to the recipient's collection_35 let mintedNFT <- self.minter.createNFT()_35 self.recipientCollectionRef.deposit(token: <-mintedNFT)_35 }_35}`

To run this transaction, use the Flow CLI. Remember, the contract account
(which has the minting resource) should be the one signing the transaction.
Pass the test account's address (from the `flow.json` file) as the recipient argument
(note: replace `0x123` with the address for `test-acct` from `flow.json`):

 `_10flow transactions send cadence/transactions/mint_foobar_nft.cdc 0x123 --signer emulator-account --network emulator`

After executing the transaction, you can run the earlier script to verify
that the NFT was added to the `test-acct`'s collection (remember to replace `0x123`):

 `_10flow scripts execute cadence/scripts/get_foobar_ids.cdc 0x123`

You should now see a value in the `test-acct`'s collection array!

## Transferring an NFT to Another Account[​](#transferring-an-nft-to-another-account "Direct link to Transferring an NFT to Another Account")

To transfer an NFT to another account, create a new transaction file using `generate`:

 `_10flow generate transaction transfer_foobar_nft`

In this file, define a transaction that takes a recipient's address and the ID
of the NFT you want to transfer as arguments.
This transaction will borrow the sender's collection, get the recipient's capability,
withdraw the NFT from the sender's collection, and deposit it into the recipient's collection:

 `_37import "FooBar"_37import "NonFungibleToken"_37_37transaction(recipient: Address, withdrawID: UInt64) {_37_37 /// Reference to the withdrawer's collection_37 let withdrawRef: auth(NonFungibleToken.Withdraw) &{NonFungibleToken.Collection}_37_37 /// Reference of the collection to deposit the NFT to_37 let receiverRef: &{NonFungibleToken.Receiver}_37_37 prepare(signer: auth(BorrowValue) &Account) {_37_37 // borrow a reference to the signer's NFT collection_37 self.withdrawRef = signer.storage.borrow<auth(NonFungibleToken.Withdraw) &{NonFungibleToken.Collection}>(_37 from: FooBar.CollectionStoragePath_37 ) ?? panic("The signer does not store a FooBar Collection object at the path "_37 .concat(FooBar.CollectionStoragePath.toString())_37 .concat("The signer must initialize their account with this collection first!"))_37_37 // get the recipients public account object_37 let recipient = getAccount(recipient)_37_37 // borrow a public reference to the receivers collection_37 let receiverCap = recipient.capabilities.get<&{NonFungibleToken.Receiver}>(FooBar.CollectionPublicPath)_37_37 self.receiverRef = receiverCap.borrow()_37 ?? panic("The account ".concat(recipient.toString()).concat(" does not have a NonFungibleToken Receiver at ")_37 .concat(FooBar.CollectionPublicPath.toString())_37 .concat(". The account must initialize their account with this collection first!"))_37 }_37_37 execute {_37 let nft <- self.withdrawRef.withdraw(withdrawID: withdrawID)_37 self.receiverRef.deposit(token: <-nft)_37 }_37}`

To transfer the NFT, first create a new account:

 `_10flow accounts create`

Name it `test-acct-2` and select `Emulator` as the network. Next, create a collection for this new account:

 `_10flow transactions send cadence/transactions/setup_foobar_collection.cdc --signer test-acct-2 --network emulator`

Now, run the transaction to transfer the NFT from `test-acct` to `test-acct-2`
using the addresses from the `flow.json` file (replace `0x124` with `test-acct-2`'s address.
Also note that `0` is the `id` of the `NFT` we'll be transferring):

 `_10flow transactions send cadence/transactions/transfer_foobar_nft.cdc 0x124 0 --signer test-acct --network emulator`

To verify the transfer, you can run the earlier script for `test-acct-2` (replace `0x124`):

 `_10flow scripts execute cadence/scripts/get_foobar_ids.cdc 0x123`

The transfer transaction also has a [generic version](https://github.com/onflow/flow-nft/blob/master/transactions/generic_transfer_with_address.cdc)
that developers are encouraged to use!

Congrats, you did it! You're now ready to launch the next fun NFT project on Flow.

## More[​](#more "Direct link to More")

* Explore [an example NFT repository](https://github.com/nvdtf/flow-nft-scaffold/blob/main/cadence/contracts/exampleNFT/ExampleNFT.cdc)
* Dive into the details of [the NFT Standard](https://github.com/onflow/flow-nft)
* For a deeper dive into `MetadataViews`, consult the [introduction guide](/build/advanced-concepts/metadata-views) or [the FLIP that introduced this feature](https://github.com/onflow/flips/blob/main/application/20210916-nft-metadata.md).
* Use a [no code tool for creating NFT projects on Flow](https://www.touchstone.city/)
[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/guides/nft.md)Last updated on **Feb 5, 2025** by **Brian Doyle**[PreviousMore Guides](/build/guides/more-guides)[NextCreating a Fungible Token](/build/guides/fungible-token)
###### Rate this page

😞😐😊

* [What are NFTs](#what-are-nfts)
* [Setting Up a Project](#setting-up-a-project)
  + [Installing Flow CLI](#installing-flow-cli)
  + [Initializing a New Project](#initializing-a-new-project)
* [Setting Up Our NFT on the Contract](#setting-up-our-nft-on-the-contract)
  + [Understanding Resources](#understanding-resources)
  + [Setting Up an NFT Collection](#setting-up-an-nft-collection)
* [Fitting the Flow NFT Standard](#fitting-the-flow-nft-standard)
  + [Applying the Standard](#applying-the-standard)
  + [Standard NFT Events](#standard-nft-events)
  + [Supporting NFT Metadata](#supporting-nft-metadata)
* [Deploying the Contract](#deploying-the-contract)
* [Creating an NFTCollection](#creating-an-nftcollection)
* [Get an Account's NFTs](#get-an-accounts-nfts)
* [Minting and Depositing an NFT to a Collection](#minting-and-depositing-an-nft-to-a-collection)
* [Transferring an NFT to Another Account](#transferring-an-nft-to-another-account)
* [More](#more)
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

