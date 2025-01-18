# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/epoch/scripts/get_epoch_timing_config.cdc

```
import FlowEpoch from "FlowEpoch"

access(all) fun main(): FlowEpoch.EpochTimingConfig {
    return FlowEpoch.getEpochTimingConfig()
}
```