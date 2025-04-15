# Source: https://github.com/onflow/flow-evm-bridge/blob/main/cadence/scripts/bridge/get_bridge_coa_address.cdc

```
import "EVM"

import "FlowEVMBridge"

/// Returns the EVM address associated with the FlowEVMBridge
///
/// @return The EVM address associated with the FlowEVMBridge's coordinating CadenceOwnedAccount
///
access(all) fun main(): String {
    return FlowEVMBridge.getBridgeCOAEVMAddress().toString()
}
```