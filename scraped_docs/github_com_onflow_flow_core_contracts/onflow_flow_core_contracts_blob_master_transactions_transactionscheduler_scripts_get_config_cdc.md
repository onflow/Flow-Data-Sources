# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/transactionScheduler/scripts/get_config.cdc

```
import "FlowTransactionScheduler"

access(all) fun main(): {FlowTransactionScheduler.SchedulerConfig} {
    let config = FlowTransactionScheduler.getConfig()
    return config
}

```