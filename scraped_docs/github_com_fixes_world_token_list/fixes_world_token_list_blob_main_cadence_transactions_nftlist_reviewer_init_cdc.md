# Source: https://github.com/fixes-world/token-list/blob/main/cadence/transactions/nftlist/reviewer-init.cdc

```
import "NFTList"

transaction() {
    prepare(acct: auth(Storage, Capabilities) &Account) {
        /// ---------- Reviewer Initialization: Start ----------
        if !acct.storage.check<@NFTList.NFTListReviewer>(from: NFTList.reviewerStoragePath) {
            log("Creating a new reviewer")
            let reviewer <- NFTList.createNFTListReviewer()
            acct.storage.save(<- reviewer, to: NFTList.reviewerStoragePath)

            // public the public capability
            let cap = acct.capabilities
                .storage.issue<&NFTList.NFTListReviewer>(NFTList.reviewerStoragePath)
            acct.capabilities.publish(cap, at: NFTList.reviewerPublicPath)
        } else {
            log("Reviewer already exists")
        }
        /// ---------- Reviewer Initialization: End ----------

        assert(
            acct.storage.borrow<&NFTList.NFTListReviewer>(
                from: NFTList.reviewerStoragePath
            ) != nil,
            message: "Missing the reviewer capability"
        )
    }
}

```