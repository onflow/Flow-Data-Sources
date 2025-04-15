# Source: https://github.com/Outblock/FRW-scripts/blob/main/scripts/src/cadence/bridges/get_associated_evm_address.cdc

```
import EVM from 0xEVM

import EVMUtils from 0xFlowEVMBridge
import FlowEVMBridgeConfig from 0xFlowEVMBridge

/// Returns the EVM address associated with the given Cadence type (as its identifier String)
///
/// @param typeIdentifier The Cadence type identifier String
///
/// @return The EVM address as a hex string if the type has an associated EVMAddress, otherwise nil
///
access(all)
fun main(identifier: String): String? {
    if let type = CompositeType(identifier) {
        if let address = FlowEVMBridgeConfig.getEVMAddressAssociated(with: type) {
            return EVMUtils.getEVMAddressAsHexString(address: address)
        }
    }
    return nil
}
```