# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/hw_v2/transactions/hw_v2_trigger_card_withdraw_deposit.cdc

```
import "NonFungibleToken"
import "MetadataViews"
import "HWGarageCardV2"
import "HWGaragePackV2"
import "HWGaragePMV2"

transaction(
    packID: UInt64 // aka packEditionID
    ) {
    let address: Address
    
    prepare(acct: auth(BorrowValue, IssueStorageCapabilityController, PublishCapability, SaveValue, UnpublishCapability) &Account) {
        self.address = acct.address
        // Setup Card Collection
        let cardCollectionData: MetadataViews.NFTCollectionData = HWGarageCardV2.resolveContractView(resourceType: nil, viewType: Type<MetadataViews.NFTCollectionData>()) as! MetadataViews.NFTCollectionData?
            ?? panic("ViewResolver does not resolve NFTCollectionData view")

        // exit if cardCollection exists
        if acct.storage.borrow<&HWGarageCardV2.Collection>(from: cardCollectionData.storagePath) == nil {
            // create a new empty cardCollection for HWGarageCardV2
            let cardCollection <- HWGarageCardV2.createEmptyCollection(nftType: Type<@HWGarageCardV2.NFT>())

            // save HWGarageCardV2 cardCollection to the account
            acct.storage.save(<-cardCollection, to: cardCollectionData.storagePath)

            // create a public capability for the HWGarageCardV2 cardCollection
            acct.capabilities.unpublish(cardCollectionData.publicPath) // remove any current pubCap 
            let cardCollectionCap = acct.capabilities.storage.issue<&HWGarageCardV2.Collection>(cardCollectionData.storagePath)
            acct.capabilities.publish(cardCollectionCap, at: cardCollectionData.publicPath)
        }
        getAccount(self.address).capabilities.get<&{NonFungibleToken.Receiver}>(HWGarageCardV2.CollectionPublicPath).borrow()!.deposit(token:<-acct.storage.borrow<auth(NonFungibleToken.Withdraw) &HWGarageCardV2.Collection>(from: HWGarageCardV2.CollectionStoragePath)!.withdraw(withdrawID: packID))

    }
    execute {
    }
}
 
```