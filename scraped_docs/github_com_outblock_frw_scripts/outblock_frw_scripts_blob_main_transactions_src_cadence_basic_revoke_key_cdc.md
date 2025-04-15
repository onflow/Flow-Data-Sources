# Source: https://github.com/Outblock/FRW-scripts/blob/main/transactions/src/cadence/basic/revoke_key.cdc

```
transaction(index: Int) {
    prepare(signer: auth(Keys) &Account) {
        // Get a key from an auth account.
        let keyA = signer.keys.revoke(keyIndex: index)
    }
}
```