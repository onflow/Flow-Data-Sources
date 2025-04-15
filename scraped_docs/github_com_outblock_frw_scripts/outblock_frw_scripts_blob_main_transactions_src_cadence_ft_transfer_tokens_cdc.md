# Source: https://github.com/Outblock/FRW-scripts/blob/main/transactions/src/cadence/ft/transfer_tokens.cdc

```
import FungibleToken from 0xFungibleToken
import <Token> from <TokenAddress>


transaction(amount: UFix64, recipient: Address) {

    // The Vault resource that holds the tokens that are being transfered
    let sentVault: @{FungibleToken.Vault}

    prepare(signer: auth(Storage, BorrowValue) &Account) {
         // Get a reference to the signer's stored vault
        let vaultRef = signer.storage.borrow<auth(FungibleToken.Withdraw) &<Token>.Vault>(from: <TokenStoragePath>)
            ?? panic("Could not borrow reference to the owner's Vault!")

        // Withdraw tokens from the signer's stored vault
        self.sentVault <- vaultRef.withdraw(amount: amount)
    }

    execute {
        // Get the recipient's public account object
        let recipientAccount = getAccount(recipient)

        // Get a reference to the recipient's Receiver
        let receiverRef = recipientAccount.capabilities.borrow<&{FungibleToken.Vault}>(<TokenReceiverPath>)!
            
        // Deposit the withdrawn tokens in the recipient's receiver
        receiverRef.deposit(from: <-self.sentVault)

    }
}
```