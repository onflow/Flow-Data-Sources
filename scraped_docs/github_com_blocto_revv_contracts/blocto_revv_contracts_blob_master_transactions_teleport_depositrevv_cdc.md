# Source: https://github.com/blocto/revv-contracts/blob/master/transactions/teleport/depositRevv.cdc

```
import "REVV"
import "TeleportCustody"
import "FungibleToken"

transaction(amount: UFix64) {
  prepare(admin: auth(BorrowValue) &Account) {

    let adminRef = admin.storage.borrow<auth(TeleportCustody.AdministratorEntitlement) &TeleportCustody.Administrator>(from: TeleportCustody.AdminStoragePath)
      ?? panic("Could not borrow a reference to the admin resource")

    let revvVaultRef = admin.storage.borrow<auth(FungibleToken.Withdraw) &REVV.Vault>(from: REVV.RevvVaultStoragePath)
      ?? panic("Could not borrow a reference to the REVV vault")

    let revvVault <- revvVaultRef.withdraw(amount: amount)

    adminRef.depositRevv(from: <- (revvVault as! @REVV.Vault))
  }
}

```