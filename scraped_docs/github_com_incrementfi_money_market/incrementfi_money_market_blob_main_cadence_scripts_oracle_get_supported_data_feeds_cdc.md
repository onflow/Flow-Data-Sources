# Source: https://github.com/IncrementFi/Money-Market/blob/main/cadence/scripts/Oracle/get_supported_data_feeds.cdc

```
import LendingInterfaces from "../../contracts/LendingInterfaces.cdc"
import LendingOracle from "../../contracts/LendingOracle.cdc"

access(all) fun main(oracle: Address): [Address] {
    let oracleGetterRef = getAccount(oracle)
        .capabilities.borrow<&{LendingInterfaces.OraclePublic}>(LendingOracle.OraclePublicPath)
            ?? panic("Could not borrow reference to OracleGetter")

    return oracleGetterRef.getSupportedFeeds()
}
```