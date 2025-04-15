# Source: https://github.com/onflow/flow-evm-bridge/blob/main/cadence/scripts/utils/derive_bridged_nft_contract_name.cdc

```
import "EVM"

import "FlowEVMBridgeUtils"

access(all)
fun main(evmAddressHex: String): String {
    return FlowEVMBridgeUtils.deriveBridgedNFTContractName(
        from: EVM.addressFromString(evmAddressHex)
    )
}

```