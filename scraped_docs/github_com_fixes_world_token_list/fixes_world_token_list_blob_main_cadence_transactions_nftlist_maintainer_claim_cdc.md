# Source: https://github.com/fixes-world/token-list/blob/main/cadence/transactions/nftlist/maintainer-claim.cdc

```
import "NFTList"

transaction(
    reviewer: Address
) {
    prepare(acct: auth(Storage, Inbox) &Account) {
        let registry = NFTList.borrowRegistry()
        let registryAddr = registry.owner?.address ?? panic("Failed to get registry address")

        if acct.storage.check<@NFTList.ReviewMaintainer>(from: NFTList.maintainerStoragePath) {
            // remove old Maintainer
            let old <- acct.storage.load<@NFTList.ReviewMaintainer>(from: NFTList.maintainerStoragePath)
            destroy old
        }

        let maintainerId = NFTList.generateReviewMaintainerCapabilityId(acct.address)
        let reviewerCap = acct.inbox
            .claim<auth(NFTList.Maintainer) &NFTList.NFTListReviewer>(
                maintainerId,
                provider: reviewer
            ) ?? panic("Failed to claim reviewer capability")
        assert(
            reviewerCap.check() == true,
            message: "Failed to check reviewer capability"
        )

        let maintainer <- NFTList.createNFTListReviewMaintainer(reviewerCap)
        acct.storage.save(<- maintainer, to: NFTList.maintainerStoragePath)
    }
}

```