# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/idTableStaking/scripts/get_role_counts.cdc

```
import "FlowIDTableStaking"

// This script returns the slot limits for node roles

access(all) fun main(): {UInt8: UInt16} {
    return FlowIDTableStaking.getCurrentRoleNodeCounts()
}
```