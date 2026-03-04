# Source: https://github.com/fixes-world/token-list/blob/main/cadence/transactions/nftlist/maintainer-update-customized-display.cdc

```
import "ViewResolver"
import "NonFungibleToken"
import "NFTViewUtils"
import "NFTList"

transaction(
    address: Address,
    contractName: String,
    name: String,
    description: String?,
    externalURL: String?,
    squareImage: String?,
    bannerImage: String?,
    socials: {String: String},
) {
    let maintainer: auth(NFTList.Maintainer) &{NFTList.NFTListReviewMaintainer}

    prepare(acct: auth(Storage) &Account) {
        var maintainer: auth(NFTList.Maintainer) &{NFTList.NFTListReviewMaintainer}? = nil
        // Try borrow maintainer
        if acct.storage.check<@{NFTList.NFTListReviewMaintainer}>(from: NFTList.maintainerStoragePath) {
            maintainer = acct.storage
                .borrow<auth(NFTList.Maintainer) &{NFTList.NFTListReviewMaintainer}>(from: NFTList.maintainerStoragePath)
                ?? panic("Failed to load NFTListReviewMaintainer from review maintainer")
        }
        // Try borrow review
        if acct.storage.check<@NFTList.NFTListReviewer>(from: NFTList.reviewerStoragePath) {
            maintainer = acct.storage.borrow<auth(NFTList.Maintainer) &{NFTList.NFTListReviewMaintainer}>(from: NFTList.reviewerStoragePath)
                    ?? panic("Failed to load NFTListReviewMaintainer from reviewer")
        }
        self.maintainer = maintainer ?? panic("Missing maintainer")
    }

    execute {
        var editorRef = self.maintainer.borrowNFTCollectionDisplayEditor(address, contractName)
        if editorRef == nil {
            self.maintainer.registerNFTCollectionDisplayPatch(address, contractName)
            editorRef = self.maintainer.borrowNFTCollectionDisplayEditor(address, contractName)
        }

        if editorRef == nil {
            panic("Failed to borrow NFTCollectionDisplayEditor")
        }

        editorRef!.setDisplay(
            name: name,
            description: description,
            externalURL: externalURL,
            squareImage: squareImage,
            bannerImage: bannerImage,
            socials: socials
        )
    }
}

```