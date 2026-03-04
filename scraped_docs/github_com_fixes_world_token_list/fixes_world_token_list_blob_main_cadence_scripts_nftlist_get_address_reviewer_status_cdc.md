# Source: https://github.com/fixes-world/token-list/blob/main/cadence/scripts/nftlist/get-address-reviewer-status.cdc

```
import "NFTList"
import "MetadataViews"

access(all)
fun main(
    _ addr: Address
): Status {
    let acct = getAuthAccount<auth(Capabilities, Storage, Inbox) &Account>(addr)
    let registry = NFTList.borrowRegistry()
    let registryAddr = registry.owner?.address ?? panic("Failed to get registry address")

    let isReviewer = NFTList.borrowReviewerPublic(addr) != nil

    let maintainerId = NFTList.generateReviewMaintainerCapabilityId(addr)
    let reviewers = registry.getReviewers()
    var reviewerAddr: Address? = nil
    var isPendingToClaimReviewMaintainer = false
    for one in reviewers {
        let cap = acct.inbox
            .claim<auth(NFTList.Maintainer) &NFTList.NFTListReviewer>(
                maintainerId,
                provider: one
            )
        if cap != nil {
            reviewerAddr = one
            isPendingToClaimReviewMaintainer = true
            break
        }
    }

    let isReviewMaintainer = acct.storage.check<@NFTList.ReviewMaintainer>(from: NFTList.maintainerStoragePath)
    if isReviewMaintainer {
        let maintainer = acct.storage
            .borrow<&NFTList.ReviewMaintainer>(from: NFTList.maintainerStoragePath)
        reviewerAddr = maintainer?.getReviewerAddress()
    }

    return Status(
        isReviewer,
        isReviewMaintainer,
        isPendingToClaimReviewMaintainer,
        isReviewer
            ? addr
            : reviewerAddr,
    )
}

access(all) struct Status {
    access(all)
    let isReviewer: Bool
    access(all)
    let isReviewMaintainer: Bool
    access(all)
    let isPendingToClaimReviewMaintainer: Bool
    access(all)
    let reviewerAddr: Address?

    init(
        _ isReviewer: Bool,
        _ isReviewMaintainer: Bool,
        _ isPendingToClaimReviewMaintainer: Bool,
        _ reviewerAddr: Address?,
    ) {
        self.isReviewer = isReviewer
        self.reviewerAddr = reviewerAddr
        self.isReviewMaintainer = isReviewMaintainer
        self.isPendingToClaimReviewMaintainer = isPendingToClaimReviewMaintainer
    }
}

```