# Source: https://github.com/fixes-world/token-list/blob/main/cadence/scripts/nftlist/get-reviewer-info.cdc

```
import "FTViewUtils"
import "NFTList"

access(all)
fun main(
    addr: Address
): FTViewUtils.ReviewerInfo? {
    let registry = NFTList.borrowRegistry()
    if let reviewerRef = NFTList.borrowReviewerPublic(addr) {
        return FTViewUtils.ReviewerInfo(
            address: addr,
            verified: registry.isReviewerVerified(addr),
            name: reviewerRef.getName(),
            url: reviewerRef.getUrl(),
            0,
            reviewerRef.getReviewedNFTAmount(),
            reviewerRef.getCustomizedNFTAmount(),
        )
    }
    return nil
}

```