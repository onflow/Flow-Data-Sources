# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/epoch/scripts/get_epoch_metadata.cdc

```
import FlowEpoch from "FlowEpoch"

access(all) fun main(epochCounter: UInt64): FlowEpoch.EpochMetadata {
    return FlowEpoch.getEpochMetadata(epochCounter)!
}
```