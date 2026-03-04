# Source: https://github.com/fixes-world/token-list/blob/main/cadence/scripts/query-evm-bridged-nft-list.cdc

```
import "TokenListHelper"

access(all)
fun main(
    page: Int,
    size: Int,
    reviewer: Address?,
): TokenListHelper.QueryResult {
    return TokenListHelper.queryEVMBridgedNFTs(page: page, size: size, reviewer: reviewer)
}

```