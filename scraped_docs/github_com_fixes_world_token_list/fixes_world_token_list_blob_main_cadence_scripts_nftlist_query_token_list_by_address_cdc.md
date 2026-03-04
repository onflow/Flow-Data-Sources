# Source: https://github.com/fixes-world/token-list/blob/main/cadence/scripts/nftlist/query-token-list-by-address.cdc

```
import "TokenListHelper"

access(all)
fun main(
    address: Address,
    reviewer: Address?,
): TokenListHelper.QueryResult {
    return TokenListHelper.queryNFTsByAddress(address: address, reviewer: reviewer)
}

```