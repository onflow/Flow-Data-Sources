# Source: https://github.com/blocto/revv-contracts/blob/master/transactions/teleport/withdrawTeleportFees.cdc

```
import "TeleportCustody"
import "FungibleToken"
import "REVV"

transaction(feeReceiver: Address) {
  prepare(teleportAdmin: auth(BorrowValue) &Account) {
    let teleportAdminRef = teleportAdmin.storage.borrow<auth(TeleportCustody.AdminEntitlement) &TeleportCustody.TeleportAdmin>(from: TeleportCustody.TeleportAdminStoragePath)
        ?? panic("Could not borrow a reference to the teleport admin resource")
    
    let fee <- teleportAdminRef.withdrawFee(amount: teleportAdminRef.getFeeAmount())

    let receiverRef = getAccount(feeReceiver).capabilities.borrow<&{FungibleToken.Receiver}>(REVV.RevvReceiverPublicPath)
			?? panic("Could not borrow receiver reference to the recipient's Vault")
    receiverRef.deposit(from: <- fee)
  }
}

```