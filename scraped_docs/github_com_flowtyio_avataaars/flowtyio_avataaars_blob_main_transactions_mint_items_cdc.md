# Source: https://github.com/Flowtyio/avataaars/blob/main/transactions/mint_items.cdc

```
import Avataaars from 0xf8d6e0586b0a20c7
import NonFungibleToken from 0xf8d6e0586b0a20c7
import MetadataViews from 0xf8d6e0586b0a20c7

transaction(quantity: Int) {
    prepare(acct: AuthAccount) {
        if acct.borrow<&AnyResource>(from: Avataaars.CollectionStoragePath) == nil {
            let c <- Avataaars.createEmptyCollection()
            acct.save(<-c, to: Avataaars.CollectionStoragePath)
        }

        acct.unlink(Avataaars.CollectionPublicPath)
        acct.unlink(Avataaars.CollectionProviderPath)

        acct.link<&Avataaars.Collection{Avataaars.AvataaarsCollectionPublic, NonFungibleToken.CollectionPublic, MetadataViews.ResolverCollection}>(Avataaars.CollectionPublicPath, target: Avataaars.CollectionStoragePath)
        acct.link<&Avataaars.Collection{Avataaars.AvataaarsCollectionPublic, NonFungibleToken.CollectionPublic, MetadataViews.ResolverCollection, NonFungibleToken.Provider}>(Avataaars.CollectionProviderPath, target: Avataaars.CollectionStoragePath)

        let collection = acct.borrow<&Avataaars.Collection>(from: Avataaars.CollectionStoragePath)!

        let minter = Avataaars.borrowMinter()
        
        var count = 0
        while count < quantity {
            count = count + 1
            minter.mintNFT(recipient: collection)
        }
    }
}
```