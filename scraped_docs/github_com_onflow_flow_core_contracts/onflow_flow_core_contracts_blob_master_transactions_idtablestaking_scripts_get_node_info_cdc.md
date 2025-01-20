# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/idTableStaking/scripts/get_node_info.cdc

```
import FlowIDTableStaking from "FlowIDTableStaking"

// This script gets all the info about a node and returns it

access(all) fun main(nodeID: String): FlowIDTableStaking.NodeInfo {
    return FlowIDTableStaking.NodeInfo(nodeID: nodeID)
}

```