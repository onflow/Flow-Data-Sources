# Source: https://github.com/blocto/revv-contracts/blob/master/transactions/teleport/updateTeleportFees.cdc

```
import "TeleportCustody"

transaction(inwardFee: UFix64, outwardFee: UFix64) {
  prepare(teleportAdmin: auth(BorrowValue) &Account) {
    let teleportAdminRef = teleportAdmin.storage.borrow<auth(TeleportCustody.AdminEntitlement) &TeleportCustody.TeleportAdmin>(from: TeleportCustody.TeleportAdminStoragePath)
        ?? panic("Could not borrow a reference to the teleport admin resource")
    
    teleportAdminRef.updateInwardFee(fee: inwardFee)
    teleportAdminRef.updateOutwardFee(fee: outwardFee)
  }
}

```