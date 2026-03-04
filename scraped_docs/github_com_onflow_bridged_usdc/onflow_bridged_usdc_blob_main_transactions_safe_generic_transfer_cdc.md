# Source: https://github.com/onflow/bridged-usdc/blob/main/transactions/safe_generic_transfer.cdc

```
import FungibleToken from "FungibleToken"

/// Can pass in any storage path and receiver path instead of just the default.
/// This lets you choose the token you want to send as well the capability you want to send it to.
///
/// Any token path can be passed as an argument here, so wallets should
/// should check argument values to make sure the intended token path is passed in
///
transaction(amount: UFix64, to: Address, senderPath: String, receiverPath: String) {

    // The Vault resource that holds the tokens that are being transferred
    let tempVault: @{FungibleToken.Vault}

    // Borrowed teference receive tokens if receiving account doesn't support the sending token
    let senderReceiverRef: &{FungibleToken.Receiver}

    prepare(signer: auth(BorrowValue) &Account) {

        // Get a reference to the signer's stored vault
        let vaultRef = signer.storage.borrow<auth(FungibleToken.Withdraw) &{FungibleToken.Vault}>(from: StoragePath(identifier: senderPath)!)
            ?? panic("Could not borrow a reference to the signer's FungibleToken.Vault"
                     .concat(" from the path ").concat(StoragePath(identifier: senderPath)!.toString())
                     .concat(". Make sure you are signing with the correct account ")
                     .concat(" and that it has a vault stored at that path."))
        
        self.senderReceiverRef = signer.storage.borrow<&{FungibleToken.Receiver}>(from: StoragePath(identifier: senderPath)!)
			?? panic("Could not borrow {FungibleToken.Receiver} reference to the signer's Vault!")

        self.tempVault <- vaultRef.withdraw(amount: amount)
    }

    execute {
        let receiverRef = getAccount(to).capabilities.get<&{FungibleToken.Receiver}>(PublicPath(identifier: receiverPath)!).borrow()
            ?? panic("Could not borrow a {FungibleToken.Receiver} reference to the Vault in account"
                    .concat(to.toString()).concat(". at the path ").concat(PublicPath(identifier: receiverPath)!.toString())
                    .concat(". Make sure the recipient address is correct and that ")
                    .concat("the account being queried has initialized itselt with ")
                    .concat("a Vault and Receiver at that path."))

        let supportedVaultTypes = receiverRef.getSupportedVaultTypes()
        // Only transfer tokens when the receiver is willing to receive the targeted FT.
        if supportedVaultTypes.containsKey(self.tempVault.getType()) {
            // Transfer tokens from the signer's stored vault to the receiver capability
            receiverRef.deposit(from: <-self.tempVault)
        } else {
            self.senderReceiverRef.deposit(from: <-self.tempVault)
        }
    }
}
```