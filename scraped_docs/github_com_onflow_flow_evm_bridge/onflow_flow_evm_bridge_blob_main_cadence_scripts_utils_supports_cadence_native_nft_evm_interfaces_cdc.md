# Source: https://github.com/onflow/flow-evm-bridge/blob/main/cadence/scripts/utils/supports_cadence_native_nft_evm_interfaces.cdc

```
import "EVM"

import "FlowEVMBridgeUtils"

/// Returns whether a given EVM contract supports the ICrossVMBridgeCallable.sol and ICrossVMBridgeERC721Fulfillment.sol
/// contract interfaces required for Cadence-native cross-VM NFTs to be properly supported by the VM bridge.
///
access(all)
fun main(evmContractAddress: String): Bool {
    return FlowEVMBridgeUtils.supportsCadenceNativeNFTEVMInterfaces(
        evmContract: EVM.addressFromString(evmContractAddress)
    )
}

```