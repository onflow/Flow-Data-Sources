# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/FlowServiceAccount/scripts/get_account_fee.cdc

```
import FlowServiceAccount from "FlowServiceAccount"

access(all) fun main(): UFix64 {
    return FlowServiceAccount.accountCreationFee
}
```