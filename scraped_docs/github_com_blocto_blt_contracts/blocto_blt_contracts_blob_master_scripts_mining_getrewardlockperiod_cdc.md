# Source: https://github.com/blocto/blt-contracts/blob/master/scripts/mining/getRewardLockPeriod.cdc

```
import BloctoTokenMining from "../../contracts/flow/mining/BloctoTokenMining.cdc"

pub fun main(): UInt64 {
    return BloctoTokenMining.getRewardLockPeriod()
}

```