# Source: https://github.com/Outblock/FRW-scripts/blob/main/scripts/src/cadence/staking/get_node_info.cdc

```
import FlowIDTableStaking from 0xFlowIDTableStaking

access(all) fun main(nodeID: String): FlowIDTableStaking.NodeInfo {
  return FlowIDTableStaking.NodeInfo(nodeID: nodeID)
}
```