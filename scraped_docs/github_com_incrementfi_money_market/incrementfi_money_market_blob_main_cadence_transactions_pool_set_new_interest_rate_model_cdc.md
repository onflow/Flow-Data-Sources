# Source: https://github.com/IncrementFi/Money-Market/blob/main/cadence/transactions/Pool/set_new_interest_rate_model.cdc

```
import LendingPool from "../../contracts/LendingPool.cdc"

transaction(newInterestRateModelAddr: Address) {
    prepare(poolAccount: auth(BorrowValue) &Account) {
        let poolAdminRef = poolAccount.storage.borrow<&LendingPool.PoolAdmin>(from: LendingPool.PoolAdminStoragePath)
            ?? panic("cannot borrow reference to pool admin")
        poolAdminRef.setInterestRateModel(newInterestRateModelAddress: newInterestRateModelAddr)
    }
}
```