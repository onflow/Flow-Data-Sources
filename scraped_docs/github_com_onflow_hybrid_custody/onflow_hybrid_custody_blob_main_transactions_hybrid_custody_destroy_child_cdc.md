# Source: https://github.com/onflow/hybrid-custody/blob/main/transactions/hybrid-custody/destroy_child.cdc

```
import "HybridCustody"
import "Burner"

transaction(parent: Address) {
    prepare(acct: auth(Storage) &Account) {
        let s = StoragePath(identifier: HybridCustody.getChildAccountIdentifier(parent))!
        let m <- acct.storage.load<@AnyResource>(from: s)
            ?? panic("no resource found in child account storage path")
        Burner.burn(<- m)
    }
}
```