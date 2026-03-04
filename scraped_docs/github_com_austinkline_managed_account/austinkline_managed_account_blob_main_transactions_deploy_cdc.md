# Source: https://github.com/austinkline/managed-account/blob/main/transactions/deploy.cdc

```
transaction(name: String, code: [UInt8]) {
    prepare(acct: auth(Contracts) &Account) {
        acct.contracts.add(name: name, code: code)
    }
}
```