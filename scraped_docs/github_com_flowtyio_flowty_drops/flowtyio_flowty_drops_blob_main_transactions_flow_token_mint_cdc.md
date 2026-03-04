# Source: https://github.com/Flowtyio/flowty-drops/blob/main/transactions/flow-token/mint.cdc

```
import "FlowToken"
import "FungibleToken"

transaction(receiver: Address, amount: UFix64) {
    prepare(acct: auth(BorrowValue) &Account) {
        let admin = acct.storage.borrow<&FlowToken.Administrator>(from: /storage/flowTokenAdmin)
            ?? panic("flow token admin not found")

        let minter <- admin.createNewMinter(allowedAmount: amount)
        let tokens <- minter.mintTokens(amount: amount)

        getAccount(receiver).capabilities.get<&{FungibleToken.Receiver}>(/public/flowTokenReceiver).borrow()!.deposit(from: <-tokens)
        destroy minter
    }
}
```