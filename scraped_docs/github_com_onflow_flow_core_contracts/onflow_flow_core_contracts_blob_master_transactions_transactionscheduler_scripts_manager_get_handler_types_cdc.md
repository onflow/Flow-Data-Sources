# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/transactionScheduler/scripts/manager/get_handler_types.cdc

```
import "FlowTransactionSchedulerUtils"

access(all) fun main(address: Address): {String: [UInt64]} {
    let managerRef = FlowTransactionSchedulerUtils.borrowManager(at: address)
        ?? panic("Invalid address: Could not borrow a reference to the Scheduled Transaction Manager at address \(address)")
    return managerRef.getHandlerTypeIdentifiers()
}
```