# Source: https://github.com/onflow/flow-evm-bridge/blob/main/cadence/scripts/bridge/is_evm_address_blocked.cdc

```
import "EVM"

import "FlowEVMBridgeConfig"

/// Returns whether a EVM contract is blocked from onboarded to the FlowEVMBridge
///
/// @param evmAddressHex: The hex-encoded address of the EVM contract as a String
///
/// @return Whether the contract is blocked from onboarding to the FlowEVMBridge
///
access(all) fun main(evmAddressHex: String): Bool {
    let address = EVM.addressFromString(evmAddressHex)
    return FlowEVMBridgeConfig.isEVMAddressBlocked(address)
}

```