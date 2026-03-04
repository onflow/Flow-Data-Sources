# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/hw_v1/scripts/hw_v1_get_allowed_commission_receivers.cdc

```
import "NFTStorefrontV2"
import "FungibleToken"

// This script returns the list of allowed commission receivers supported by the given listing Id.
access(all) fun main(account: Address, listingResourceID: UInt64): [Capability<&{FungibleToken.Receiver}>]? {
    let storefrontRef: &NFTStorefrontV2.Storefront = getAccount(account)
        .capabilities.get<&NFTStorefrontV2.Storefront>(
            NFTStorefrontV2.StorefrontPublicPath
        )
        .borrow()
        ?? panic("Could not borrow public storefront from address")

    let listing: &{NFTStorefrontV2.ListingPublic} = storefrontRef.borrowListing(listingResourceID: listingResourceID)
        ?? panic("No item with that ID")
    
    return listing.getAllowedCommissionReceivers()
}
```