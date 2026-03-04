# Source: https://github.com/onflow/hybrid-custody/blob/main/transactions/hybrid-custody/unlink_child_capability.cdc

```
import "HybridCustody"

transaction(parent: Address) {
    prepare(acct: auth(Storage, Capabilities) &Account) {
        let storagePath = StoragePath(identifier: HybridCustody.getChildAccountIdentifier(parent))!
        for c in acct.capabilities.storage.getControllers(forPath: storagePath) {
            c.delete()
        }
    }
}
```