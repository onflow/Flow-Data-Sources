# Source: https://github.com/onflow/nft-storefront/blob/main/transactions-v1/cleanup_item.cdc

```
import "NFTStorefront"

transaction(listingResourceID: UInt64, storefrontAddress: Address) {

    let storefront: &{NFTStorefront.StorefrontPublic}

    prepare(acct: &Account) {
        self.storefront = getAccount(storefrontAddress).capabilities.borrow<&{NFTStorefront.StorefrontPublic}>(
                NFTStorefront.StorefrontPublicPath
            ) ?? panic("Could not borrow Storefront from provided address")
    }

    execute {
        // Be kind and recycle
        self.storefront.cleanup(listingResourceID: listingResourceID)
    }

    post {
        self.storefront.getListingIDs().contains(listingResourceID) == false:
            "Listing was not successfully removed"
    }
}

```