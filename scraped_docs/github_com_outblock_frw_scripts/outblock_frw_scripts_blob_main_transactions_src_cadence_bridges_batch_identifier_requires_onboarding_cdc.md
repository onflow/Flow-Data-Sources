# Source: https://github.com/Outblock/FRW-scripts/blob/main/transactions/src/cadence/bridges/batch_identifier_requires_onboarding.cdc

```
import FlowEVMBridge from 0xFlowEVMBridge

/// Returns whether a type needs to be onboarded to the FlowEVMBridge
///
/// @param Types: The array of types to check for onboarding status
///
/// @return Whether the type requires onboarding to the FlowEVMBridge if the type is bridgeable, otherwise nil indexed
///     on the type
///
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