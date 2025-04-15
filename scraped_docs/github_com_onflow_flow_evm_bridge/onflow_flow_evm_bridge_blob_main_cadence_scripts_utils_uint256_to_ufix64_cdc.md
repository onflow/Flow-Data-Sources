# Source: https://github.com/onflow/flow-evm-bridge/blob/main/cadence/scripts/utils/uint256_to_ufix64.cdc

```
import "FlowEVMBridgeUtils"

access(all)
fun main(value: UInt256, decimals: UInt8): UFix64 {
    return FlowEVMBridgeUtils.uint256ToUFix64(value: value, decimals: decimals)
}

```