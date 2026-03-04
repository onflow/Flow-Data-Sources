# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/hw_v2/transactions/hw_v2_setup_project_collections.cdc

```
import "NonFungibleToken"
import "MetadataViews"
import "FungibleToken"
import "FlowToken"
import "HWGarageTokenV2"
import "HWGarageCardV2"
import "HWGaragePackV2"


transaction() {

    prepare(acct: auth(BorrowValue, IssueStorageCapabilityController, PublishCapability, SaveValue, UnpublishCapability) &Account) {

        // Setup Token Collection

        let tokenCollectionData: MetadataViews.NFTCollectionData = HWGarageTokenV2.resolveContractView(resourceType: nil, viewType: Type<MetadataViews.NFTCollectionData>()) as! MetadataViews.NFTCollectionData?
            ?? panic("ViewResolver does not resolve NFTCollectionData view")

        // exit if tokenCollection exists
        if acct.storage.borrow<&HWGarageTokenV2.Collection>(from: tokenCollectionData.storagePath) == nil {
            // create a new empty tokenCollection for HWGarageTokenV2
            let tokenCollection: @{NonFungibleToken.Collection} <- HWGarageTokenV2.createEmptyCollection(nftType: Type<@HWGarageTokenV2.NFT>())

            // save HWGarageTokenV2 tokenCollection to the account
            acct.storage.save(<-tokenCollection, to: tokenCollectionData.storagePath)

            // create a public capability for the HWGarageTokenV2 tokenCollection
            acct.capabilities.unpublish(tokenCollectionData.publicPath) // remove any current pubCap 
            let tokenCollectionCap = acct.capabilities.storage.issue<&HWGarageTokenV2.Collection>(tokenCollectionData.storagePath)
            acct.capabilities.publish(tokenCollectionCap, at: tokenCollectionData.publicPath)
        }



        // Setup Card Collection

        let cardCollectionData: MetadataViews.NFTCollectionData = HWGarageCardV2.resolveContractView(resourceType: nil, viewType: Type<MetadataViews.NFTCollectionData>()) as! MetadataViews.NFTCollectionData?
            ?? panic("ViewResolver does not resolve NFTCollectionData view")

        // exit if cardCollection exists
        if acct.storage.borrow<&HWGarageCardV2.Collection>(from: cardCollectionData.storagePath) == nil {
            // create a new empty cardCollection for HWGarageCardV2
            let cardCollection: @{NonFungibleToken.Collection} <- HWGarageCardV2.createEmptyCollection(nftType: Type<@HWGarageCardV2.NFT>())

            // save HWGarageCardV2 cardCollection to the account
            acct.storage.save(<-cardCollection, to: cardCollectionData.storagePath)

            // create a public capability for the HWGarageCardV2 cardCollection
            acct.capabilities.unpublish(cardCollectionData.publicPath) // remove any current pubCap 
            let cardCollectionCap = acct.capabilities.storage.issue<&HWGarageCardV2.Collection>(cardCollectionData.storagePath)
            acct.capabilities.publish(cardCollectionCap, at: cardCollectionData.publicPath)
        }



        // Setup Pack Collection

        let packCollectionData: MetadataViews.NFTCollectionData = HWGaragePackV2.resolveContractView(resourceType: nil, viewType: Type<MetadataViews.NFTCollectionData>()) as! MetadataViews.NFTCollectionData?
            ?? panic("ViewResolver does not resolve NFTCollectionData view")

        // exit if packCollection exists
        if acct.storage.borrow<&HWGaragePackV2.Collection>(from: packCollectionData.storagePath) == nil {
            // create a new empty packCollection for HWGaragePackV2
            let packCollection: @{NonFungibleToken.Collection} <- HWGaragePackV2.createEmptyCollection(nftType: Type<@HWGaragePackV2.NFT>())

            // save HWGaragePackV2 packCollection to the account
            acct.storage.save(<-packCollection, to: packCollectionData.storagePath)

            // create a public capability for the HWGaragePackV2 packCollection
            acct.capabilities.unpublish(packCollectionData.publicPath) // remove any current pubCap 
            let packCollectionCap = acct.capabilities.storage.issue<&HWGaragePackV2.Collection>(packCollectionData.storagePath)
            acct.capabilities.publish(packCollectionCap, at: packCollectionData.publicPath)
        }


    }
    execute {
    }
}
 
```