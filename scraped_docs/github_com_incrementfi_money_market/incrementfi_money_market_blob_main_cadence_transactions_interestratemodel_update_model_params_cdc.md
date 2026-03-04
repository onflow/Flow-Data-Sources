# Source: https://github.com/IncrementFi/Money-Market/blob/main/cadence/transactions/InterestRateModel/update_model_params.cdc

```
import TwoSegmentsInterestRateModel from "../../contracts/TwoSegmentsInterestRateModel.cdc"

transaction(newBlocksPerYear: UInt256, newScaledZeroUtilInterestRatePerYear: UInt256, newScaledCriticalUtilInterestRatePerYear: UInt256, newScaledFullUtilInterestRatePerYear: UInt256, newScaledCriticalUtilPoint: UInt256) {
    prepare(adminAccount: auth(BorrowValue) &Account) {
        let adminRef = adminAccount.storage.borrow<&TwoSegmentsInterestRateModel.Admin>(from: TwoSegmentsInterestRateModel.InterestRateModelAdminStoragePath)
            ?? panic("Cannot borrow reference to InterestRateModel Admin")
        let modelRef = adminAccount.storage.borrow<&TwoSegmentsInterestRateModel.InterestRateModel>(from: TwoSegmentsInterestRateModel.InterestRateModelStoragePath)
            ?? panic("Cannot borrow reference to owned InterestRateModel")

        adminRef.updateInterestRateModelParams(
            interestRateModel: modelRef,
            newBlocksPerYear: newBlocksPerYear,
            newScaledZeroUtilInterestRatePerYear: newScaledZeroUtilInterestRatePerYear,
            newScaledCriticalUtilInterestRatePerYear: newScaledCriticalUtilInterestRatePerYear,
            newScaledFullUtilInterestRatePerYear: newScaledFullUtilInterestRatePerYear,
            newScaledCriticalUtilPoint: newScaledCriticalUtilPoint
        )
    }
}
```