# Source: https://github.com/onflow/hybrid-custody/blob/main/transactions/hybrid-custody/metadata/set_child_account_display_to_nil.cdc

```
import "HybridCustody"

transaction(childAddress: Address) {
    prepare(acct: auth(Storage) &Account) {
        let m = acct.storage.borrow<auth(HybridCustody.Manage) &HybridCustody.Manager>(from: HybridCustody.ManagerStoragePath)
            ?? panic("manager not found")

        m.setChildAccountDisplay(address: childAddress, nil)
    }
}
```