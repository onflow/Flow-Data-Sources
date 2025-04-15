# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/FlowServiceAccount/scripts/get_is_account_creation_restricted.cdc

```
import "FlowServiceAccount"

access(all) fun main(): Bool {
    return FlowServiceAccount.isAccountCreationRestricted()
}
```