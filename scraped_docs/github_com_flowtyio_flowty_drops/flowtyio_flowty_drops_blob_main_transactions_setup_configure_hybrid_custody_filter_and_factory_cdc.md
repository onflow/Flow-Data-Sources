# Source: https://github.com/Flowtyio/flowty-drops/blob/main/transactions/setup/configure_hybrid_custody_filter_and_factory.cdc

```
import "FTAllFactory"
import "CapabilityFilter"
import "CapabilityFactory"
import "FungibleToken"

transaction {
    prepare(acct: auth(Storage, Capabilities) &Account) {
        if acct.storage.type(at: CapabilityFilter.StoragePath) == nil {
            acct.storage.save(<- CapabilityFilter.createFilter(Type<@CapabilityFilter.AllowAllFilter>()), to: CapabilityFilter.StoragePath)

            acct.capabilities.unpublish(CapabilityFilter.PublicPath)
            acct.capabilities.publish(
                acct.capabilities.storage.issue<&{CapabilityFilter.Filter}>(CapabilityFilter.StoragePath),
                at: CapabilityFilter.PublicPath
            )
        }

        if acct.storage.type(at: CapabilityFactory.StoragePath) == nil {
            acct.storage.save(<- CapabilityFactory.createFactoryManager(), to: CapabilityFactory.StoragePath)

            acct.capabilities.unpublish(CapabilityFactory.PublicPath)
            acct.capabilities.publish(
                acct.capabilities.storage.issue<&CapabilityFactory.Manager>(CapabilityFactory.StoragePath),
                at: CapabilityFactory.PublicPath
            )

            let manager = acct.storage.borrow<auth(CapabilityFactory.Add) &CapabilityFactory.Manager>(from: CapabilityFactory.StoragePath)
                ?? panic("manager not found")
            manager.addFactory(Type<auth(FungibleToken.Withdraw) &{FungibleToken.Provider, FungibleToken.Balance, FungibleToken.Receiver}>(), FTAllFactory.Factory())
            manager.addFactory(Type<auth(FungibleToken.Withdraw) &{FungibleToken.Provider}>(), FTAllFactory.Factory())
            manager.addFactory(Type<&{FungibleToken.Balance}>(), FTAllFactory.Factory())
            manager.addFactory(Type<&{FungibleToken.Receiver}>(), FTAllFactory.Factory())
            manager.addFactory(Type<&{FungibleToken.Receiver, FungibleToken.Balance}>(), FTAllFactory.Factory())
        }
    }
}
```