# Source: https://github.com/IncrementFi/Swap/blob/main/src/transactions/user/burn_ft.cdc

```
import FungibleToken from "../../contracts/env/FungibleToken.cdc"
import Burner from "../../contracts/env/Burner.cdc"

transaction(
    amountToBurn: UFix64,
    vaultPath: StoragePath
) {
    prepare(userAccount: auth(BorrowValue) &Account) {
        let vaultRef = userAccount.storage.borrow<auth(FungibleToken.Withdraw) &{FungibleToken.Vault}>(from: vaultPath)
            ?? panic("Could not borrow reference to the owner's Vault!")
        let valutToBurn <- vaultRef.withdraw(amount: amountToBurn)
        Burner.burn(<-valutToBurn)
    }
}
```