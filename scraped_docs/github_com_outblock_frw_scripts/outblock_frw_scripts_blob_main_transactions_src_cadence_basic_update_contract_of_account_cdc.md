# Source: https://github.com/Outblock/FRW-scripts/blob/main/transactions/src/cadence/basic/update_contract_of_account.cdc

```
transaction(name: String, code: String) {
    prepare(signer: auth(UpdateContract) &Account) {
        signer.contracts.update(name: name, code: code.utf8)
    }
}
```