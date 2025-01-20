# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/idTableStaking/scripts/get_slot_limits.cdc

```
import FlowIDTableStaking from "FlowIDTableStaking"

// This script returns the slot limits for node roles

access(all) fun main(role: UInt8): UInt16 {
    let slotLimit = FlowIDTableStaking.getRoleSlotLimits()[role]
        ?? panic("Could not find slot limit for the specified role")

    return slotLimit
}
```