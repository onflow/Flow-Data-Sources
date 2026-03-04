# Source: https://github.com/IncrementFi/Money-Market/blob/main/cadence/scripts/Test/query_interest_rates_template.cdc

```
import LendingInterfaces from "../../contracts/LendingInterfaces.cdc"
import TwoSegmentsInterestRateModel from "../../contracts/TwoSegmentsInterestRateModel.cdc"
import LendingConfig from "../../contracts/LendingConfig.cdc"
import LendingPool from "../../contracts/LendingPool.cdc"

// Print current model parameters
access(all) fun main(model: Address): [UInt256; 3] {
    let cash: UInt256 = LendingPool.getPoolCash()
    let borrows: UInt256 = LendingPool.scaledTotalBorrows
    let reserves: UInt256 = LendingPool.scaledTotalReserves
    let interestRateModelRef = getAccount(model)
        .capabilities.borrow<&{LendingInterfaces.InterestRateModelPublic}>(LendingConfig.InterestRateModelPublicPath)
            ?? panic("Could not borrow reference to InterestRateModelParamsGetter")
    let utilRate =  interestRateModelRef.getUtilizationRate(cash: cash, borrows: borrows, reserves: reserves)
    let borrowRate = interestRateModelRef.getBorrowRate(cash: cash, borrows: borrows, reserves: reserves)
    let supplyRate = interestRateModelRef.getSupplyRate(cash: cash, borrows: borrows, reserves: reserves, reserveFactor: 0)
    return [utilRate, borrowRate, supplyRate]
}
```