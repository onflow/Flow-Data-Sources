# Source: https://github.com/Flowtyio/flowty-drops/blob/main/transactions/util/send_flow_tokens.cdc

```
import "FungibleToken"

transaction(to: Address, amount: UFix64) {
    prepare(acct: auth(BorrowValue) &Account) {
        let receiver = getAccount(to).capabilities.get<&{FungibleToken.Receiver}>(/public/flowTokenReceiver)
            .borrow() ?? panic("receiver not found")
        
        let provider = acct.storage.borrow<auth(FungibleToken.Withdraw)&{FungibleToken.Provider}>(from: /storage/flowTokenVault)!
        let tokens <- provider.withdraw(amount: amount)
        receiver.deposit(from: <-tokens)
    }
}
```