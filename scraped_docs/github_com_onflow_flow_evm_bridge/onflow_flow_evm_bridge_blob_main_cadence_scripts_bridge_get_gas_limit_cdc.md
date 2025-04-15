# Source: https://github.com/onflow/flow-evm-bridge/blob/main/cadence/scripts/bridge/get_gas_limit.cdc

```
import "FlowEVMBridgeConfig"

/// Returns the gas limit for the Flow-EVM bridge.
///
/// @returns The current gas limit shared by all the bridge-related EVM operations.
///
access(all)
fun main(): UInt64 {
    return FlowEVMBridgeConfig.gasLimit
}

```