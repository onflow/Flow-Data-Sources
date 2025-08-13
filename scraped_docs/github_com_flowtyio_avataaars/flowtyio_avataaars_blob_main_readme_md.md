# Source: https://github.com/Flowtyio/avataaars/blob/main/README.md

# Avataaars - A Sample PFP Generator Cadence Smart Contract

Welcome! This repo serves as a complete example for how to build a smart contract fully compliant with
NFT-standards. This repo brings Avataaars, an open-source avatar generator, to the blockchain, randomly generating
avatars for users and storing them as NFTs. It makes full use of 
[Metadata Standards](https://github.com/onflow/flow-nft/blob/master/contracts/MetadataViews.cdc)
needed for NFTs to be compatible with the Flowty marketplace and suite of products. Enjoy!

## Metadata

Metadata is broken up into things called "Views" and can be "resolved" using the `resolveView` method on any resource
which implements the `MetadataViews.Resolver` interface. In order for an NFT to be compliant with metadata standards,
it should be able to resolve
the [NFTView](https://github.com/onflow/flow-nft/blob/master/contracts/MetadataViews.cdc#L36)
Metadata View which encapsulates the minimum set of data needed to fully describe an NFT. Don't worry about resolving
the NFTView yourself, though! There is
a [helper method](https://github.com/onflow/flow-nft/blob/master/contracts/MetadataViews.cdc#L73)
that consumers of these standards use to grab everything at once, so you can avoid as much boilerplate as possible.

### NFT-level Metadata

The following metadata views are expected by Flowty to be available in order for NFTs to be compatible with
our marketplace and suite of products.

1. [Display](https://github.com/Flowtyio/avataaars/blob/main/contracts/Avataaars.cdc#L104) - 
This is the primary view that is used to display an NFT in the marketplace. It contains information about the NFT's
image, name, and description

2. [Royalties](https://github.com/Flowtyio/avataaars/blob/main/contracts/Avataaars.cdc#L124) -
This view is used to describe how royalties should be paid out to the NFT's creators. To learn more about
Royalties, check out Austin's thread on the topic [here](https://twitter.com/austin_flowty/status/1636818524529360896)

3. [External URL](https://github.com/Flowtyio/avataaars/blob/main/contracts/Avataaars.cdc#L135) -  
   This view is optional, and is used to provide a backlink for a specific NFT to your website or app.

4. [NFTCollectionData](https://github.com/Flowtyio/avataaars/blob/main/contracts/Avataaars.cdc#L139) -
   This view contains information necessary to interact with your collection. Flowty makes use of
this view to determine where to save and retrieve your NFTs. This view is used as a fallback if your collection is **not**
on the NFT Catalog, and does **not** describe this view on the contract-level (described below).
 
5. [NFTCollectionDisplay](https://github.com/Flowtyio/avataaars/blob/main/contracts/Avataaars.cdc#L141) -
   This view described how your collection should be shown on marketplaces. Just like NFTCollectionData,
this view is used as a fallback if your collection is **not** on the NFT Catalog, and does **not** describe this view on
the contract-level (described below).

6. [Traits](https://github.com/Flowtyio/avataaars/blob/main/contracts/Avataaars.cdc#L143) -
   This view describes traits that users can perform filtering on. For example, Avataars have a trait called
"Clothing" which has various values such as "Shirt", "Jacket", "Hoodie", etc. When ingested, each of these traits becomes
a filterable option for users to search for on your collection page.

### Contract-level Metadata

In addition to the `Resolver` interface, there is also a contract-level interface called
[ViewResolver](https://github.com/onflow/flow-nft/blob/master/contracts/ViewResolver.cdc) which can be used
to describe metadata about the contract itself. These views all can exist on NFTs as well, but contract-level views
take precedence where described. Currently, the following metadata views are supported by Flowty at the contract level:

1. [NFTCollectionData](https://github.com/Flowtyio/avataaars/blob/main/contracts/Avataaars.cdc#L139) -
Flowty makes use of this view to determine where to save and retrieve your NFTs. Without it, **Flowty will not be able to
detect your collection's NFTs automatically.**

2. [NFTCollectionDisplay](https://github.com/Flowtyio/avataaars/blob/main/contracts/Avataaars.cdc#L141) -
This view described how your collection should be shown on marketplaces. Without this, Flowty will use placeholder
images for your collection's banner and thumbnail, and will use your contract's name as the collection's name.

3. [External URL](https://github.com/Flowtyio/avataaars/blob/main/contracts/Avataaars.cdc#L135) -  
This view is optional, and is used to provide a backlink to your website or app. 
**NOTE: Unlike the other contract-level views, External URL does not override the NFTs implementation of this view 
as they serve different purposes**

You can find the Avataaars implementation of `ViewResolver`
[here](https://github.com/Flowtyio/avataaars/blob/main/contracts/Avataaars.cdc#L319).

## Sample transactions

[Mint - Mainnet](https://run.ecdao.org?code=aW1wb3J0IEF2YXRhYWFycyBmcm9tIDB4YzkzNGVkMGMwZjQ3ODhiYwppbXBvcnQgTm9uRnVuZ2libGVUb2tlbiBmcm9tIDB4MWQ3ZTU3YWE1NTgxNzQ0OAppbXBvcnQgTWV0YWRhdGFWaWV3cyBmcm9tIDB4MWQ3ZTU3YWE1NTgxNzQ0OAoKdHJhbnNhY3Rpb24ocXVhbnRpdHk6IEludCkgewogICAgcHJlcGFyZShhY2N0OiBBdXRoQWNjb3VudCkgewogICAgICAgIGlmIGFjY3QuYm9ycm93PCZBbnlSZXNvdXJjZT4oZnJvbTogQXZhdGFhYXJzLkNvbGxlY3Rpb25TdG9yYWdlUGF0aCkgPT0gbmlsIHsKICAgICAgICAgICAgbGV0IGMgPC0gQXZhdGFhYXJzLmNyZWF0ZUVtcHR5Q29sbGVjdGlvbigpCiAgICAgICAgICAgIGFjY3Quc2F2ZSg8LWMsIHRvOiBBdmF0YWFhcnMuQ29sbGVjdGlvblN0b3JhZ2VQYXRoKQogICAgICAgIH0KCiAgICAgICAgYWNjdC51bmxpbmsoQXZhdGFhYXJzLkNvbGxlY3Rpb25QdWJsaWNQYXRoKQogICAgICAgIGFjY3QudW5saW5rKEF2YXRhYWFycy5Db2xsZWN0aW9uUHJvdmlkZXJQYXRoKQoKICAgICAgICBhY2N0Lmxpbms8JkF2YXRhYWFycy5Db2xsZWN0aW9ue0F2YXRhYWFycy5BdmF0YWFhcnNDb2xsZWN0aW9uUHVibGljLCBOb25GdW5naWJsZVRva2VuLkNvbGxlY3Rpb25QdWJsaWMsIE1ldGFkYXRhVmlld3MuUmVzb2x2ZXJDb2xsZWN0aW9ufT4oQXZhdGFhYXJzLkNvbGxlY3Rpb25QdWJsaWNQYXRoLCB0YXJnZXQ6IEF2YXRhYWFycy5Db2xsZWN0aW9uU3RvcmFnZVBhdGgpCiAgICAgICAgYWNjdC5saW5rPCZBdmF0YWFhcnMuQ29sbGVjdGlvbntBdmF0YWFhcnMuQXZhdGFhYXJzQ29sbGVjdGlvblB1YmxpYywgTm9uRnVuZ2libGVUb2tlbi5Db2xsZWN0aW9uUHVibGljLCBNZXRhZGF0YVZpZXdzLlJlc29sdmVyQ29sbGVjdGlvbiwgTm9uRnVuZ2libGVUb2tlbi5Qcm92aWRlcn0%2BKEF2YXRhYWFycy5Db2xsZWN0aW9uUHJvdmlkZXJQYXRoLCB0YXJnZXQ6IEF2YXRhYWFycy5Db2xsZWN0aW9uU3RvcmFnZVBhdGgpCgogICAgICAgIGxldCBjb2xsZWN0aW9uID0gYWNjdC5ib3Jyb3c8JkF2YXRhYWFycy5Db2xsZWN0aW9uPihmcm9tOiBBdmF0YWFhcnMuQ29sbGVjdGlvblN0b3JhZ2VQYXRoKSEKCiAgICAgICAgbGV0IG1pbnRlciA9IEF2YXRhYWFycy5ib3Jyb3dNaW50ZXIoKQogICAgICAgIAogICAgICAgIHZhciBjb3VudCA9IDAKICAgICAgICB3aGlsZSBjb3VudCA8IHF1YW50aXR5IHsKICAgICAgICAgICAgY291bnQgPSBjb3VudCArIDEKICAgICAgICAgICAgbWludGVyLm1pbnRORlQocmVjaXBpZW50OiBjb2xsZWN0aW9uKQogICAgICAgIH0KICAgIH0KfQ%3D%3D&network=mainnet&args=eyJxdWFudGl0eSI6NX0%3D)

[Mint - Testnet](https://run.ecdao.org?code=aW1wb3J0IEF2YXRhYWFycyBmcm9tIDB4ZmNkMWY5YmU0Y2M1ZTQ3YgppbXBvcnQgTm9uRnVuZ2libGVUb2tlbiBmcm9tIDB4NjMxZTg4YWU3ZjFkN2MyMAppbXBvcnQgTWV0YWRhdGFWaWV3cyBmcm9tIDB4NjMxZTg4YWU3ZjFkN2MyMAoKdHJhbnNhY3Rpb24ocXVhbnRpdHk6IEludCkgewogICAgcHJlcGFyZShhY2N0OiBBdXRoQWNjb3VudCkgewogICAgICAgIGlmIGFjY3QuYm9ycm93PCZBbnlSZXNvdXJjZT4oZnJvbTogQXZhdGFhYXJzLkNvbGxlY3Rpb25TdG9yYWdlUGF0aCkgPT0gbmlsIHsKICAgICAgICAgICAgbGV0IGMgPC0gQXZhdGFhYXJzLmNyZWF0ZUVtcHR5Q29sbGVjdGlvbigpCiAgICAgICAgICAgIGFjY3Quc2F2ZSg8LWMsIHRvOiBBdmF0YWFhcnMuQ29sbGVjdGlvblN0b3JhZ2VQYXRoKQogICAgICAgIH0KCiAgICAgICAgYWNjdC51bmxpbmsoQXZhdGFhYXJzLkNvbGxlY3Rpb25QdWJsaWNQYXRoKQogICAgICAgIGFjY3QudW5saW5rKEF2YXRhYWFycy5Db2xsZWN0aW9uUHJvdmlkZXJQYXRoKQoKICAgICAgICBhY2N0Lmxpbms8JkF2YXRhYWFycy5Db2xsZWN0aW9ue0F2YXRhYWFycy5BdmF0YWFhcnNDb2xsZWN0aW9uUHVibGljLCBOb25GdW5naWJsZVRva2VuLkNvbGxlY3Rpb25QdWJsaWMsIE1ldGFkYXRhVmlld3MuUmVzb2x2ZXJDb2xsZWN0aW9ufT4oQXZhdGFhYXJzLkNvbGxlY3Rpb25QdWJsaWNQYXRoLCB0YXJnZXQ6IEF2YXRhYWFycy5Db2xsZWN0aW9uU3RvcmFnZVBhdGgpCiAgICAgICAgYWNjdC5saW5rPCZBdmF0YWFhcnMuQ29sbGVjdGlvbntBdmF0YWFhcnMuQXZhdGFhYXJzQ29sbGVjdGlvblB1YmxpYywgTm9uRnVuZ2libGVUb2tlbi5Db2xsZWN0aW9uUHVibGljLCBNZXRhZGF0YVZpZXdzLlJlc29sdmVyQ29sbGVjdGlvbiwgTm9uRnVuZ2libGVUb2tlbi5Qcm92aWRlcn0%2BKEF2YXRhYWFycy5Db2xsZWN0aW9uUHJvdmlkZXJQYXRoLCB0YXJnZXQ6IEF2YXRhYWFycy5Db2xsZWN0aW9uU3RvcmFnZVBhdGgpCgogICAgICAgIGxldCBjb2xsZWN0aW9uID0gYWNjdC5ib3Jyb3c8JkF2YXRhYWFycy5Db2xsZWN0aW9uPihmcm9tOiBBdmF0YWFhcnMuQ29sbGVjdGlvblN0b3JhZ2VQYXRoKSEKCiAgICAgICAgbGV0IG1pbnRlciA9IEF2YXRhYWFycy5ib3Jyb3dNaW50ZXIoKQogICAgICAgIAogICAgICAgIHZhciBjb3VudCA9IDAKICAgICAgICB3aGlsZSBjb3VudCA8IHF1YW50aXR5IHsKICAgICAgICAgICAgY291bnQgPSBjb3VudCArIDEKICAgICAgICAgICAgbWludGVyLm1pbnRORlQocmVjaXBpZW50OiBjb2xsZWN0aW9uKQogICAgICAgIH0KICAgIH0KfQ%3D%3D&network=testnet&args=eyJxdWFudGl0eSI6MX0%3D)