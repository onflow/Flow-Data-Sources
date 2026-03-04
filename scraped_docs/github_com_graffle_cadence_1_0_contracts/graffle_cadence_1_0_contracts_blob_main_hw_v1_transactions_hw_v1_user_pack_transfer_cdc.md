# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/hw_v1/transactions/hw_v1_user_pack_transfer.cdc

```
import NonFungibleToken from "../contracts/utility/NonFungibleToken.cdc"
import MetadataViews from "../contracts/utility/MetadataViews.cdc"
import HWGaragePack from "../contracts/HWGaragePack.cdc"


transaction(
    packEditionID: UInt64
    , to: Address
    ) {

    prepare(acct: AuthAccount) {
        // Setup card collection if they aren't already setup
        if acct.borrow<&HWGaragePack.Collection>(from: HWGaragePack.CollectionStoragePath) == nil {
            let collection: @NonFungibleToken.Collection <- HWGaragePack.createEmptyCollection()
            acct.save(<-collection, to: HWGaragePack.CollectionStoragePath)
        }
        if acct.getCapability<&HWGaragePack.Collection{NonFungibleToken.CollectionPublic, NonFungibleToken.Receiver, HWGaragePack.PackCollectionPublic, MetadataViews.ResolverCollection}>(HWGaragePack.CollectionPublicPath).borrow() == nil {
            acct.link<&HWGaragePack.Collection{NonFungibleToken.CollectionPublic, NonFungibleToken.Receiver, HWGaragePack.PackCollectionPublic, MetadataViews.ResolverCollection}>(HWGaragePack.CollectionPublicPath, target: HWGaragePack.CollectionStoragePath)
        }
        
        let packToTransfer: @HWGaragePack.NFT <-acct.borrow<&{NonFungibleToken.Provider}>(from: HWGaragePack.CollectionStoragePath)!.withdraw(withdrawID: packEditionID) as! @HWGaragePack.NFT
        let packToTransferRef: &HWGaragePack.NFT = &packToTransfer as! &HWGaragePack.NFT
        getAccount(to).getCapability<&{NonFungibleToken.Receiver}>(HWGaragePack.CollectionPublicPath).borrow()!.deposit(token: <-packToTransfer)
        HWGaragePack.transfer(uuid: packToTransferRef.uuid, id: packToTransferRef.id, packSeriesId: packToTransferRef.packID, packEditionId: packToTransferRef.packEditionID,  toAddress: to)

    }
    execute {
    }
}
 
```