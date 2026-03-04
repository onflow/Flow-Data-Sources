# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/transactionScheduler/scripts/manager/get_tx_ids_by_time_range.cdc

```
import "FlowTransactionSchedulerUtils"

access(all) fun main(address: Address, startTimestamp: UFix64, endTimestamp: UFix64): {UFix64: [UInt64]} {
    let managerRef = FlowTransactionSchedulerUtils.borrowManager(at: address)
        ?? panic("Invalid address: Could not borrow a reference to the Scheduled Transaction Manager at address \(address)")
    return managerRef.getTransactionIDsByTimestampRange(startTimestamp: startTimestamp, endTimestamp: endTimestamp)
}
```