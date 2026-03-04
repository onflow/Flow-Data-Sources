# Source: https://github.com/IncrementFi/Money-Market/blob/main/cadence/scripts/Test/query_pool_state_template.cdc

```
import LendingInterfaces from "../../contracts/LendingInterfaces.cdc"
import LendingConfig from "../../contracts/LendingConfig.cdc"
import LendingPool from "../../contracts/LendingPool.cdc"

access(all) fun main(): {String: AnyStruct} {
    var res:{String: AnyStruct} = {
        "BlockNumber": LendingPool.accrualBlockNumber.toString(),
        "BorrowIndex": LendingPool.scaledBorrowIndex.toString(),
        "TotalBorrows": LendingPool.scaledTotalBorrows.toString(),
        "TotalReserves": LendingPool.scaledTotalReserves.toString(),
        "TotalSupply": LendingPool.scaledTotalSupply.toString(),
        "ReserveFactor": LendingPool.scaledReserveFactor.toString(),
        "PoolSeizeShare": LendingPool.scaledPoolSeizeShare.toString(),
        "TotalCash": LendingPool.getPoolCash().toString(),
        "LpTokenMintRate": LendingPool.underlyingToLpTokenRateSnapshotScaled().toString()
    }
    return res
}
```