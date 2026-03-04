# Source: https://github.com/IncrementFi/Swap/blob/main/src/transactions/test/mint_flow_emulator.cdc

```
import FungibleToken from "../../contracts/env/FungibleToken.cdc"
import FlowToken from "../../contracts/tokens/FlowToken.cdc"


transaction(to: Address, amount: UFix64) {
    prepare(signer: auth(Storage) &Account) {
        log("Transaction Start --------------- emulator_flow_transfer")

        log("account deposit FlowToken".concat(amount.toString()))
        // Get a reference to the signer's stored vault
        let vaultRef = signer.storage.borrow<auth(FungibleToken.Withdraw) &FlowToken.Vault>(from: /storage/flowTokenVault)
          ?? panic("Could not borrow reference to the owner's Vault!")

        // Withdraw tokens from the signer's stored vault
        let sentVault <- vaultRef.withdraw(amount: amount)

        // Get a reference to the recipient's Receiver
        let receiverRef =  getAccount(to).capabilities.borrow<&{FungibleToken.Receiver}>(/public/flowTokenReceiver)
            ?? panic("Could not borrow receiver reference to the recipient's Vault")

        // Deposit the withdrawn tokens in the recipient's receiver
        receiverRef.deposit(from: <-sentVault)

        log("End -----------------------------")
    }

    execute {
    }
}
```