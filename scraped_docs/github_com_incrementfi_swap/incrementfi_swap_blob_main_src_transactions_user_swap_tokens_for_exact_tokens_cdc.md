# Source: https://github.com/IncrementFi/Swap/blob/main/src/transactions/user/swap_tokens_for_exact_tokens.cdc

```
import FungibleToken from "../../contracts/env/FungibleToken.cdc"
import SwapRouter from "../../contracts/SwapRouter.cdc"

transaction(
    tokenKeyPath: [String],
    amountInMax: UFix64,
    exactAmountOut: UFix64,
    deadline: UFix64
) {
    prepare(userAccount: auth(BorrowValue) &Account) {
        let tokenInVaultPath = /storage/flowTokenVault
        let tokenOutVaultPath = /storage/fusdVault
        
        var tokenOutReceiverRef = userAccount.storage.borrow<&{FungibleToken.Vault}>(from: tokenOutVaultPath)
            ?? panic("cannot borrow reference to tokenOut FT.Vault")

        let vaultInRef = userAccount.storage.borrow<auth(FungibleToken.Withdraw) &{FungibleToken.Vault}>(from: tokenInVaultPath)
            ?? panic("cannot borrow reference to tokenIn FT.Vault")
        let vaultInMax <- vaultInRef.withdraw(amount: amountInMax)

        let swapResVault <- SwapRouter.swapTokensForExactTokens(
            vaultInMax: <-vaultInMax,
            exactAmountOut: exactAmountOut,
            tokenKeyPath: tokenKeyPath,
            deadline: deadline
        )
        let vaultOut <- swapResVault.removeFirst()
        let vaultInLeft <- swapResVault.removeLast()
        destroy swapResVault

        tokenOutReceiverRef.deposit(from: <-vaultOut)
        vaultInRef.deposit(from: <-vaultInLeft)
    }
}
```