# Source: https://github.com/onflow/flow-evm-bridge/blob/main/cadence/scripts/utils/supports_icross_vm_bridge_callable.cdc

```
import "EVM"

import "FlowEVMBridgeUtils"

/// Returns whether a given EVM contract supports the ICrossVMBridgeCallable.sol contract interface
///
access(all)
fun main(evmContractAddress: String): Bool {
    return FlowEVMBridgeUtils.supportsICrossVMBridgeCallable(
        evmContract: EVM.addressFromString(evmContractAddress)
    )
}

```