# Source: https://github.com/fixes-world/token-list/blob/main/cadence/scripts/nftlist/get-reviewers.cdc

```
import "FTViewUtils"
import "NFTList"

access(all)
fun main(): [FTViewUtils.ReviewerInfo] {
    let registry = NFTList.borrowRegistry()
    let addrs = registry.getReviewers()
    let ret: [FTViewUtils.ReviewerInfo] = []
    for addr in addrs {
        if let reviewerRef = NFTList.borrowReviewerPublic(addr) {
            ret.append(FTViewUtils.ReviewerInfo(
                address: addr,
                verified: registry.isReviewerVerified(addr),
                name: reviewerRef.getName(),
                url: reviewerRef.getUrl(),
                0,
                reviewerRef.getReviewedNFTAmount(),
                reviewerRef.getCustomizedNFTAmount(),
            ))
        }
    }
    return ret
}

```