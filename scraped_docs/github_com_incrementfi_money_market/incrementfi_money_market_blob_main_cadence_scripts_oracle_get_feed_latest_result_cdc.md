# Source: https://github.com/IncrementFi/Money-Market/blob/main/cadence/scripts/Oracle/get_feed_latest_result.cdc

```
import LendingInterfaces from "../../contracts/LendingInterfaces.cdc"
import LendingOracle from "../../contracts/LendingOracle.cdc"

/// Return pool's underlying asset's latest data in [timestamp, priceData].
/// Return value of [0.0, 0.0] means the queried pool's underlying asset's data feed is not available.
access(all) fun main(oracle: Address, pool: Address): [UFix64; 2] {
    let oracleGetterRef = getAccount(oracle)
        .capabilities.borrow<&{LendingInterfaces.OraclePublic}>(LendingOracle.OraclePublicPath)
            ?? panic("Could not borrow reference to OracleGetter")

    return oracleGetterRef.latestResult(pool: pool)
}
```