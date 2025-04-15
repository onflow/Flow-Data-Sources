# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/FlowServiceAccount/scripts/get_execution_effort_weights.cdc

```
import "FlowServiceAccount"

access(all) fun main(): {UInt64: UInt64} {
    return FlowServiceAccount.getExecutionEffortWeights()
}
```