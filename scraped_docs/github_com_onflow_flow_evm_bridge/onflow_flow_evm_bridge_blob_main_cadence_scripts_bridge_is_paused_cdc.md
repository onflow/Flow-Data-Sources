# Source: https://github.com/onflow/flow-evm-bridge/blob/main/cadence/scripts/bridge/is_paused.cdc

```
import "FlowEVMBridgeConfig"

access(all)
fun main(): Bool {
    return FlowEVMBridgeConfig.isPaused()
}

```