# Source: https://github.com/onflow/nft-storefront/blob/main/scripts/read_listing_details.cdc

```
import NFTStorefrontV2 from "../contracts/NFTStorefrontV2.cdc"

/// This script returns the details for a listing within a storefront
///
access(all) fun main(account: Address, listingResourceID: UInt64): NFTStorefrontV2.ListingDetails {
    let storefrontRef = getAccount(account).capabilities.borrow<&{NFTStorefrontV2.StorefrontPublic}>(
            NFTStorefrontV2.StorefrontPublicPath
        ) ?? panic("Could not borrow public storefront from address")
    let listing = storefrontRef.borrowListing(listingResourceID: listingResourceID)
        ?? panic("No listing with that ID")
    
    return listing.getDetails()
}

```