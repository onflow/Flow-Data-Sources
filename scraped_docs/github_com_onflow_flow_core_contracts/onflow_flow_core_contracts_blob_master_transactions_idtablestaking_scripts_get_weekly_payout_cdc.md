# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/idTableStaking/scripts/get_weekly_payout.cdc

```
import FlowIDTableStaking from "FlowIDTableStaking"

// This script returns the balance of staked tokens of a node

access(all) fun main(): UFix64 {
    return FlowIDTableStaking.getEpochTokenPayout()
}
```