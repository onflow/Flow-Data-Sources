# Source: https://github.com/onflow/hybrid-custody/blob/main/transactions/hybrid-custody/destroy_owned_account.cdc

```
import "HybridCustody"
import "Burner"

transaction {
    prepare(acct: auth(Storage) &Account) {
        let m <- acct.storage.load<@AnyResource>(from: HybridCustody.OwnedAccountStoragePath)
            ?? panic("no resource found in owned account storage path")
        Burner.burn(<- m)
    }
}
```