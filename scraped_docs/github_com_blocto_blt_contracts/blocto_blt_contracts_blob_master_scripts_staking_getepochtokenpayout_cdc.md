# Source: https://github.com/blocto/blt-contracts/blob/master/scripts/staking/getEpochTokenPayout.cdc

```
import "BloctoTokenStaking"

access(all)
fun main(): UFix64 {
  return BloctoTokenStaking.getEpochTokenPayout()
}

```