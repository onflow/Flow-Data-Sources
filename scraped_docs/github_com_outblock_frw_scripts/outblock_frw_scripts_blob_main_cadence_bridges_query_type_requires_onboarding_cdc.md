# Source: https://github.com/Outblock/FRW-scripts/blob/main/cadence/bridges/query/type_requires_onboarding.cdc

```
import FlowEVMBridge from 0xFlowEVMBridge

access(all) fun main(type: Type): Bool? {
  return FlowEVMBridge.typeRequiresOnboarding(type)
}

```