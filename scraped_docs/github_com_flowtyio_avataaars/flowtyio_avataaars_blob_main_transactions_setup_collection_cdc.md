# Source: https://github.com/Flowtyio/avataaars/blob/main/transactions/setup_collection.cdc

```
import "Avataaars"
import "NonFungibleToken"
import "MetadataViews"

transaction {
    prepare(acct: AuthAccount) {
        if acct.borrow<&AnyResource>(from: Avataaars.CollectionStoragePath) == nil {
            let c <- Avataaars.createEmptyCollection()
            acct.save(<-c, to: Avataaars.CollectionStoragePath)
        }

        acct.unlink(Avataaars.CollectionPublicPath)
        acct.unlink(Avataaars.CollectionProviderPath)

        acct.link<&Avataaars.Collection{Avataaars.AvataaarsCollectionPublic, NonFungibleToken.CollectionPublic, MetadataViews.ResolverCollection}>(Avataaars.CollectionPublicPath, target: Avataaars.CollectionStoragePath)
        acct.link<&Avataaars.Collection{Avataaars.AvataaarsCollectionPublic, NonFungibleToken.CollectionPublic, MetadataViews.ResolverCollection, NonFungibleToken.Provider}>(Avataaars.CollectionProviderPath, target: Avataaars.CollectionStoragePath)
    }
}
```