# Source: https://github.com/onflow/hybrid-custody/blob/main/scripts/hybrid-custody/get_parent_addresses.cdc

```
import "HybridCustody"

access(all) fun main(child: Address): [Address] {
    let acct = getAuthAccount<auth(Storage) &Account>(child)
    let o = acct.storage.borrow<&HybridCustody.OwnedAccount>(from: HybridCustody.OwnedAccountStoragePath)
        ?? panic("owned account not found")
    return  o.getParentAddresses() 
}
```