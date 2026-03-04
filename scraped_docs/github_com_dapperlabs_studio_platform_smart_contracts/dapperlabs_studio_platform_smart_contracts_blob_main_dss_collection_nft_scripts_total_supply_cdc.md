# Source: https://github.com/dapperlabs/studio-platform-smart-contracts/blob/main/dss-collection-nft/scripts/total_supply.cdc

```
import DSSCollection from "../../contracts/DSSCollection.cdc"

pub fun main(): UInt64 {
    return DSSCollection.totalSupply
}
```