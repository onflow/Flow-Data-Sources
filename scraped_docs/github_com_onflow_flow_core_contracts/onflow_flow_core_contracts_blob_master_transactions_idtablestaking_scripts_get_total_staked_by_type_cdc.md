# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/idTableStaking/scripts/get_total_staked_by_type.cdc

```
import "FlowIDTableStaking"

// This script returns the balance of staked tokens of a node

access(all) fun main(role: UInt8): UFix64 {
    let staked = FlowIDTableStaking.getTotalTokensStakedByNodeType()

    return staked[role]!
}
```