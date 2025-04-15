# Source: https://github.com/Outblock/FRW-scripts/blob/main/transactions/src/cadence/basic/remove_contract_from_account.cdc

```
transaction(name: String) {
    prepare(signer: auth(RemoveContract) &Account) {
        signer.contracts.remove(name: name)
    }
}
```