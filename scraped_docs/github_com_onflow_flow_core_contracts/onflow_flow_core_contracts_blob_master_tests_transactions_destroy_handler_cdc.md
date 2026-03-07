# Source: https://github.com/onflow/flow-core-contracts/blob/master/tests/transactions/destroy_handler.cdc

```
import "TestFlowScheduledTransactionHandler"
import "FlowTransactionScheduler"

transaction {
    prepare(account: auth(BorrowValue, LoadValue) &Account) {
        let handler <- account.storage.load<@TestFlowScheduledTransactionHandler.Handler>(from: TestFlowScheduledTransactionHandler.HandlerStoragePath)
            ?? panic("Could not load TestFlowScheduledTransactionHandler")
        destroy handler
    }
}


```