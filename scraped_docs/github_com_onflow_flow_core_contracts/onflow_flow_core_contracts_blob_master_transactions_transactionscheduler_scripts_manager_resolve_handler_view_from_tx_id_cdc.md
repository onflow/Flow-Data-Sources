# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/transactionScheduler/scripts/manager/resolve_handler_view_from_tx_id.cdc

```
import "FlowTransactionSchedulerUtils"

access(all) fun main(address: Address, id: UInt64, viewType: Type): AnyStruct? {
    let managerRef = FlowTransactionSchedulerUtils.borrowManager(at: address)
        ?? panic("Invalid address: Could not borrow a reference to the Scheduled Transaction Manager at address \(address)")
    return managerRef.resolveHandlerViewFromTransactionID(id, viewType: viewType)
}
```