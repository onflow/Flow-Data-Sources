# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/FlowServiceAccount/scripts/get_execution_memory_limit.cdc

```
import FlowServiceAccount from "FlowServiceAccount"

access(all) fun main(): UInt64 {
    return FlowServiceAccount.getExecutionMemoryLimit()
}
```