# Source: https://github.com/IncrementFi/Money-Market/blob/main/cadence/transactions/InterestRateModel/create_interest_rate_model.cdc

```
import LendingInterfaces from "../../contracts/LendingInterfaces.cdc"
import TwoSegmentsInterestRateModel from "../../contracts/TwoSegmentsInterestRateModel.cdc"
import LendingConfig from "../../contracts/LendingConfig.cdc"

// Note: Only run once.
//       Any subsequent runs will discard existing InterestRateModel resource and create & link a new one.
transaction(modelName: String, blocksPerYear: UInt256, scaledZeroUtilInterestRatePerYear: UInt256, scaledCriticalUtilInterestRatePerYear: UInt256, scaledFullUtilInterestRatePerYear: UInt256, scaledCriticalUtilRate: UInt256) {
    prepare(adminAccount: auth(Storage, Capabilities) &Account) {
        let adminRef = adminAccount.storage.borrow<&TwoSegmentsInterestRateModel.Admin>(from: TwoSegmentsInterestRateModel.InterestRateModelAdminStoragePath)
            ?? panic("Could not borrow reference to InterestRateModel Admin")

        // Discard any existing contents
        let oldAny <- adminAccount.storage.load<@AnyResource>(from: TwoSegmentsInterestRateModel.InterestRateModelStoragePath)
        destroy oldAny

        // Create an InterestRateModel resource, stores it and publishes public capability to it.
        let newModel <- adminRef.createInterestRateModel(
            modelName: modelName,
            blocksPerYear: blocksPerYear,
            scaledZeroUtilInterestRatePerYear: scaledZeroUtilInterestRatePerYear,
            scaledCriticalUtilInterestRatePerYear: scaledCriticalUtilInterestRatePerYear,
            scaledFullUtilInterestRatePerYear: scaledFullUtilInterestRatePerYear,
            scaledCriticalUtilPoint: scaledCriticalUtilRate
        )
        adminAccount.storage.save(<-newModel, to: TwoSegmentsInterestRateModel.InterestRateModelStoragePath)
        adminAccount.capabilities.unpublish(LendingConfig.InterestRateModelPublicPath)
        adminAccount.capabilities.publish(
            adminAccount.capabilities.storage.issue<&{LendingInterfaces.InterestRateModelPublic}>(TwoSegmentsInterestRateModel.InterestRateModelStoragePath),
            at: LendingConfig.InterestRateModelPublicPath
        )
    }
}
```