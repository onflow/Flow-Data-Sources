# Source: https://github.com/IncrementFi/Money-Market/blob/main/cadence/scripts/InterestRateModel/get_interest_rates.cdc

```
import LendingInterfaces from "../../contracts/LendingInterfaces.cdc"
import TwoSegmentsInterestRateModel from "../../contracts/TwoSegmentsInterestRateModel.cdc"
import LendingConfig from "../../contracts/LendingConfig.cdc"

/// Print current model parameters
access(all) fun main(model: Address, cash: UInt256, borrows: UInt256, reserves: UInt256): [UInt256; 3] {
    let interestRateModelRef = getAccount(model)
        .capabilities.borrow<&{LendingInterfaces.InterestRateModelPublic}>(LendingConfig.InterestRateModelPublicPath)
            ?? panic("Could not borrow reference to InterestRateModelParamsGetter")
    let utilRate =  interestRateModelRef.getUtilizationRate(cash: cash, borrows: borrows, reserves: reserves)
    let borrowRate = interestRateModelRef.getBorrowRate(cash: cash, borrows: borrows, reserves: reserves)
    let supplyRate = interestRateModelRef.getSupplyRate(cash: cash, borrows: borrows, reserves: reserves, reserveFactor: 0)
    return [utilRate, borrowRate, supplyRate]
}
```