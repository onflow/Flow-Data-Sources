# Source: https://github.com/onflow/hybrid-custody/blob/main/transactions/hybrid-custody/remove_owned_account.cdc

```
import "HybridCustody"

transaction(addr: Address) {
    prepare(acct: auth(Storage) &Account) {
        let m = acct.storage.borrow<auth(HybridCustody.Manage) &HybridCustody.Manager>(from: HybridCustody.ManagerStoragePath)
            ?? panic("manager not found")
        
        m.removeOwned(addr: addr)
    }
}
```