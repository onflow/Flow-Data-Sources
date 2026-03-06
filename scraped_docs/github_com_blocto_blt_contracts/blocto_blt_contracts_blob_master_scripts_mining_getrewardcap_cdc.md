# Source: https://github.com/blocto/blt-contracts/blob/master/scripts/mining/getRewardCap.cdc

```
import BloctoTokenMining from "../../contracts/flow/mining/BloctoTokenMining.cdc"

pub fun main(): UFix64 {
    return BloctoTokenMining.getRewardCap()
}

```