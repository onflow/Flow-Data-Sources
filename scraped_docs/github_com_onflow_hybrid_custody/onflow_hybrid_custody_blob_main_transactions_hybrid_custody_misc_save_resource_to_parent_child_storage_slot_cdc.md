# Source: https://github.com/onflow/hybrid-custody/blob/main/transactions/hybrid-custody/misc/save_resource_to_parent_child_storage_slot.cdc

```
import "ExampleToken"
import "HybridCustody"

transaction(parent: Address) {
    prepare(acct: auth(Storage) &Account) {
        let v <- ExampleToken.createEmptyVault(vaultType: Type<@ExampleToken.Vault>())
        let identifier = HybridCustody.getChildAccountIdentifier(parent)
        let storagePath = StoragePath(identifier: identifier)!
        acct.storage.save(<-v, to: storagePath)
    }
}
```