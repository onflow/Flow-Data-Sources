# Source: https://github.com/IncrementFi/Swap/blob/main/src/transactions/user/add_liquidity_migrate_v1_v2.cdc

```
import FungibleToken from "../../contracts/env/FungibleToken.cdc"
import SwapFactory from "../../contracts/SwapFactory.cdc"
import StableSwapFactory from "../../contracts/StableSwapFactory.cdc"
import SwapInterfaces from "../../contracts/SwapInterfaces.cdc"
import SwapConfig from "../../contracts/SwapConfig.cdc"
import LogEntry from "../../contracts/env/LogEntry.cdc"

transaction(
    token0Key: String,
    token1Key: String,
    lpTokenAmount: UFix64,
    token0VaultPath: StoragePath,
    token1VaultPath: StoragePath
) {
    prepare(userAccount: auth(Storage, Capabilities) &Account) {
        let pairAddrFrom = SwapFactory.getPairAddress(token0Key: token0Key, token1Key: token1Key) ?? panic("AddLiquidity: nonexistent pair ".concat(token0Key).concat(" <-> ").concat(token1Key).concat(", create pair first"))
        let pairAddrTo = StableSwapFactory.getPairAddress(token0Key: token0Key, token1Key: token1Key) ?? panic("AddLiquidity: nonexistent stable pair ".concat(token0Key).concat(" <-> ").concat(token1Key).concat(", create stable pair first"))
        let lpTokenCollectionRef = userAccount.storage.borrow<auth(FungibleToken.Withdraw) &SwapFactory.LpTokenCollection>(from: SwapConfig.LpTokenCollectionStoragePath)
            ?? panic("RemoveLiquidity: cannot borrow reference to LpTokenCollection")
        
        // remove lp
        let lpTokenRemove <- lpTokenCollectionRef.withdraw(pairAddr: pairAddrFrom, amount: lpTokenAmount)
        let tokens <- getAccount(pairAddrFrom).capabilities.borrow<&{SwapInterfaces.PairPublic}>(SwapConfig.PairPublicPath)!.removeLiquidity(lpTokenVault: <-lpTokenRemove)
        let token0Vault <- tokens[0].withdraw(amount: tokens[0].balance)
        let token1Vault <- tokens[1].withdraw(amount: tokens[1].balance)
        destroy tokens

        let token0Amount = token0Vault.balance
        let token1Amount = token1Vault.balance
        // add lp
        let pairPublicRef = getAccount(pairAddrTo).capabilities.borrow<&{SwapInterfaces.PairPublic}>(SwapConfig.PairPublicPath)!
        let pairInfo = pairPublicRef.getPairInfo()
        var token0In = 0.0
        var token1In = 0.0
        var token0Reserve = 0.0
        var token1Reserve = 0.0
        if token0Key == (pairInfo[0] as! String) {
            token0Reserve = (pairInfo[2] as! UFix64)
            token1Reserve = (pairInfo[3] as! UFix64)
        } else {
            token0Reserve = (pairInfo[3] as! UFix64)
            token1Reserve = (pairInfo[2] as! UFix64)
        }
        var token0Left = 0.0
        var token1Left = 0.0
        if token0Reserve == 0.0 && token1Reserve == 0.0 {
            assert (false, message: "Lp migrate cannot be used in initialized pools")
        } else {
            var amount1Optimal = SwapConfig.quote(amountA: token0Amount, reserveA: token0Reserve, reserveB: token1Reserve)
            if (amount1Optimal <= token1Amount) {
                token0In = token0Amount
                token1In = amount1Optimal
                token1Left = token1Amount - amount1Optimal
            } else {
                var amount0Optimal = SwapConfig.quote(amountA: token1Amount, reserveA: token1Reserve, reserveB: token0Reserve)
                assert(amount0Optimal <= token0Amount)
                token0In = amount0Optimal
                token1In = token1Amount
                token0Left = token0Amount - amount0Optimal
            }
        }
        let lpTokenVault <- pairPublicRef.addLiquidity(
            tokenAVault: <- token0Vault.withdraw(amount: token0In),
            tokenBVault: <- token1Vault.withdraw(amount: token1In)
        )

        // zapped add lp
        let pairInfoZapped = pairPublicRef.getPairInfo()
        var token0ReserveZapped = 0.0
        var token1ReserveZapped = 0.0
        if token0Key == (pairInfoZapped[0] as! String) {
            token0ReserveZapped = (pairInfoZapped[2] as! UFix64)
            token1ReserveZapped = (pairInfoZapped[3] as! UFix64)
        } else {
            token0ReserveZapped = (pairInfoZapped[3] as! UFix64)
            token1ReserveZapped = (pairInfoZapped[2] as! UFix64)
        }
        var tokenZappedKey = ""
        var tokenZappedIn = 0.0
        if token0Left > 0.0 {
            tokenZappedKey = token0Key
            tokenZappedIn = token0Left
        }
        if token1Left > 0.0 {
            tokenZappedKey = token1Key
            tokenZappedIn = token1Left
        }
        var zappedAmount = 0.0
        if tokenZappedIn > 0.0 {
            var minAmount = SwapConfig.ufix64NonZeroMin
            var maxAmount = tokenZappedIn - SwapConfig.ufix64NonZeroMin
            var midAmount = 0.0
            var epoch = 0
            while (epoch < 36) {
                midAmount = (minAmount + maxAmount) * 0.5;
                if maxAmount - midAmount < SwapConfig.ufix64NonZeroMin {
                    break
                }
                let amountOut = pairPublicRef.getAmountOut(amountIn: midAmount, tokenInKey: tokenZappedKey)
                let reserveAft0 = token0ReserveZapped + midAmount
                let reserveAft1 = token1ReserveZapped - amountOut
                let ratioUser = (tokenZappedIn - midAmount) / amountOut
                let ratioPool = reserveAft0 / reserveAft1
                var ratioBias = 0.0
                if (ratioUser >= ratioPool) {
                    if (ratioUser - ratioPool) <= SwapConfig.ufix64NonZeroMin {
                        break
                    }
                    minAmount = midAmount
                } else {
                    if (ratioPool - ratioUser) <= SwapConfig.ufix64NonZeroMin {
                        break
                    }
                    maxAmount = midAmount
                }
                epoch = epoch + 1
            }
            zappedAmount = midAmount

            // Swap
            if token0Left > 0.0 {
                let swapVaultIn <- token0Vault.withdraw(amount: zappedAmount)
                let token0VaultZapped <- token0Vault.withdraw(amount: tokenZappedIn - zappedAmount)
                let token1VaultZapped <- pairPublicRef.swap(vaultIn: <-swapVaultIn, exactAmountOut: nil)

                // Add liquidity
                let lpTokenVaultZapped <- pairPublicRef.addLiquidity(
                    tokenAVault: <- token0VaultZapped,
                    tokenBVault: <- token1VaultZapped
                )
                lpTokenVault.deposit(from: <-lpTokenVaultZapped)
            } else if token1Left > 0.0 {
                let swapVaultIn <- token1Vault.withdraw(amount: zappedAmount)
                let token1VaultZapped <- token1Vault.withdraw(amount: tokenZappedIn - zappedAmount)
                let token0VaultZapped <- pairPublicRef.swap(vaultIn: <-swapVaultIn, exactAmountOut: nil)

                // Add liquidity
                let lpTokenVaultZapped <- pairPublicRef.addLiquidity(
                    tokenAVault: <- token0VaultZapped,
                    tokenBVault: <- token1VaultZapped
                )
                lpTokenVault.deposit(from: <-lpTokenVaultZapped)
            }
        }
        assert(token0Vault.balance==0.0, message: "token0Vault.balance!=0")
        assert(token1Vault.balance==0.0, message: "token0Vault.balance!=0")
        destroy token0Vault
        destroy token1Vault
        
        let lpTokenCollectionStoragePath = SwapConfig.LpTokenCollectionStoragePath
        let lpTokenCollectionPublicPath = SwapConfig.LpTokenCollectionPublicPath
        lpTokenCollectionRef.deposit(pairAddr: pairAddrTo, lpTokenVault: <- lpTokenVault)

        LogEntry.LogMigrateSwapLpFromV1ToV2(
            token0Key: token0Key,
            token1Key: token1Key,
            lpToRemove: lpTokenAmount,
            token0WithdrawFromV1: token0Amount,
            token1WithdrawFromV1: token1Amount,
            token0LeftAfterFirstAddV2Lp: token0Left,
            token1LeftAfterFirstAddV2Lp: token1Left,
            zappedAmount: zappedAmount
        )
    }
}
```