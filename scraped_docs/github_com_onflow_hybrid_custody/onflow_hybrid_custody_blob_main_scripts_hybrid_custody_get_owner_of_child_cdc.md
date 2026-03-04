# Source: https://github.com/onflow/hybrid-custody/blob/main/scripts/hybrid-custody/get_owner_of_child.cdc

```
import "HybridCustody"

access(all) fun main(addr: Address): Address? {
    let acct = getAuthAccount<auth(Storage) &Account>(addr)
    let o = acct.storage.borrow<&HybridCustody.OwnedAccount>(from: HybridCustody.OwnedAccountStoragePath)
        ?? panic("owned account missing")
    
    return o.getOwner()
}
```