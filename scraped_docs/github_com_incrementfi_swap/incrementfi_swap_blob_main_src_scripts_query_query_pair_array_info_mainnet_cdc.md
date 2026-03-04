# Source: https://github.com/IncrementFi/Swap/blob/main/src/scripts/query/query_pair_array_info.mainnet.cdc

```
import FungibleToken from "../../contracts/env/FungibleToken.cdc"
import SwapFactory from "../../contracts/SwapFactory.cdc"
import StableSwapFactory from "../../contracts/StableSwapFactory.cdc"

import FlowSwapPair from "../../contracts/env/FlowSwapPair.cdc"
import BltUsdtSwapPair from "../../contracts/env/BltUsdtSwapPair.cdc"
import RevvFlowSwapPair from "../../contracts/env/RevvFlowSwapPair.cdc"
import StarlyUsdtSwapPair from "../../contracts/env/StarlyUsdtSwapPair.cdc"
import UsdcUsdtSwapPair from "../../contracts/env/UsdcUsdtSwapPair.cdc"
import FusdUsdtSwapPair from "../../contracts/env/FusdUsdtSwapPair.cdc"

import IPierPair from "../../contracts/env/IPierPair.cdc"
import PierPair from "../../contracts/env/PierPair.cdc"
import PierSwapFactory from "../../contracts/env/PierSwapFactory.cdc"
import PierSwapSettings from "../../contracts/env/PierSwapSettings.cdc"

/**
    [
        [
            token0Key,            // 0
            token1Key,
            token0Vault.balance,
            token1Vault.balance,
            SwapPair.address,
            totalSupply,          // 5
            liquiditySource,
            ammAlgo,
            swapFeeBps,
            stableCurveP
        ]
    ]
*/
access(all) fun main(from: UInt64, to: UInt64, poolSources: [String]): [AnyStruct] {
    pre {
        from <= to: "from > to"
    }
    let poolInfos: [AnyStruct] = [];
    for poolSource in poolSources {
        if (poolSource == "increment-v1") {
            var increment_v1: [AnyStruct] = []
            // Get rid of runtime error of the bad SwapPair at index 43.
            if (from > 43 || to < 43) {
                increment_v1 = SwapFactory.getSlicedPairInfos(from: from, to: to)
            } else if (from == 43 && to > 43) {
                increment_v1 = SwapFactory.getSlicedPairInfos(from: 44, to: to)
            } else if (to == 43 && from < 43) {
                increment_v1 = SwapFactory.getSlicedPairInfos(from: from, to: 42)
            } else if (from < to) {
                increment_v1 = SwapFactory.getSlicedPairInfos(from: from, to: 42)
                let tmp = SwapFactory.getSlicedPairInfos(from: 44, to: to)
                increment_v1.appendAll(tmp)
            }
            // increment-v1
            for element in increment_v1 {
                let poolInfo = element as! [AnyStruct]
                if poolInfo.length == 6 {
                    poolInfos.append([poolInfo[0], poolInfo[1], poolInfo[2], poolInfo[3], poolInfo[4], poolInfo[5], "increment-v1", "uni", 30, "1.0"])
                } else {
                    if (poolInfo[7] as! Bool) == true {
                        poolInfos.append([poolInfo[0], poolInfo[1], poolInfo[2], poolInfo[3], poolInfo[4], poolInfo[5], "increment-stable", "solidly", poolInfo[6], poolInfo[8]])
                    } else {
                        poolInfos.append([poolInfo[0], poolInfo[1], poolInfo[2], poolInfo[3], poolInfo[4], poolInfo[5], "increment-v1", "uni", poolInfo[6], "1.0"])
                    }
                }
            }
        }
        if (poolSource == "increment-stable") {
            // increment-stable
            let increment_stable: [AnyStruct] = StableSwapFactory.getSlicedPairInfos(from: from, to: to)
            for element in increment_stable {
                let poolInfo = element as! [AnyStruct]
                poolInfos.append([poolInfo[0], poolInfo[1], poolInfo[2], poolInfo[3], poolInfo[4], poolInfo[5], "increment-stable", "solidly", poolInfo[6], poolInfo[8]])
            }
        }
        if (poolSource == "metapier") {
            // metapier pools
            let metapierPoolSize = UInt64(PierSwapFactory.getPoolsSize())
            let metapierSwapFeeBps = UInt64(PierSwapSettings.getPoolTotalFeeCoefficient() * 10.0)
            var metapierPoolIndex: UInt64 = from
            while(metapierPoolIndex < metapierPoolSize && metapierPoolIndex < to) {
                let pool = PierSwapFactory.getPoolByIndex(index: metapierPoolIndex)
                let poolAddress = Address(PierSwapFactory.getPoolIdByIndex(index: metapierPoolIndex))
                let token0Key = pool.tokenAType.identifier.slice(from: 0, upTo: pool.tokenAType.identifier.length - 6)
                let token1Key = pool.tokenBType.identifier.slice(from: 0, upTo: pool.tokenBType.identifier.length - 6)
                let reserves = pool.getReserves();

                poolInfos.append([token0Key, token1Key, reserves[0], reserves[1], poolAddress, 0.0, "metapier", "uni", metapierSwapFeeBps, "1.0"])
                metapierPoolIndex = metapierPoolIndex + 1
            }
        }
        if (poolSource == "blocto") {
            // blocto pools
            let one = 10000.0
            let flowUsdtFeeBps = FlowSwapPair.feePercentage * one
            let bltUsdtFeeBps = BltUsdtSwapPair.feePercentage * one
            let revvFlowFeeBps = RevvFlowSwapPair.feePercentage * one
            let starlyUsdtFeeBps = StarlyUsdtSwapPair.feePercentage * one
            assert(flowUsdtFeeBps % 1.0 == 0.0, message: "blocto-flow-usdt-feeBps!")
            assert(bltUsdtFeeBps % 1.0 == 0.0, message: "blocto-blt-usdt-feeBps!")
            assert(revvFlowFeeBps % 1.0 == 0.0, message: "blocto-revv-flow-feeBps!")
            assert(starlyUsdtFeeBps % 1.0 == 0.0, message: "blocto-starly-usdt-feeBps!")

            if FlowSwapPair.isFrozen == false {poolInfos.append(["A.1654653399040a61.FlowToken", "A.cfdd90d4a00f7b5b.TeleportedTetherToken", FlowSwapPair.getPoolAmounts().token1Amount, FlowSwapPair.getPoolAmounts().token2Amount, "0xc6c77b9f5c7a378f", 0.0, "blocto", "uni", UInt64(flowUsdtFeeBps), "1.0"])}
            if BltUsdtSwapPair.isFrozen == false {poolInfos.append(["A.0f9df91c9121c460.BloctoToken", "A.cfdd90d4a00f7b5b.TeleportedTetherToken", BltUsdtSwapPair.getPoolAmounts().token1Amount, BltUsdtSwapPair.getPoolAmounts().token2Amount, "0xfcb06a5ae5b21a2d", 0.0, "blocto", "uni", UInt64(bltUsdtFeeBps), "1.0"])}
            if RevvFlowSwapPair.isFrozen == false {poolInfos.append(["A.d01e482eb680ec9f.REVV", "A.1654653399040a61.FlowToken", RevvFlowSwapPair.getPoolAmounts().token1Amount, RevvFlowSwapPair.getPoolAmounts().token2Amount, "0x5e284fb7cff23a3f", 0.0, "blocto", "uni", UInt64(revvFlowFeeBps), "1.0"])}
            if StarlyUsdtSwapPair.isFrozen == false {poolInfos.append(["A.142fa6570b62fd97.StarlyToken", "A.cfdd90d4a00f7b5b.TeleportedTetherToken", StarlyUsdtSwapPair.getPoolAmounts().token1Amount, StarlyUsdtSwapPair.getPoolAmounts().token2Amount, "0x6efab66df92c37e4", 0.0, "blocto", "uni", UInt64(starlyUsdtFeeBps), "1.0"])}
            if UsdcUsdtSwapPair.isFrozen == false {poolInfos.append(["A.b19436aae4d94622.FiatToken", "A.cfdd90d4a00f7b5b.TeleportedTetherToken", UsdcUsdtSwapPair.getPoolAmounts().token1Amount, UsdcUsdtSwapPair.getPoolAmounts().token2Amount, "0x9c6f94adf47904b5", 0.0, "blocto", "blocto-stable", 0, "1.0"])}
            if FusdUsdtSwapPair.isFrozen == false {poolInfos.append(["A.3c5959b568896393.FUSD", "A.cfdd90d4a00f7b5b.TeleportedTetherToken", FusdUsdtSwapPair.getPoolAmounts().token1Amount, FusdUsdtSwapPair.getPoolAmounts().token2Amount, "0x87f3f233f34b0733", 0.0, "blocto", "blocto-stable", 0, "1.0"])}
        }
    }
    return poolInfos
}
```