# Source: https://github.com/Outblock/FRW-scripts/blob/main/scripts/src/cadence/staking/check_setup.cdc

```
import FlowStakingCollection from 0xFlowStakingCollection

/// Determines if an account is set up with a Staking Collection

access(all) fun main(address: Address): Bool {
    return FlowStakingCollection.doesAccountHaveStakingCollection(address: address)
}
```