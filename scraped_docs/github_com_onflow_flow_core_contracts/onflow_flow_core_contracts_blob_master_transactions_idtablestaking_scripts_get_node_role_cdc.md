# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/idTableStaking/scripts/get_node_role.cdc

```
import FlowIDTableStaking from "FlowIDTableStaking"

// This script returns the role of a node

access(all) fun main(nodeID: String): UInt8 {
    let nodeInfo = FlowIDTableStaking.NodeInfo(nodeID: nodeID)
    return nodeInfo.role
}
```