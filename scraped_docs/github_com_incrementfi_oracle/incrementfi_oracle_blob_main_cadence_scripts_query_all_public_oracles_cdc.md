# Source: https://github.com/IncrementFi/Oracle/blob/main/cadence/scripts/query_all_public_oracles.cdc

```
import PublicPriceOracle from "../contracts/PublicPriceOracle.cdc"

access(all) fun main(): {Address: String} {
    return PublicPriceOracle.getAllSupportedOracles()
}
```