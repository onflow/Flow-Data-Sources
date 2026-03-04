# Source: https://github.com/blocto/blt-contracts/blob/master/transactions/teleport/Ethereum/updateTeleportFeesEthereum.cdc

```
import "TeleportCustodyEthereum"

transaction(lockFee: UFix64, unlockFee: UFix64) {
  prepare(teleportAdmin: auth(BorrowValue) &Account) {
    let teleportAdminRef = teleportAdmin.storage.borrow<auth(TeleportCustodyEthereum.AdminEntitlement) &TeleportCustodyEthereum.TeleportAdmin>(from: TeleportCustodyEthereum.TeleportAdminStoragePath)
        ?? panic("Could not borrow a reference to the teleport admin resource")
    
    teleportAdminRef.updateLockFee(fee: lockFee)
    teleportAdminRef.updateUnlockFee(fee: unlockFee)
  }
}

```