# Source: https://github.com/IncrementFi/Swap/blob/main/src/transactions/user/aggregate_swap_tokens_for_exact_tokens.testnet.cdc

```
import FungibleToken from "../../contracts/env/FungibleToken.cdc"
import FlowToken from "../../contracts/tokens/FlowToken.cdc"
import TeleportedTetherToken from "../../contracts/tokens/TeleportedTetherToken.cdc"
import FiatToken from "../../contracts/tokens/FiatToken.cdc"
import FUSD from "../../contracts/tokens/FUSD.cdc"
import BloctoToken from "../../contracts/tokens/BloctoToken.cdc"
import StarlyToken from "../../contracts/tokens/StarlyToken.cdc"
import REVV from "../../contracts/tokens/REVV.cdc"

import SwapInterfaces from "../../contracts/SwapInterfaces.cdc"
import SwapConfig from "../../contracts/SwapConfig.cdc"
import SwapError from "../../contracts/SwapError.cdc"

import PierRouter from "../../contracts/env/PierRouter.cdc"
import PierRouterLib from "../../contracts/env/PierRouterLib.cdc"
import IPierPair from "../../contracts/env/IPierPair.cdc"

import FlowSwapPair from "../../contracts/env/FlowSwapPair.cdc"
import UsdcUsdtSwapPair from "../../contracts/env/UsdcUsdtSwapPair.cdc"
import FusdUsdtSwapPair from "../../contracts/env/FusdUsdtSwapPair.cdc"
import BltUsdtSwapPair from "../../contracts/env/BltUsdtSwapPair.cdc"
import StarlyUsdtSwapPair from "../../contracts/env/StarlyUsdtSwapPair.cdc"
import RevvFlowSwapPair from "../../contracts/env/RevvFlowSwapPair.cdc"

access(all) fun getBloctoAmountIn(amountOut: UFix64, reserveIn: UFix64, reserveOut: UFix64, swapFeeRateBps: UInt64): UFix64 {
    let amountIn = reserveIn * amountOut / (reserveOut - amountOut) / (1.0 - UFix64(swapFeeRateBps)/10000.0)
    var tryTimes: Int = 10
    var curIn = amountIn
    while(tryTimes >= 0) {
        let curOut = getBloctoAmountOut(amountIn: curIn, reserveIn: reserveIn, reserveOut: reserveOut, swapFeeRateBps: swapFeeRateBps)
        if curOut >= amountOut {
            break
        }
        curIn = curIn + 0.00000001
        tryTimes = tryTimes - 1
    }
    return curIn
}

access(all) fun getBloctoAmountOut(amountIn: UFix64, reserveIn: UFix64, reserveOut: UFix64, swapFeeRateBps: UInt64): UFix64 {
    let amountInWithFee = amountIn * (1.0 - UFix64(swapFeeRateBps)/10000.0)
    let amountOut = reserveOut * amountInWithFee / (reserveIn + amountInWithFee);
    return amountOut
}

transaction(
    tokenKeyFlatSplitPath: [String],
    tokenAddressFlatSplitPath: [Address],
    tokenNameFlatSplitPath: [String],
    poolAddressesToPairs: [[[Address]]],
    poolKeysToPairs: [[[String]]],
    poolOutRatiosToPairs: [[[UFix64]]],
    amountOutSplit: [UFix64],

    amountInMax: UFix64,
    deadline: UFix64,
    tokenInVaultPath: StoragePath,
    tokenOutVaultPath: StoragePath,
    tokenOutReceiverPath: PublicPath,
    tokenOutBalancePath: PublicPath,
) {
    prepare(userAccount: auth(Storage, Capabilities) &Account) {
        assert(deadline >= getCurrentBlock().timestamp, message:
            SwapError.ErrorEncode(
                msg: "EXPIRED",
                err: SwapError.ErrorCode.EXPIRED
            )
        )

        let len = tokenKeyFlatSplitPath.length
        let swapInKey = tokenKeyFlatSplitPath[0]
        let swapOutKey = tokenKeyFlatSplitPath[len-1]
        let swapOutTokenName = tokenNameFlatSplitPath[len-1]
        let swapOutTokenAddress = tokenAddressFlatSplitPath[len-1]

        var tokenInAmountTotal = 0.0

        var tokenOutReceiverRef = userAccount.storage.borrow<&{FungibleToken.Vault}>(from: tokenOutVaultPath)
        if tokenOutReceiverRef == nil {
            let outTokenAddrStr = swapOutTokenAddress.toString()
            let outTokenAddrStr0xTrimmed = outTokenAddrStr.slice(from: 2, upTo: outTokenAddrStr.length)
            /// e.g.: "A.1654653399040a61.FlowToken.Vault"
            let outTokenVaultRuntimeType = CompositeType("A.".concat(outTokenAddrStr0xTrimmed).concat(".").concat(swapOutTokenName).concat(".Vault")) ?? panic("outToken get runtime type fail")
            userAccount.storage.save(<-getAccount(swapOutTokenAddress).contracts.borrow<&{FungibleToken}>(name: swapOutTokenName)!.createEmptyVault(vaultType: outTokenVaultRuntimeType), to: tokenOutVaultPath)
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

        var pathIndex = 0
        var i = 0
        var path: [String] = []
        var pathTokenAddress: [Address] = []
        var pathTokenName: [String] = []
        while(i < len) {
            var curTokenKey = tokenKeyFlatSplitPath[i]
            path.append(curTokenKey)
            pathTokenAddress.append(tokenAddressFlatSplitPath[i])
            pathTokenName.append(tokenNameFlatSplitPath[i])
            if (curTokenKey == swapOutKey) {
                let pathOutAmount = amountOutSplit[pathIndex]
                
                let pathLength = path.length
                // cal amount in
                var curOutAmount = pathOutAmount;
                var curOutLeftAmount = pathOutAmount;
                let poolsInOnPath: [[UFix64]] = [];
                let poolsOutOnPath: [[UFix64]] = [];
                var pathStep = pathLength - 2
                while(pathStep >= 0) {
                    poolsInOnPath.append([])
                    poolsOutOnPath.append([])
                    pathStep = pathStep - 1
                }
                pathStep = pathLength - 2
                while(pathStep >= 0) {
                    let tokenInKey = path[pathStep]
                    let tokenOutKey = path[pathStep+1]
                    var pairInAmount = 0.0
                    var poolIndex = 0
                    let poolLength = poolAddressesToPairs[pathIndex][pathStep].length
                    while(poolIndex < poolLength) {
                        let poolOutRatio = poolOutRatiosToPairs[pathIndex][pathStep][poolIndex]
                        let poolKey = poolKeysToPairs[pathIndex][pathStep][poolIndex]
                        let poolAddress = poolAddressesToPairs[pathIndex][pathStep][poolIndex]

                        var poolOutAmount = curOutAmount * poolOutRatio
                        if (poolIndex == poolLength - 1) {
                            poolOutAmount = curOutLeftAmount
                        }
                        curOutLeftAmount = curOutLeftAmount - poolOutAmount

                        poolsOutOnPath[pathStep].append(poolOutAmount)

                        var poolInAmount = 0.0
                        let one = 10000.0
                        // amount in
                        switch poolKey {
                            case "increment-v1":
                                let pool = getAccount(poolAddress).capabilities.borrow<&{SwapInterfaces.PairPublic}>(SwapConfig.PairPublicPath)!
                                poolInAmount = pool.getAmountIn(amountOut: poolOutAmount, tokenOutKey: tokenOutKey)
                            case "increment-stable":
                                let pool = getAccount(poolAddress).capabilities.borrow<&{SwapInterfaces.PairPublic}>(SwapConfig.PairPublicPath)!
                                poolInAmount = pool.getAmountIn(amountOut: poolOutAmount, tokenOutKey: tokenOutKey)
                            case "metapier":
                                let pathRef = &[tokenInKey.concat(".Vault"), tokenOutKey.concat(".Vault")] as &[String]
                                let pools = PierRouterLib.getPoolsByPath(path: pathRef)
                                let poolsRef = &pools as &[&{IPierPair.IPool}]

                                let amounts = PierRouterLib.getAmountsByAmountOut(amountOut: poolOutAmount, path: pathRef, pools: poolsRef)
                                poolInAmount = amounts[0]
                            case "blocto":
                                switch poolAddress {
                                    case 0xd9854329b7edf136:
                                        let flowReserve = FlowSwapPair.getPoolAmounts().token1Amount
                                        let usdtReserve = FlowSwapPair.getPoolAmounts().token2Amount
                                        let flowUsdtFeeBps = UInt64(FlowSwapPair.feePercentage * one)
                                        if tokenInKey == "A.7e60df042a9c0868.FlowToken" {
                                            poolInAmount = getBloctoAmountIn(amountOut: poolOutAmount, reserveIn: flowReserve, reserveOut: usdtReserve, swapFeeRateBps: flowUsdtFeeBps)
                                        } else {
                                            poolInAmount = getBloctoAmountIn(amountOut: poolOutAmount, reserveIn: usdtReserve, reserveOut: flowReserve, swapFeeRateBps: flowUsdtFeeBps)
                                        }
                                    case 0x481744401ea249c0:  // UsdcUsdtSwapPair
                                        poolInAmount = poolOutAmount
                                    case 0x3502a5dacaf350bb:  // FusdUsdtSwapPair
                                        if tokenInKey == "A.e223d8a629e49c68.FUSD" {
                                            poolInAmount = poolOutAmount / 1.001 + 0.00000001
                                        } else {
                                            poolInAmount = poolOutAmount / 0.999 + 0.00000001
                                        }
                                    case 0xc59604d4e65f14b3:
                                        let bltReserve = BltUsdtSwapPair.getPoolAmounts().token1Amount
                                        let usdtReserve = BltUsdtSwapPair.getPoolAmounts().token2Amount    
                                        let bltUsdtFeeBps = UInt64(BltUsdtSwapPair.feePercentage * one)
                                        if tokenInKey == "A.6e0797ac987005f5.BloctoToken" {
                                            poolInAmount = getBloctoAmountIn(amountOut: poolOutAmount, reserveIn: bltReserve, reserveOut: usdtReserve, swapFeeRateBps: bltUsdtFeeBps)
                                        } else {
                                            poolInAmount = getBloctoAmountIn(amountOut: poolOutAmount, reserveIn: usdtReserve, reserveOut: bltReserve, swapFeeRateBps: bltUsdtFeeBps)
                                        }
                                    case 0x22d84efc93a8b21a:
                                        let starlyReserve = StarlyUsdtSwapPair.getPoolAmounts().token1Amount
                                        let usdtReserve = StarlyUsdtSwapPair.getPoolAmounts().token2Amount
                                        let starlyUsdtFeeBps = UInt64(StarlyUsdtSwapPair.feePercentage * one)   
                                        if tokenInKey == "A.f63219072aaddd50.StarlyToken" {
                                            poolInAmount = getBloctoAmountIn(amountOut: poolOutAmount, reserveIn: starlyReserve, reserveOut: usdtReserve, swapFeeRateBps: starlyUsdtFeeBps)
                                        } else {
                                            poolInAmount = getBloctoAmountIn(amountOut: poolOutAmount, reserveIn: usdtReserve, reserveOut: starlyReserve, swapFeeRateBps: starlyUsdtFeeBps)
                                        }
                                    case 0xd017f81bffc9aa05:
                                        let revvReserve = RevvFlowSwapPair.getPoolAmounts().token1Amount
                                        let flowReserve = RevvFlowSwapPair.getPoolAmounts().token2Amount
                                        let revvFlowFeeBps = UInt64(RevvFlowSwapPair.feePercentage * one)
                                        if tokenInKey == "A.14ca72fa4d45d2c3.REVV" {
                                            poolInAmount = getBloctoAmountIn(amountOut: poolOutAmount, reserveIn: revvReserve, reserveOut: flowReserve, swapFeeRateBps: revvFlowFeeBps)
                                        } else {
                                            poolInAmount = getBloctoAmountIn(amountOut: poolOutAmount, reserveIn: flowReserve, reserveOut: revvReserve, swapFeeRateBps: revvFlowFeeBps)
                                        }
                                    default:
                                        assert(false, message: "invalid blocto pool address")
                                }
                            default:
                                assert(false, message: "invalid pool type")
                        }

                        poolsInOnPath[pathStep].append(poolInAmount)
                        pairInAmount = pairInAmount + poolInAmount
                        poolIndex = poolIndex + 1
                    }
                    curOutAmount = pairInAmount
                    curOutLeftAmount = pairInAmount
                    pathStep = pathStep - 1
                }
 
                // swap in path
                pathStep = 0
                var pathInAmount = 0.0
                for poolIn in poolsInOnPath[0] {
                    pathInAmount = pathInAmount + poolIn
                }
                
                tokenInAmountTotal = tokenInAmountTotal + pathInAmount

                var pairInVault <- userAccount.storage.borrow<auth(FungibleToken.Withdraw) &{FungibleToken.Vault}>(from: tokenInVaultPath)!.withdraw(amount: pathInAmount) 
                
                while(pathStep < pathLength-1) {
                    let tokenInKey = path[pathStep]
                    let tokenOutKey = path[pathStep+1]
                    let tokenInAddress: Address = pathTokenAddress[pathStep]
                    let tokenOutAddress: Address = pathTokenAddress[pathStep+1]
                    let tokenInName: String = pathTokenName[pathStep]
                    let tokenOutName: String = pathTokenName[pathStep+1]
                    var poolIndex = 0;
                    let poolLength = poolAddressesToPairs[pathIndex][pathStep].length

                    let outTokenAddrStr = tokenOutAddress.toString()
                    let outTokenAddrStr0xTrimmed = outTokenAddrStr.slice(from: 2, upTo: outTokenAddrStr.length)
                    /// e.g.: "A.1654653399040a61.FlowToken.Vault"
                    let outTokenVaultRuntimeType = CompositeType("A.".concat(outTokenAddrStr0xTrimmed).concat(".").concat(tokenOutName).concat(".Vault")) ?? panic("outToken get runtime type fail")
                    var poolOutVault <- getAccount(tokenOutAddress).contracts.borrow<&{FungibleToken}>(name: tokenOutName)!.createEmptyVault(vaultType: outTokenVaultRuntimeType)

                    // swap in pool
                    while(poolIndex < poolLength) {
                        let poolAddress = poolAddressesToPairs[pathIndex][pathStep][poolIndex]
                        let poolKey = poolKeysToPairs[pathIndex][pathStep][poolIndex]
                        
                        var poolInAmount = poolsInOnPath[pathStep][poolIndex]
                        if (poolIndex == poolLength-1) { poolInAmount = pairInVault.balance }

                        var poolOutAmount = poolsOutOnPath[pathStep][poolIndex]
                        
                        switch poolKey {
                            case "increment-v1":
                                let pool = getAccount(poolAddress).capabilities.borrow<&{SwapInterfaces.PairPublic}>(SwapConfig.PairPublicPath)!
                                poolOutVault.deposit(from: <-pool.swap(vaultIn: <- pairInVault.withdraw(amount: poolInAmount), exactAmountOut: poolOutAmount))
                            
                            case "increment-stable":
                                let pool = getAccount(poolAddress).capabilities.borrow<&{SwapInterfaces.PairPublic}>(SwapConfig.PairPublicPath)!
                                poolOutVault.deposit(from: <-pool.swap(vaultIn: <- pairInVault.withdraw(amount: poolInAmount), exactAmountOut: poolOutAmount))
                            
                            case "metapier":
                                PierRouter.swapTokensAForExactTokensB(
                                    fromVault: &pairInVault as auth(FungibleToken.Withdraw) &{FungibleToken.Vault},
                                    toVault: &poolOutVault as &{FungibleToken.Receiver},
                                    amountInMax: UFix64.max,
                                    amountOut: poolOutAmount,
                                    path: [tokenInKey.concat(".Vault"), tokenOutKey.concat(".Vault")],
                                    deadline: deadline,
                                )
                            case "blocto":
                                switch poolAddress {
                                    case 0xd9854329b7edf136:
                                        if tokenInKey == "A.7e60df042a9c0868.FlowToken" {
                                            poolOutVault.deposit(from: <-FlowSwapPair.swapToken1ForToken2(from: <-(pairInVault.withdraw(amount: poolInAmount) as! @FlowToken.Vault)))
                                        } else {
                                            poolOutVault.deposit(from: <-FlowSwapPair.swapToken2ForToken1(from: <-(pairInVault.withdraw(amount: poolInAmount) as! @TeleportedTetherToken.Vault)))
                                        }
                                    case 0x481744401ea249c0:
                                        if tokenInKey == "A.a983fecbed621163.FiatToken" {
                                            poolOutVault.deposit(from: <-UsdcUsdtSwapPair.swapToken1ForToken2(from: <-(pairInVault.withdraw(amount: poolInAmount) as! @FiatToken.Vault)))
                                        } else {
                                            poolOutVault.deposit(from: <-UsdcUsdtSwapPair.swapToken2ForToken1(from: <-(pairInVault.withdraw(amount: poolInAmount) as! @TeleportedTetherToken.Vault)))
                                        }
                                    case 0x3502a5dacaf350bb:
                                        if tokenInKey == "A.e223d8a629e49c68.FUSD" {
                                            poolOutVault.deposit(from: <-FusdUsdtSwapPair.swapToken1ForToken2(from: <-(pairInVault.withdraw(amount: poolInAmount) as! @FUSD.Vault)))
                                        } else {
                                            poolOutVault.deposit(from: <-FusdUsdtSwapPair.swapToken2ForToken1(from: <-(pairInVault.withdraw(amount: poolInAmount) as! @TeleportedTetherToken.Vault)))
                                        }
                                    case 0xc59604d4e65f14b3:
                                        if tokenInKey == "A.6e0797ac987005f5.BloctoToken" {
                                            poolOutVault.deposit(from: <-BltUsdtSwapPair.swapToken1ForToken2(from: <-(pairInVault.withdraw(amount: poolInAmount) as! @BloctoToken.Vault)))
                                        } else {
                                            poolOutVault.deposit(from: <-BltUsdtSwapPair.swapToken2ForToken1(from: <-(pairInVault.withdraw(amount: poolInAmount) as! @TeleportedTetherToken.Vault)))
                                        }
                                    case 0x22d84efc93a8b21a:
                                        if tokenInKey == "A.f63219072aaddd50.StarlyToken" {
                                            poolOutVault.deposit(from: <-StarlyUsdtSwapPair.swapToken1ForToken2(from: <-(pairInVault.withdraw(amount: poolInAmount) as! @StarlyToken.Vault)))
                                        } else {
                                            poolOutVault.deposit(from: <-StarlyUsdtSwapPair.swapToken2ForToken1(from: <-(pairInVault.withdraw(amount: poolInAmount) as! @TeleportedTetherToken.Vault)))
                                        }
                                    case 0xd017f81bffc9aa05:
                                        if tokenInKey == "A.14ca72fa4d45d2c3.REVV" {
                                            poolOutVault.deposit(from: <-RevvFlowSwapPair.swapToken1ForToken2(from: <-(pairInVault.withdraw(amount: poolInAmount) as! @REVV.Vault)))
                                        } else {
                                            poolOutVault.deposit(from: <-RevvFlowSwapPair.swapToken2ForToken1(from: <-(pairInVault.withdraw(amount: poolInAmount) as! @FlowToken.Vault)))
                                        }

                                    default:
                                        assert(false, message: "invalid blocto pool address")
                                }
                            default:
                                assert(false, message: "invalid pool type")
                        }

                        poolIndex = poolIndex + 1
                    }
                    pairInVault <-> poolOutVault
                    destroy poolOutVault
                    pathStep = pathStep + 1
                }
                tokenOutReceiverRef!.deposit(from: <- pairInVault)

                path = []
                pathTokenAddress = []
                pathTokenName = []
        
                pathIndex = pathIndex + 1
            }
            i = i + 1
        }

        assert(tokenInAmountTotal <= amountInMax, message:
            SwapError.ErrorEncode(
                msg: "SLIPPAGE_OFFSET_TOO_LARGE max in ".concat(amountInMax.toString()).concat(" got ").concat(tokenInAmountTotal.toString()),
                err: SwapError.ErrorCode.SLIPPAGE_OFFSET_TOO_LARGE
            )
        )
    }
}
```