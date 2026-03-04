# Source: https://github.com/IncrementFi/Swap/blob/main/src/transactions/user/swap_exact_tokens_for_tokens.cdc

```
import FUSD from "../../contracts/tokens/FUSD.cdc"
import FungibleToken from "../../contracts/env/FungibleToken.cdc"
import SwapRouter from "../../contracts/SwapRouter.cdc"

transaction(
    tokenKeyPath: [String],
    exactAmountIn: UFix64,
    amountOutMin: UFix64,
    deadline: UFix64
) {
    prepare(userAccount: auth(Storage, Capabilities) &Account) {
        let len = tokenKeyPath.length
        let tokenInKey = tokenKeyPath[0]
        let tokenOutKey = tokenKeyPath[len-1]

        let tokenInVaultPath = /storage/flowTokenVault

        let tokenOutVaultPath = /storage/fusdVault
        let tokenOutReceiverPath = /public/fusdReceiver
        let tokenOutBalancePath = /public/fusdBalance

        var tokenOutReceiverRef = userAccount.storage.borrow<&{FungibleToken.Vault}>(from: tokenOutVaultPath)
        if tokenOutReceiverRef == nil {
            userAccount.storage.save(<- FUSD.createEmptyVault(vaultType: Type<@FUSD.Vault>()), to: /storage/fusdVault)
            userAccount.capabilities.publish(
                userAccount.capabilities.storage.issue<&{FungibleToken.Receiver}>(tokenOutVaultPath),
                at: tokenOutReceiverPath
            )
            userAccount.capabilities.publish(
                userAccount.capabilities.storage.issue<&{FungibleToken.Balance}>(tokenOutVaultPath),
                at: tokenOutBalancePath
            )

            tokenOutReceiverRef = userAccount.storage.borrow<&{FungibleToken.Vault}>(from: tokenOutVaultPath)
        }

        let exactVaultIn <- userAccount.storage.borrow<auth(FungibleToken.Withdraw) &{FungibleToken.Vault}>(from: tokenInVaultPath)!.withdraw(amount: exactAmountIn)
        /// 
        let vaultOut <- SwapRouter.swapExactTokensForTokens(
            exactVaultIn: <-exactVaultIn,
            amountOutMin: amountOutMin,
            tokenKeyPath: tokenKeyPath,
            deadline: deadline
        )

        tokenOutReceiverRef!.deposit(from: <-vaultOut)
    }
}
```