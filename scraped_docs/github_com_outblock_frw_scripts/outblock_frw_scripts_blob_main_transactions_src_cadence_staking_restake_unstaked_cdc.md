# Source: https://github.com/Outblock/FRW-scripts/blob/main/transactions/src/cadence/staking/restake_unstaked.cdc

```
import FlowStakingCollection from 0xFlowStakingCollection

/// Commits unstaked tokens to stake for the specified node or delegator in the staking collection

transaction(nodeID: String, delegatorID: UInt32?, amount: UFix64) {
    
    let stakingCollectionRef: auth(FlowStakingCollection.CollectionOwner) &FlowStakingCollection.StakingCollection

    prepare(account: auth(BorrowValue) &Account) {
        self.stakingCollectionRef = account.storage.borrow<auth(FlowStakingCollection.CollectionOwner) &FlowStakingCollection.StakingCollection>(from: FlowStakingCollection.StakingCollectionStoragePath)
            ?? panic("Could not borrow a reference to a StakingCollection in the primary user's account")
    }

    execute {
        self.stakingCollectionRef.stakeUnstakedTokens(nodeID: nodeID, delegatorID: delegatorID, amount: amount)
    }
}
```