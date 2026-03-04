# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/bbxb/transactions/bb_v1_redeem_pack.cdc

```
import "NonFungibleToken"
import "MetadataViews"
import "BBxBarbieCard"
import "BBxBarbiePack"
import "BBxBarbiePM"

transaction(packID: UInt64, packHash: String) {
    let address: Address
    let collectionRef: auth(NonFungibleToken.Withdraw) &BBxBarbiePack.Collection
    let packToRedeem: @{NonFungibleToken.NFT}
    
    prepare(acct: auth(BorrowValue, IssueStorageCapabilityController, PublishCapability, SaveValue, UnpublishCapability) &Account) {
        self.address = acct.address

        // Setup Card Collection
        let cardCollectionData: MetadataViews.NFTCollectionData = BBxBarbieCard.resolveContractView(resourceType: nil, viewType: Type<MetadataViews.NFTCollectionData>()) as! MetadataViews.NFTCollectionData?
            ?? panic("ViewResolver does not resolve NFTCollectionData view")

        // exit if cardCollection exists
        if acct.storage.borrow<&BBxBarbieCard.Collection>(from: cardCollectionData.storagePath) == nil {
            // create a new empty cardCollection for BBxBarbieCard
            let cardCollection: @{NonFungibleToken.Collection} <- BBxBarbieCard.createEmptyCollection(nftType: Type<@BBxBarbieCard.NFT>())

            // save BBxBarbieCard cardCollection to the account
            acct.storage.save(<-cardCollection, to: cardCollectionData.storagePath)

            // create a public capability for the BBxBarbieCard cardCollection
            acct.capabilities.unpublish(cardCollectionData.publicPath) // remove any current pubCap 
            let cardCollectionCap: Capability<&BBxBarbieCard.Collection> = acct.capabilities.storage.issue<&BBxBarbieCard.Collection>(cardCollectionData.storagePath)
            acct.capabilities.publish(cardCollectionCap, at: cardCollectionData.publicPath)
        }

        let collectionData: MetadataViews.NFTCollectionData = BBxBarbiePack.resolveContractView(resourceType: nil, viewType: Type<MetadataViews.NFTCollectionData>()) as! MetadataViews.NFTCollectionData?
            ?? panic("ViewResolver does not resolve NFTCollectionData view")
        
        // borrow reference to pack owner's collection
        self.collectionRef = acct.storage.borrow<auth(NonFungibleToken.Withdraw) &BBxBarbiePack.Collection>(from: collectionData.storagePath) ?? panic("Account does not store an oject at the specified path")

        self.packToRedeem <- self.collectionRef.withdraw(withdrawID: packID)

    }
    execute {
        // Call public redeem method
        BBxBarbiePM.publicRedeemPack(address: self.address, pack: <-self.packToRedeem, packHash: packHash)
    }
}
 
```