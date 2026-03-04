# Source: https://github.com/onflow/flow-evm-bridge/blob/main/cadence/scripts/utils/get_declared_cadence_address.cdc

```
import "EVM"

import "FlowEVMBridgeUtils"

access(all)
fun main(evmContractAddress: String): Address? {
    return FlowEVMBridgeUtils.getDeclaredCadenceAddressFromCrossVM(
        evmContract: EVM.addressFromString(evmContractAddress)
    )
}

```