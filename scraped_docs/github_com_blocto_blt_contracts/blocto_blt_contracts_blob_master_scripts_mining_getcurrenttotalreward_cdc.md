# Source: https://github.com/blocto/blt-contracts/blob/master/scripts/mining/getCurrentTotalReward.cdc

```
import BloctoTokenMining from "../../contracts/flow/mining/BloctoTokenMining.cdc"

pub fun main(): UFix64 {
    return BloctoTokenMining.getCurrentTotalReward()
}

```