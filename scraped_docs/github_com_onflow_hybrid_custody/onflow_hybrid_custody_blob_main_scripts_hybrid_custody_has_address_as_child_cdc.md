# Source: https://github.com/onflow/hybrid-custody/blob/main/scripts/hybrid-custody/has_address_as_child.cdc

```
import "HybridCustody"

access(all) fun main(parent: Address, child: Address): Bool {
    let acct = getAuthAccount<auth(Storage) &Account>(parent)
    let m = acct.storage.borrow<auth(HybridCustody.Manage) &HybridCustody.Manager>(from: HybridCustody.ManagerStoragePath)
        ?? panic("manager not found")

    let childAccount = m.borrowAccount(addr: child)
        ?? panic("child not found")

    return true
}
```