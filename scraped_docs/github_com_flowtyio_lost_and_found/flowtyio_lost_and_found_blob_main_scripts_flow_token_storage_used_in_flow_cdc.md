# Source: https://github.com/Flowtyio/lost-and-found/blob/main/scripts/flow-token/storage_used_in_flow.cdc

```
import FeeEstimator from "../../contracts/FeeEstimator.cdc"

pub fun main(addr: Address): UFix64 {
    return FeeEstimator.storageUsedToFlowAmount(getAccount(addr).storageUsed)
}

```