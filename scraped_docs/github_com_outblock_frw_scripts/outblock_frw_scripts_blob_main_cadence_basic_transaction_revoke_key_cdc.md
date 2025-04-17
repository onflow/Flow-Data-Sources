# Source: https://github.com/Outblock/FRW-scripts/blob/main/cadence/basic/transaction/revoke_key.cdc

```
transaction(index: Int) {
  prepare(signer: auth(Keys) &Account) {
    let keyA = signer.keys.revoke(keyIndex: index)
  }
}
```