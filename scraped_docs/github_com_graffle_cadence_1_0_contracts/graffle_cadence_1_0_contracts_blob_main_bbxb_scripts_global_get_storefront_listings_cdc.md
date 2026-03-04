# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/bbxb/scripts/global_get_storefront_listings.cdc

```
import "NFTStorefrontV2"

// This script returns an array of all the nft uuids for sale through a Storefront

access(all) fun main(account: Address): [UInt64] {
    return getAccount(account).capabilities.borrow<&{NFTStorefrontV2.StorefrontPublic}>(
            NFTStorefrontV2.StorefrontPublicPath
        )?.getListingIDs()
        ?? panic("Could not borrow public storefront from address")
}
```