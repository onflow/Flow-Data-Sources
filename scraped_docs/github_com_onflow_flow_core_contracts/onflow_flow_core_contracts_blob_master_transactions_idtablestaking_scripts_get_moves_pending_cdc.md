# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/idTableStaking/scripts/get_moves_pending.cdc

```
import "FlowIDTableStaking"

// This script returns the current moves pending list

access(all) fun main(): {String: {UInt32: Bool}} {
    return FlowIDTableStaking.getMovesPendingList()!
}
```