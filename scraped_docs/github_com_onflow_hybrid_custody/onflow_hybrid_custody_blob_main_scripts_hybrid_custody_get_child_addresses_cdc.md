# Source: https://github.com/onflow/hybrid-custody/blob/main/scripts/hybrid-custody/get_child_addresses.cdc

```
import "HybridCustody"

access(all) fun main(parent: Address): [Address] {
    let acct = getAuthAccount<auth(Storage) &Account>(parent)
    let manager = acct.storage.borrow<&HybridCustody.Manager>(from: HybridCustody.ManagerStoragePath)
        ?? panic("manager not found")
    return  manager.getChildAddresses()
}
```