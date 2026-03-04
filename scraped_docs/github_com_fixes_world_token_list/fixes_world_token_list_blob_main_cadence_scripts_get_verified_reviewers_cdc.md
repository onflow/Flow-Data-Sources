# Source: https://github.com/fixes-world/token-list/blob/main/cadence/scripts/get-verified-reviewers.cdc

```
import "FTViewUtils"
import "TokenList"

access(all)
fun main(): [FTViewUtils.ReviewerInfo] {
    let registry = TokenList.borrowRegistry()
    let addrs = registry.getVerifiedReviewers()
    let ret: [FTViewUtils.ReviewerInfo] = []
    for addr in addrs {
        if let reviewerRef = TokenList.borrowReviewerPublic(addr) {
            ret.append(FTViewUtils.ReviewerInfo(
                address: addr,
                verified: true,
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