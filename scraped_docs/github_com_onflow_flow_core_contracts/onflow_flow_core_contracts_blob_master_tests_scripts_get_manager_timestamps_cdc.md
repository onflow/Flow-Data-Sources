# Source: https://github.com/onflow/flow-core-contracts/blob/master/tests/scripts/get_manager_timestamps.cdc

```
import "FlowTransactionSchedulerUtils"
import "FlowTransactionScheduler"

access(all) fun main(address: Address): [UFix64] {
    let managerRef = FlowTransactionSchedulerUtils.borrowManager(at: address)
        ?? panic("Invalid address: Could not borrow a reference to the Scheduled Transaction Manager at address \(address)")
    return managerRef.getSortedTimestamps().getBefore(current: getCurrentBlock().timestamp)
}
```