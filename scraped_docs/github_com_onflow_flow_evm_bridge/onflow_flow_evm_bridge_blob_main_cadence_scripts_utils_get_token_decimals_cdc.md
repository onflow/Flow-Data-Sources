# Source: https://github.com/onflow/flow-evm-bridge/blob/main/cadence/scripts/utils/get_token_decimals.cdc

```
import "EVM"

import "FlowEVMBridgeUtils"

access(all)
fun main(erc20ContractAddressHex: String): UInt8 {
    return FlowEVMBridgeUtils.getTokenDecimals(
        evmContractAddress: EVM.addressFromString(erc20ContractAddressHex)
    )
}

```