# Source: https://github.com/fixes-world/token-list/blob/main/cadence/transactions/maintainer-reivew-ft.cdc

```
import "FungibleToken"
import "FTViewUtils"
import "TokenList"

transaction(
    ftAddress: Address,
    ftContractName: String,
    rank: UInt8?,
    tags: [String],
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
        let tokenType = FTViewUtils.buildFTVaultType(ftAddress, ftContractName)
            ?? panic("Failed to build ft type")

        // update rank
        if rank != nil {
            if let evalRank = FTViewUtils.Evaluation(rawValue: rank!) {
                self.maintainer.reviewFTEvalute(tokenType, rank: evalRank)
            }
        }
        // add tags
        if tags.length > 0 {
            self.maintainer.reviewFTAddTags(tokenType, tags: tags)
        }
    }
}

```