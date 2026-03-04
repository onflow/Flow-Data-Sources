# Source: https://github.com/fixes-world/token-list/blob/main/cadence/transactions/reviewer-init.cdc

```
import "TokenList"

transaction() {
    prepare(acct: auth(Storage, Capabilities) &Account) {
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
            acct.storage.borrow<&TokenList.FungibleTokenReviewer>(
                from: TokenList.reviewerStoragePath
            ) != nil,
            message: "Missing the reviewer capability"
        )
    }
}

```