# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/transactionScheduler/scripts/get_transaction_data.cdc

```
import "FlowTransactionScheduler"

access(all) fun main(id: UInt64): FlowTransactionScheduler.TransactionData? {
    return FlowTransactionScheduler.getTransactionData(id: id)
}

```