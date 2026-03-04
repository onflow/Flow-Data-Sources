# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/bbxb/scripts/global_read_listing_details.cdc

```
import "NFTStorefrontV2"

/// This script returns the details for a listing within a storefront

access(all) fun main(account: Address, listingResourceID: UInt64): NFTStorefrontV2.ListingDetails {
    let storefrontRef: &{NFTStorefrontV2.StorefrontPublic} = getAccount(account).capabilities.borrow<&{NFTStorefrontV2.StorefrontPublic}>(
            NFTStorefrontV2.StorefrontPublicPath
        ) ?? panic("Could not borrow public storefront from address")
    let listing: &{NFTStorefrontV2.ListingPublic} = storefrontRef.borrowListing(listingResourceID: listingResourceID)
        ?? panic("No listing with that ID")
    
    return listing.getDetails()
}

// - storefrontAddress (Address): 0x56da62d87aaf2736
// - listingResourceID (UInt64): 162769657
// - nftType (Type): Type<A.6d0f55821f6b2dbe.BBxBarbieCard.NFT>()
// - nftUUID (UInt64): 160717594
// - nftID (UInt64): 318
// - salePaymentVaultType (Type): Type<A.7e60df042a9c0868.FlowToken.Vault>()
// - salePrice (UFix64): 10.00000000
// - customID (String?): "CustomID Goes here"
// - commissionAmount (UFix64): 0.03000000
// - commissionReceivers (?): [0x56da62d87aaf2736]
// - expiry (UInt64): 1689293699
```