# Source: https://github.com/IncrementFi/Liquid-Staking/blob/main/cadence/scripts/flow-service/query_nodes_id.cdc

```
import FlowEpoch from "../../contracts/standard/mainnet/FlowEpoch.cdc"
import FlowIDTableStaking from "../../contracts/standard/mainnet/FlowIDTableStaking.cdc"

access(all) fun main(): AnyStruct {
    // current nodes can be staked
    let stakedNodeIds = FlowIDTableStaking.getStakedNodeIDs();
    let nodeIDs = FlowIDTableStaking.getNodeIDs();
    
    return [nodeIDs.length, stakedNodeIds.length]
}
```