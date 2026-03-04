# Source: https://github.com/emerald-dao/float/blob/main/src/flow/cadence/scripts/has_float_collection_setup.cdc

```
import "FLOAT"
import "NonFungibleToken"

access(all) fun main(user: Address): Bool {
  return getAccount(user).capabilities.borrow<&FLOAT.Collection>(FLOAT.FLOATCollectionPublicPath) != nil
}
```