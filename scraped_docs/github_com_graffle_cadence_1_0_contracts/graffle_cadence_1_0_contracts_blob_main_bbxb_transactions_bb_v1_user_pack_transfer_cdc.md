# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/bbxb/transactions/bb_v1_user_pack_transfer.cdc

```
import "NonFungibleToken"
import "MetadataViews"
import "BBxBarbiePack"

transaction(
    packEditionID: UInt64
    , to: Address
    ) {

    prepare(acct: auth(BorrowValue, IssueStorageCapabilityController, PublishCapability, SaveValue, UnpublishCapability) &Account) {
        // Setup Card Collection
        let cardCollectionData: MetadataViews.NFTCollectionData = BBxBarbiePack.resolveContractView(resourceType: nil, viewType: Type<MetadataViews.NFTCollectionData>()) as! MetadataViews.NFTCollectionData?
            ?? panic("ViewResolver does not resolve NFTCollectionData view")

        // exit if cardCollection exists
        if acct.storage.borrow<&BBxBarbiePack.Collection>(from: cardCollectionData.storagePath) == nil {
            // create a new empty cardCollection for BBxBarbiePack
            let cardCollection: @{NonFungibleToken.Collection} <- BBxBarbiePack.createEmptyCollection(nftType: Type<@BBxBarbiePack.NFT>())

            // save BBxBarbiePack cardCollection to the account
            acct.storage.save(<-cardCollection, to: cardCollectionData.storagePath)

            // create a public capability for the BBxBarbiePack cardCollection
            acct.capabilities.unpublish(cardCollectionData.publicPath) // remove any current pubCap 
            let cardCollectionCap: Capability<&BBxBarbiePack.Collection> = acct.capabilities.storage.issue<&BBxBarbiePack.Collection>(cardCollectionData.storagePath)
            acct.capabilities.publish(cardCollectionCap, at: cardCollectionData.publicPath)
        }

        let packToTransfer: @BBxBarbiePack.NFT <-acct.storage.borrow<auth(NonFungibleToken.Withdraw) &{NonFungibleToken.Provider}>(from: BBxBarbiePack.CollectionStoragePath)!.withdraw(withdrawID: packEditionID) as! @BBxBarbiePack.NFT
        BBxBarbiePack.transfer(uuid: packToTransfer.uuid, id: packToTransfer.id, packSeriesId: packToTransfer.packSeriesID, packEditionId: packToTransfer.packEditionID,  toAddress: to)
        getAccount(to).capabilities.get<&{NonFungibleToken.Receiver}>(BBxBarbiePack.CollectionPublicPath).borrow()!.deposit(token: <-packToTransfer)

    }
    execute {
    }
}
 
```