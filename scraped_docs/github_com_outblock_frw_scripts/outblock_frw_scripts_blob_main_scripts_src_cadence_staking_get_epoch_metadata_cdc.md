# Source: https://github.com/Outblock/FRW-scripts/blob/main/scripts/src/cadence/staking/get_epoch_metadata.cdc

```
import FlowEpoch from 0xFlowEpoch

access(all) fun main(epochCounter: UInt64): FlowEpoch.EpochMetadata {
    return FlowEpoch.getEpochMetadata(epochCounter)!
}
```