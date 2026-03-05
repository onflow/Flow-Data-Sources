# Source: https://github.com/IncrementFi/Money-Market/blob/main/cadence/scripts/InterestRateModel/get_model_params.cdc

```
import LendingInterfaces from "../../contracts/LendingInterfaces.cdc"
import TwoSegmentsInterestRateModel from "../../contracts/TwoSegmentsInterestRateModel.cdc"
import LendingConfig from "../../contracts/LendingConfig.cdc"

/// Print current model parameters
access(all) fun main(model: Address): {String: AnyStruct} {
    let interestRateModelRef = getAccount(model)
        .capabilities.borrow<&{LendingInterfaces.InterestRateModelPublic}>(LendingConfig.InterestRateModelPublicPath)
            ?? panic("Could not borrow reference to InterestRateModelParamsGetter")
    
    return interestRateModelRef.getInterestRateModelParams()
}
```