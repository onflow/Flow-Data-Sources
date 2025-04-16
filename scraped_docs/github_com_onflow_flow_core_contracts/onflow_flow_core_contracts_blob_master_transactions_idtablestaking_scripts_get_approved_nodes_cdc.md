# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/idTableStaking/scripts/get_approved_nodes.cdc

```
import "FlowIDTableStaking"

// This script returns the current approved list

access(all) fun main(): [String] {
    let approveList = FlowIDTableStaking.getApprovedList()
        ?? panic("Could not read approved list from storage")

    return approveList.keys
}
```