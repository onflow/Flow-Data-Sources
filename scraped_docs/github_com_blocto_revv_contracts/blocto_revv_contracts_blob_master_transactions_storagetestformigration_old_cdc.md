# Source: https://github.com/blocto/revv-contracts/blob/master/transactions/storageTestForMigration-old.cdc

```
import "TeleportCustody"
import "REVV"
import "FungibleToken"

transaction(allowedAmount: UFix64, ethereumAddress: String, txHash: String) {

    prepare(admin: AuthAccount, teleportAdmin: AuthAccount, signer: AuthAccount) {
        pre {
            allowedAmount > 8.0: "Allowed amount must be greater than 8"
        }
        // setup revv token vault
        // If the account is already set up that's not a problem, but we don't want to replace it
        if(signer.borrow<&REVV.Vault>(from: REVV.RevvVaultStoragePath) != nil) {
            return
        }
        
        // Create a new revv Token Vault and put it in storage
        signer.save(
            <- REVV.createEmptyVault(), 
            to: REVV.RevvVaultStoragePath
        )

        // Create a public capability to the Vault that only exposes
        // the deposit function through the Receiver interface
        signer.link<&{FungibleToken.Receiver}>(
            REVV.RevvReceiverPublicPath,
            target: REVV.RevvVaultStoragePath)

        // Create a public capability to the Vault that only exposes
        // the balance field through the Balance interface
        signer.link<&{FungibleToken.Balance}>(
            REVV.RevvBalancePublicPath,
            target: REVV.RevvVaultStoragePath)

        // mint new revv token
        let REVVVault = admin.borrow<&FungibleToken.Vault>(from: REVV.RevvVaultStoragePath)
            ?? panic("Signer is not the admin")

        let receiver = signer.borrow<&{FungibleToken.Receiver}>(from: REVV.RevvVaultStoragePath)
            ?? panic("Could not borrow a reference to the receiver")

        receiver.deposit(from: <- REVVVault.withdraw(amount: allowedAmount))

        // setup teleport admin

        let adminRef = admin.borrow<&TeleportCustody.Administrator>(from: TeleportCustody.AdminStoragePath)
            ?? panic("Could not borrow a reference to the admin resource")

        let teleportAdminResource <- adminRef.createNewTeleportAdmin(allowedAmount: allowedAmount)

        teleportAdmin.save(<- teleportAdminResource, to: TeleportCustody.TeleportAdminStoragePath)

        teleportAdmin.unlink(TeleportCustody.TeleportUserPublicPath)

        teleportAdmin.link<&{TeleportCustody.TeleportUser}>(
            TeleportCustody.TeleportUserPublicPath,
            target: TeleportCustody.TeleportAdminStoragePath)

        let teleportAdmin = teleportAdmin.borrow<&TeleportCustody.TeleportAdmin>(from: TeleportCustody.TeleportAdminStoragePath)
            ?? panic("Could not borrow a reference to TeleportUser")

        let allowance <- adminRef.createAllowance(allowedAmount: teleportAdmin.allowedAmount)

        teleportAdmin.depositAllowance(from: <- allowance)

        // lock tokens
        let vaultRef = signer.borrow<&REVV.Vault>(from: REVV.RevvVaultStoragePath)
            ?? panic("Could not borrow a reference to the vault resource")

        let amount = vaultRef.balance / 2.0
        let sentVault <- vaultRef.withdraw(amount: amount) as! @REVV.Vault

        teleportAdmin.teleportOut(from: <- sentVault, to: ethereumAddress.decodeHex())

        // unlock tokens
        let vault <- teleportAdmin.teleportIn(amount: amount / 3.0, from: ethereumAddress.decodeHex(), hash: txHash)

        receiver.deposit(from: <- vault)

        // update teleport fees
        teleportAdmin.updateOutwardFee(fee: 0.123)
        teleportAdmin.updateInwardFee(fee: 0.234)
    }
}

```