# Source: https://github.com/fixes-world/token-list/blob/main/cadence/scripts/query-token-list-by-address.cdc

```
import "TokenListHelper"

access(all)
fun main(
    ftAddress: Address,
    reviewer: Address?,
): TokenListHelper.QueryResult {
    return TokenListHelper.queryFTsByAddress(ftAddress: ftAddress, reviewer: reviewer)
}

```