# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/idTableStaking/scripts/get_node_rewarded_tokens.cdc

```
import "FlowIDTableStaking"

// This script returns the balance of rewarded tokens of a node

access(all) fun main(nodeID: String): UFix64 {
    let nodeInfo = FlowIDTableStaking.NodeInfo(nodeID: nodeID)
    return nodeInfo.tokensRewarded
}
```