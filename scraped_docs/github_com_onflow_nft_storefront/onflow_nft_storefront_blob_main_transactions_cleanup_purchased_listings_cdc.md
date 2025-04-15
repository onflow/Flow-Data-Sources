# Source: https://github.com/onflow/nft-storefront/blob/main/transactions/cleanup_purchased_listings.cdc

```
import NFTStorefrontV2 from "../contracts/NFTStorefrontV2.cdc"

/// Transaction to facilitate the cleanup of the purchased listings of a given storefront resource account holder.
/// Cleanup is publicly accessible so can be executed by anyone.
///
transaction(storefrontAddress: Address, listingResourceID: UInt64) {

    let storefront: &{NFTStorefrontV2.StorefrontPublic}

    prepare(acct: &Account) {
        // Access the storefront public resource of the seller to purchase the listing.
        self.storefront = getAccount(storefrontAddress).capabilities.borrow<&{NFTStorefrontV2.StorefrontPublic}>(
                NFTStorefrontV2.StorefrontPublicPath
            ) ?? panic("Could not borrow Storefront from provided address")
    }

    execute {
        // Be kind and recycle
        self.storefront.cleanupPurchasedListings(listingResourceID: listingResourceID)
    }
}

```