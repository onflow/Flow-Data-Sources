# Source: https://github.com/onflow/hybrid-custody/blob/main/transactions/hybrid-custody/set_capability_factory_for_parent.cdc

```
import "HybridCustody"
import "CapabilityFactory"

transaction(parent: Address, factoryAddress: Address) {
    prepare(acct: auth(Storage) &Account) {
        let cap = getAccount(factoryAddress).capabilities.get<&CapabilityFactory.Manager>(CapabilityFactory.PublicPath)
        
        let ownedAccount = acct.storage.borrow<auth(HybridCustody.Owner) &{HybridCustody.OwnedAccountPrivate}>(from: HybridCustody.OwnedAccountStoragePath)
            ?? panic("owned account not found")
        ownedAccount.setCapabilityFactoryForParent(parent: parent, cap: cap)
    }
}
```