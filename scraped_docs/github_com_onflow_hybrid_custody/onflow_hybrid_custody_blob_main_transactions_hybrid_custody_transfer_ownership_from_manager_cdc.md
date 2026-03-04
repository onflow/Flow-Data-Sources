# Source: https://github.com/onflow/hybrid-custody/blob/main/transactions/hybrid-custody/transfer_ownership_from_manager.cdc

```
#allowAccountLinking

import "HybridCustody"

transaction(ownedAddress: Address, owner: Address) {
    prepare(acct: auth(Storage) &Account) {
        let manager = acct.storage.borrow<auth(HybridCustody.Manage) &HybridCustody.Manager>(from: HybridCustody.ManagerStoragePath)
            ?? panic("manager not found")
        manager.giveOwnership(addr: ownedAddress, to: owner)
    }
}
```