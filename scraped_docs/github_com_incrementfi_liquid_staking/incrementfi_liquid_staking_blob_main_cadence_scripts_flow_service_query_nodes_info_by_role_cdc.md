# Source: https://github.com/IncrementFi/Liquid-Staking/blob/main/cadence/scripts/flow-service/query_nodes_info_by_role.cdc

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
    access(all) let tokensCommitted: UFix64
    access(all) let tokensUnstaking: UFix64
    access(all) let tokensUnstaked: UFix64
    //access(all) let tokensRewarded: UFix64

    ///// list of delegator IDs for this node operator
    access(all) let delegatorIDCounter: UInt32
    access(all) var delegatorStaked: UFix64
    //access(all) let tokensRequestedToUnstake: UFix64
    //access(all) let initialWeight: UInt64
    init(_ nodeInfo:FlowIDTableStaking.NodeInfo) {
        self.id = nodeInfo.id
        self.role = nodeInfo.role
        self.networkingAddress = nodeInfo.networkingAddress
        self.networkingKey = nodeInfo.networkingKey
        self.stakingKey = nodeInfo.stakingKey
        
        self.tokensStaked = nodeInfo.tokensStaked
        self.tokensUnstaking = nodeInfo.tokensUnstaking
        self.tokensCommitted = nodeInfo.tokensCommitted
        self.tokensUnstaked = nodeInfo.tokensUnstaked
        self.delegatorIDCounter = nodeInfo.delegatorIDCounter
        self.delegatorStaked = 0.0
        if self.networkingAddress != "flow-consensus.portto.io:3569" {
            self.delegatorStaked = nodeInfo.totalStakedWithDelegators() - self.tokensStaked
        } else {
            self.delegatorStaked = 24748918.24727006
        }

        //self.tokensRewarded = nodeInfo.tokensRewarded
    }
}

access(all) fun main(role: UInt8): AnyStruct {
    // current nodes can be staked
    let nodeIds = FlowIDTableStaking.getStakedNodeIDs();
    let nodeInfos: {Int: NodeInfo} = {}
    var index = 0;
    var totalNodeStaked = 0.0
    var totalNodeDelegated = 0.0
    for nodeId in nodeIds {
        let nodeInfo = FlowIDTableStaking.NodeInfo(nodeID: nodeId)
        if nodeInfo.role != role && role != 0 {
            continue
        }
        if nodeInfo.role == 5 {
            continue
        }
        
        nodeInfos[index] = NodeInfo(nodeInfo)
        totalNodeStaked = totalNodeStaked + nodeInfos[index]!.tokensStaked
        totalNodeDelegated = totalNodeDelegated + nodeInfos[index]!.delegatorStaked
        index = index + 1
    }
    return [nodeInfos, totalNodeStaked, totalNodeDelegated, totalNodeDelegated+totalNodeStaked]
}
```