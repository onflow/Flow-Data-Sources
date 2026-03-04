# Source: https://github.com/IncrementFi/Liquid-Staking/blob/main/cadence/contracts/standard/mainnet/SwapInterfaces.cdc

```
/**

# Swap related interface definitions all-in-one

# Author: Increment Labs

*/
import FungibleToken from "../FungibleToken.cdc"

access(all) contract interface SwapInterfaces {
    // A redundant PairInfo struct for the purpose of better indexing
    access(all) struct interface PairInfo {
        access(all) let token0Key: String
        access(all) let token1Key: String
        access(all) let token0Reserve: UFix64
        access(all) let token1Reserve: UFix64
        access(all) let pairAddr: Address
        access(all) let lpTokenSupply: UFix64
        access(all) let swapFeeInBps: UInt64
        access(all) let isStableswap: Bool
        access(all) let stableCurveP: UFix64
    }

    access(all) resource interface PairPublic {
        access(all) fun addLiquidity(tokenAVault: @{FungibleToken.Vault}, tokenBVault: @{FungibleToken.Vault}): @{FungibleToken.Vault}
        access(all) fun removeLiquidity(lpTokenVault: @{FungibleToken.Vault}) : @[{FungibleToken.Vault}]
        access(all) fun swap(vaultIn: @{FungibleToken.Vault}, exactAmountOut: UFix64?): @{FungibleToken.Vault}
        access(all) fun flashloan(executor: &{SwapInterfaces.FlashLoanExecutor}, requestedTokenVaultType: Type, requestedAmount: UFix64, params: {String: AnyStruct}) { return }
        access(all) view fun getAmountIn(amountOut: UFix64, tokenOutKey: String): UFix64
        access(all) view fun getAmountOut(amountIn: UFix64, tokenInKey: String): UFix64
        access(all) view fun getPrice0CumulativeLastScaled(): UInt256
        access(all) view fun getPrice1CumulativeLastScaled(): UInt256
        access(all) view fun getBlockTimestampLast(): UFix64
        access(all) view fun getPairInfo(): [AnyStruct]
        access(all) view fun getPairInfoStruct(): {PairInfo}
        access(all) view fun getLpTokenVaultType(): Type
        access(all) view fun isStableSwap(): Bool { return false }
        access(all) view fun getStableCurveP(): UFix64 { return 1.0 }
    }

    access(all) resource interface LpTokenCollectionPublic {
        access(all) fun deposit(pairAddr: Address, lpTokenVault: @{FungibleToken.Vault})
        access(all) view fun getCollectionLength(): Int
        access(all) view fun getLpTokenBalance(pairAddr: Address): UFix64
        access(all) view fun getAllLPTokens(): [Address]
        access(all) view fun getSlicedLPTokens(from: UInt64, to: UInt64): [Address]
    }

    access(all) resource interface FlashLoanExecutor {
        access(all) fun executeAndRepay(loanedToken: @{FungibleToken.Vault}, params: {String: AnyStruct}): @{FungibleToken.Vault}
    }
}
```