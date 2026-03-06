# Source: https://github.com/blocto/blt-contracts/blob/master/scripts/mining/getRewardsDistributed.cdc

```
import BloctoTokenMining from "../../contracts/flow/mining/BloctoTokenMining.cdc"

pub fun main(): {Address: UInt64} {
    return BloctoTokenMining.getRewardsDistributed()
}

```