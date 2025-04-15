# Source: https://github.com/onflow/flow-evm-bridge/blob/main/cadence/scripts/bridge/is_type_paused.cdc

```
import "FlowEVMBridgeConfig"

access(all)
fun main(typeIdentifier: String): Bool? {
    return FlowEVMBridgeConfig.isTypePaused(
        CompositeType(typeIdentifier) ?? panic("Invalid type identifier provided: ".concat(typeIdentifier))
    )
}

```