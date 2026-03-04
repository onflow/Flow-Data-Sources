# Source: https://github.com/fixes-world/token-list/blob/main/cadence/transactions/blackhole/register-new-blackhole.cdc

```
import "FungibleToken"
import "BlackHole"

transaction() {
    prepare(acct: auth(Storage, Capabilities) &Account) {
        let newAcct = Account(payer: acct)

        // create a new BlackHole receiver and save it to the new account's storage
        let blackHole <- BlackHole.createNewBlackHole()
        let storagePath = BlackHole.getBlackHoleReceiverStoragePath()
        newAcct.storage.save(<- blackHole, to: storagePath)

        // Link the public capability to the new account so it can be used
        let pubCap = newAcct.capabilities.storage.issue<&BlackHole.Receiver>(storagePath)
        newAcct.capabilities.publish(pubCap, at: BlackHole.getBlackHoleReceiverPublicPath())

        // register the new account as a black hole receiver
        BlackHole.registerAsBlackHole(newAcct.address)
    }
}

```