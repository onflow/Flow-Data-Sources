# Source: https://github.com/IncrementFi/Liquid-Staking/blob/main/cadence/scripts/flow-service/query_nodes_not_in_approved.cdc

```
import FlowEpoch from "../../contracts/standard/mainnet/FlowEpoch.cdc"
import FlowIDTableStaking from "../../contracts/standard/mainnet/FlowIDTableStaking.cdc"

access(all) struct NodeInfo {
    access(all) let id: String
    access(all) let role: UInt8
    access(all) let networkingAddress: String
    access(all) let networkingKey: String
    access(all) let stakingKey: String

    access(all) let tokensStaked: UFix64
    //access(all) let tokensCommitted: UFix64
    //access(all) let tokensUnstaking: UFix64
    //access(all) let tokensUnstaked: UFix64
    //access(all) let tokensRewarded: UFix64

    ///// list of delegator IDs for this node operator
    access(all) let delegatorIDCounter: UInt32
    access(all) let delegatorStaked: UFix64
    //access(all) let tokensRequestedToUnstake: UFix64
    //access(all) let initialWeight: UInt64
    init(_ nodeInfo:FlowIDTableStaking.NodeInfo) {
        self.id = nodeInfo.id
        self.role = nodeInfo.role
        self.networkingAddress = nodeInfo.networkingAddress
        self.networkingKey = nodeInfo.networkingKey
        self.stakingKey = nodeInfo.stakingKey
        
        self.tokensStaked = nodeInfo.tokensStaked
        self.delegatorIDCounter = nodeInfo.delegatorIDCounter
        self.delegatorStaked = nodeInfo.totalStakedWithDelegators() - self.tokensStaked

        //self.tokensRewarded = nodeInfo.tokensRewarded
    }
}

access(all) fun main(): AnyStruct {
    // nodes not in approved list
    let stakedNodeIds = FlowIDTableStaking.getStakedNodeIDs();
    let nodeIds = FlowIDTableStaking.getNodeIDs();
    let nodeInfos: {Int: NodeInfo} = {}
    var index = 0;
    var totalDelegatorStaked = 0.0
    for nodeId in nodeIds {
        if stakedNodeIds.contains(nodeId) {
            //continue
        }
        let nodeInfo = FlowIDTableStaking.NodeInfo(nodeID: nodeId)

        if nodeInfo.tokensStaked == 0.0 {
            continue
        }
        
        nodeInfos[index] = NodeInfo(nodeInfo)
        totalDelegatorStaked = totalDelegatorStaked + nodeInfos[index]!.delegatorStaked
        index = index + 1
    }
    return totalDelegatorStaked
}
```