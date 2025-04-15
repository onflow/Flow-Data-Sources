# Source: https://github.com/onflow/flow-evm-bridge/blob/main/cadence/scripts/bridge/type_requires_onboarding_by_identifier.cdc

```
import "FlowEVMBridge"

/// Returns whether a type needs to be onboarded to the FlowEVMBridge
///
/// @param identifier: The identifier of the Cadence Type in question
///
/// @return Whether the type requires onboarding to the FlowEVMBridge if the type is bridgeable, otherwise nil
///
access(all) fun main(identifier: String): Bool? {
    if let type = CompositeType(identifier) {
        return FlowEVMBridge.typeRequiresOnboarding(type)
    }
    return nil
}

```