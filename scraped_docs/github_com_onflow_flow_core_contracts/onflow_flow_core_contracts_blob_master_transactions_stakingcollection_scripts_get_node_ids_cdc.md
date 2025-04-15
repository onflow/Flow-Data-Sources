# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/stakingCollection/scripts/get_node_ids.cdc

```
import "FlowStakingCollection"

/// Returns an array of all the node IDs stored in the staking collection

access(all) fun main(address: Address): [String] {
    return FlowStakingCollection.getNodeIDs(address: address)
}
```