# Source: https://github.com/onflow/nft-catalog/blob/main/cadence/scripts/get_nft_catalog_identifiers.cdc

```
import "NFTCatalog"

access(all) fun main(): [String] {
    return NFTCatalog.getCatalogKeys()
}
 
```