# Source: https://github.com/fixes-world/token-list/blob/main/cadence/scripts/get-reviewer-info.cdc

```
import "FTViewUtils"
import "TokenList"

access(all)
fun main(
    addr: Address
): FTViewUtils.ReviewerInfo? {
    let registry = TokenList.borrowRegistry()
    if let reviewerRef = TokenList.borrowReviewerPublic(addr) {
        return FTViewUtils.ReviewerInfo(
            address: addr,
            verified: registry.isReviewerVerified(addr),
            name: reviewerRef.getName(),
            url: reviewerRef.getUrl(),
            reviewerRef.getManagedTokenAmount(),
            reviewerRef.getReviewedTokenAmount(),
            reviewerRef.getCustomizedTokenAmount(),
        )
    }
    return nil
}

```