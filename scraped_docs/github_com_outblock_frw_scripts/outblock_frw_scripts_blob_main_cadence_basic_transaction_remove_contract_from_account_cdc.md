# Source: https://github.com/Outblock/FRW-scripts/blob/main/cadence/basic/transaction/remove_contract_from_account.cdc

```
transaction(name: String) {
  prepare(signer: auth(RemoveContract) &Account) {
    signer.contracts.remove(name: name)
  }
}
```