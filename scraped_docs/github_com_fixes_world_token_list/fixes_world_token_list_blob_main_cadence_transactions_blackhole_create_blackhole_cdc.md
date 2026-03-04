# Source: https://github.com/fixes-world/token-list/blob/main/cadence/transactions/blackhole/create-blackhole.cdc

```
import "FungibleToken"
import "BlackHole"

transaction() {
    prepare(acct: auth(Storage, Capabilities) &Account) {
        let ftStoragePath = BlackHole.getBlackHoleReceiverStoragePath()
        if acct.storage.borrow<&AnyResource>(from: ftStoragePath) == nil {
            // create a new BlackHole receiver and save it to the new account's storage
            let blackHole <- BlackHole.createNewBlackHole()
            acct.storage.save(<- blackHole, to: ftStoragePath)

            // Link the public capability to the new account so it can be used
            let cap = acct.capabilities
                .storage.issue<&BlackHole.Receiver>(ftStoragePath)
            acct.capabilities.publish(cap, at: BlackHole.getBlackHoleReceiverPublicPath())
        }

        let nftStoragePath = BlackHole.getBlackHoleCollectionStoragePath()
        if acct.storage.borrow<&AnyResource>(from: nftStoragePath) == nil {
            // create a new BlackHole collection and save it to the new account's storage
            let blackHoleCollection <- BlackHole.createNewBlackHoleCollection()
            acct.storage.save(<- blackHoleCollection, to: nftStoragePath)

            // Link the public capability to the new account so it can be used
            let cap = acct.capabilities
                .storage.issue<&BlackHole.Collection>(nftStoragePath)
            acct.capabilities.publish(cap, at: BlackHole.getBlackHoleCollectionPublicPath())
        }
    }
}

```