# Source: https://github.com/Flowtyio/fungible-token-router/blob/main/transactions/setup.cdc

```
import "FungibleTokenRouter"
import "FungibleToken"

transaction(defaultAddress: Address) {
    prepare(acct: auth(Storage, Capabilities) &Account) {
        if acct.storage.borrow<&AnyResource>(from: FungibleTokenRouter.StoragePath) == nil {
            let router <- FungibleTokenRouter.createRouter(defaultAddress: defaultAddress)
            acct.storage.save(<-router, to: FungibleTokenRouter.StoragePath)
        }
        
        if !acct.capabilities.get<&{FungibleToken.Receiver}>(FungibleTokenRouter.PublicPath).check() {
            acct.capabilities.publish(
                acct.capabilities.storage.issue<&{FungibleToken.Receiver}>(FungibleTokenRouter.StoragePath),
                at: FungibleTokenRouter.PublicPath
            )
        }
    }
}
```