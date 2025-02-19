# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/storageFees/scripts/get_account_available_balance.cdc

```
import "FlowStorageFees"

access(all) fun main(accountAddress: Address): UFix64 {
    return FlowStorageFees.defaultTokenAvailableBalance(accountAddress)
}


```