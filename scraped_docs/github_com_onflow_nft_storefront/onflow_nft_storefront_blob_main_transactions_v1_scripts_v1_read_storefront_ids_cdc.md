# Source: https://github.com/onflow/nft-storefront/blob/main/transactions-v1/scripts-v1/read_storefront_ids.cdc

```
import "NFTStorefront"

/// This script returns an array of all the Listing IDs for sale through a Storefront
///
access(all) fun main(account: Address): [UInt64] {
    return getAccount(account).capabilities.borrow<&{NFTStorefront.StorefrontPublic}>(
            NFTStorefront.StorefrontPublicPath
        )?.getListingIDs()
        ?? panic("Could not borrow public storefront from address")
}

```