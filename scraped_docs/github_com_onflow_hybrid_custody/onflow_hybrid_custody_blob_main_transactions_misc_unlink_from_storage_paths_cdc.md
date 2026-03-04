# Source: https://github.com/onflow/hybrid-custody/blob/main/transactions/misc/unlink_from_storage_paths.cdc

```
transaction(storagePaths: [StoragePath]) {
    prepare(acct: auth(Capabilities) &Account) {
        for storagePath in storagePaths {
            let controllers = acct.capabilities.storage.getControllers(forPath: storagePath)
            for con in controllers {
                acct.capabilities.storage.getController(byCapabilityID: con.capabilityID)?.delete()
            }
        }
    }
}
```