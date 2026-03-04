# Source: https://github.com/fixes-world/token-list/blob/main/cadence/scripts/get-evm-assets-contract-uris.cdc

```
import "EVM"
import "FlowEVMBridgeUtils"

access(all)
fun main(evmContractAddressesHex: [String]): {String: String} {
    let ret: {String: String} = {}
    for hex in evmContractAddressesHex {
        if hex.length != 40 {
            continue
        }
        let addr = EVM.addressFromString(hex)
        if let uri = FlowEVMBridgeUtils.getContractURI(evmContractAddress: addr) {
            ret[hex] = uri
        }
    }
    return ret
}


```