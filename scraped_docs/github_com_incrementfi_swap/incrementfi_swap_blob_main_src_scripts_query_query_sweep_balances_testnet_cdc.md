# Source: https://github.com/IncrementFi/Swap/blob/main/src/scripts/query/query_sweep_balances.testnet.cdc

```
import FungibleToken from "../../contracts/env/FungibleToken.cdc"
import StableSwapFactory from "../../contracts/StableSwapFactory.cdc"
import SwapFactory from "../../contracts/SwapFactory.cdc"
import SwapConfig from "../../contracts/SwapConfig.cdc"
import SwapInterfaces from "../../contracts/SwapInterfaces.cdc"

access(all) fun main(userAddr: Address, tokenKeys: [String], balancePathPrefixs: [String], onlySetup: Bool): [AnyStruct] {
    let res: [AnyStruct] = []
    let flowTokenKey = "A.7e60df042a9c0868.FlowToken"
    let flow2usdcInfo = SwapFactory.getPairInfo(token0Key: flowTokenKey, token1Key: "A.e223d8a629e49c68.FUSD")! as! [AnyStruct]
    let flowPrice = (flow2usdcInfo[3] as! UFix64) / (flow2usdcInfo[2] as! UFix64)
    
    var i = 0
    for balancePathPrefix in balancePathPrefixs {
        let balancePath = PublicPath(identifier: balancePathPrefix)!
        let balanceRef = getAccount(userAddr).capabilities.borrow<&{FungibleToken.Balance}>(balancePath)
        var balance = 0.0
        if balanceRef != nil {
            balance = balanceRef!.balance
        }
        if onlySetup == true && balanceRef == nil {
            i = i + 1
            continue
        }
        let sPairAddr = StableSwapFactory.getPairAddress(token0Key: flowTokenKey, token1Key: tokenKeys[i])
        let vPairAddr = SwapFactory.getPairAddress(token0Key: flowTokenKey, token1Key: tokenKeys[i])

        var sPoolFlowReserve = 0.0;
        var vPoolFlowReserve = 0.0;
        var sAmountOut = 0.0
        var vAmountOut = 0.0
        var sQuote = 0.0
        var vQuote = 0.0

        if sPairAddr != nil {
            let poolRef = getAccount(sPairAddr!).capabilities.borrow<&{SwapInterfaces.PairPublic}>(SwapConfig.PairPublicPath)!
            let poolInfo = poolRef.getPairInfo()
            let token0Key = poolInfo[0] as! String
            let token1Key = poolInfo[1] as! String
            var token0Reserve = poolInfo[2] as! UFix64
            var token1Reserve = poolInfo[3] as! UFix64
            if token0Key == flowTokenKey { sPoolFlowReserve = token0Reserve }
            else { sPoolFlowReserve = token1Reserve }
            if balance > 0.0 && sPoolFlowReserve > 0.0 {
                sAmountOut = poolRef.getAmountOut(amountIn: balance, tokenInKey: tokenKeys[i])
            }
            if sPoolFlowReserve > 10.0 {
                let curveP = poolRef.getStableCurveP()
                if token0Key == flowTokenKey {
                    sQuote = SwapConfig.quoteStable(amountA: 1.0, reserveA: token1Reserve, reserveB: token0Reserve, p: 1.0/curveP)
                } else {
                    sQuote = SwapConfig.quoteStable(amountA: 1.0, reserveA: token0Reserve, reserveB: token1Reserve, p: curveP)
                }
            }
        }
        if vPairAddr != nil {
            let poolRef = getAccount(vPairAddr!).capabilities.borrow<&{SwapInterfaces.PairPublic}>(SwapConfig.PairPublicPath)!
            let poolInfo = poolRef.getPairInfo()
            let token0Key = poolInfo[0] as! String
            let token1Key = poolInfo[1] as! String
            var token0Reserve = poolInfo[2] as! UFix64
            var token1Reserve = poolInfo[3] as! UFix64
            
            if token0Key == flowTokenKey { vPoolFlowReserve = token0Reserve }
            else { vPoolFlowReserve = token1Reserve }
            if balance > 0.0 && vPoolFlowReserve > 0.0 {
                vAmountOut = poolRef.getAmountOut(amountIn: balance, tokenInKey: tokenKeys[i])
            }
            if vPoolFlowReserve > 10.0 {
                if token0Key == flowTokenKey {
                    vQuote = SwapConfig.quote(amountA: 1.0, reserveA: token1Reserve, reserveB: token0Reserve)
                } else {
                    vQuote = SwapConfig.quote(amountA: 1.0, reserveA: token0Reserve, reserveB: token1Reserve)
                }
            }
        }

        var flowQuote = (sPoolFlowReserve > vPoolFlowReserve)? sQuote : vQuote
        var sweepFlowAmount = (sAmountOut>vAmountOut)? sAmountOut:vAmountOut
        if tokenKeys[i] == flowTokenKey {
            flowQuote = 1.0
            sweepFlowAmount = balance
        }
        res.append({
            "tokenKey": tokenKeys[i],
            "ifSetup": (balanceRef != nil),
            "balance": balance,
            "sweepFlowAmount": sweepFlowAmount,
            "flowQuote": flowQuote,
            "usdcQuote": flowQuote * flowPrice
        })

        i = i + 1
    }
    return res
}
```