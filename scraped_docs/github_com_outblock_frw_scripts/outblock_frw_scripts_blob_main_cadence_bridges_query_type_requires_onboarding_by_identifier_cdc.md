# Source: https://github.com/Outblock/FRW-scripts/blob/main/cadence/bridges/query/type_requires_onboarding_by_identifier.cdc

```
import FlowEVMBridge from 0xFlowEVMBridge

access(all) fun main(identifier: String): Bool? {
  if let type = CompositeType(identifier) {
    return FlowEVMBridge.typeRequiresOnboarding(type)
  }
  return nil
}

```