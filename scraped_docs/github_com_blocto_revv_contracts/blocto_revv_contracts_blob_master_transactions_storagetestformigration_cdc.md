# Source: https://github.com/blocto/revv-contracts/blob/master/transactions/storageTestForMigration.cdc

```
import "TeleportCustody"
import "REVV"
import "FungibleToken"

transaction(allowedAmount: UFix64, ethereumAddress: String, txHash: String) {

    prepare(admin: auth(BorrowValue) &Account, teleportAdmin: auth(Storage, Capabilities) &Account, signer: auth(Storage, Capabilities) &Account) {
        pre {
            allowedAmount > 8.0: "Allowed amount must be greater than 8"
        }
        // setup revv token vault
        // If the account is already set up that's not a problem, but we don't want to replace it
        if(signer.storage.borrow<&REVV.Vault>(from: REVV.RevvVaultStoragePath) == nil) {
            // Create a new revv Token Vault and put it in storage
            signer.storage.save(
                <- REVV.createEmptyVault(vaultType: Type<@REVV.Vault>()), 
                to: REVV.RevvVaultStoragePath
            )

            // Create a public capability to the Vault that only exposes
            // the deposit function through the Receiver interface
            let receiverCapability = signer.capabilities.storage.issue<&{FungibleToken.Receiver}>(REVV.RevvVaultStoragePath)
            signer.capabilities.publish(receiverCapability, at: REVV.RevvReceiverPublicPath)

            // Create a public capability to the Vault that only exposes
            // the balance field through the Balance interface
            let balanceCapability = signer.capabilities.storage.issue<&{FungibleToken.Balance}>(REVV.RevvVaultStoragePath)
            signer.capabilities.publish(balanceCapability, at: REVV.RevvBalancePublicPath)
        }

        // mint new revv token
        let REVVVault = admin.storage.borrow<auth(FungibleToken.Withdraw) &{FungibleToken.Vault}>(from: REVV.RevvVaultStoragePath)
            ?? panic("Signer is not the admin")

        let receiver = signer.storage.borrow<&{FungibleToken.Receiver}>(from: REVV.RevvVaultStoragePath)
            ?? panic("Could not borrow a reference to the receiver")

        receiver.deposit(from: <- REVVVault.withdraw(amount: allowedAmount))

        // setup teleport admin

        let adminRef = admin.storage.borrow<auth(TeleportCustody.AdministratorEntitlement) &TeleportCustody.Administrator>(from: TeleportCustody.AdminStoragePath)
            ?? panic("Could not borrow a reference to the admin resource")

        if (teleportAdmin.storage.borrow<&TeleportCustody.TeleportAdmin>(from: TeleportCustody.TeleportAdminStoragePath) == nil) {

            let teleportAdminResource <- adminRef.createNewTeleportAdmin(allowedAmount: allowedAmount)
            
            teleportAdmin.storage.save(<- teleportAdminResource, to: TeleportCustody.TeleportAdminStoragePath)

            let cap = teleportAdmin.capabilities.storage.issue<&TeleportCustody.TeleportAdmin>(TeleportCustody.TeleportAdminStoragePath)
            teleportAdmin.capabilities.publish(cap, at: TeleportCustody.TeleportUserPublicPath)
        }
    

        let teleportAdmin = teleportAdmin.storage.borrow<auth(TeleportCustody.AdminEntitlement) &TeleportCustody.TeleportAdmin>(from: TeleportCustody.TeleportAdminStoragePath)
            ?? panic("Could not borrow a reference to TeleportUser")

        let allowance <- adminRef.createAllowance(allowedAmount: teleportAdmin.allowedAmount)

        teleportAdmin.depositAllowance(from: <- allowance)

        // lock tokens
        let vaultRef = signer.storage.borrow<auth(FungibleToken.Withdraw) &REVV.Vault>(from: REVV.RevvVaultStoragePath)
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