# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/storageFees/scripts/get_accounts_capacity_for_transaction_storage_check.cdc

```
import FlowStorageFees from "FlowStorageFees"

access(all) fun main(accountAddresses: [Address], payer: Address, maxTxFees: UFix64): [UFix64] {
    return FlowStorageFees.getAccountsCapacityForTransactionStorageCheck(
        accountAddresses: accountAddresses, 
        payer: payer, 
        maxTxFees: maxTxFees)
}
```