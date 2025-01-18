# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/stakingCollection/restake_all_stakers.cdc

```
import FlowStakingCollection from "FlowStakingCollection"
import FlowIDTableStaking from "FlowIDTableStaking"

/// Commits rewarded tokens to stake for all nodes and delegators in a collection

transaction {
    
    let stakingCollectionRef: auth(FlowStakingCollection.CollectionOwner) &FlowStakingCollection.StakingCollection

    prepare(account: auth(BorrowValue) &Account) {
        self.stakingCollectionRef = account.storage.borrow<auth(FlowStakingCollection.CollectionOwner) &FlowStakingCollection.StakingCollection>(from: FlowStakingCollection.StakingCollectionStoragePath)
            ?? panic(FlowStakingCollection.getCollectionMissingError(nil))
    }

    execute {
        let nodeIDs = self.stakingCollectionRef.getNodeIDs()

        for nodeID in nodeIDs {
            let nodeInfo = FlowIDTableStaking.NodeInfo(nodeID: nodeID)
            self.stakingCollectionRef.stakeRewardedTokens(nodeID: nodeID, delegatorID: nil, amount: nodeInfo.tokensRewarded)
        }

        let delegators = self.stakingCollectionRef.getDelegatorIDs()

        for delegator in delegators {
            let delegatorInfo = FlowIDTableStaking.DelegatorInfo(nodeID: delegator.delegatorNodeID, delegatorID: delegator.delegatorID)
            
            self.stakingCollectionRef.stakeRewardedTokens(nodeID: delegator.delegatorNodeID, delegatorID: delegator.delegatorID, amount: delegatorInfo.tokensRewarded)
        }
    }
}

```