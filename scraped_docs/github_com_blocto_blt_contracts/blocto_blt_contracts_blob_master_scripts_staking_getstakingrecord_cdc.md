# Source: https://github.com/blocto/blt-contracts/blob/master/scripts/staking/getStakingRecord.cdc

```
import BloctoTokenStaking from "../../contracts/flow/staking/BloctoTokenStaking.cdc"

pub fun main(stakerID: UInt64): UFix64 {
    return BloctoTokenStaking.getStakerBalance(stakerID: stakerID)
}

```