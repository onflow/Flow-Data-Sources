# Source: https://github.com/IncrementFi/Money-Market/blob/main/cadence/scripts/Query/query_market_infos.cdc

```
import LendingInterfaces from "../../contracts/LendingInterfaces.cdc"
import LendingConfig from "../../contracts/LendingConfig.cdc"
import LendingError from "../../contracts/LendingError.cdc"

access(all) fun main(comptrollerAddr: Address): {Address: AnyStruct} {
    let comptrollerRef = getAccount(comptrollerAddr).capabilities.borrow<&{LendingInterfaces.ComptrollerPublic}>(LendingConfig.ComptrollerPublicPath)
        ?? panic(
            LendingError.ErrorEncode (
                msg: "Invailid comptroller cap.",
                err: LendingError.ErrorCode.CANNOT_ACCESS_COMPTROLLER_PUBLIC_CAPABILITY
            )
        )
    let poolAddrs = comptrollerRef.getAllMarkets()

    var poolInfos: {Address: AnyStruct} = {}
    for poolAddr in poolAddrs {
        let poolInfo = comptrollerRef.getMarketInfo(poolAddr: poolAddr)
        poolInfos.insert(key: poolAddr, poolInfo)
    }
    
    return poolInfos
}
```