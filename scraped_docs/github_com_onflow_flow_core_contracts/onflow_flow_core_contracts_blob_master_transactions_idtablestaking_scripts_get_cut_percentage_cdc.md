# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/idTableStaking/scripts/get_cut_percentage.cdc

```
import FlowIDTableStaking from "FlowIDTableStaking"

// This script returns the balance of staked tokens of a node

access(all) fun main(): UFix64 {
    return FlowIDTableStaking.getRewardCutPercentage()
}
```