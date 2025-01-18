# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/epoch/scripts/get_epoch_phase.cdc

```
import FlowEpoch from "FlowEpoch"

access(all) fun main(): UInt8 {
    return FlowEpoch.currentEpochPhase.rawValue
}
```