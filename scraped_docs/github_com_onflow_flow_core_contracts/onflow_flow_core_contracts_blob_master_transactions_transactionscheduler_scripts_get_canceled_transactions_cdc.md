# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/transactionScheduler/scripts/get_canceled_transactions.cdc

```
import "FlowTransactionScheduler"

access(all) fun main(): [UInt64] {
    return FlowTransactionScheduler.getCanceledTransactions()
}

```