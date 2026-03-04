# Source: https://github.com/blocto/revv-contracts/blob/master/transactions/teleport/setupTeleportAdmin.cdc

```
import "TeleportCustody"

transaction(amount: UFix64) {
  prepare(admin: auth(BorrowValue) &Account, teleportAdmin: auth(SaveValue, Capabilities) &Account) {

    let adminRef = admin.storage.borrow<auth(TeleportCustody.AdministratorEntitlement) &TeleportCustody.Administrator>(from: TeleportCustody.AdminStoragePath)
        ?? panic("Could not borrow a reference to the admin resource")

    let teleportAdminRes <- adminRef.createNewTeleportAdmin(allowedAmount: amount)

    teleportAdmin.storage.save(<- teleportAdminRes, to: TeleportCustody.TeleportAdminStoragePath)

    let cap = teleportAdmin.capabilities.storage.issue<&TeleportCustody.TeleportAdmin>(TeleportCustody.TeleportAdminStoragePath)
    teleportAdmin.capabilities.publish(cap, at: TeleportCustody.TeleportUserPublicPath)
  }
}

```