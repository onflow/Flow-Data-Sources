# Source: https://developers.flow.com/build/advanced-concepts/metadata-views

NFT Metadata Views | Flow Developer Portal



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

  + [Account Abstraction](/build/advanced-concepts/account-abstraction)
  + [FLIX (Flow Interaction Templates)](/build/advanced-concepts/flix)
  + [NFT Metadata Views](/build/advanced-concepts/metadata-views)
  + [VRF (Randomness) in Cadence](/build/advanced-concepts/randomness)
  + [Scaling Transactions from a Single Account](/build/advanced-concepts/scaling)
* [Guides](/build/guides/account-linking)
* [Core Smart Contracts](/build/core-contracts)
* [Explore More](/build/explore-more)

* Advanced Concepts
* NFT Metadata Views

On this page

# NFT Metadata Views on Flow

`MetadataViews` on Flow offer a standardized way to represent onchain metadata
across different NFTs. Through its integration, developers can ensure
that different platforms and marketplaces can interpret the NFT metadata
in a unified manner. This means that when users visit different websites,
wallets, and marketplaces,
the NFT metadata will be presented in a consistent manner,
ensuring a uniform experience across various platforms.

info

It is important to understand this document so you can make meaningful decisions
about how to manage your project's metadata as support for metadata views does
not happen by default. Each project has unique metadata and therefore will have to
define how they expose it in unique ways.

