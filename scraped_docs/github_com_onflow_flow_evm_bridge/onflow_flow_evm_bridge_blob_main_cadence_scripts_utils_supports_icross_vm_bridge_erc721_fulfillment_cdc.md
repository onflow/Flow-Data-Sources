# Source: https://github.com/onflow/flow-evm-bridge/blob/main/cadence/scripts/utils/supports_icross_vm_bridge_erc721_fulfillment.cdc

```
import "EVM"

import "FlowEVMBridgeUtils"

/// Returns whether a given EVM contract supports the ICrossVMBridgeERC721Fulfillment.sol contract interface
///
access(all)
fun main(evmContractAddress: String): Bool {
    return FlowEVMBridgeUtils.supportsICrossVMBridgeERC721Fulfillment(
        evmContract: EVM.addressFromString(evmContractAddress)
    )
}

```