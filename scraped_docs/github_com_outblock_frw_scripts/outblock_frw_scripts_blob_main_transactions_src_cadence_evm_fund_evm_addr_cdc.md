# Source: https://github.com/Outblock/FRW-scripts/blob/main/transactions/src/cadence/evm/fund_evm_addr.cdc

```
import FungibleToken from 0xFungibleToken
import FlowToken from 0xFlowToken
import EVM from 0xEVM

transaction(evmAddr: String, amount: UFix64) {

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
        let receiverRef = recipientAccount.capabilities.borrow<&{FungibleToken.Receiver}>(<TokenReceiverPath>)!
            
        // Deposit the withdrawn tokens in the recipient's receiver
        receiverRef.deposit(from: <-self.sentVault)
    }
}
```