# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/idTableStaking/scripts/get_proposed_table.cdc

```
import "FlowIDTableStaking"

// This script returns the current identity table length

access(all) fun main(): [String] {
    return FlowIDTableStaking.getProposedNodeIDs()
}
```