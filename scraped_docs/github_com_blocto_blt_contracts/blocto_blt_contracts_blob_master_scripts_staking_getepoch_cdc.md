# Source: https://github.com/blocto/blt-contracts/blob/master/scripts/staking/getEpoch.cdc

```
import "BloctoTokenStaking"

access(all)
fun main(): UInt64 {
    return BloctoTokenStaking.getEpoch()
}

```