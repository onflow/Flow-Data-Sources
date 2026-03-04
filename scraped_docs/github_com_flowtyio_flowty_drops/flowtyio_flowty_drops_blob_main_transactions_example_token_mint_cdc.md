# Source: https://github.com/Flowtyio/flowty-drops/blob/main/transactions/example-token/mint.cdc

```
import "ExampleToken"
import "FungibleToken"
import "FungibleTokenMetadataViews"

transaction(to: Address, amount: UFix64) {
    prepare(acct: auth(Storage) &Account) {
        let tokens <- ExampleToken.mintTokens(amount: amount)
        let ftVaultData = tokens.resolveView(Type<FungibleTokenMetadataViews.FTVaultData>())! as! FungibleTokenMetadataViews.FTVaultData
        getAccount(to).capabilities.get<&{FungibleToken.Receiver}>(ftVaultData.receiverPath).borrow()!.deposit(from: <-tokens)
    }
}
```