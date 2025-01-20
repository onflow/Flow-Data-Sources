# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/storageFees/scripts/get_storage_capacity.cdc

```
import FlowStorageFees from "FlowStorageFees"

access(all) fun main(accountAddress: Address): UFix64 {
    return FlowStorageFees.calculateAccountCapacity(accountAddress)
}


```