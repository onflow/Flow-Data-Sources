# Source: https://github.com/onflow/flow-evm-bridge/blob/main/cadence/scripts/bridge/get_associated_type.cdc

```
import "EVM"

import "FlowEVMBridgeConfig"

/// Returns the Cadence Type associated with the given EVM address (as its hex String)
///
/// @param evmAddressHex: The hex-encoded address of the EVM contract as a String
///
/// @return The Cadence Type associated with the EVM address or nil if the address is not onboarded. `nil` may also be
///        returned if the address is not a valid EVM address.
///
access(all)
fun main(addressHex: String): Type? {
    let address = EVM.addressFromString(addressHex)
    return FlowEVMBridgeConfig.getTypeAssociated(with: address)
}

```