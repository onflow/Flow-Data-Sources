# Source: https://github.com/onflow/flow-core-contracts/blob/master/tests/scripts/get_executed_transactions.cdc

```
import "TestFlowScheduledTransactionHandler"

access(all) fun main(): [UInt64] {
    return TestFlowScheduledTransactionHandler.getSucceededTransactions()
}

```