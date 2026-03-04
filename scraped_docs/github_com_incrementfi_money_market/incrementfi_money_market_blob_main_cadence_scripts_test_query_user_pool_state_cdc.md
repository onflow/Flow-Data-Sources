# Source: https://github.com/IncrementFi/Money-Market/blob/main/cadence/scripts/Test/query_user_pool_state.cdc

```
import LendingInterfaces from "../../contracts/LendingInterfaces.cdc"
import LendingConfig from "../../contracts/LendingConfig.cdc"

access(all) fun main(poolAddr: Address, userAddr: Address): [String;5] {
    let poolRef = getAccount(poolAddr).capabilities.borrow<&{LendingInterfaces.PoolPublic}>(LendingConfig.PoolPublicPublicPath)!
    let res = poolRef.getAccountSnapshotScaled(account: userAddr)
    return [res[0].toString(), res[1].toString(), res[2].toString(), res[3].toString(), res[4].toString()]
}
```