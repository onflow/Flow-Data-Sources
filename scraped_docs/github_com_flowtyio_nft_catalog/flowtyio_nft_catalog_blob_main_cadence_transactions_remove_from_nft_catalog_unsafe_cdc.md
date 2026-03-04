# Source: https://github.com/Flowtyio/nft-catalog/blob/main/cadence/transactions/remove_from_nft_catalog_unsafe.cdc

```
import "MetadataViews"
import "NFTCatalog"
import "NFTCatalogAdmin"

transaction(
    collectionIdentifier : String,
    nftTypeIdentifier: String
) {
    let adminProxyRef: auth(NFTCatalogAdmin.CatalogActions) &NFTCatalogAdmin.AdminProxy

    prepare(acct: auth(BorrowValue) &Account) {
        self.adminProxyRef = acct.storage.borrow<auth(NFTCatalogAdmin.CatalogActions) &NFTCatalogAdmin.AdminProxy>(from : NFTCatalogAdmin.AdminProxyStoragePath)!
    }

    execute {     
        self.adminProxyRef.getCapability()!.borrow()!.removeCatalogEntryUnsafe(collectionIdentifier : collectionIdentifier, nftTypeIdentifier: nftTypeIdentifier)
    }
}
```