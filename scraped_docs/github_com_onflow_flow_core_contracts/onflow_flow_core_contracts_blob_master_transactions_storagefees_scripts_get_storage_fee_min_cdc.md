# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/storageFees/scripts/get_storage_fee_min.cdc

```
import FlowStorageFees from "FlowStorageFees"

access(all) fun main(): UFix64 {
    return FlowStorageFees.minimumStorageReservation
}


```