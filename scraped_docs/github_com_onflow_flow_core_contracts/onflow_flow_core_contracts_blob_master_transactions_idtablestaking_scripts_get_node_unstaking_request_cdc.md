# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/idTableStaking/scripts/get_node_unstaking_request.cdc

```
import "FlowIDTableStaking"

// This script returns the requested unstaking amount for a node

access(all) fun main(nodeID: String): UFix64 {
    let nodeInfo = FlowIDTableStaking.NodeInfo(nodeID: nodeID)
    return nodeInfo.tokensRequestedToUnstake
}
```