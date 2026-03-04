# Source: https://github.com/IncrementFi/Money-Market/blob/main/cadence/scripts/Query/query_market_interestrate_model_params.cdc

```
import LendingInterfaces from "../../contracts/LendingInterfaces.cdc"
import LendingConfig from "../../contracts/LendingConfig.cdc"
import LendingError from "../../contracts/LendingError.cdc"

access(all) fun main(poolAddr: Address): {String: AnyStruct} {

    let poolPublicCap = getAccount(poolAddr).capabilities.borrow<&{LendingInterfaces.PoolPublic}>(LendingConfig.PoolPublicPublicPath)
        ?? panic(
            LendingError.ErrorEncode (
                msg: "Invalid pool capability.",
                err: LendingError.ErrorCode.CANNOT_ACCESS_POOL_PUBLIC_CAPABILITY
            )
        )
    let interestRateAddress = poolPublicCap.getInterestRateModelAddress()

    let interestRateModelRef = getAccount(interestRateAddress)
        .capabilities.borrow<&{LendingInterfaces.InterestRateModelPublic}>(LendingConfig.InterestRateModelPublicPath) ?? panic(
            LendingError.ErrorEncode (
                msg: "Invalid interest rate model capability.",
                err: LendingError.ErrorCode.CANNOT_ACCESS_INTEREST_RATE_MODEL_CAPABILITY
            )
        )
    
    return interestRateModelRef.getInterestRateModelParams()
}
```