# Source: https://github.com/fixes-world/token-list/blob/main/cadence/transactions/maintainer-update-reviewer-metadata.cdc

```
import "TokenList"

transaction(
    name: String?,
    url: String?,
) {
    let maintainer: auth(TokenList.Maintainer) &{TokenList.FungibleTokenReviewMaintainer}

    prepare(acct: auth(Storage) &Account) {
        var maintainer: auth(TokenList.Maintainer) &{TokenList.FungibleTokenReviewMaintainer}? = nil
        // Try borrow maintainer
        if acct.storage.check<@{TokenList.FungibleTokenReviewMaintainer}>(from: TokenList.maintainerStoragePath) {
            maintainer = acct.storage.borrow<auth(TokenList.Maintainer) &{TokenList.FungibleTokenReviewMaintainer}>(from: TokenList.maintainerStoragePath)
                ?? panic("Failed to load FungibleTokenReviewMaintainer from review maintainer")
        }
        // Try borrow review
        if acct.storage.check<@TokenList.FungibleTokenReviewer>(from: TokenList.reviewerStoragePath) {
            maintainer = acct.storage.borrow<auth(TokenList.Maintainer) &{TokenList.FungibleTokenReviewMaintainer}>(from: TokenList.reviewerStoragePath)
                    ?? panic("Failed to load FungibleTokenReviewMaintainer from reviewer")
        }
        self.maintainer = maintainer ?? panic("Missing maintainer")
    }

    execute {
        self.maintainer.updateMetadata(name: name, url: url)
    }
}

```