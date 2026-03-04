# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/hw_v1/transactions/hw_v1_userCardBurn.cdc

```
import NonFungibleToken from "../contracts/utility/NonFungibleToken.cdc"
import MetadataViews from "../contracts/utility/MetadataViews.cdc"
import HWGarageCard from "../contracts/HWGarageCard.cdc"

transaction(cardIDs: [UInt64]) {
    
    prepare(acct: AuthAccount) {
        // Setup collection if they aren't already setup
        if acct.borrow<&HWGarageCard.Collection>(from: HWGarageCard.CollectionStoragePath) == nil {
            let collection <- HWGarageCard.createEmptyCollection()
            acct.save(<-collection, to: HWGarageCard.CollectionStoragePath)
        }
        if acct.getCapability<&HWGarageCard.Collection{NonFungibleToken.CollectionPublic, NonFungibleToken.Receiver, HWGarageCard.HWGarageCardCollectionPublic, MetadataViews.ResolverCollection}>(HWGarageCard.CollectionPublicPath).borrow() == nil {
            acct.link<&HWGarageCard.Collection{NonFungibleToken.CollectionPublic, NonFungibleToken.Receiver, HWGarageCard.HWGarageCardCollectionPublic, MetadataViews.ResolverCollection}>(HWGarageCard.CollectionPublicPath, target: HWGarageCard.CollectionStoragePath)
        }
        for cardID in cardIDs {
            let cardInstance <- acct.borrow<&{NonFungibleToken.Provider}>(from: HWGarageCard.CollectionStoragePath)!.withdraw(withdrawID: cardID) as! @HWGarageCard.NFT
            destroy cardInstance
        }  
    }

    execute {        
    }
}
 
```