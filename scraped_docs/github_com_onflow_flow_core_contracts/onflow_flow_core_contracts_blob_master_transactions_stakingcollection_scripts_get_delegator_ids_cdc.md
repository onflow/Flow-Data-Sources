# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/stakingCollection/scripts/get_delegator_ids.cdc

```
import "FlowStakingCollection"

/// Returns an array of all the delegator IDs stored in the staking collection

access(all) fun main(address: Address): [FlowStakingCollection.DelegatorIDs] {
    return FlowStakingCollection.getDelegatorIDs(address: address)
}
```