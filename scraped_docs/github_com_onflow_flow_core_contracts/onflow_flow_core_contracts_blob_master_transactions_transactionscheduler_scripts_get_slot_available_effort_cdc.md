# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/transactionScheduler/scripts/get_slot_available_effort.cdc

```
import "FlowTransactionScheduler"

access(all) fun main(timestamp: UFix64, priority: UInt8): UInt64 {
    let priortyEnum = FlowTransactionScheduler.Priority(rawValue: priority)!
    return FlowTransactionScheduler.getSlotAvailableEffort(timestamp: timestamp, priority: priortyEnum)
}

```