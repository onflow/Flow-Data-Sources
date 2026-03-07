# Source: https://github.com/onflow/flow-core-contracts/blob/master/tests/transactions/upgrade_contract.cdc

```
transaction(name: String, code: String) {
    prepare(account: auth(UpdateContract) &Account) {
        // Upgrade the contract
        account.contracts.update(name: name, code: code.utf8)
    }
}
```