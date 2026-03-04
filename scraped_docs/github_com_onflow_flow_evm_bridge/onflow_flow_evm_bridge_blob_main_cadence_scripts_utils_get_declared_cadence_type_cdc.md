# Source: https://github.com/onflow/flow-evm-bridge/blob/main/cadence/scripts/utils/get_declared_cadence_type.cdc

```
import "EVM"

import "FlowEVMBridgeUtils"

access(all)
fun main(evmContractAddress: String): Type? {
    return FlowEVMBridgeUtils.getDeclaredCadenceTypeFromCrossVM(
        evmContract: EVM.addressFromString(evmContractAddress)
    )
}

```