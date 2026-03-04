# Source: https://github.com/IncrementFi/Swap/blob/main/src/scripts/query/query_pair_info_by_addrs.testnet.cdc

```
import SwapInterfaces from "../../contracts/SwapInterfaces.cdc"
import SwapConfig from "../../contracts/SwapConfig.cdc"
import IPierPair from "../../contracts/env/IPierPair.cdc"
import PierPair from "../../contracts/env/PierPair.cdc"
import PierSwapFactory from "../../contracts/env/PierSwapFactory.cdc"
import PierSwapSettings from "../../contracts/env/PierSwapSettings.cdc"

import FlowSwapPair from "../../contracts/env/FlowSwapPair.cdc"
import BltUsdtSwapPair from "../../contracts/env/BltUsdtSwapPair.cdc"
import RevvFlowSwapPair from "../../contracts/env/RevvFlowSwapPair.cdc"
import StarlyUsdtSwapPair from "../../contracts/env/StarlyUsdtSwapPair.cdc"
import UsdcUsdtSwapPair from "../../contracts/env/UsdcUsdtSwapPair.cdc"
import FusdUsdtSwapPair from "../../contracts/env/FusdUsdtSwapPair.cdc"

access(all) fun main(pairAddrs: [Address]): [AnyStruct] {
    var res: [AnyStruct] = []
    var i = 0
    var len = pairAddrs.length
    while(i < len) {
        let addr = pairAddrs[i]
        let incrementPool = getAccount(addr).capabilities.borrow<&{SwapInterfaces.PairPublic}>(SwapConfig.PairPublicPath)
            ?? panic("cannot borrow reference to PairPublic")
        let metapierPool = getAccount(addr).capabilities.borrow<&{IPierPair.IPool}>(PierSwapFactory.SwapPoolPublicPath)
            ?? panic("cannot borrow reference to IPierPair")
        if (incrementPool != nil) {
            let poolInfo = incrementPool.getPairInfo()
            if poolInfo.length == 6 {
                res.append([poolInfo[0], poolInfo[1], poolInfo[2], poolInfo[3], poolInfo[4], poolInfo[5], "increment-v1", "uni", 30, "1.0"])
            } else {
                if (poolInfo[7] as! Bool) == true {
                    res.append([poolInfo[0], poolInfo[1], poolInfo[2], poolInfo[3], poolInfo[4], poolInfo[5], "increment-stable", "solidly", poolInfo[6], poolInfo[8]])
                } else {
                    res.append([poolInfo[0], poolInfo[1], poolInfo[2], poolInfo[3], poolInfo[4], poolInfo[5], "increment-v1", "uni", poolInfo[6], "1.0"])
                }
            }
        } else if(metapierPool != nil) {
            let poolAddress = addr
            let token0Key = metapierPool.tokenAType.identifier.slice(from: 0, upTo: metapierPool.tokenAType.identifier.length - 6)
            let token1Key = metapierPool.tokenBType.identifier.slice(from: 0, upTo: metapierPool.tokenBType.identifier.length - 6)
            let reserves = metapierPool.getReserves();
            let metapierSwapFeeBps = UInt64(PierSwapSettings.getPoolTotalFeeCoefficient() * 10.0)
            res.append([token0Key, token1Key, reserves[0], reserves[1], poolAddress, 0.0, "metapier", "uni", metapierSwapFeeBps, "1.0"])
        } else {
            let one = 10000.0
            let flowUsdtFeeBps = FlowSwapPair.feePercentage * one
            let bltUsdtFeeBps = BltUsdtSwapPair.feePercentage * one
            let revvFlowFeeBps = RevvFlowSwapPair.feePercentage * one
            let starlyUsdtFeeBps = StarlyUsdtSwapPair.feePercentage * one
            assert(flowUsdtFeeBps % 1.0 == 0.0, message: "blocto-flow-usdt-feeBps!")
            assert(bltUsdtFeeBps % 1.0 == 0.0, message: "blocto-blt-usdt-feeBps!")
            assert(revvFlowFeeBps % 1.0 == 0.0, message: "blocto-revv-flow-feeBps!")
            assert(starlyUsdtFeeBps % 1.0 == 0.0, message: "blocto-starly-usdt-feeBps!")
            if addr == 0xd9854329b7edf136 && FlowSwapPair.isFrozen == false { res.append(["A.7e60df042a9c0868.FlowToken", "A.ab26e0a07d770ec1.TeleportedTetherToken", FlowSwapPair.getPoolAmounts().token1Amount, FlowSwapPair.getPoolAmounts().token2Amount, "0xd9854329b7edf136", 0.0, "blocto", "uni", UInt64(flowUsdtFeeBps), "1.0"]) }
            if addr == 0xc59604d4e65f14b3 && BltUsdtSwapPair.isFrozen == false { res.append(["A.6e0797ac987005f5.BloctoToken", "A.ab26e0a07d770ec1.TeleportedTetherToken", BltUsdtSwapPair.getPoolAmounts().token1Amount, BltUsdtSwapPair.getPoolAmounts().token2Amount, "0xc59604d4e65f14b3", 0.0, "blocto", "uni", UInt64(bltUsdtFeeBps), "1.0"])}
            if addr == 0xd017f81bffc9aa05 && RevvFlowSwapPair.isFrozen == false { res.append(["A.14ca72fa4d45d2c3.REVV", "A.7e60df042a9c0868.FlowToken", RevvFlowSwapPair.getPoolAmounts().token1Amount, RevvFlowSwapPair.getPoolAmounts().token2Amount, "0xd017f81bffc9aa05", 0.0, "blocto", "uni", UInt64(revvFlowFeeBps), "1.0"])}
            if addr == 0x22d84efc93a8b21a && StarlyUsdtSwapPair.isFrozen == false { res.append(["A.f63219072aaddd50.StarlyToken", "A.ab26e0a07d770ec1.TeleportedTetherToken", StarlyUsdtSwapPair.getPoolAmounts().token1Amount, StarlyUsdtSwapPair.getPoolAmounts().token2Amount, "0x22d84efc93a8b21a", 0.0, "blocto", "uni", UInt64(starlyUsdtFeeBps), "1.0"])}
            if addr == 0x481744401ea249c0 && UsdcUsdtSwapPair.isFrozen == false { res.append(["A.a983fecbed621163.FiatToken", "A.ab26e0a07d770ec1.TeleportedTetherToken", UsdcUsdtSwapPair.getPoolAmounts().token1Amount, UsdcUsdtSwapPair.getPoolAmounts().token2Amount, "0x481744401ea249c0", 0.0, "blocto", "blocto-stable", 0, "1.0"])}
            if addr == 0x3502a5dacaf350bb && FusdUsdtSwapPair.isFrozen == false { res.append(["A.e223d8a629e49c68.FUSD", "A.ab26e0a07d770ec1.TeleportedTetherToken", FusdUsdtSwapPair.getPoolAmounts().token1Amount, FusdUsdtSwapPair.getPoolAmounts().token2Amount, "0x3502a5dacaf350bb", 0.0, "blocto", "blocto-stable", 0, "1.001"])}
        }
        i = i + 1
    }
    return res
}
```