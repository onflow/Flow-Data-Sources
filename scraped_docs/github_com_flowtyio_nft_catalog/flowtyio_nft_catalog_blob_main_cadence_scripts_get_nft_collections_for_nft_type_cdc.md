# Source: https://github.com/Flowtyio/nft-catalog/blob/main/cadence/scripts/get_nft_collections_for_nft_type.cdc

```
import "NFTCatalog"

access(all) fun main(nftTypeIdentifer: String): {String : Bool}? {
    return NFTCatalog.getCollectionsForType(nftTypeIdentifier: CompositeType(nftTypeIdentifer)!.identifier)
}
```