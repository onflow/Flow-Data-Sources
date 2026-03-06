# Source: https://github.com/blocto/blt-contracts/blob/master/scripts/mining/getUserRewards.cdc

```
import BloctoTokenMining from "../../contracts/flow/mining/BloctoTokenMining.cdc"

pub fun main(): {Address: UFix64} {
    return BloctoTokenMining.getUserRewards()
}

```