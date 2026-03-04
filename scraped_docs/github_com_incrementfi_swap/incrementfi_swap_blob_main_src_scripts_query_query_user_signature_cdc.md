# Source: https://github.com/IncrementFi/Swap/blob/main/src/scripts/query/query_user_signature.cdc

```

access(all) fun main(userAddr: Address): Bool {
    return getAuthAccount<auth(Storage) &Account>(userAddr).storage.copy<Bool>(from: /storage/incrementFiTerms) ?? false
}
```