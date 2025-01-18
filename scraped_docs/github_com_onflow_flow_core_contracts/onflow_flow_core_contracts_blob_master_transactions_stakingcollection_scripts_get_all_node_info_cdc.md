# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/stakingCollection/scripts/get_all_node_info.cdc

```
import FlowStakingCollection from "FlowStakingCollection"
import FlowIDTableStaking from "FlowIDTableStaking"

/// Gets an array of all the node metadata for nodes stored in the staking collection

access(all) fun main(address: Address): [FlowIDTableStaking.NodeInfo] {
    return FlowStakingCollection.getAllNodeInfo(address: address)
}
```