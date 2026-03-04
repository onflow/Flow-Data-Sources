# Source: https://github.com/blocto/revv-contracts/blob/master/transactions/replenishTeleportRevv.cdc

```
import "REVV"
import "REVVVaultAccess"
import "TeleportCustody"

transaction(teleportAdminAddress: Address, amount: UFix64) {
  let vaultProxyRef: &REVVVaultAccess.VaultProxy
  let adminRef: auth(TeleportCustody.AdministratorEntitlement) &TeleportCustody.Administrator

  prepare(acct: auth(BorrowValue) &Account) {
    self.vaultProxyRef = acct.storage.borrow<&REVVVaultAccess.VaultProxy>(from: REVVVaultAccess.VaultProxyStoragePath)!
    self.adminRef = acct.storage.borrow<auth(TeleportCustody.AdministratorEntitlement) &TeleportCustody.Administrator>(from: TeleportCustody.AdminStoragePath)
      ?? panic("Could not borrow a reference to the admin resource")
  }

  execute {
    // Add allowance to teleport admin
    let allowance <- self.adminRef.createAllowance(allowedAmount: amount)

    let teleportUserRef = getAccount(teleportAdminAddress).capabilities.borrow<&{TeleportCustody.TeleportUser}>(TeleportCustody.TeleportUserPublicPath)
      ?? panic("Could not borrow a reference to TeleportUser")

    teleportUserRef.depositAllowance(from: <- allowance)

    // Withdraw from VaultProxy and deposit into contract
    let revvVault <- self.vaultProxyRef.withdraw(amount: amount)
    self.adminRef.depositRevv(from: <- (revvVault as! @REVV.Vault))
  }
}

```