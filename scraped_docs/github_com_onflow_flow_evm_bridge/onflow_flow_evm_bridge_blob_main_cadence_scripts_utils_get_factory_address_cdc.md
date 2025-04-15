# Source: https://github.com/onflow/flow-evm-bridge/blob/main/cadence/scripts/utils/get_factory_address.cdc

```
import "EVM"

import "FlowEVMBridgeUtils"

/// Returns the EVM address of the FlowEVMBridgeFactory solidity contract
///
/// @return The EVM address of the FlowEVMBridgeFactory contract as hex string (without 0x prefix)
///
access(all) fun main(): String {
    return FlowEVMBridgeUtils.getBridgeFactoryEVMAddress().toString()
}
```