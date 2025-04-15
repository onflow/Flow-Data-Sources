# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/stakingCollection/scripts/does_account_have_staking_collection.cdc

```
import "FlowStakingCollection"

/// Determines if an account is set up with a Staking Collection

access(all) fun main(address: Address): Bool {
    return FlowStakingCollection.doesAccountHaveStakingCollection(address: address)
}
```