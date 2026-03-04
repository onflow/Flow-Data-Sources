# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/hw_v1/transactions/hw_v1_setup_usdc_vault.cdc

```
// This transaction is a template for a transaction to allow 
// anyone to add a Vault resource to their account so that 
// they can use the FiatTokenf (usdc)
import FungibleToken from "./../contracts/utility/FungibleToken.cdc"
import FiatToken from "./../contracts/utility/FiatToken.cdc"

transaction {

    prepare(signer: AuthAccount) {

        // Return early if the account already stores a FiatToken Vault
        if signer.borrow<&FiatToken.Vault>(from: FiatToken.VaultStoragePath) != nil {
            return
        }

        // Create a new FiatToken Vault and put it in storage
        signer.save(
            <-FiatToken.createEmptyVault(),
            to: FiatToken.VaultStoragePath
        )

        // Create a public capability to the Vault that only exposes
        // the deposit function through the Receiver interface
        signer.link<&FiatToken.Vault{FungibleToken.Receiver}>(
            FiatToken.VaultReceiverPubPath,
            target: FiatToken.VaultStoragePath
        )

        // Create a public capability to the Vault that only exposes
        // the balance field through the Balance interface
        signer.link<&FiatToken.Vault{FungibleToken.Balance}>(
            FiatToken.VaultBalancePubPath,
            target: FiatToken.VaultStoragePath
        )
    }
}
```