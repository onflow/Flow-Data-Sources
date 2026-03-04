# Source: https://github.com/onflow/bridged-usdc/blob/main/transactions/setup_account.cdc

```
// This script is used to add a Vault resource to their account so that they can use USDCFlow 
//
// If the Vault already exist for the account, the script will return immediately without error
// 
import "FungibleToken"
import "USDCFlow"

transaction {

    prepare(signer: auth(Storage, BorrowValue, Capabilities, AddContract) &Account) {

        // Return early if the account already stores a USDCFlow Vault
        if signer.storage.borrow<&USDCFlow.Vault>(from: USDCFlow.VaultStoragePath) != nil {
            return
        }

        // Create a new ExampleToken Vault and put it in storage
        signer.storage.save(
            <-USDCFlow.createEmptyVault(vaultType: Type<@USDCFlow.Vault>()),
            to: USDCFlow.VaultStoragePath
        )

        let receiver = signer.capabilities.storage.issue<&USDCFlow.Vault>(
            USDCFlow.VaultStoragePath
        )
        signer.capabilities.publish(receiver, at: USDCFlow.ReceiverPublicPath)
        signer.capabilities.publish(receiver, at: USDCFlow.VaultPublicPath)
    }
}

```