# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/epoch/scripts/get_epoch_counter.cdc

```
import FlowEpoch from "FlowEpoch"

access(all) fun main(): UInt64 {
    return FlowEpoch.currentEpochCounter
}
```