# Source: https://github.com/onflow/flow-evm-bridge/blob/main/cadence/scripts/bridge/get_legacy_evm_address_for_custom_cross_vm_evm_address.cdc

```
import "EVM"
import "FlowEVMBridgeConfig"

/// Returns the bridge-defined EVM contract address that was originally associated with the related Cadence NFT
/// given some externally defined contract. This would arise in the event a Cadence-native project onboarded to the
/// bridge via permissionless onboarding & later registered their own EVM contract as associated with their
/// Cadence NFT per FLIP-318 mechanisms. If there is not a related bridge-defined EVM contract registered with the
/// bridge, `nil` is returned.
///
/// @param evmContract: The cross-VM EVM contract for which the caller is seeking the originally associated bridged
///     EVM contract
///
/// @return The bridge-defined EVM contract originally associated with the updated cross-VM asset association if exists
///
access(all)
fun main(evmAddress: String): EVM.EVMAddress? {
    return FlowEVMBridgeConfig.getLegacyEVMAddressForCustomCrossVMAddress(
        EVM.addressFromString(evmAddress)
    )
}

```