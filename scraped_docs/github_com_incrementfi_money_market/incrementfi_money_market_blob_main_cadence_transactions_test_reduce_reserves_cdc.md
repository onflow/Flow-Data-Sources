# Source: https://github.com/IncrementFi/Money-Market/blob/main/cadence/transactions/Test/reduce_reserves.cdc

```
import LendingPool from "../../contracts/LendingPool.cdc"

transaction() {
    prepare(poolAccount: auth(BorrowValue) &Account) {
        log("Transaction Start --------------- init_flow_pool")
        
        log("Init pool of fusd:")

        let PoolAdminRef = poolAccount.storage.borrow<&LendingPool.PoolAdmin>(from: LendingPool.PoolAdminStoragePath) ?? panic("Lost pool admin.")
        let v <- PoolAdminRef.withdrawReserves(reduceAmount: 0.000001)
        destroy v

        log("End -----------------------------")
    }
}
```