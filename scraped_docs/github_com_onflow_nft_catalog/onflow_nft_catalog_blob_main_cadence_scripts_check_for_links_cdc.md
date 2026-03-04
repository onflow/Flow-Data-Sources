# Source: https://github.com/onflow/nft-catalog/blob/main/cadence/scripts/check_for_links.cdc

```
import "MetadataViews"

/*
    Script to check for the implementation of all recommended MetadataViews.
 */
access(all) fun main(ownerAddress: Address, collectionPublicPath: String): {String: Bool} {
    let owner = getAccount(ownerAddress)
    return { 
        "MetadataViews": owner.getCapability<&AnyResource{MetadataViews.ResolverCollection}>(PublicPath(identifier: collectionPublicPath)!).check(),
        "AnyResource": owner.getCapability<&AnyResource>(PublicPath(identifier: collectionPublicPath)!).check()
    }
}
```