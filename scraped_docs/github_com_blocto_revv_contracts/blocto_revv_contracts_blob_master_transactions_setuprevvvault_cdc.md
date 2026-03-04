# Source: https://github.com/blocto/revv-contracts/blob/master/transactions/setupREVVVault.cdc

```
import "FungibleToken"
import "REVV"

transaction {

    prepare(signer: auth(Storage, Capabilities) &Account) {

        // If the account is already set up that's not a problem, but we don't want to replace it
        if(signer.storage.borrow<&REVV.Vault>(from: REVV.RevvVaultStoragePath) != nil) {
            return
        }
        
        // Create a new Blocto Token Vault and put it in storage
        signer.storage.save(<- REVV.createEmptyVault(vaultType: Type<@REVV.Vault>()), to: REVV.RevvVaultStoragePath)

        let receiverCapability = signer.capabilities.storage.issue<&{FungibleToken.Receiver}>(REVV.RevvVaultStoragePath)
        signer.capabilities.publish(receiverCapability, at: REVV.RevvReceiverPublicPath)

        let balanceCapability = signer.capabilities.storage.issue<&{FungibleToken.Balance}>(REVV.RevvVaultStoragePath)
        signer.capabilities.publish(balanceCapability, at: REVV.RevvBalancePublicPath)
    }
}

```