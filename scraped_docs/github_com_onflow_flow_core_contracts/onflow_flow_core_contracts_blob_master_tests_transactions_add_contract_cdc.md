# Source: https://github.com/onflow/flow-core-contracts/blob/master/tests/transactions/add_contract.cdc

```
transaction(name: String, code: String) {
    prepare(account: auth(AddContract) &Account) {
        // Add the contract
        account.contracts.add(name: name, code: code.utf8)
    }
}

```