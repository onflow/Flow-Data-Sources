# Source: https://github.com/IncrementFi/Swap/blob/main/src/scripts/query/query_pair_array_info.testnet.cdc

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

access(all) fun main(from: UInt64, to: UInt64, poolSources: [String]): [AnyStruct] {
    pre {
        from <= to: "from > to"
    }
    let poolInfos: [AnyStruct] = [];
    for poolSource in poolSources {
        if (poolSource == "increment-v1") {
            var increment_v1: [AnyStruct] = []
            // Get rid of runtime error of bad SwapPairs at index range: [ [16, 18], [39, 42] ]
            if (to < 16 || (from > 18 && to < 39) || from > 42) {
                increment_v1 = SwapFactory.getSlicedPairInfos(from: from, to: to)
            } else if (from < 16) {
                if (to >= 16 && to <= 18) {
                    increment_v1 = SwapFactory.getSlicedPairInfos(from: from, to: 15)
                } else if (to > 18 && to < 39) {
                    increment_v1 = SwapFactory.getSlicedPairInfos(from: from, to: 15)
                    let tmp = SwapFactory.getSlicedPairInfos(from: 19, to: to)
                    increment_v1.appendAll(tmp)
                } else if (to >= 39 && to <= 42) {
                    increment_v1 = SwapFactory.getSlicedPairInfos(from: from, to: 15)
                    let tmp = SwapFactory.getSlicedPairInfos(from: 19, to: 38)
                    increment_v1.appendAll(tmp)
                } else if (to > 42) {
                    increment_v1 = SwapFactory.getSlicedPairInfos(from: from, to: 15)
                    let tmp1 = SwapFactory.getSlicedPairInfos(from: 19, to: 38)
                    increment_v1.appendAll(tmp1)
                    let tmp2 = SwapFactory.getSlicedPairInfos(from: 43, to: to)
                    increment_v1.appendAll(tmp2)
                }
            } else if (from >= 16 && from <= 18) {
                if (to > 18 && to < 39) {
                    increment_v1 = SwapFactory.getSlicedPairInfos(from: 19, to: to)
                } else if (to >= 39 && to <= 42) {
                    increment_v1 = SwapFactory.getSlicedPairInfos(from: 19, to: 38)
                } else if (to > 42) {
                    increment_v1 = SwapFactory.getSlicedPairInfos(from: 19, to: 38)
                    let tmp = SwapFactory.getSlicedPairInfos(from: 43, to: to)
                    increment_v1.appendAll(tmp)
                }
            } else if (from > 18 && from < 39) {
                if (to >= 39 && to <= 42) {
                    increment_v1 = SwapFactory.getSlicedPairInfos(from: from, to: 38)
                } else if (to > 42) {
                    increment_v1 = SwapFactory.getSlicedPairInfos(from: from, to: 38)
                    let tmp = SwapFactory.getSlicedPairInfos(from: 43, to: to)
                    increment_v1.appendAll(tmp)
                }
            } else if (from >= 39 && from <= 42) {
                if (to > 42) {
                    increment_v1 = SwapFactory.getSlicedPairInfos(from: 43, to: to)
                }
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
            while(metapierPoolIndex < metapierPoolSize && metapierPoolIndex <= to) {
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

            if FlowSwapPair.isFrozen == false {poolInfos.append(["A.7e60df042a9c0868.FlowToken", "A.ab26e0a07d770ec1.TeleportedTetherToken", FlowSwapPair.getPoolAmounts().token1Amount, FlowSwapPair.getPoolAmounts().token2Amount, "0xd9854329b7edf136", 0.0, "blocto", "uni", UInt64(flowUsdtFeeBps), "1.0"])}
            if BltUsdtSwapPair.isFrozen == false {poolInfos.append(["A.6e0797ac987005f5.BloctoToken", "A.ab26e0a07d770ec1.TeleportedTetherToken", BltUsdtSwapPair.getPoolAmounts().token1Amount, BltUsdtSwapPair.getPoolAmounts().token2Amount, "0xc59604d4e65f14b3", 0.0, "blocto", "uni", UInt64(bltUsdtFeeBps), "1.0"])}
            if RevvFlowSwapPair.isFrozen == false {poolInfos.append(["A.14ca72fa4d45d2c3.REVV", "A.7e60df042a9c0868.FlowToken", RevvFlowSwapPair.getPoolAmounts().token1Amount, RevvFlowSwapPair.getPoolAmounts().token2Amount, "0xd017f81bffc9aa05", 0.0, "blocto", "uni", UInt64(revvFlowFeeBps), "1.0"])}
            if StarlyUsdtSwapPair.isFrozen == false {poolInfos.append(["A.f63219072aaddd50.StarlyToken", "A.ab26e0a07d770ec1.TeleportedTetherToken", StarlyUsdtSwapPair.getPoolAmounts().token1Amount, StarlyUsdtSwapPair.getPoolAmounts().token2Amount, "0x22d84efc93a8b21a", 0.0, "blocto", "uni", UInt64(starlyUsdtFeeBps), "1.0"])}
            if UsdcUsdtSwapPair.isFrozen == false {poolInfos.append(["A.a983fecbed621163.FiatToken", "A.ab26e0a07d770ec1.TeleportedTetherToken", UsdcUsdtSwapPair.getPoolAmounts().token1Amount, UsdcUsdtSwapPair.getPoolAmounts().token2Amount, "0x481744401ea249c0", 0.0, "blocto", "blocto-stable", 0, "1.0"])}
            if FusdUsdtSwapPair.isFrozen == false {poolInfos.append(["A.e223d8a629e49c68.FUSD", "A.ab26e0a07d770ec1.TeleportedTetherToken", FusdUsdtSwapPair.getPoolAmounts().token1Amount, FusdUsdtSwapPair.getPoolAmounts().token2Amount, "0x3502a5dacaf350bb", 0.0, "blocto", "blocto-stable", 0, "1.001"])}
        }
    }
    return poolInfos
}
```