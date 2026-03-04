# Source: https://github.com/IncrementFi/Money-Market/blob/main/cadence/transactions/AprSnapshot/admin_erase_market_data.cdc

```
import LendingAprSnapshot from "../../contracts/LendingAprSnapshot.cdc"

// LendingAprSnapshot's Admin erases stored apr data of the given lending market and stop tracking
transaction(poolAddr: Address) {
    prepare(aprDataAdmin: auth(BorrowValue) &Account) {
        let aprAdminRef = aprDataAdmin.storage.borrow<&LendingAprSnapshot.Admin>(from: LendingAprSnapshot.AdminStoragePath)
            ?? panic("Lost AprSnapshot admin")
        aprAdminRef.eraseMarketData(poolAddr: poolAddr)
    }
}
```