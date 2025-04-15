# Source: https://github.com/Outblock/FRW-scripts/blob/main/transactions/src/cadence/bridges/batch_evm_address_requires_onboarding.cdc

```
import EVMUtils from 0xFlowEVMBridge
import FlowEVMBridge from 0xFlowEVMBridge

/// Returns whether a EVM contract needs to be onboarded to the FlowEVMBridge
///
/// @param evmAddresses: Array of hex-encoded address of the EVM contract as a String without 0x prefix to check for
///     onboarding status
///
/// @return Whether the contract requires onboarding to the FlowEVMBridge if the type is bridgeable, otherwise nil
///     indexed on the hex-encoded address of the EVM contract without 0x prefix
///
access(all) fun main(evmAddresses: [String]): {String: Bool?} {
    let results: {String: Bool?} = {}
    for addressHex in evmAddresses {
        if results[addressHex] != nil {
            continue
        }
        if let address = EVMUtils.getEVMAddressFromHexString(address: addressHex) {
            let requiresOnboarding = FlowEVMBridge.evmAddressRequiresOnboarding(address)
            results.insert(key: addressHex, requiresOnboarding)
        }
    }
    return results
}

```