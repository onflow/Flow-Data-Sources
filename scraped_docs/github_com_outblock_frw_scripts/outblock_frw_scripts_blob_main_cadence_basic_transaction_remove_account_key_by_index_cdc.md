# Source: https://github.com/Outblock/FRW-scripts/blob/main/cadence/basic/transaction/remove_account_key_by_index.cdc

```
transaction(keyIndex: Int) {
  prepare(signer: auth(Keys) &Account) {
    signer.keys.revoke(keyIndex: keyIndex)
  }
}
```