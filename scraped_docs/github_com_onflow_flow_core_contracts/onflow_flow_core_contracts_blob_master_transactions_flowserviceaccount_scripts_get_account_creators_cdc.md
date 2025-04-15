# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/FlowServiceAccount/scripts/get_account_creators.cdc

```
import "FlowServiceAccount"

access(all) fun main(): [Address] {
    return FlowServiceAccount.getAccountCreators()
}
```