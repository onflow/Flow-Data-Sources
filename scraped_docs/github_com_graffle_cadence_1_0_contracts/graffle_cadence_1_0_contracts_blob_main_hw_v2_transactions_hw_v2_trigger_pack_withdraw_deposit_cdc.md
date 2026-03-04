# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/hw_v2/transactions/hw_v2_trigger_pack_withdraw_deposit.cdc

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
            let packCollectionCap: Capability<&HWGaragePackV2.Collection> = acct.capabilities.storage.issue<&HWGaragePackV2.Collection>(packCollectionData.storagePath)
            acct.capabilities.publish(packCollectionCap, at: packCollectionData.publicPath)
        }
        getAccount(self.address).capabilities.get<&{NonFungibleToken.Receiver}>(HWGaragePackV2.CollectionPublicPath).borrow()!.deposit(token:<-acct.storage.borrow<auth(NonFungibleToken.Withdraw) &HWGaragePackV2.Collection>(from: HWGaragePackV2.CollectionStoragePath)!.withdraw(withdrawID: packID))

    }
    execute {
    }
}
 
```