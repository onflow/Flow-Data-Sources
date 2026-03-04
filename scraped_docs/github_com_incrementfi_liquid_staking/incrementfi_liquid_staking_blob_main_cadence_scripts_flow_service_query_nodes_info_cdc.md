# Source: https://github.com/IncrementFi/Liquid-Staking/blob/main/cadence/scripts/flow-service/query_nodes_info.cdc

```
import FlowEpoch from "../../contracts/standard/mainnet/FlowEpoch.cdc"
import FlowIDTableStaking from "../../contracts/standard/mainnet/FlowIDTableStaking.cdc"

access(all) struct NodeInfo {
    access(all) let id: String
    access(all) let role: UInt8
    access(all) let networkingAddress: String
    //access(all) let tokensStaked: UFix64
    //access(all) let tokensCommitted: UFix64
    //access(all) let tokensUnstaking: UFix64
    //access(all) let tokensUnstaked: UFix64
    //access(all) let tokensRewarded: UFix64

    // list of delegator IDs for this node operator
    //access(all) let delegatorIDCounter: UInt32
    //access(all) let tokensRequestedToUnstake: UFix64
    //access(all) let initialWeight: UInt64
    init(_ nodeInfo:FlowIDTableStaking.NodeInfo) {
        self.id = nodeInfo.id
        self.role = nodeInfo.role
        self.networkingAddress = nodeInfo.networkingAddress       
    }
}

access(all) fun main(): AnyStruct {
    // current nodes can be staked
    let nodeIds = FlowIDTableStaking.getNodeIDs();
    let nodeInfos: {Int: FlowIDTableStaking.NodeInfo} = {}
    var index = 0;
    for nodeId in nodeIds {
        let nodeInfo = FlowIDTableStaking.NodeInfo(nodeID: nodeId)
        if nodeInfo.role > 4 {
            continue
        }

        nodeInfos[index] = nodeInfo // NodeInfo(nodeInfo)
        
        index = index + 1
    }
    return nodeInfos
}
```