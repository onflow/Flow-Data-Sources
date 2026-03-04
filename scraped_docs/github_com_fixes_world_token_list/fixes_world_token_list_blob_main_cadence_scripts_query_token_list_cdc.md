# Source: https://github.com/fixes-world/token-list/blob/main/cadence/scripts/query-token-list.cdc

```
import "TokenListHelper"

/// Filter type:
///   0 - All
///   1 - Reviewed by Reviewer
///   2 - Managed by Reviewer
///   3 - Verified by Reviewer
///   4 - Featured by Reviewer
///   5 - Blocked by Reviewer
///
access(all)
fun main(
    page: Int,
    size: Int,
    reviewer: Address?,
    filterType: UInt8?,
): TokenListHelper.QueryResult {
    return TokenListHelper.queryFTs(page: page, size: size, reviewer: reviewer, filterType: filterType)
}

```