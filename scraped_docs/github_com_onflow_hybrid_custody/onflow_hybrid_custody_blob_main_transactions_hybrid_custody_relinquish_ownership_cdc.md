# Source: https://github.com/onflow/hybrid-custody/blob/main/transactions/hybrid-custody/relinquish_ownership.cdc

```
#allowAccountLinking

import "HybridCustody"

transaction {
    prepare(acct: auth(Storage) &Account) {
        let owned = acct.storage.borrow<auth(HybridCustody.Owner) &HybridCustody.OwnedAccount>(from: HybridCustody.OwnedAccountStoragePath)
            ?? panic("owned not found")
        owned.seal()
    }
}
```