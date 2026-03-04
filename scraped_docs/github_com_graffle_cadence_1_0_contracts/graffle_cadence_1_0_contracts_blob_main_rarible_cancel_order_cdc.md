# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/rarible/cancel-order.cdc

```
/*
    Cancel order
*/
import NFTStorefrontV2 from "NFTStorefrontV2"

transaction(listingResourceID: UInt64) {

    let storefront: auth(NFTStorefrontV2.RemoveListing) &{NFTStorefrontV2.StorefrontManager}

    prepare(acct: auth(BorrowValue) &Account) {
        self.storefront = acct.storage.borrow<auth(NFTStorefrontV2.RemoveListing) &NFTStorefrontV2.Storefront>(
                from: NFTStorefrontV2.StorefrontStoragePath
            ) ?? panic("Missing or mis-typed NFTStorefront.Storefront")
    }

    execute {
        self.storefront.removeListing(listingResourceID: listingResourceID)
    }
}

```