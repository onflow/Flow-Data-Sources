# Source: https://github.com/IncrementFi/Swap/blob/main/src/transactions/user/transfer_ft.cdc

```
import FungibleToken from "../../contracts/env/FungibleToken.cdc"

transaction(
    amountToTransfer: UFix64,
    to: Address,
    vaultPath: StoragePath,
    receiverPath: PublicPath
) {
    prepare(userAccount: auth(BorrowValue) &Account) {
        let vaultRef = userAccount.storage.borrow<auth(FungibleToken.Withdraw) &{FungibleToken.Vault}>(from: vaultPath)
            ?? panic("Could not borrow reference to the owner's Vault!")
        let valutToTransfer <- vaultRef.withdraw(amount: amountToTransfer)

        let receiverRef = getAccount(to).capabilities.borrow<&{FungibleToken.Receiver}>(receiverPath)
            ?? panic("[IncErrorMsg:Could not borrow receiver reference to the recipient's Vault][IncErrorCode:6001]")
        receiverRef.deposit(from: <-valutToTransfer)
    }
}
```