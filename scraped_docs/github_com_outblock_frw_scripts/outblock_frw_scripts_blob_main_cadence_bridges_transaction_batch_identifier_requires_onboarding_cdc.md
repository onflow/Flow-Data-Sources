# Source: https://github.com/Outblock/FRW-scripts/blob/main/cadence/bridges/transaction/batch_identifier_requires_onboarding.cdc

```
import FlowEVMBridge from 0xFlowEVMBridge

access(all) fun main(identifiers: [String]): {String: Bool?} {
  let results: {String: Bool?} = {}

  for identifier in identifiers {
    if results[identifier] != nil {
      continue
    }
    let type: Type = CompositeType(identifier) ?? panic("Invalid type identifier")
    results.insert(key: identifier, FlowEVMBridge.typeRequiresOnboarding(type))
  }
  return results
}

```