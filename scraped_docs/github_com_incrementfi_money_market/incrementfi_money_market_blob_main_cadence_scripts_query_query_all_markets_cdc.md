# Source: https://github.com/IncrementFi/Money-Market/blob/main/cadence/scripts/Query/query_all_markets.cdc

```
import LendingInterfaces from "../../contracts/LendingInterfaces.cdc"
import LendingConfig from "../../contracts/LendingConfig.cdc"
import LendingError from "../../contracts/LendingError.cdc"

access(all) fun main(comptrollerAddr: Address): [Address] {
    let comptrollerRef = getAccount(comptrollerAddr).capabilities.borrow<&{LendingInterfaces.ComptrollerPublic}>(LendingConfig.ComptrollerPublicPath)
        ?? panic(
            LendingError.ErrorEncode (
                msg: "Invailid comptroller cap.",
                err: LendingError.ErrorCode.CANNOT_ACCESS_COMPTROLLER_PUBLIC_CAPABILITY
            )
        )
    let poolAddrs = comptrollerRef.getAllMarkets()
    return poolAddrs
}
```