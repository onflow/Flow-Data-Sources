# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/stakingCollection/scripts/get_does_stake_exist.cdc

```
import "FlowStakingCollection"
import "FlowIDTableStaking"

/// Tells if the specified node or delegator exists in the staking collection 
/// for the specified address

access(all) fun main(address: Address, nodeID: String, delegatorID: UInt32?): Bool {
    return FlowStakingCollection.doesStakeExist(address: address, nodeID: nodeID, delegatorID: delegatorID)
}
```