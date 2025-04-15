# Source: https://github.com/Outblock/FRW-scripts/blob/main/transactions/src/cadence/bridges/evm_address_requires_onboarding.cdc

```
import EVMUtils from 0xFlowEVMBridge
import FlowEVMBridge from 0xFlowEVMBridge

/// Returns whether a EVM contract needs to be onboarded to the FlowEVMBridge
///
/// @param evmAddressHex: The hex-encoded address of the EVM contract as a String without 0x prefix
///
/// @return Whether the contract requires onboarding to the FlowEVMBridge if the type is bridgeable, otherwise nil
///
access(all) fun main(evmAddressHex: String): Bool? {
    if let address = EVMUtils.getEVMAddressFromHexString(address: evmAddressHex) {
        return FlowEVMBridge.evmAddressRequiresOnboarding(address)
    }
    return nil
}

```