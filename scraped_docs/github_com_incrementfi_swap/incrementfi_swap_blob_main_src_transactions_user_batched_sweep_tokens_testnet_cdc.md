# Source: https://github.com/IncrementFi/Swap/blob/main/src/transactions/user/batched_sweep_tokens.testnet.cdc

```
import FungibleToken from "../../contracts/env/FungibleToken.cdc"
import FlowToken from "../../contracts/tokens/FlowToken.cdc"
import StableSwapFactory from "../../contracts/StableSwapFactory.cdc"
import SwapFactory from "../../contracts/SwapFactory.cdc"
import SwapInterfaces from "../../contracts/SwapInterfaces.cdc"
import SwapConfig from "../../contracts/SwapConfig.cdc"

transaction(
    tokenKeys: [String],
    vaultPathPrefixs: [String],
    amountsIn: [UFix64]
) {
    prepare(userAccount: auth(BorrowValue) &Account) {
        let flowTokenKey = "A.7e60df042a9c0868.FlowToken"
        let flowVault = userAccount.storage.borrow<&FlowToken.Vault>(from: /storage/flowTokenVault)!;

        var i = 0
        for vaultPathPrefix in vaultPathPrefixs {
            let vaultPath = StoragePath(identifier: vaultPathPrefix)!
            var tokenVaultRef = userAccount.storage.borrow<auth(FungibleToken.Withdraw) &{FungibleToken.Vault}>(from: vaultPath)
            if tokenVaultRef == nil {continue}
            let balance = tokenVaultRef!.balance
            var amountIn = amountsIn[i]
            if amountIn == 0.0 || amountIn > balance {amountIn = balance}
            let sPairAddr = StableSwapFactory.getPairAddress(token0Key: flowTokenKey, token1Key: tokenKeys[i])
            let vPairAddr = SwapFactory.getPairAddress(token0Key: flowTokenKey, token1Key: tokenKeys[i])
            var sAmountOut = 0.0
            var vAmountOut = 0.0
            if sPairAddr != nil {
                var sPoolFlowReserve = 0.0
                let poolRef = getAccount(sPairAddr!).capabilities.borrow<&{SwapInterfaces.PairPublic}>(SwapConfig.PairPublicPath)!
                let poolInfo = poolRef.getPairInfo()
                let token0Key = poolInfo[0] as! String
                let token1Key = poolInfo[1] as! String
                if token0Key == flowTokenKey { sPoolFlowReserve = poolInfo[2] as! UFix64 }
                else { sPoolFlowReserve = poolInfo[3] as! UFix64 }
                if amountIn > 0.0 && sPoolFlowReserve > 0.0 {
                    sAmountOut = poolRef.getAmountOut(amountIn: amountIn, tokenInKey: tokenKeys[i])
                }
            }
            if vPairAddr != nil {
                var vPoolFlowReserve = 0.0
                let poolRef = getAccount(vPairAddr!).capabilities.borrow<&{SwapInterfaces.PairPublic}>(SwapConfig.PairPublicPath)!
                let poolInfo = poolRef.getPairInfo()
                let token0Key = poolInfo[0] as! String
                let token1Key = poolInfo[1] as! String
                if token0Key == flowTokenKey { vPoolFlowReserve = poolInfo[2] as! UFix64 }
                else { vPoolFlowReserve = poolInfo[3] as! UFix64 }
                if amountIn > 0.0 && vPoolFlowReserve > 0.0 {
                    vAmountOut = poolRef.getAmountOut(amountIn: amountIn, tokenInKey: tokenKeys[i])
                }
            }
            if sAmountOut >= 0.0 && sAmountOut >= vAmountOut {
                let poolRef = getAccount(sPairAddr!).capabilities.borrow<&{SwapInterfaces.PairPublic}>(SwapConfig.PairPublicPath)!
                flowVault.deposit(from: <-poolRef.swap(vaultIn: <-tokenVaultRef!.withdraw(amount: amountIn), exactAmountOut: nil))
            } else if vAmountOut >= 0.0 && vAmountOut > sAmountOut {
                let poolRef = getAccount(vPairAddr!).capabilities.borrow<&{SwapInterfaces.PairPublic}>(SwapConfig.PairPublicPath)!
                flowVault.deposit(from: <-poolRef.swap(vaultIn: <-tokenVaultRef!.withdraw(amount: amountIn), exactAmountOut: nil))
            }
            i = i + 1
        }
    }
}
```