# Source: https://github.com/fixes-world/token-list/blob/main/cadence/transactions/nftlist/reviewer-publish-maintainer.cdc

```
import "NFTList"

transaction(
    target: Address
) {
    prepare(acct: auth(Storage, Capabilities, Inbox) &Account) {
        /// ---------- Reviewer Initialization: Start ----------
        if !acct.storage.check<@NFTList.NFTListReviewer>(from: NFTList.reviewerStoragePath) {
            log("Creating a new reviewer")
            let reviewer <- NFTList.createNFTListReviewer()
            acct.storage.save(<- reviewer, to: NFTList.reviewerStoragePath)

            // public the public capability
            let cap = acct.capabilities.storage.issue<&NFTList.NFTListReviewer>(NFTList.reviewerStoragePath)
            acct.capabilities.publish(cap, at: NFTList.reviewerPublicPath)
        } else {
            log("Reviewer already exists")
        }
        /// ---------- Reviewer Initialization: End ----------

        assert(
            acct.storage.check<&NFTList.NFTListReviewer>(from: NFTList.reviewerStoragePath),
            message: "Missing the reviewer capability"
        )

        let maintainerId = NFTList.generateReviewMaintainerCapabilityId(target)
        // issue private cap
        let cap = acct.capabilities.storage
            .issue<auth(NFTList.Maintainer) &NFTList.NFTListReviewer>(NFTList.reviewerStoragePath)
        assert(cap.check(), message: "Failed to link the capability")

        acct.inbox.publish(cap, name: maintainerId, recipient: target)
    }
}

```