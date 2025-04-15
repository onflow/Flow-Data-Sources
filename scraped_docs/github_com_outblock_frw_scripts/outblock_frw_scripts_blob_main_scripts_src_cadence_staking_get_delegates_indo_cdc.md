# Source: https://github.com/Outblock/FRW-scripts/blob/main/scripts/src/cadence/staking/get_delegates_indo.cdc

```

import FlowStakingCollection from 0xFlowStakingCollection
import FlowIDTableStaking from 0xFlowIDTableStaking
import LockedTokens from 0xLockedTokens

access(all) struct DelegateInfo {
    access(all) let delegatorID: UInt32
    access(all) let nodeID: String
    access(all) let tokensCommitted: UFix64
    access(all) let tokensStaked: UFix64
    access(all) let tokensUnstaking: UFix64
    access(all) let tokensRewarded: UFix64
    access(all) let tokensUnstaked: UFix64
    access(all) let tokensRequestedToUnstake: UFix64

    // Projected Values

    access(all) let id: String
    access(all) let role: UInt8
    access(all) let unstakableTokens: UFix64
    access(all) let delegatedNodeInfo: FlowIDTableStaking.NodeInfo
    access(all) let restakableUnstakedTokens: UFix64

    init(delegatorInfo: FlowIDTableStaking.DelegatorInfo) {
        self.delegatorID = delegatorInfo.id
        self.nodeID = delegatorInfo.nodeID
        self.tokensCommitted = delegatorInfo.tokensCommitted
        self.tokensStaked = delegatorInfo.tokensStaked
        self.tokensUnstaking = delegatorInfo.tokensUnstaking
        self.tokensUnstaked = delegatorInfo.tokensUnstaked
        self.tokensRewarded = delegatorInfo.tokensRewarded
        self.tokensRequestedToUnstake = delegatorInfo.tokensRequestedToUnstake

        // Projected Values
        let nodeInfo = FlowIDTableStaking.NodeInfo(nodeID: delegatorInfo.nodeID)
        self.delegatedNodeInfo = nodeInfo
        self.id = nodeInfo.id
        self.role = nodeInfo.role
        self.unstakableTokens = self.tokensStaked + self.tokensCommitted
        self.restakableUnstakedTokens = self.tokensUnstaked + self.tokensRequestedToUnstake
    }
}

access(all) fun main(account: Address): {String: {UInt32: DelegateInfo}}? {
    let doesAccountHaveStakingCollection = FlowStakingCollection.doesAccountHaveStakingCollection(address: account)
    if (!doesAccountHaveStakingCollection) {
        return nil
    }

    let delegatorIDs: [FlowStakingCollection.DelegatorIDs] = FlowStakingCollection.getDelegatorIDs(address: account)

    let formattedDelegatorInfo: {String: {UInt32: DelegateInfo}} = {}

    for delegatorID in delegatorIDs {
        if let _formattedDelegatorInfo = formattedDelegatorInfo[delegatorID.delegatorNodeID] {
            let delegatorInfo: FlowIDTableStaking.DelegatorInfo = FlowIDTableStaking.DelegatorInfo(nodeID: delegatorID.delegatorNodeID, delegatorID: delegatorID.delegatorID)
            _formattedDelegatorInfo[delegatorID.delegatorID] = DelegateInfo(delegatorInfo: delegatorInfo)
        } else {
            let delegatorInfo: FlowIDTableStaking.DelegatorInfo = FlowIDTableStaking.DelegatorInfo(nodeID: delegatorID.delegatorNodeID, delegatorID: delegatorID.delegatorID)
            formattedDelegatorInfo[delegatorID.delegatorNodeID] = { delegatorID.delegatorID: DelegateInfo(delegatorInfo: delegatorInfo)}
        }
    }

    return formattedDelegatorInfo
}

```