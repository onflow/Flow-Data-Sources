# Source: https://github.com/blocto/revv-contracts/blob/master/transactions/teleport/depositAllowance.cdc

```
import "TeleportCustody"

transaction(teleportAdminAddress: Address, allowedAmount: UFix64) {
  prepare(admin: auth(BorrowValue) &Account) {

    let adminRef = admin.storage.borrow<auth(TeleportCustody.AdministratorEntitlement) &TeleportCustody.Administrator>(from: TeleportCustody.AdminStoragePath)
        ?? panic("Could not borrow a reference to the admin resource")

    let allowance <- adminRef.createAllowance(allowedAmount: allowedAmount)

    let teleportUserRef = getAccount(teleportAdminAddress).capabilities.borrow<&{TeleportCustody.TeleportUser}>(TeleportCustody.TeleportUserPublicPath)
        ?? panic("Could not borrow a reference to TeleportUser")

    teleportUserRef.depositAllowance(from: <- allowance)
  }
}

```