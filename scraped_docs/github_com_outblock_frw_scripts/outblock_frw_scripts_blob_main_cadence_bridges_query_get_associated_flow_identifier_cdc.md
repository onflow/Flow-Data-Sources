# Source: https://github.com/Outblock/FRW-scripts/blob/main/cadence/bridges/query/get_associated_flow_identifier.cdc

```
import EVM from 0xEVM
import FlowEVMBridgeConfig from 0xFlowEVMBridge

access(all)
fun main(address: String): String? {
  if let typeInfo = FlowEVMBridgeConfig.getTypeAssociated(with: EVM.addressFromString(address)) {
    return typeInfo.identifier
  }
  return nil
}
```