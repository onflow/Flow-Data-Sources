# Source: https://github.com/fixes-world/token-list/blob/main/cadence/transactions/reviewer-publish-maintainer.cdc

```
import "MetadataViews"
import "TokenList"

transaction(
    target: Address
) {
    prepare(acct: auth(Storage, Capabilities, Inbox) &Account) {
        /// ---------- Reviewer Initialization: Start ----------
        if !acct.storage.check<@TokenList.FungibleTokenReviewer>(from: TokenList.reviewerStoragePath) {
            log("Creating a new reviewer")
            let reviewer <- TokenList.createFungibleTokenReviewer()
            acct.storage.save(<- reviewer, to: TokenList.reviewerStoragePath)

            // public the public capability
            let cap = acct.capabilities.storage.issue<&TokenList.FungibleTokenReviewer>(TokenList.reviewerStoragePath)
            acct.capabilities.publish(cap, at: TokenList.reviewerPublicPath)
        } else {
            log("Reviewer already exists")
        }
        /// ---------- Reviewer Initialization: End ----------

        assert(
            acct.storage.check<@TokenList.FungibleTokenReviewer>(from: TokenList.reviewerStoragePath),
            message: "Missing the reviewer capability"
        )

        let maintainerId = TokenList.generateReviewMaintainerCapabilityId(target)
        // issue private cap
        let cap = acct.capabilities.storage
            .issue<auth(TokenList.Maintainer) &TokenList.FungibleTokenReviewer>(TokenList.reviewerStoragePath)
        assert(cap.check(), message: "Failed to link the capability")

        acct.inbox.publish(cap, name: maintainerId, recipient: target)
    }
}

```