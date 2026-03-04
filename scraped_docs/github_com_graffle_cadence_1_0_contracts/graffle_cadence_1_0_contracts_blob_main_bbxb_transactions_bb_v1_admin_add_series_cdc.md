# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/bbxb/transactions/bb_v1_admin_add_series.cdc

```

import "BBxBarbiePM"

transaction(
    seriesID: UInt64
    ) {
    let manager: &BBxBarbiePM.Manager

    prepare(acct: auth(BorrowValue) &Account) {
        self.manager = acct.storage.borrow<&BBxBarbiePM.Manager>(from: BBxBarbiePM.ManagerStoragePath)
            ?? panic("This account does not have a manager resource")
    }

    execute {
        self.manager.addNewSeriesID(seriesID: seriesID)
    }
}
 
```