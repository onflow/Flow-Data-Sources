# Source: https://github.com/IncrementFi/Liquid-Staking/blob/main/cadence/transactions/user/stake_with_swap.cdc

```
import LiquidStaking from "../../contracts/LiquidStaking.cdc"
import stFlowToken from "../../contracts/stFlowToken.cdc"
import FlowToken from "../../contracts/standard/FlowToken.cdc"
import FungibleToken from "../../contracts/standard/FungibleToken.cdc"
import SwapInterfaces from "../../contracts/standard/mainnet/SwapInterfaces.cdc"

transaction(flowAmount: UFix64) {
    prepare(userAccount: auth(Storage, Capabilities) &Account) {
        let flowVault = userAccount.storage.borrow<auth(FungibleToken.Withdraw) &FlowToken.Vault>(from: /storage/flowTokenVault)!
        let inVault <- flowVault.withdraw(amount: flowAmount) as! @FlowToken.Vault
        var stFlowVaultRef = userAccount.storage.borrow<&stFlowToken.Vault>(from: stFlowToken.tokenVaultPath)
        if stFlowVaultRef == nil {
            userAccount.storage.save(<- stFlowToken.createEmptyVault(vaultType: Type<@stFlowToken.Vault>()), to: stFlowToken.tokenVaultPath)
            userAccount.capabilities.unpublish(stFlowToken.tokenReceiverPath)
            userAccount.capabilities.unpublish(stFlowToken.tokenBalancePath)
            userAccount.capabilities.publish(
                userAccount.capabilities.storage.issue<&{FungibleToken.Receiver}>(stFlowToken.tokenVaultPath),
                at: stFlowToken.tokenReceiverPath
            )
            userAccount.capabilities.publish(
                userAccount.capabilities.storage.issue<&{FungibleToken.Balance}>(stFlowToken.tokenVaultPath),
                at: stFlowToken.tokenBalancePath
            )
            stFlowVaultRef = userAccount.storage.borrow<&stFlowToken.Vault>(from: stFlowToken.tokenVaultPath)
        }

        let poolRefV1 = getAccount(0x396c0cda3302d8c5).capabilities.borrow<&{SwapInterfaces.PairPublic}>(/public/increment_swap_pair)!
        let poolRefStable = getAccount(0xc353b9d685ec427d).capabilities.borrow<&{SwapInterfaces.PairPublic}>(/public/increment_swap_pair)!

        let estimatedStakeOut = LiquidStaking.calcStFlowFromFlow(flowAmount: flowAmount)
        let estimatedSwapOutV1 = poolRefV1.getAmountOut(amountIn: flowAmount, tokenInKey: "A.1654653399040a61.FlowToken")
        let estimatedSwapOutStable = poolRefStable.getAmountOut(amountIn: flowAmount, tokenInKey: "A.1654653399040a61.FlowToken")
        let estimatedSwapOut = estimatedSwapOutStable > estimatedSwapOutV1 ? estimatedSwapOutStable:estimatedSwapOutV1
        let estimatedSwapPoolRef = estimatedSwapOutStable > estimatedSwapOutV1 ? poolRefStable : poolRefV1

        if estimatedStakeOut > estimatedSwapOut {
            let outVault <- LiquidStaking.stake(flowVault: <-inVault)
            stFlowVaultRef!.deposit(from: <-outVault)
        } else {
            let outVault <- estimatedSwapPoolRef.swap(vaultIn: <- inVault, exactAmountOut: nil)
            stFlowVaultRef!.deposit(from: <-outVault)
        }
    }
}
```