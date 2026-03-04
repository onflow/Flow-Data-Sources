# Source: https://github.com/fixes-world/token-list/blob/main/cadence/transactions/maintainer-claim.cdc

```
import "TokenList"

transaction(
    reviewer: Address
) {
    prepare(acct: auth(Storage, Inbox) &Account) {
        let registry = TokenList.borrowRegistry()
        let registryAddr = registry.owner?.address ?? panic("Failed to get registry address")

        if acct.storage.check<@TokenList.ReviewMaintainer>(from: TokenList.maintainerStoragePath) {
            // remove old Maintainer
            let old <- acct.storage.load<@TokenList.ReviewMaintainer>(from: TokenList.maintainerStoragePath)
            destroy old
        }

        let maintainerId = TokenList.generateReviewMaintainerCapabilityId(acct.address)
        let reviewerCap = acct.inbox
            .claim<auth(TokenList.Maintainer) &TokenList.FungibleTokenReviewer>(
                maintainerId,
                provider: reviewer
            ) ?? panic("Failed to claim reviewer capability")
        assert(
            reviewerCap.check() == true,
            message: "Failed to check reviewer capability"
        )

        let maintainer <- TokenList.createFungibleTokenReviewMaintainer(reviewerCap)
        acct.storage.save(<- maintainer, to: TokenList.maintainerStoragePath)
    }
}

```