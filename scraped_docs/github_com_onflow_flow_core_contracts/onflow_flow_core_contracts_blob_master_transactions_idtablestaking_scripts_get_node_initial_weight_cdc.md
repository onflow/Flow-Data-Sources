# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/idTableStaking/scripts/get_node_initial_weight.cdc

```
import FlowIDTableStaking from "FlowIDTableStaking"

// This script returns the initial weight of a node

access(all) fun main(nodeID: String): UInt64 {
    let nodeInfo = FlowIDTableStaking.NodeInfo(nodeID: nodeID)
    return nodeInfo.initialWeight
}
```