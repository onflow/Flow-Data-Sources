# Source: https://github.com/Flowtyio/lost-and-found/blob/main/transactions/depositor/add_flow_tokens.cdc

```
import "LostAndFound"
import "FungibleToken"
import "FlowToken"

transaction(amount: UFix64) {
    prepare(acct: auth(Storage) &Account) {
        let flowVault = acct.storage.borrow<auth(FungibleToken.Withdraw) &FlowToken.Vault>(from: /storage/flowTokenVault)!
        let tokens <- flowVault.withdraw(amount: amount)
        let vault <-tokens as! @FlowToken.Vault

        let depositor = acct.storage.borrow<&LostAndFound.Depositor>(from: LostAndFound.DepositorStoragePath)!
        depositor.addFlowTokens(vault: <- vault)
    }
}

```