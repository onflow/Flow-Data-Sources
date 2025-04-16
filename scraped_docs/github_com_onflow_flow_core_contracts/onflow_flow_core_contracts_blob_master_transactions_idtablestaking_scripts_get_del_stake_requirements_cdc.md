# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/idTableStaking/scripts/get_del_stake_requirements.cdc

```
import "FlowIDTableStaking"

// This script returns the minimum stake requirement for delegators

access(all) fun main(): UFix64 {
    return FlowIDTableStaking.getDelegatorMinimumStakeRequirement()
}
```