A view is a standard Cadence struct that represents a specific type of metadata,
such as a [Royalty specification](https://github.com/onflow/flow-nft?tab=readme-ov-file#royalty-view):

`_10

access(all) struct Royalty {

_10

/// Where royalties should be paid to

_10

access(all) let receiver: Capability<&{FungibleToken.Receiver}>

_10

_10

/// The cut of the sale that should be taken for royalties.

_10

access(all) let cut: UFix64

_10

_10

/// Optional description of the royalty

_10

access(all) let description: String

_10

}`

or a [rarity description](https://github.com/onflow/flow-nft/blob/master/contracts/MetadataViews.cdc#L614):

`_10

access(all) struct Rarity {

_10

/// The score of the rarity as a number

_10

access(all) let score: UFix64?

_10

_10

/// The maximum value of score

_10

access(all) let max: UFix64?

_10

_10

/// The description of the rarity as a string.

_10

access(all) let description: String?

_10

}`

This guide acts as a specification for the correct ways to use each metadata view.
Many of the standard metadata views do not have built-in requirements
for how they are meant to be used, so it is important for developers to understand
the content of this document so third party apps can integrate with their
smart contracts as easily and effectively as possible.

> If you'd like to follow along while we discuss the concepts below,
> you can do so by referring to
> the [ExampleNFT contract](https://github.com/onflow/flow-nft/blob/master/contracts/ExampleNFT.cdc).
> Additionally, here is the source code for the
> [`ViewResolver` contract](https://github.com/onflow/flow-nft/blob/master/contracts/ViewResolver.cdc)
> and the [`MetadataViews` contract](https://github.com/onflow/flow-nft/blob/master/contracts/MetadataViews.cdc).

Flowty has also provided [a useful guide](https://docs.flowty.io/developer-docs/)
for how to manage metadata views properly
in order to be compatible with their marketplace. This guide is very useful
because all of their advice is generally good advice for any NFT contract,
regardless of what marketplace it is using.

## Two Levels of Metadata: An Overview[​](#two-levels-of-metadata-an-overview "Direct link to Two Levels of Metadata: An Overview")

Metadata in Cadence is structured at two distinct levels:

1. **Contract-Level Metadata**: This provides an overarching description
   of the entire NFT collection/project.
   Any metadata about individual NFTs is not included here.
2. **NFT-Level Metadata**: Diving deeper, this metadata relates to individual NFTs.
   It provides context, describes rarity, and highlights other distinctive attributes
   that distinguish one NFT from another within the same collection.

While these distinct levels describe different aspects of a project,
they both use the same view system for representing the metadata
and the same basic function calls to query the information,
just from different places.

## Understanding `ViewResolver` and `MetadataViews.Resolver`[​](#understanding-viewresolver-and-metadataviewsresolver "Direct link to understanding-viewresolver-and-metadataviewsresolver")

When considering Flow and how it handles metadata for NFTs,
it is crucial to understand two essential interfaces:
`ViewResolver` and `MetadataViews.Resolver`.
[Interfaces](https://cadence-lang.org/docs/language/interfaces)
serve as blueprints for types that specify the required fields and methods
that your contract or [composite type](https://cadence-lang.org/docs/language/composite-types) must adhere to
to be considered a subtype of that interface.
This guarantees that any contract asserting adherence to these interfaces
will possess a consistent set of functionalities
that other applications or contracts can rely on.

1. **`ViewResolver` for Contract-Level Metadata**:
   * This interface ensures that **contracts**, particularly those encapsulating NFT collections, conform to the Metadata Views standard.
   * Through the adoption of this interface, contracts can provide dynamic metadata that represents the entirety of the collection.
2. **`MetadataViews.Resolver` (`ViewResolver.Resolver` in Cadence 1.0) for NFT-Level Metadata**:
   * Used within **individual NFT resources**, this interface ensures each token adheres to the Metadata standard format.
   * It focuses on the distinct attributes of an individual NFT, such as its unique ID, name, description, and other defining characteristics.

### Core Functions[​](#core-functions "Direct link to Core Functions")

Both the `ViewResolver` and `MetadataViews.Resolver` utilize the following core functions:

### `getViews` Function[​](#getviews-function "Direct link to getviews-function")

This function provides a list of supported metadata view types,
which can be applied either by the contract (in the case of `ViewResolver`)
or by an individual NFT (in the case of `MetadataViews.Resolver`).

`_10

access(all) fun getViews(): [Type] {

_10

return [

_10

Type<MetadataViews.Display>(),

_10

Type<MetadataViews.Royalties>(),

_10

...

_10

]

_10

}`

### `resolveView` Function[​](#resolveview-function "Direct link to resolveview-function")

Whether utilized at the contract or NFT level, this function's role
is to deliver the actual metadata associated with a given view type.

The caller provides the type of the view they want to query as the only argument,
and the view is returned if it exists, and `nil` is returned if it doesn't.

`_10

access(all) fun resolveView(_ view: Type): AnyStruct? {

_10

switch view {

_10

case Type<MetadataViews.Display>():

_10

...

_10

...

_10

}

_10

return nil

_10

}`

As you can see, the return values of `getViews()` can be used as arguments
for `resolveView()` if you want to just iterate through all the views
that an NFT implements.

## NFT-Level Metadata Implementation[​](#nft-level-metadata-implementation "Direct link to NFT-Level Metadata Implementation")

NFT-level metadata addresses the unique attributes of individual tokens
within a collection. It provides structured information for each NFT,
including its identifier, descriptive elements, royalties,
and other associated metadata. Incorporating this level of detail
ensures consistency and standardization among individual NFTs,
making them interoperable and recognizable across various platforms and marketplaces.

### Core Properties[​](#core-properties "Direct link to Core Properties")

In the code below, an NFT has properties such as
its unique ID, name, description, and others.
When we add the `NonFungibleToken.NFT` and by extension,
the `MetadataViews.Resolver` to our NFT resource,
we are indicating that these variables will adhere to the specifications
outlined in the MetadataViews contract for each of these properties.
This facilitates interoperability within the Flow ecosystem
and assures that the metadata of our NFT can be consistently accessed
and understood by various platforms and services that interact with NFTs.

`_10

access(all) resource NFT: NonFungibleToken.NFT {

_10

access(all) let id: UInt64

_10

access(all) let name: String

_10

access(all) let description: String

_10

access(all) let thumbnail: String

_10

access(self) let royalties: [MetadataViews.Royalty]

_10

access(self) let metadata: {String: AnyStruct}

_10

...

_10

}`

To make this possible though, it is **vital** that projects
all use the standard metadata views in the same way, so third-party
applications can consume them in standard ways.

For example, many metadata views have `String`-typed fields. It is difficult
to enforce that these fields are formatted in the correct way, so it is important
for projects to be dilligent about how they use them. Take `Traits` for example,
a commonly misused metadata view:

`_10

access(all) struct Trait {

_10

// The name of the trait. Like Background, Eyes, Hair, etc.

_10

access(all) let name: String

_10

...

_10

...

_10

}`

The name of the trait should be formatted in a way so that it is easy to display
on a user-facing website. Many projects will use something like CamelCase for
the value, so it looks like "HairColor", which is not pretty on a website.
The correct format for this example would be "Hair Color".
This is just one of many common view uses that projects need to be aware of
to maximize the chance of success for their project.

## Metadata Views for NFTs[​](#metadata-views-for-nfts "Direct link to Metadata Views for NFTs")

`MetadataViews` types define how the NFT presents its data.
When invoked, the system knows precisely which view to return,
ensuring that the relevant information is presented consistently across various platforms.
In this section of the document, we will explore each metadata view and describe
how projects should properly use them.

### Display[​](#display "Direct link to Display")

This view provides the bare minimum information about the NFT
suitable for listing or display purposes. When the `Display` type is invoked,
it dynamically assembles the visual and descriptive information
that is typically needed for showcasing the NFT in marketplaces or collections.

`_10

case Type<MetadataViews.Display>():

_10

return MetadataViews.Display(

_10

name: self.name,

_10

description: self.description,

_10

thumbnail: MetadataViews.HTTPFile(

_10

url: self.thumbnail

_10

)

_10

)`

If the thumbnail is a HTTP resource:

`_10

thumbnail : MetadataViews.HTTPFile(url: *Please put your url here)`

If the thumbnail is an IPFS resource:

`_10

//

_10

thumbnail : MetadataViews.IPFSFile(

_10

cid: thumbnail cid, // Type <String>

_10

path: ipfs path // Type <String?> specify path if the cid is a folder hash, otherwise use nil here

_10

)`

![MetadataViews.Display](/assets/images/display-db0a98f662c5d015e754dfc04ef45c00.png "Display")

info

Note about SVG files on-chain: SVG field should be sent as `thumbnailURL`,
should be base64 encoded, and should have a dataURI prefix, like so:

`_10

data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMSIgaGVpZ2h0PSIxIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxyZWN0IHdpZHRoPSIxMDAlIiBoZWlnaHQ9IjEwMCUiIGZpbGw9InJlZCIvPjwvc3ZnPg==`

### Editions[​](#editions "Direct link to Editions")

The `Editions` view provides intricate details regarding the particular release of an NFT
within a set of NFTs with the same metadata.
This can include information about the number of copies in an edition,
the specific NFT's sequence number within that edition, or its inclusion in a limited series.
When the `Editions` view is queried, it retrieves this data,
providing collectors with the information they need to comprehend
the rarity and exclusivity of the NFT they are interested in.

An NFT can also be part of multiple editions, which is why the `Editions` view
can hold any number of `Edition` structs in an array.

For example, if an NFT is number 11 of 30 of an exclusive edition,
the code to return the `Editions` view would look like this:

`_10

case Type<MetadataViews.Editions>():

_10

let editionInfo = MetadataViews.Edition(

_10

name: "Example NFT Edition",

_10

number: 11,

_10

max: 30

_10

)

_10

return MetadataViews.Editions([editionInfo])`

### Serial Number Metadata[​](#serial-number-metadata "Direct link to Serial Number Metadata")

The `Serial` metadata provides the unique serial number of the NFT,
akin to a serial number on a currency note or a VIN on a car.
This serial number is a fundamental attribute that certifies the individuality
of each NFT and is critical for identification and verification processes.
Serial numbers are expected to be unique among other NFTs from the same project.
Many projects are already using the NFT resource's
[globally unique UUID]([resource's globally unique UUID](https://cadence-lang.org/docs/language/resources#resource-identifier))
as the ID already, so they will typically also use that as the serial number.

`_10

case Type<MetadataViews.Serial>():

_10

return MetadataViews.Serial(self.uuid)`

### Royalties Metadata[​](#royalties-metadata "Direct link to Royalties Metadata")

Royalty information is vital for the sustainable economics of the creators in the NFT space.
[The `Royalties` metadata view](https://github.com/onflow/flow-nft/blob/master/contracts/MetadataViews.cdc#L295)
defines the specifics of any royalty agreements in place,
including the percentage of sales revenue that will go to the original creator
or other stakeholders on secondary sales.

Each royalty view contains a fungible token receiver capability where royalties should be paid:

`_10

access(all) struct Royalty {

_10

_10

access(all) let receiver: Capability<&{FungibleToken.Receiver}>

_10

_10

access(all) let cut: UFix64

_10

}`

here is an example of how an NFT might return a `Royalties` view:

`_13

case Type<MetadataViews.Royalties>():

_13

// Assuming each 'Royalty' in the 'royalties' array has 'cut' and 'description' fields

_13

let royalty =

_13

MetadataViews.Royalty(

_13

// The beneficiary of the royalty: in this case, the contract account

_13

receiver: ExampleNFT.account.capabilities.get<&AnyResource{FungibleToken.Receiver}>(/public/GenericFTReceiver),

_13

// The percentage cut of each sale

_13

cut: 0.05,

_13

// A description of the royalty terms

_13

description: "Royalty payment to the original creator"

_13

)

_13

}

_13

return MetadataViews.Royalties(detailedRoyalties)`

If someone wants to make a listing for their NFT on a marketplace,
the marketplace can check to see if the royalty receiver
accepts the seller's desired fungible token by calling
the `receiver.getSupportedVaultTypes(): {Type: Bool}`
function via the `receiver` reference:

`_10

let royaltyReceiverRef = royalty.receiver.borrow()

_10

?? panic("Could not borrow a reference to the receiver")

_10

let supportedTypes = receiverRef.getSupportedVaultTypes()

_10

if supportedTypes[**royalty.getType()**] {

_10

// The type is supported, so you can deposit

_10

recieverRef.deposit(<-royalty)

_10

} else {

_10

// if it is not supported, you can do something else,

_10

// like revert, or send the royalty tokens to the seller instead

_10

}`

If the desired type is not supported, the marketplace has a few options.
They could either get the address of the receiver by using the
`receiver.owner.address` field and check to see if the account
has a receiver for the desired token, they could perform the sale without a royalty cut,
or they could abort the sale since the token type isn't accepted by the royalty beneficiary.

You can see example implementations of royalties in the `ExampleNFT` contract
and the associated transactions and scripts.
NFTs are often sold for a variety of currencies, so the royalty receiver should ideally
be a [fungible token switchboard](https://github.com/onflow/flow-ft?tab=readme-ov-file#fungible-token-switchboard) receiver that forwards any received tokens
to the correct vault in the receiving account.

#### Important instructions for royalty receivers[​](#important-instructions-for-royalty-receivers "Direct link to Important instructions for royalty receivers")

If you plan to set your account as a receiver of royalties,
you'll likely want to be able to accept as many token types as possible.
This is possible with the `FungibleTokenSwitchboard`.
If you initialize a switchboard in your account, it can accept any generic fungible token
and route it to the correct vault in your account.

Therefore, if you want to receive royalties, you should set up your account with the
[`setup_royalty_account_by_paths.cdc`](https://github.com/onflow/flow-ft/blob/master/transactions/switchboard/setup_royalty_account_by_paths.cdc) transaction.

This will link generic public path from `MetadataViews.getRoyaltyReceiverPublicPath()`
to the capability paths and types that you provide as arguments.
Then you can use that public path and capability for your royalty receiver.

### External URL Metadata[​](#external-url-metadata "Direct link to External URL Metadata")

The ExternalURL view returns to an associated webpage URL,
providing additional content or information about the NFT.
This can be a website, social media page, or anything else related to the project
that uses a URL.

`_10

case Type<MetadataViews.ExternalURL>():

_10

return MetadataViews.ExternalURL("<https://example-nft.onflow.org/>".concat(self.id.toString()))`

### Traits Metadata[​](#traits-metadata "Direct link to Traits Metadata")

The [`Trait`](https://github.com/onflow/flow-nft/blob/master/contracts/MetadataViews.cdc#L655) view type encapsulates the unique attributes of an NFT, like any visual aspects or category-defining properties. These can be essential for marketplaces that need to sort or filter NFTs based on these characteristics.
By returning trait views as recommended, you can fit the data in the places you want.

`_15

access(all) struct Trait {

_15

// The name of the trait. Like Background, Eyes, Hair, etc.

_15

access(all) let name: String

_15

_15

// The underlying value of the trait

_15

access(all) let value: AnyStruct

_15

_15

// displayType is used to show some context about what this name and value represent

_15

// for instance, you could set value to a unix timestamp, and specify displayType as "Date" to tell

_15

// platforms to consume this trait as a date and not a number

_15

access(all) let displayType: String?

_15

_15

// Rarity can also be used directly on an attribute.

_15

// This is optional because not all attributes need to contribute to the NFT's rarity.

_15

access(all) let rarity: Rarity?`

The traits view is extremely important to get right, because many third-party apps
and marketplaces are heavily reliant on it to properly display the entirety of your NFTs.
For example, the names and values of the traits are likely going to be displayed
on a user-facing website, so it is important to return them in a presentable form, such as `First Name`, instead of `first_name` or `firstName`.

Additionally, limit your `value` field to primitive types like `String`, `Int`, or `Bool`.

Additionally, the `displayType` is important as well, because it tells websites
how to display the trait properly. Developers should not just default
to `String` or `Integer` for all their display types.
When applicable, the display types to accurately reflect the data that needs to be displayed.

![MetadataViews.Traits](/assets/images/traits_String-183a7543a327e232391a34f19a4df34a.png "traits_String")

#### Note: Always prefer wrappers over single views[​](#note-always-prefer-wrappers-over-single-views "Direct link to Note: Always prefer wrappers over single views")

When exposing a view that could have multiple occurrences on a single NFT,
such as `Edition`, `Royalty`, `Media` or `Trait` the wrapper view should always be used
(such as `Editions`, `Royalties`, etc), even if there is only a single occurrence.
The wrapper view is always the plural version of the single view name
and can be found below the main view definition in the `MetadataViews` contract.

When resolving the view, the wrapper view should be the returned value,
instead of returning the single view or just an array of several occurrences of the view.

`_11

access(all) fun resolveView(_ view: Type): AnyStruct? {

_11

switch view {

_11

case Type<MetadataViews.Editions>():

_11

let editionInfo = MetadataViews.Edition(name: "Example NFT Edition", number: self.id, max: nil)

_11

let editionList: [MetadataViews.Edition] = [editionInfo]

_11

// return the wrapped view

_11

return MetadataViews.Editions(

_11

editionList

_11

)

_11

}

_11

}`

## Contract-Level Metadata Implementation[​](#contract-level-metadata-implementation "Direct link to Contract-Level Metadata Implementation")

Contract-level metadata provides a holistic view of an NFT collection,
capturing overarching attributes and contextual information about the entire set,
rather than specifics of individual tokens. These views describe attributes
at the collection or series level rather than individual NFTs.
These views should still should be queryable via individual NFTs though.
One can accomplish this by just forwarding the call
from the NFT's `resolveView()` method to the contract's `resolveView()` method, like so:

`_10

/// this line is in `ExampleNFT.NFT.resolveView()`

_10

case Type<MetadataViews.NFTCollectionDisplay>():

_10

return ExampleNFT.getCollectionDisplay(nftType: Type<@ExampleNFT.NFT>())`

### NFTCollectionData[​](#nftcollectiondata "Direct link to NFTCollectionData")

This view provides paths and types related to the NFT collection's storage
and access within the smart contract. The information in this view
is critical for understanding how to interact with a collection.

`_14

case Type<MetadataViews.NFTCollectionData>():

_14

return MetadataViews.NFTCollectionData(

_14

// where should the collection be saved?

_14

storagePath: ExampleNFT.CollectionStoragePath,

_14

// where to borrow public capabilities from?

_14

publicPath: ExampleNFT.CollectionPublicPath,

_14

// Important types for how the collection should be linked

_14

publicCollection: Type<&ExampleNFT.Collection>(),

_14

publicLinkedType: Type<&ExampleNFT.Collection>(),

_14

// function that can be accessed to create an empty collection for the project

_14

createEmptyCollectionFunction: (fun(): @{NonFungibleToken.Collection} {

_14

return <-ExampleNFT.createEmptyCollection(nftType: Type<@ExampleNFT.NFT>())

_14

})

_14

)`

Here, `NFTCollectionData` is specifying several important elements
related to how the collection is stored and accessed on the Flow blockchain.
It provides information on storage paths and access control paths
for both public and private data, as well as linked types
that specify what capabilities are publicly available
(like collection, receiver, or provider interfaces).

### NFTCollectionDisplay[​](#nftcollectiondisplay "Direct link to NFTCollectionDisplay")

This view describes the collection with visual elements and metadata
that are useful for display purposes, such as in a marketplace or gallery.
Many third party apps need this in order to display high-level information
about an NFT project properly.

`_17

case Type<MetadataViews.NFTCollectionDisplay>():

_17

let media = MetadataViews.Media(

_17

file: MetadataViews.HTTPFile(

_17

url: "<https://assets.website-files.com/5f6294c0c7a8cdd643b1c820/5f6294c0c7a8cda55cb1c936_Flow_Wordmark.svg>"

_17

),

_17

mediaType: "image/svg+xml"

_17

)

_17

return MetadataViews.NFTCollectionDisplay(

_17

name: "The Example Collection",

_17

description: "This collection is used as an example to help you develop your next Flow NFT.",

_17

externalURL: MetadataViews.ExternalURL("<https://example-nft.onflow.org>"),

_17

squareImage: media,

_17

bannerImage: media,

_17

socials: {

_17

"twitter": MetadataViews.ExternalURL("<https://twitter.com/flow_blockchain>")

_17

}

_17

)`

In the example above, the `NFTCollectionDisplay` not only offers fundamental metadata
like the collection's name and description but also provides image URLs
for visual representations of the collection (`squareImage` and `bannerImage`)
and external links, including social media profiles.

![MetadataViews.CollectionDisplay](/assets/images/collectionDisplay-c46eba803c52ece34661178c113354f2.png "CollectionDisplay")

### Contract-borrowing Metadata[​](#contract-borrowing-metadata "Direct link to Contract-borrowing Metadata")

With the contract borrowing feature, the [ViewResolver](https://github.com/onflow/flow-nft/blob/master/contracts/ViewResolver.cdc)
interface on contracts can be borrowed directly without needing to import the contract first.
Views can be resolved directly from there.
As an example, you might want to allow your contract
to resolve `NFTCollectionData` and `NFTCollectionDisplay` so that platforms
do not need to find an NFT that belongs to your contract
to get information about how to set up or show your collection.

`_15

import ViewResolver from 0xf8d6e0586b0a20c7

_15

import MetadataViews from 0xf8d6e0586b0a20c7

_15

_15

access(all) fun main(addr: Address, name: String): StoragePath? {

_15

let t = Type<MetadataViews.NFTCollectionData>()

_15

let borrowedContract = getAccount(addr).contracts.borrow<&ViewResolver>(name: name) ?? panic("contract could not be borrowed")

_15

_15

let view = borrowedContract.resolveView(t)

_15

if view == nil {

_15

return nil

_15

}

_15

_15

let cd = view! as! MetadataViews.NFTCollectionData

_15

return cd.storagePath

_15

}`

Will Return

`_10

{"domain":"storage","identifier":"exampleNFTCollection"}`

## More[​](#more "Direct link to More")

Understanding `MetadataViews` and the core functions associated with it
is crucial for developers aiming to deploy NFTs on Flow.
With these views and functions, NFTs can maintain a consistent presentation
across various platforms and marketplaces and foster interoperability
between contracts and applications in the Flow ecosystem.
To gain a deeper understanding of implementing the MetadataView standard,
check out our documentation on "How to Create an NFT Project on Flow".
It provides an introduction to integrating these standards into your NFT contracts.

* See the [API reference for a complete list of Metadata functions](https://developers.flow.com/build/core-contracts/flow-nft/MetdataViews/MetadataViews)
* Check out [an Example NFT project](https://github.com/onflow/flow-nft/blob/master/contracts/ExampleNFT.cdc) implementing `MetadataViews`
* Read [the NFT Guide](/build/guides/nft) for an introduction to implementation

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/advanced-concepts/metadata-views.md)

Last updated on **Mar 27, 2025** by **Brian Doyle**

[Previous

FLIX (Flow Interaction Templates)](/build/advanced-concepts/flix)[Next

VRF (Randomness) in Cadence](/build/advanced-concepts/randomness)

###### Rate this page

😞😐😊

* [Two Levels of Metadata: An Overview](#two-levels-of-metadata-an-overview)
* [Understanding `ViewResolver` and `MetadataViews.Resolver`](#understanding-viewresolver-and-metadataviewsresolver)
  + [Core Functions](#core-functions)
  + [`getViews` Function](#getviews-function)
  + [`resolveView` Function](#resolveview-function)
* [NFT-Level Metadata Implementation](#nft-level-metadata-implementation)
  + [Core Properties](#core-properties)
* [Metadata Views for NFTs](#metadata-views-for-nfts)
  + [Display](#display)
  + [Editions](#editions)
  + [Serial Number Metadata](#serial-number-metadata)
  + [Royalties Metadata](#royalties-metadata)
  + [External URL Metadata](#external-url-metadata)
  + [Traits Metadata](#traits-metadata)
* [Contract-Level Metadata Implementation](#contract-level-metadata-implementation)
  + [NFTCollectionData](#nftcollectiondata)
  + [NFTCollectionDisplay](#nftcollectiondisplay)
  + [Contract-borrowing Metadata](#contract-borrowing-metadata)
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