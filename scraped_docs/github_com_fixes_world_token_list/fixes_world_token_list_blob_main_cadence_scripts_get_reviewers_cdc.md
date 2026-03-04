# Source: https://github.com/fixes-world/token-list/blob/main/cadence/scripts/get-reviewers.cdc

```
import "FTViewUtils"
import "TokenList"

access(all)
fun main(): [FTViewUtils.ReviewerInfo] {
    let registry = TokenList.borrowRegistry()
    let addrs = registry.getReviewers()
    let ret: [FTViewUtils.ReviewerInfo] = []
    for addr in addrs {
        if let reviewerRef = TokenList.borrowReviewerPublic(addr) {
            ret.append(FTViewUtils.ReviewerInfo(
                address: addr,
                verified: registry.isReviewerVerified(addr),
                name: reviewerRef.getName(),
                url: reviewerRef.getUrl(),
                reviewerRef.getManagedTokenAmount(),
                reviewerRef.getReviewedTokenAmount(),
                reviewerRef.getCustomizedTokenAmount(),
            ))
        }
    }
    return ret
}

```