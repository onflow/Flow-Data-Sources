# Source: https://github.com/onflow/flow-evm-bridge/blob/main/cadence/scripts/bridge/get_associated_evm_address.cdc

```
import "EVM"

import "FlowEVMBridgeConfig"

/// Returns the EVM address associated with the given Cadence type (as its identifier String)
///
/// @param typeIdentifier: The Cadence type identifier String
///
/// @return The EVM address as a hex string if the type has an associated EVMAddress, otherwise nil
///
access(all)
fun main(identifier: String): String? {
    if let type = CompositeType(identifier) {
        if let address = FlowEVMBridgeConfig.getEVMAddressAssociated(with: type) {
            return address.toString()
        }
    }
    return nil
}
```