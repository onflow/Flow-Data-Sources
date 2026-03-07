# Source: https://github.com/blocto/flow-transactions/blob/main/build/TheFootballClub/removeListing.mainnet.cdc

```
import NFTStorefront from 0x4eb8a10cb9f87357

/*
    Removes a listing from an account's storefront
*/
transaction(listingResourceID: UInt64) {
    let storefront: &NFTStorefront.Storefront{NFTStorefront.StorefrontManager}

    prepare(acct: AuthAccount) {
        self.storefront = acct.borrow<&NFTStorefront.Storefront{NFTStorefront.StorefrontManager}>(from: NFTStorefront.StorefrontStoragePath)
            ?? panic("Missing or mis-typed NFTStorefront.Storefront")
    }

    execute {
        self.storefront.removeListing(listingResourceID: listingResourceID)
    }
}
```