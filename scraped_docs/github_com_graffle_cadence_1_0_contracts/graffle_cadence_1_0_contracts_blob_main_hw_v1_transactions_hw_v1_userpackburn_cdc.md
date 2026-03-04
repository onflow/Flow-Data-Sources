# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/hw_v1/transactions/hw_v1_userPackBurn.cdc

```
import NonFungibleToken from "../contracts/utility/NonFungibleToken.cdc"
import MetadataViews from "../contracts/utility/MetadataViews.cdc"
import HWGaragePack from "../contracts/HWGaragePack.cdc"

transaction(packIDs: [UInt64]) {
    
    prepare(acct: AuthAccount) {
        // Setup collection if they aren't already setup
        if acct.borrow<&HWGaragePack.Collection>(from: HWGaragePack.CollectionStoragePath) == nil {
            let collection <- HWGaragePack.createEmptyCollection()
            acct.save(<-collection, to: HWGaragePack.CollectionStoragePath)
        }
        if acct.getCapability<&HWGaragePack.Collection{NonFungibleToken.CollectionPublic, NonFungibleToken.Receiver, HWGaragePack.PackCollectionPublic, MetadataViews.ResolverCollection}>(HWGaragePack.CollectionPublicPath).borrow() == nil {
            acct.link<&HWGaragePack.Collection{NonFungibleToken.CollectionPublic, NonFungibleToken.Receiver, HWGaragePack.PackCollectionPublic, MetadataViews.ResolverCollection}>(HWGaragePack.CollectionPublicPath, target: HWGaragePack.CollectionStoragePath)
        }
        for packID in packIDs {
            let packInstance <- acct.borrow<&{NonFungibleToken.Provider}>(from: HWGaragePack.CollectionStoragePath)!.withdraw(withdrawID: packID) as! @HWGaragePack.NFT
            destroy packInstance
        }
    }

    execute {        
    }
}
 
```