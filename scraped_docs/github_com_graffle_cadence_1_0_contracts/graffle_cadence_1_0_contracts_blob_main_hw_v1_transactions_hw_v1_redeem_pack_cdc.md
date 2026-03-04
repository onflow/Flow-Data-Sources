# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/hw_v1/transactions/hw_v1_redeem_pack.cdc

```
import "MetadataViews"
import "NonFungibleToken"
import "FungibleToken"
import "FlowToken"

import "HWGarageCard"
import "HWGaragePack"
import "HWGaragePM"

// Use the burn transaction as a guide
transaction(packID: UInt64, packHash: String) {
    let address: Address
    let collectionRef: auth(NonFungibleToken.Withdraw) &HWGaragePack.Collection
    let packToRedeem: @{NonFungibleToken.NFT}
    
    prepare(acct: auth(BorrowValue, IssueStorageCapabilityController, PublishCapability, SaveValue, UnpublishCapability) &Account) {
        self.address = acct.address
        // Setup Card Collection
        let cardCollectionData = HWGarageCard.resolveContractView(resourceType: nil, viewType: Type<MetadataViews.NFTCollectionData>()) as! MetadataViews.NFTCollectionData?
            ?? panic("ViewResolver does not resolve NFTCollectionData view")

        // exit if cardCollection exists
        if acct.storage.borrow<&HWGarageCard.Collection>(from: cardCollectionData.storagePath) == nil {
            // create a new empty cardCollection for HWGarageCard
            let cardCollection <- HWGarageCard.createEmptyCollection(nftType: Type<@HWGarageCard.NFT>())

            // save HWGarageCard cardCollection to the account
            acct.storage.save(<-cardCollection, to: cardCollectionData.storagePath)

            // create a public capability for the HWGarageCard cardCollection
            acct.capabilities.unpublish(cardCollectionData.publicPath) // remove any current pubCap 
            let cardCollectionCap = acct.capabilities.storage.issue<&HWGarageCard.Collection>(cardCollectionData.storagePath)
            acct.capabilities.publish(cardCollectionCap, at: cardCollectionData.publicPath)
        }

        let collectionData = HWGaragePack.resolveContractView(resourceType: nil, viewType: Type<MetadataViews.NFTCollectionData>()) as! MetadataViews.NFTCollectionData?
            ?? panic("ViewResolver does not resolve NFTCollectionData view")
        
        // borrow reference to pack owner's collection
        self.collectionRef = acct.storage.borrow<auth(NonFungibleToken.Withdraw) &HWGaragePack.Collection>(from: collectionData.storagePath) ?? panic("Account does not store an oject at the specified path")
        self.packToRedeem <- self.collectionRef.withdraw(withdrawID: packID)
    }

    execute {
        // withdraw Pack from owner's collection
        // Call public redeem method
        HWGaragePM.publicRedeemPack(pack: <-self.packToRedeem, address: self.address, packHash: packHash)
    }
}
 
```