# Source: https://github.com/Outblock/FRW-scripts/blob/main/cadence/staking/query/get_epoch_metadata.cdc

```
import FlowEpoch from 0xFlowEpoch

access(all) fun main(epochCounter: UInt64): FlowEpoch.EpochMetadata {
  return FlowEpoch.getEpochMetadata(epochCounter)!
}
```