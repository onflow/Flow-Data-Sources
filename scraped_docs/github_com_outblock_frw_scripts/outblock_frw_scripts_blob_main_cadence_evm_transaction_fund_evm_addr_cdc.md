# Source: https://github.com/Outblock/FRW-scripts/blob/main/cadence/evm/transaction/fund_evm_addr.cdc

```
import FungibleToken from 0xFungibleToken
import FlowToken from 0xFlowToken
import EVM from 0xEVM

transaction(evmAddr: String, amount: UFix64) {
  let sentVault: @{FungibleToken.Vault}

  prepare(signer: auth(Storage, BorrowValue) &Account) {
    // Get a reference to the signer's stored vault
    let vaultRef = signer.storage.borrow<auth(FungibleToken.Withdraw) &FlowToken.Vault>(from: /storage/flowTokenVault)
      ?? panic("Could not borrow reference to the owner's Vault!")

    // Withdraw tokens from the signer's stored vault
    self.sentVault <- vaultRef.withdraw(amount: amount)
  }

  execute {
    // Get the recipient's public account object
    let recipientAccount = getAccount(evmAddr)

    // Get a reference to the recipient's Receiver
    let receiverRef = recipientAccount.capabilities.borrow<&{FungibleToken.Receiver}>(/public/flowTokenReceiver)!
      
    // Deposit the withdrawn tokens in the recipient's receiver
    receiverRef.deposit(from: <-self.sentVault)
  }
}
```