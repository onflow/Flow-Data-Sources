# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/bbxb/transactions/bb_v1_user_card_transfer.cdc

```
import "NonFungibleToken"
import "MetadataViews"
import "BBxBarbieCard"

transaction(
    cardEditionID: UInt64
    , to: Address
    ) {

    prepare(acct: auth(BorrowValue, IssueStorageCapabilityController, PublishCapability, SaveValue, UnpublishCapability) &Account) {
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

        let cardToTransfer: @BBxBarbieCard.NFT <-acct.storage.borrow<auth(NonFungibleToken.Withdraw) &{NonFungibleToken.Provider}>(from: BBxBarbieCard.CollectionStoragePath)!.withdraw(withdrawID: cardEditionID) as! @BBxBarbieCard.NFT
        BBxBarbieCard.transfer(uuid: cardToTransfer.uuid, id: cardToTransfer.id, packSeriesId: cardToTransfer.packSeriesID, cardEditionId: cardToTransfer.cardEditionID,  toAddress: to)
        getAccount(to).capabilities.get<&{NonFungibleToken.Receiver}>(BBxBarbieCard.CollectionPublicPath).borrow()!.deposit(token: <-cardToTransfer)

    }
    execute {
    }
}
 
```