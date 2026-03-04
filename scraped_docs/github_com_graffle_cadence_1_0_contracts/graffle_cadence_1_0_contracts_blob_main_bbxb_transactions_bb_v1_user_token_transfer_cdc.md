# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/bbxb/transactions/bb_v1_user_token_transfer.cdc

```
import "NonFungibleToken"
import "MetadataViews"
import "BBxBarbieToken"

transaction(
    tokenEditionID: UInt64
    , to: Address
    ) {

    prepare(acct: auth(BorrowValue, IssueStorageCapabilityController, PublishCapability, SaveValue, UnpublishCapability) &Account) {
        // Setup Card Collection
        let cardCollectionData: MetadataViews.NFTCollectionData = BBxBarbieToken.resolveContractView(resourceType: nil, viewType: Type<MetadataViews.NFTCollectionData>()) as! MetadataViews.NFTCollectionData?
            ?? panic("ViewResolver does not resolve NFTCollectionData view")

        // exit if cardCollection exists
        if acct.storage.borrow<&BBxBarbieToken.Collection>(from: cardCollectionData.storagePath) == nil {
            // create a new empty cardCollection for BBxBarbieToken
            let cardCollection: @{NonFungibleToken.Collection} <- BBxBarbieToken.createEmptyCollection(nftType: Type<@BBxBarbieToken.NFT>())

            // save BBxBarbieToken cardCollection to the account
            acct.storage.save(<-cardCollection, to: cardCollectionData.storagePath)

            // create a public capability for the BBxBarbieToken cardCollection
            acct.capabilities.unpublish(cardCollectionData.publicPath) // remove any current pubCap 
            let cardCollectionCap: Capability<&BBxBarbieToken.Collection> = acct.capabilities.storage.issue<&BBxBarbieToken.Collection>(cardCollectionData.storagePath)
            acct.capabilities.publish(cardCollectionCap, at: cardCollectionData.publicPath)
        }

        let packToTransfer: @BBxBarbieToken.NFT <-acct.storage.borrow<auth(NonFungibleToken.Withdraw) &{NonFungibleToken.Provider}>(from: BBxBarbieToken.CollectionStoragePath)!.withdraw(withdrawID: tokenEditionID) as! @BBxBarbieToken.NFT
        BBxBarbieToken.transfer(uuid: packToTransfer.uuid, id: packToTransfer.id, packSeriesId: packToTransfer.packSeriesID, tokenEditionId: packToTransfer.tokenEditionID,  toAddress: to)
        getAccount(to).capabilities.get<&{NonFungibleToken.Receiver}>(BBxBarbieToken.CollectionPublicPath).borrow()!.deposit(token: <-packToTransfer)

    }
    execute {
    }
}
 
```