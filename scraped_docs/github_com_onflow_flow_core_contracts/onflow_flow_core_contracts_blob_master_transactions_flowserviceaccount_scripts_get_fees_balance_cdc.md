# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/FlowServiceAccount/scripts/get_fees_balance.cdc

```
import "FlowFees"

access(all) fun main(): UFix64 {
    return FlowFees.getFeeBalance()
}
```