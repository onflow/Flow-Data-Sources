# Source: https://github.com/onflow/flow-evm-bridge/blob/main/cadence/scripts/bridge/evm_address_requires_onboarding.cdc

```
import "EVM"

import "FlowEVMBridge"

/// Returns whether a EVM contract needs to be onboarded to the FlowEVMBridge
///
/// @param evmAddressHex: The hex-encoded address of the EVM contract as a String without 0x prefix
///
/// @return Whether the contract requires onboarding to the FlowEVMBridge if the type is bridgeable, otherwise nil
///
access(all) fun main(evmAddressHex: String): Bool? {
    let address = EVM.addressFromString(evmAddressHex)
    return FlowEVMBridge.evmAddressRequiresOnboarding(address)
}

```