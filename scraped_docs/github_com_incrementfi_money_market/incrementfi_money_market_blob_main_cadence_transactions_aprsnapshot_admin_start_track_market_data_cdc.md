# Source: https://github.com/IncrementFi/Money-Market/blob/main/cadence/transactions/AprSnapshot/admin_start_track_market_data.cdc

```
import LendingAprSnapshot from "../../contracts/LendingAprSnapshot.cdc"

// LendingAprSnapshot's Admin starts tracking apr data of the given lending market
transaction(poolAddr: Address) {
    prepare(aprDataAdmin: auth(BorrowValue) &Account) {
        let aprAdminRef = aprDataAdmin.storage.borrow<&LendingAprSnapshot.Admin>(from: LendingAprSnapshot.AdminStoragePath)
            ?? panic("Lost AprSnapshot admin")
        aprAdminRef.trackMarketData(poolAddr: poolAddr)
    }
}
```