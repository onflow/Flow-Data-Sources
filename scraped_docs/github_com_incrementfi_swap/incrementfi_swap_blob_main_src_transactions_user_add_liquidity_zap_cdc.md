# Source: https://github.com/IncrementFi/Swap/blob/main/src/transactions/user/add_liquidity_zap.cdc

```
import FungibleToken from "../../contracts/env/FungibleToken.cdc"
import SwapFactory from "../../contracts/SwapFactory.cdc"
import StableSwapFactory from "../../contracts/StableSwapFactory.cdc"
import SwapInterfaces from "../../contracts/SwapInterfaces.cdc"
import SwapConfig from "../../contracts/SwapConfig.cdc"
import SwapError from "../../contracts/SwapError.cdc"
import SwapRouter from "../../contracts/SwapRouter.cdc"

transaction(
    token0Key: String,
    token1Key: String,
    token0In: UFix64,
    desiredZappedAmount: UFix64,
    slippageTolerance: UFix64,

    deadline: UFix64,
    token0VaultPath: StoragePath,
    token1VaultPath: StoragePath,
    token1ReceiverPath: PublicPath,
    token1BalancePath: PublicPath,
    Token1Name: String,
    Token1Addr: Address,
    stableMode: Bool
) {
    prepare(userAccount: auth(Storage, Capabilities) &Account) {
        assert(deadline >= getCurrentBlock().timestamp, message:
            SwapError.ErrorEncode(
                msg: "AddLiquidityZapped: expired ".concat(deadline.toString()).concat(" < ").concat(getCurrentBlock().timestamp.toString()),
                err: SwapError.ErrorCode.EXPIRED
            )
        )
        let pairAddr = (stableMode)? 
            StableSwapFactory.getPairAddress(token0Key: token0Key, token1Key: token1Key) ?? panic("AddLiquidity: nonexistent stable pair ".concat(token0Key).concat(" <-> ").concat(token1Key).concat(", create stable pair first"))
            :
            SwapFactory.getPairAddress(token0Key: token0Key, token1Key: token1Key) ?? panic("AddLiquidity: nonexistent pair ".concat(token0Key).concat(" <-> ").concat(token1Key).concat(", create pair first"))
        let pairPublicRef = getAccount(pairAddr).capabilities.borrow<&{SwapInterfaces.PairPublic}>(SwapConfig.PairPublicPath)!
        
        let pairInfo = pairPublicRef.getPairInfo()
        var token0Reserve = 0.0
        var token1Reserve = 0.0
        if token0Key == (pairInfo[0] as! String) {
            token0Reserve = (pairInfo[2] as! UFix64)
            token1Reserve = (pairInfo[3] as! UFix64)
        } else {
            token0Reserve = (pairInfo[3] as! UFix64)
            token1Reserve = (pairInfo[2] as! UFix64)
        }
        assert(token0Reserve != 0.0, message: "Cannot add liquidity zapped in a new pool.")
        
        var zappedAmount = 0.0
        if (stableMode == false) {
            // Cal optimized zapped amount through dex
            let r0Scaled = SwapConfig.UFix64ToScaledUInt256(token0Reserve)
            let swapFeeRateBps = pairInfo[6] as! UInt64
            let fee = 1.0 - UFix64(swapFeeRateBps)/10000.0
            let kplus1SquareScaled = SwapConfig.UFix64ToScaledUInt256((1.0+fee)*(1.0+fee))
            let kScaled = SwapConfig.UFix64ToScaledUInt256(fee)
            let kplus1Scaled = SwapConfig.UFix64ToScaledUInt256(fee+1.0)
            let token0InScaled = SwapConfig.UFix64ToScaledUInt256(token0In)
            let qScaled = SwapConfig.sqrt(
                r0Scaled * r0Scaled / SwapConfig.scaleFactor * kplus1SquareScaled / SwapConfig.scaleFactor
                + 4 * kScaled * r0Scaled / SwapConfig.scaleFactor * token0InScaled / SwapConfig.scaleFactor)
            zappedAmount = SwapConfig.ScaledUInt256ToUFix64(
                (qScaled - r0Scaled*kplus1Scaled/SwapConfig.scaleFactor)*SwapConfig.scaleFactor/(kScaled*2)
            )

            var slippage = 0.0
            if (desiredZappedAmount > zappedAmount) {
                slippage = (desiredZappedAmount - zappedAmount) / desiredZappedAmount * 100.0
            } else {
                slippage = (zappedAmount - desiredZappedAmount) / desiredZappedAmount * 100.0
            }
            assert(slippage <= slippageTolerance, message:
                SwapError.ErrorEncode(
                    msg: "ZAPPED_ADD_LIQUIDITY_SLIPPAGE_OFFSET_TOO_LARGE expect min ".concat(zappedAmount.toString()).concat(" got ").concat(desiredZappedAmount.toString()),
                    err: SwapError.ErrorCode.SLIPPAGE_OFFSET_TOO_LARGE
                )
            )
        } else {
            let desiredAmountOut = pairPublicRef.getAmountOut(amountIn: desiredZappedAmount, tokenInKey: token0Key)
            let propAmountOut = (token0In - desiredZappedAmount) / (token0Reserve + desiredZappedAmount) * (token1Reserve - desiredAmountOut)
            var bias = 0.0
            if (desiredAmountOut > propAmountOut) {
                bias = desiredAmountOut - propAmountOut
            } else {
                bias = propAmountOut - desiredAmountOut
            }
            if (bias <= 0.0001) {
                zappedAmount = desiredZappedAmount
            } else {
                var minAmount = SwapConfig.ufix64NonZeroMin
                var maxAmount = token0In - SwapConfig.ufix64NonZeroMin
                var midAmount = 0.0
                if (desiredAmountOut > propAmountOut) {
                    maxAmount = desiredZappedAmount
                } else {
                    minAmount = desiredZappedAmount
                }
                var epoch = 0
                while (epoch < 36) {
                    midAmount = (minAmount + maxAmount) * 0.5;
                    if maxAmount - midAmount < SwapConfig.ufix64NonZeroMin {
                        break
                    }
                    let amountOut = pairPublicRef.getAmountOut(amountIn: midAmount, tokenInKey: token0Key)
                    let reserveAft0 = token0Reserve + midAmount
                    let reserveAft1 = token1Reserve - amountOut
                    let ratioUser = (token0In - midAmount) / amountOut
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

                var slippage = 0.0
                if (desiredZappedAmount > zappedAmount) {
                    slippage = (desiredZappedAmount - zappedAmount) / desiredZappedAmount * 100.0
                } else {
                    slippage = (zappedAmount - desiredZappedAmount) / desiredZappedAmount * 100.0
                }
                assert(slippage <= slippageTolerance, message:
                    SwapError.ErrorEncode(
                        msg: "ZAPPED_ADD_LIQUIDITY_SLIPPAGE_OFFSET_TOO_LARGE expect min ".concat(zappedAmount.toString()).concat(" got ").concat(desiredZappedAmount.toString()),
                        err: SwapError.ErrorCode.SLIPPAGE_OFFSET_TOO_LARGE
                    )
                )
            }
        }

        // Setup the other token's Vault if necessary
        let tokenOutReceiverRef = userAccount.storage.borrow<&{FungibleToken.Vault}>(from: token1VaultPath)
        if tokenOutReceiverRef == nil {
            let token1AddrStr = Token1Addr.toString()
            let token1AddrStr0xTrimmed = token1AddrStr.slice(from: 2, upTo: token1AddrStr.length)
            let token1VaultRuntimeType = CompositeType("A.".concat(token1AddrStr0xTrimmed).concat(".").concat(Token1Name).concat(".Vault")) ?? panic("token1 get runtime type fail")
            userAccount.storage.save(<- getAccount(Token1Addr).contracts.borrow<&{FungibleToken}>(name: Token1Name)!.createEmptyVault(vaultType: token1VaultRuntimeType), to: token1VaultPath)
            let receiverCapability = userAccount.capabilities.storage.issue<&{FungibleToken.Receiver}>(token1VaultPath)
            userAccount.capabilities.publish(receiverCapability, at: token1ReceiverPath)
            let balanceCapability = userAccount.capabilities.storage.issue<&{FungibleToken.Balance}>(token1VaultPath)
            userAccount.capabilities.publish(balanceCapability, at: token1BalancePath)
        }

        // Swap
        let vaultInRef  = userAccount.storage.borrow<auth(FungibleToken.Withdraw) &{FungibleToken.Vault}>(from: token0VaultPath)!
        let swapVaultIn <- vaultInRef.withdraw(amount: zappedAmount)
        let token0Vault <- vaultInRef.withdraw(amount: token0In - zappedAmount)
        let token1Vault <- pairPublicRef.swap(vaultIn: <-swapVaultIn, exactAmountOut: nil)
        
        // Add liquidity
        let lpTokenVault <- pairPublicRef.addLiquidity(
            tokenAVault: <- token0Vault,
            tokenBVault: <- token1Vault
        )
        
        let lpTokenCollectionStoragePath = SwapConfig.LpTokenCollectionStoragePath
        let lpTokenCollectionPublicPath = SwapConfig.LpTokenCollectionPublicPath
        var lpTokenCollectionRef = userAccount.storage.borrow<&SwapFactory.LpTokenCollection>(from: lpTokenCollectionStoragePath)
        if lpTokenCollectionRef == nil {
            destroy <- userAccount.storage.load<@AnyResource>(from: lpTokenCollectionStoragePath)
            userAccount.storage.save(<-SwapFactory.createEmptyLpTokenCollection(), to: lpTokenCollectionStoragePath)
            let lpTokenCollectionCap = userAccount.capabilities.storage.issue<&{SwapInterfaces.LpTokenCollectionPublic}>(lpTokenCollectionStoragePath)
            userAccount.capabilities.publish(lpTokenCollectionCap, at: lpTokenCollectionPublicPath)
            lpTokenCollectionRef = userAccount.storage.borrow<&SwapFactory.LpTokenCollection>(from: lpTokenCollectionStoragePath)
        }
        lpTokenCollectionRef!.deposit(pairAddr: pairAddr, lpTokenVault: <- lpTokenVault)
    }
}
```