# Source: https://github.com/IncrementFi/Swap/blob/main/src/scripts/query/query_pair_info_by_addrs.mainnet.cdc

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
            if addr == 0xc6c77b9f5c7a378f && FlowSwapPair.isFrozen == false { res.append(["A.1654653399040a61.FlowToken", "A.cfdd90d4a00f7b5b.TeleportedTetherToken", FlowSwapPair.getPoolAmounts().token1Amount, FlowSwapPair.getPoolAmounts().token2Amount, "0xc6c77b9f5c7a378f", 0.0, "blocto", "uni", UInt64(flowUsdtFeeBps), "1.0"])}
            if addr == 0xfcb06a5ae5b21a2d && BltUsdtSwapPair.isFrozen == false { res.append(["A.0f9df91c9121c460.BloctoToken", "A.cfdd90d4a00f7b5b.TeleportedTetherToken", BltUsdtSwapPair.getPoolAmounts().token1Amount, BltUsdtSwapPair.getPoolAmounts().token2Amount, "0xfcb06a5ae5b21a2d", 0.0, "blocto", "uni", UInt64(bltUsdtFeeBps), "1.0"])}
            if addr == 0x5e284fb7cff23a3f && RevvFlowSwapPair.isFrozen == false { res.append(["A.d01e482eb680ec9f.REVV", "A.1654653399040a61.FlowToken", RevvFlowSwapPair.getPoolAmounts().token1Amount, RevvFlowSwapPair.getPoolAmounts().token2Amount, "0x5e284fb7cff23a3f", 0.0, "blocto", "uni", UInt64(revvFlowFeeBps), "1.0"])}
            if addr == 0x6efab66df92c37e4 && StarlyUsdtSwapPair.isFrozen == false { res.append(["A.142fa6570b62fd97.StarlyToken", "A.cfdd90d4a00f7b5b.TeleportedTetherToken", StarlyUsdtSwapPair.getPoolAmounts().token1Amount, StarlyUsdtSwapPair.getPoolAmounts().token2Amount, "0x6efab66df92c37e4", 0.0, "blocto", "uni", UInt64(starlyUsdtFeeBps), "1.0"])}
            if addr == 0x9c6f94adf47904b5 && UsdcUsdtSwapPair.isFrozen == false { res.append(["A.b19436aae4d94622.FiatToken", "A.cfdd90d4a00f7b5b.TeleportedTetherToken", UsdcUsdtSwapPair.getPoolAmounts().token1Amount, UsdcUsdtSwapPair.getPoolAmounts().token2Amount, "0x9c6f94adf47904b5", 0.0, "blocto", "blocto-stable", 0, "1.0"])}
            if addr == 0x87f3f233f34b0733 && FusdUsdtSwapPair.isFrozen == false { res.append(["A.3c5959b568896393.FUSD", "A.cfdd90d4a00f7b5b.TeleportedTetherToken", FusdUsdtSwapPair.getPoolAmounts().token1Amount, FusdUsdtSwapPair.getPoolAmounts().token2Amount, "0x87f3f233f34b0733", 0.0, "blocto", "blocto-stable", 0, "1.0"])}
        }
        i = i + 1
    }
    return res
}
```