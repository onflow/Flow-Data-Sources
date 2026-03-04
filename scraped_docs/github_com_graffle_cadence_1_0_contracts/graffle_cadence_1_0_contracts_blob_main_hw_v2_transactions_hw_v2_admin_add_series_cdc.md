# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/hw_v2/transactions/hw_v2_admin_add_series.cdc

```
import "HWGaragePMV2"

transaction(
    seriesID: UInt64
    ) {
    let manager: &HWGaragePMV2.Manager

    prepare(acct: auth(BorrowValue) &Account) {
        self.manager = acct.storage.borrow<&HWGaragePMV2.Manager>(from: HWGaragePMV2.ManagerStoragePath)
            ?? panic("This account does not have a manager resource")
    }

    execute {
        self.manager.addNewSeriesID(seriesID: seriesID)
    }
}
 
```