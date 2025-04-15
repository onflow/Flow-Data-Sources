# Source: https://github.com/Outblock/FRW-scripts/blob/main/scripts/src/cadence/bridges/get_bridge_coa_address.cdc

```
import EVM from 0xEVM

import EVMUtils from 0xFlowEVMBridge
import FlowEVMBridgeConfig from 0xFlowEVMBridge

access(all) fun main(): String {
    let address: EVM.EVMAddress = FlowEVMBridge.getBridgeCOAEVMAddress()
    return EVMUtils.getEVMAddressAsHexString(address: address)
}
```