# Source: https://github.com/onflow/flow-evm-bridge/blob/main/cadence/scripts/config/get_base_fee.cdc

```
import "FlowEVMBridgeConfig"

access(all) fun main(): UFix64 {
    return FlowEVMBridgeConfig.baseFee
}

```