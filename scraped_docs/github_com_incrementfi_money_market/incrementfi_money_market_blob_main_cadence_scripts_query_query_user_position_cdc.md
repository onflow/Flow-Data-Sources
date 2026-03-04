# Source: https://github.com/IncrementFi/Money-Market/blob/main/cadence/scripts/Query/query_user_position.cdc

```
import LendingInterfaces from "../../contracts/LendingInterfaces.cdc"
import LendingConfig from "../../contracts/LendingConfig.cdc"
import LendingError from "../../contracts/LendingError.cdc"

// Return: (cross-market collateral value in usd; cross-market borrows in usd)
// LTV ratio = ret[1] / ret[0]
access(all) fun main(userAddr: Address, comptrollerAddr: Address): [String; 3] {
    let comptrollerRef = getAccount(comptrollerAddr).capabilities.borrow<&{LendingInterfaces.ComptrollerPublic}>(LendingConfig.ComptrollerPublicPath)
        ?? panic(
            LendingError.ErrorEncode (
                msg: "Invailid comptroller cap.",
                err: LendingError.ErrorCode.CANNOT_ACCESS_COMPTROLLER_PUBLIC_CAPABILITY
            )
        )
    let res = comptrollerRef.getUserCrossMarketLiquidity(userAddr: userAddr)
    return res
}
```