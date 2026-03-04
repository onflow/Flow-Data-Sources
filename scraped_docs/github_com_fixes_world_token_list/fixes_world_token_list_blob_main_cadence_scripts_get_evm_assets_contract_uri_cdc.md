# Source: https://github.com/fixes-world/token-list/blob/main/cadence/scripts/get-evm-assets-contract-uri.cdc

```
import "EVM"
import "FlowEVMBridgeUtils"

access(all)
fun main(evmContractAddressesHex: String): String? {
    if evmContractAddressesHex.length != 40 {
        return nil
    }
    let addr = EVM.addressFromString(evmContractAddressesHex)
    if let uri = FlowEVMBridgeUtils.getContractURI(evmContractAddress: addr) {
        return uri
    }
    return nil
}


```