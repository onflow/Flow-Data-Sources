# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/transactionScheduler/scripts/manager/resolve_handler_view.cdc

```
import "FlowTransactionSchedulerUtils"

access(all) fun main(address: Address, handlerTypeIdentifier: String, handlerUUID: UInt64?, viewType: Type): AnyStruct? {
    let managerRef = FlowTransactionSchedulerUtils.borrowManager(at: address)
        ?? panic("Invalid address: Could not borrow a reference to the Scheduled Transaction Manager at address \(address)")
    return managerRef.resolveHandlerView(handlerTypeIdentifier: handlerTypeIdentifier, handlerUUID: handlerUUID, viewType: viewType)
}
```