# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/idTableStaking/scripts/get_node_staking_key.cdc

```
import "FlowIDTableStaking"

// This script returns the staking Key of a node

access(all) fun main(nodeID: String): String {
    let nodeInfo = FlowIDTableStaking.NodeInfo(nodeID: nodeID)
    return nodeInfo.stakingKey
}
```