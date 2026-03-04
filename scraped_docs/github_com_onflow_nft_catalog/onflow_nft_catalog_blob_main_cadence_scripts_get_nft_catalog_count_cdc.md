# Source: https://github.com/onflow/nft-catalog/blob/main/cadence/scripts/get_nft_catalog_count.cdc

```
import "NFTCatalog"

access(all) fun main(): Int {
    let catalogKeys = NFTCatalog.getCatalogKeys()
    return catalogKeys.length
}
```