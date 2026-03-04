# Source: https://github.com/Flowtyio/nft-catalog/blob/main/cadence/scripts/get_nft_catalog_identifiers.cdc

```
import "NFTCatalog"

access(all) fun main(): [String] {
    return NFTCatalog.getCatalogKeys()
}
 
```