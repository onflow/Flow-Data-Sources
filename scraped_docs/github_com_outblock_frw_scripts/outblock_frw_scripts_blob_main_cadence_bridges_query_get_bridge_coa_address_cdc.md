# Source: https://github.com/Outblock/FRW-scripts/blob/main/cadence/bridges/query/get_bridge_coa_address.cdc

```
import EVM from 0xEVM

import FlowEVMBridge from 0xFlowEVMBridge

access(all) fun main(): String {
  return FlowEVMBridge.getBridgeCOAEVMAddress().toString()

}
```