# Source: https://github.com/emerald-dao/project-toucans-v2/blob/master/frontend/src/flow/cadence/scripts/get_catalog_keys.cdc

```
import NFTCatalog from "../utility/NFTCatalog.cdc"

access(all) fun main(): [String] {
  return NFTCatalog.getCatalogKeys()
}
```