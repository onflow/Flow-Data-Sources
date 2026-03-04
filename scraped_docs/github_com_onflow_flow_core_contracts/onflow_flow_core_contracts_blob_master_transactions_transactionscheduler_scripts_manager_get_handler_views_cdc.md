# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/transactionScheduler/scripts/manager/get_handler_views.cdc

```
import "FlowTransactionSchedulerUtils"

access(all) fun main(address: Address, handlerTypeIdentifier: String, handlerUUID: UInt64?): [Type] {
    let managerRef = FlowTransactionSchedulerUtils.borrowManager(at: address)
        ?? panic("Invalid address: Could not borrow a reference to the Scheduled Transaction Manager at address \(address)")
    return managerRef.getHandlerViews(handlerTypeIdentifier: handlerTypeIdentifier, handlerUUID: handlerUUID)
}
```