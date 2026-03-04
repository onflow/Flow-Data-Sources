# Source: https://github.com/IncrementFi/Liquid-Staking/blob/main/cadence/transactions/test/stake_new_tokens_in_collection.cdc

```
import FungibleToken from "../../contracts/standard/FungibleToken.cdc"
import FlowToken from "../../contracts/standard/FlowToken.cdc"
import FlowIDTableStaking from "../../contracts/standard/mainnet/FlowIDTableStaking.cdc"
import FlowStakingCollection from "../../contracts/standard/mainnet/FlowStakingCollection.cdc"

/// Registers a delegator in the staking collection resource
/// for the specified nodeID and the amount of tokens to commit
transaction(id: String, delegatorID: UInt32, amount: UFix64) {
    prepare(account: auth(BorrowValue) &Account) {
        let stakingCollectionRef = account.storage.borrow<auth(FlowStakingCollection.CollectionOwner) &FlowStakingCollection.StakingCollection>(from: FlowStakingCollection.StakingCollectionStoragePath)
            ?? panic("Could not borrow ref to StakingCollection")

        stakingCollectionRef.stakeNewTokens(nodeID: id, delegatorID: delegatorID, amount: amount)      
    }
}
```