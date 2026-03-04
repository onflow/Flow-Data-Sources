# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/hw_v1/transactions/hw_v1_claim_pack.cdc

```
import "MetadataViews"
import "NonFungibleToken"
import "FungibleToken"
import "FlowToken"

import "HWGarageCard"
import "HWGaragePack"
import "HWGaragePM"
transaction(address: Address, packHash: String) {

// TODO - fix logic so conditionals check for state of both collections
//      - initialize the collection(s) that are/is needed or return early

    prepare(acct: auth(BorrowValue, IssueStorageCapabilityController, PublishCapability, SaveValue, UnpublishCapability) &Account) {

        // Setup Pack Collection

        let packCollectionData = HWGarageCard.resolveContractView(resourceType: nil, viewType: Type<MetadataViews.NFTCollectionData>()) as! MetadataViews.NFTCollectionData?
            ?? panic("ViewResolver does not resolve NFTCollectionData view")

        // exit if packCollection exists
        if acct.storage.borrow<&HWGarageCard.Collection>(from: packCollectionData.storagePath) != nil {
            // create a new empty packCollection for HWGarageCard
            let packCollection <- HWGarageCard.createEmptyCollection(nftType: Type<@HWGarageCard.NFT>())

            // save HWGarageCard packCollection to the account
            acct.storage.save(<-packCollection, to: packCollectionData.storagePath)

            // create a public capability for the HWGarageCard packCollection
            acct.capabilities.unpublish(packCollectionData.publicPath) // remove any current pubCap 
            let packCollectionCap = acct.capabilities.storage.issue<&HWGarageCard.Collection>(packCollectionData.storagePath)
            acct.capabilities.publish(packCollectionCap, at: packCollectionData.publicPath)
        }



        // Setup Card Collection

        let cardCollectionData = HWGarageCard.resolveContractView(resourceType: nil, viewType: Type<MetadataViews.NFTCollectionData>()) as! MetadataViews.NFTCollectionData?
            ?? panic("ViewResolver does not resolve NFTCollectionData view")

        // exit if cardCollection exists
        if acct.storage.borrow<&HWGarageCard.Collection>(from: cardCollectionData.storagePath) != nil {
            // create a new empty cardCollection for HWGarageCard
            let cardCollection <- HWGarageCard.createEmptyCollection(nftType: Type<@HWGarageCard.NFT>())

            // save HWGarageCard cardCollection to the account
            acct.storage.save(<-cardCollection, to: cardCollectionData.storagePath)

            // create a public capability for the HWGarageCard cardCollection
            acct.capabilities.unpublish(cardCollectionData.publicPath) // remove any current pubCap 
            let cardCollectionCap = acct.capabilities.storage.issue<&HWGarageCard.Collection>(cardCollectionData.storagePath)
            acct.capabilities.publish(cardCollectionCap, at: cardCollectionData.publicPath)
        }

    }
    execute {
        HWGaragePM.claimPack(address: address, packHash: packHash)
    }
}
 
```