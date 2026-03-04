# Source: https://github.com/blocto/blt-contracts/blob/master/transactions/teleport/burnTokensSolana.cdc

```
import "FungibleToken"
import "BloctoToken"
import "TeleportCustodySolana"

transaction(amount: UFix64, from: String, hash: String) {

    // The TeleportControl reference for teleport operations
    let teleportControlRef: auth(TeleportCustodySolana.AdminEntitlement) &{TeleportCustodySolana.TeleportControl}

    prepare(teleportAdmin: auth(BorrowValue) &Account) {
        self.teleportControlRef = teleportAdmin.storage.borrow<auth(TeleportCustodySolana.AdminEntitlement) &{TeleportCustodySolana.TeleportControl}>(from: TeleportCustodySolana.TeleportAdminStoragePath)
            ?? panic("Could not borrow a reference to TeleportControl")
    }

    execute {
        self.teleportControlRef.updateUnlockFee(fee: 0.0)
        let vault <- self.teleportControlRef.unlock(amount: amount, from: from.decodeHex(), txHash: hash)
        self.teleportControlRef.updateUnlockFee(fee: 0.1)

        destroy vault
    }
}

```