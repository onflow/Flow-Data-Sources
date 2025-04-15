# Source: https://github.com/Outblock/FRW-scripts/blob/main/scripts/src/cadence/hybridCustody/get_child_addresses.cdc

```
import HybridCustody from 0xHybridCustody

access(all) fun main(parent: Address): [Address] {
    let acct = getAuthAccount<auth(Storage) &Account>(parent)
    let manager = acct.storage.borrow<&HybridCustody.Manager>(from: HybridCustody.ManagerStoragePath)
        ?? panic("manager not found")
    return  manager.getChildAddresses()
}
```