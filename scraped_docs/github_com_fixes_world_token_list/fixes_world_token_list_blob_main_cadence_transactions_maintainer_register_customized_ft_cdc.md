# Source: https://github.com/fixes-world/token-list/blob/main/cadence/transactions/maintainer-register-customized-ft.cdc

```
import "ViewResolver"
import "FungibleToken"
import "FTViewUtils"
import "TokenList"

transaction(
    ftAddress: Address,
    ftContractName: String,
    storageIdentifier: String,
    receiverIdentifier: String,
    metadataIdentifier: String,
    name: String,
    symbol: String,
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
        self.maintainer.registerFungibleTokenWithEditableFTView(
            ftAddress,
            ftContractName,
            at: StoragePath(identifier: storageIdentifier) ?? panic("Invalid Identifier.")
        )
        let ftviewRef = self.maintainer.borrowFTViewEditor(tokenType)
            ?? panic("Failed to get the ft view")
        // initialize vault data
        ftviewRef.initializeVaultData(
            receiverPath: PublicPath(identifier: receiverIdentifier) ?? panic("Invalid receiver path"),
            metadataPath: PublicPath(identifier: metadataIdentifier) ?? panic("Invalid metadata path"),
            receiverType: Type<&{FungibleToken.Receiver}>(),
            metadataType: Type<&{FungibleToken.Balance, ViewResolver.Resolver}>(),
        )
        // init FT Display
        ftviewRef.setFTDisplay(
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