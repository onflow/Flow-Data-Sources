# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/stakingCollection/scripts/get_all_delegator_info.cdc

```
import FlowStakingCollection from "FlowStakingCollection"
import FlowIDTableStaking from "FlowIDTableStaking"

/// Gets an array of all the delegator metadata for delegators stored in the staking collection

access(all) fun main(address: Address): [FlowIDTableStaking.DelegatorInfo] {
    return FlowStakingCollection.getAllDelegatorInfo(address: address)
}
```