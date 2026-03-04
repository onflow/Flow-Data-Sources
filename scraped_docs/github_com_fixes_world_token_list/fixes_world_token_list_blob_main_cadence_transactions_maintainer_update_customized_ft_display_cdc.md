# Source: https://github.com/fixes-world/token-list/blob/main/cadence/transactions/maintainer-update-customized-ft-display.cdc

```
import "FungibleToken"
import "FTViewUtils"
import "TokenList"

transaction(
    ftAddress: Address,
    ftContractName: String,
    name: String?,
    symbol: String?,
    description: String?,
    externalURL: String?,
    logo: String?,
    socials: {String: String},
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
        var ftDisplayRef = self.maintainer.borrowFTDisplayEditor(tokenType)
        if ftDisplayRef == nil {
            self.maintainer.registerFungibleTokenDisplayPatch(ftAddress, ftContractName)
            ftDisplayRef = self.maintainer.borrowFTDisplayEditor(tokenType)
        }
        assert(
            ftDisplayRef != nil,
            message: "Failed to borrow FT Display Editor"
        )
        // update FT Display
        ftDisplayRef!.setFTDisplay(
            name: name,
            symbol: symbol,
            description: description,
            externalURL: externalURL,
            logo: logo,
            socials: socials
        )
    }
}

```