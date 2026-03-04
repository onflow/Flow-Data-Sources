# Source: https://github.com/Flowtyio/fungible-token-router/blob/main/transactions/add_override.cdc

```
import "FungibleTokenRouter"

transaction(typeIdentifier: String, address: Address) {
    prepare(acct: auth(BorrowValue) &Account) {
        let tokenType = CompositeType(typeIdentifier) ?? panic("invalid type identifier")

        let router = acct.storage.borrow<auth(FungibleTokenRouter.Owner) &FungibleTokenRouter.Router>(from: FungibleTokenRouter.StoragePath)
            ?? panic("router not found")
        router.addOverride(type: tokenType, addr: address)
    }
}
```