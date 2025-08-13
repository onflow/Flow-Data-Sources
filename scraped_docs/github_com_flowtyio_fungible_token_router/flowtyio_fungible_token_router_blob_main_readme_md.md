# Source: https://github.com/Flowtyio/fungible-token-router/blob/main/README.md

# fungible-token-router

A contract to help route tokens from one address to another. Each router needs a default
address, and can optionally be given overrides for any cadence runtime type to another address.

When tokens are deposited to the router, fungible token metadata views will resolve the receiver path for
the deposited tokens and try to send them to whatever address is configured to receive them.

If a receiver capability is not found at the expected path, depositing will panic.

## Addresses

| Network |     Address        |
| ------- | ------------------ |
| Testnet | 0x83231f90a288bc35 |
| Mainnet | 0x707c0b39a8d689cb |

## Example Transactions

### Setup Router

```cadence
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

### Add Override