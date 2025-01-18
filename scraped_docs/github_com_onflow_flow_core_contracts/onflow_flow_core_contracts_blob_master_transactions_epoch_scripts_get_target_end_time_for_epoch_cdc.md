# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/epoch/scripts/get_target_end_time_for_epoch.cdc

```
import FlowEpoch from "FlowEpoch"

access(all) fun main(targetEpoch: UInt64): UInt64 {
    pre {
        targetEpoch >= FlowEpoch.currentEpochCounter
    }
    let config = FlowEpoch.getEpochTimingConfig()
    return config.getTargetEndTimeForEpoch(targetEpoch)
}
```