# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/hw_v2/transactions/hw_v2_redeem_pack.cdc

```
import "NonFungibleToken"
import "MetadataViews"
import "HWGarageCardV2"
import "HWGaragePackV2"
import "HWGaragePMV2"

transaction(
    packID: UInt64 // aka packEditionID
    , packHash: String
    ) {
    let address: Address
    let collectionRef: auth(NonFungibleToken.Withdraw) &HWGaragePackV2.Collection
    let packToRedeem: @{NonFungibleToken.NFT}
    
    prepare(acct: auth(BorrowValue, IssueStorageCapabilityController, PublishCapability, SaveValue, UnpublishCapability) &Account) {
        self.address = acct.address
        // Setup collection if they aren't already setup
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
            let cardCollectionCap: Capability<&HWGarageCardV2.Collection> = acct.capabilities.storage.issue<&HWGarageCardV2.Collection>(cardCollectionData.storagePath)
            acct.capabilities.publish(cardCollectionCap, at: cardCollectionData.publicPath)
        }

        let collectionData: MetadataViews.NFTCollectionData = HWGaragePackV2.resolveContractView(resourceType: nil, viewType: Type<MetadataViews.NFTCollectionData>()) as! MetadataViews.NFTCollectionData?
            ?? panic("ViewResolver does not resolve NFTCollectionData view")
        
        // borrow reference to pack owner's collection
        self.collectionRef = acct.storage.borrow<auth(NonFungibleToken.Withdraw) &HWGaragePackV2.Collection>(from: collectionData.storagePath) ?? panic("Account does not store an oject at the specified path")

        self.packToRedeem <- self.collectionRef.withdraw(withdrawID: packID)
    
    }
    execute {
        // Call public redeem method
        HWGaragePMV2.publicRedeemPack(address: self.address, pack: <-self.packToRedeem, packHash: packHash)
    }
}
 
```