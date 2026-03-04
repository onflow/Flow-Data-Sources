# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/transactionScheduler/scripts/manager/get_tx_ids_by_handler.cdc

```
import "FlowTransactionSchedulerUtils"

access(all) fun main(address: Address, handlerTypeIdentifier: String, handlerUUID: UInt64?): [UInt64] {
    let managerRef = FlowTransactionSchedulerUtils.borrowManager(at: address)
        ?? panic("Invalid address: Could not borrow a reference to the Scheduled Transaction Manager at address \(address)")
    return managerRef.getTransactionIDsByHandler(handlerTypeIdentifier: handlerTypeIdentifier, handlerUUID: handlerUUID)
}
```