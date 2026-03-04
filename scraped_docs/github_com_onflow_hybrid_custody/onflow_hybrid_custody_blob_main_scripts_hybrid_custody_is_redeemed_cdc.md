# Source: https://github.com/onflow/hybrid-custody/blob/main/scripts/hybrid-custody/is_redeemed.cdc

```
import "HybridCustody"

access(all) fun main(child: Address, parent: Address): Bool {
    let acct = getAuthAccount<auth(Storage) &Account>(child)
    let owned = acct.storage.borrow<&HybridCustody.OwnedAccount>(from: HybridCustody.OwnedAccountStoragePath)
        ?? panic("owned account not found")

    return owned.getRedeemedStatus(addr: parent) ?? panic("no status found")
}
```