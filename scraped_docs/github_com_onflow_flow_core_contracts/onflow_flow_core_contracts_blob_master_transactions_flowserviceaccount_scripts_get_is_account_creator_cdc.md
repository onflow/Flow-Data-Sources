# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/FlowServiceAccount/scripts/get_is_account_creator.cdc

```
import FlowServiceAccount from "FlowServiceAccount"

access(all) fun main(address: Address): Bool {
    return FlowServiceAccount.isAccountCreator(address)
}
```