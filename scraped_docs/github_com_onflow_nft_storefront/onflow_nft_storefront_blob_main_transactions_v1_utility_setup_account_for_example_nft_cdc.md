# Source: https://github.com/onflow/nft-storefront/blob/main/transactions-v1/utility/setup_account_for_example_nft.cdc

```
/// This transaction is what an account would run
/// to set itself up to receive NFTs

import NonFungibleToken from "NonFungibleToken"
import ExampleNFT from "ExampleNFT"
import MetadataViews from "MetadataViews"

transaction {

    prepare(signer: auth(BorrowValue, IssueStorageCapabilityController, PublishCapability, SaveValue, UnpublishCapability) &Account) {
        
        let collectionData = ExampleNFT.resolveContractView(resourceType: nil, viewType: Type<MetadataViews.NFTCollectionData>()) as! MetadataViews.NFTCollectionData?
            ?? panic("ViewResolver does not resolve NFTCollectionData view")

        // Return early if the account already has a collection
        if signer.storage.borrow<&ExampleNFT.Collection>(from: collectionData.storagePath) != nil {
            return
        }

        // Create a new empty collection
        let collection <- ExampleNFT.createEmptyCollection(nftType: Type<@ExampleNFT.NFT>())

        // save it to the account
        signer.storage.save(<-collection, to: collectionData.storagePath)

        // create a public capability for the collection
        signer.capabilities.unpublish(collectionData.publicPath)
        let collectionCap = signer.capabilities.storage.issue<&ExampleNFT.Collection>(collectionData.storagePath)
        signer.capabilities.publish(collectionCap, at: collectionData.publicPath)
    }
}

```