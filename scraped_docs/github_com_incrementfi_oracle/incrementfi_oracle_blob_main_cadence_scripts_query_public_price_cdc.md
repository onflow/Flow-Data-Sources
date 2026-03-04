# Source: https://github.com/IncrementFi/Oracle/blob/main/cadence/scripts/query_public_price.cdc

```
import PublicPriceOracle from "../contracts/PublicPriceOracle.cdc"

access(all) fun main(oracleAddr: Address): [AnyStruct] {
    return [
        PublicPriceOracle.getLatestPrice(oracleAddr: oracleAddr),
        PublicPriceOracle.getLatestBlockHeight(oracleAddr: oracleAddr)
    ]
}
```