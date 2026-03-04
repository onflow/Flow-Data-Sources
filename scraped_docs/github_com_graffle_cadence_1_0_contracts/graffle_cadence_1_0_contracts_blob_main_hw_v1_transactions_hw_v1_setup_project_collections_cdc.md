# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/hw_v1/transactions/hw_v1_setup_project_collections.cdc

```
import "NonFungibleToken"
import "MetadataViews"
import "FungibleToken"
import "FlowToken"
import "HWGarageCard"
import "HWGaragePack"


transaction() {

    prepare(acct: auth(BorrowValue, IssueStorageCapabilityController, PublishCapability, SaveValue, UnpublishCapability) &Account) {

        // Setup Pack Collection

        let packCollectionData: MetadataViews.NFTCollectionData = HWGaragePack.resolveContractView(resourceType: nil, viewType: Type<MetadataViews.NFTCollectionData>()) as! MetadataViews.NFTCollectionData?
            ?? panic("ViewResolver does not resolve NFTCollectionData view")

        // exit if packCollection exists
        if acct.storage.borrow<&HWGaragePack.Collection>(from: packCollectionData.storagePath) == nil {
            // create a new empty packCollection for HWGaragePack
            let packCollection: @{NonFungibleToken.Collection} <- HWGaragePack.createEmptyCollection(nftType: Type<@HWGaragePack.NFT>())

            // save HWGaragePack packCollection to the account
            acct.storage.save(<-packCollection, to: packCollectionData.storagePath)

            // create a public capability for the HWGaragePack packCollection
            acct.capabilities.unpublish(packCollectionData.publicPath) // remove any current pubCap 
            let packCollectionCap: Capability<&HWGaragePack.Collection> = acct.capabilities.storage.issue<&HWGaragePack.Collection>(packCollectionData.storagePath)
            acct.capabilities.publish(packCollectionCap, at: packCollectionData.publicPath)

        }


        // Setup Card Collection

        let cardCollectionData: MetadataViews.NFTCollectionData = HWGarageCard.resolveContractView(resourceType: nil, viewType: Type<MetadataViews.NFTCollectionData>()) as! MetadataViews.NFTCollectionData?
            ?? panic("ViewResolver does not resolve NFTCollectionData view")

        // exit if cardCollection exists
        if acct.storage.borrow<&HWGarageCard.Collection>(from: cardCollectionData.storagePath) == nil {
            // create a new empty cardCollection for HWGarageCard
            let cardCollection: @{NonFungibleToken.Collection} <- HWGarageCard.createEmptyCollection(nftType: Type<@HWGarageCard.NFT>())

            // save HWGarageCard cardCollection to the account
            acct.storage.save(<-cardCollection, to: cardCollectionData.storagePath)

            // create a public capability for the HWGarageCard cardCollection
            acct.capabilities.unpublish(cardCollectionData.publicPath) // remove any current pubCap 
            let cardCollectionCap: Capability<&HWGarageCard.Collection> = acct.capabilities.storage.issue<&HWGarageCard.Collection>(cardCollectionData.storagePath)
            acct.capabilities.publish(cardCollectionCap, at: cardCollectionData.publicPath)
        }


    }
    execute {
    }
}
 
```