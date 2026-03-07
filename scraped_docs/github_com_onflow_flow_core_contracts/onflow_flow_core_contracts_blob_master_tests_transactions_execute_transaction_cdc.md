# Source: https://github.com/onflow/flow-core-contracts/blob/master/tests/transactions/execute_transaction.cdc

```
import "FlowTransactionScheduler"

// Execute a scheduled transaction by the FlowTransactionScheduler contract.
// This will be called by the FVM and the transaction will be executed by their ID.
transaction(id: UInt64) {
    prepare(serviceAccount: auth(BorrowValue) &Account) {
        let scheduler = serviceAccount.storage.borrow<auth(FlowTransactionScheduler.Execute) &FlowTransactionScheduler.SharedScheduler>(from: FlowTransactionScheduler.storagePath)
            ?? panic("Could not borrow FlowTransactionScheduler")

        scheduler.executeTransaction(id: id)
    }
}
```