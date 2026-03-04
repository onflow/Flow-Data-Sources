# Source: https://github.com/blocto/revv-contracts/blob/master/transactions/teleport/teleportIn.cdc

```
import "FungibleToken"
import "REVV"
import "TeleportCustody"

transaction(amount: UFix64, target: Address, from: String, hash: String) {
  prepare(teleportAdmin: auth(BorrowValue) &Account) {
    let teleportControlRef = teleportAdmin.storage.borrow<auth(TeleportCustody.AdminEntitlement) &{TeleportCustody.TeleportControl}>(from: TeleportCustody.TeleportAdminStoragePath)
        ?? panic("Could not borrow a reference to TeleportControl")
    
    let vault <- teleportControlRef.teleportIn(amount: amount, from: from.decodeHex(), hash: hash)

    let receiverRef = getAccount(target).capabilities.borrow<&{FungibleToken.Receiver}>(REVV.RevvReceiverPublicPath)
        ?? panic("Could not borrow a reference to Receiver")

    receiverRef.deposit(from: <- vault)
  }
}
```