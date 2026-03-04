# Source: https://github.com/fixes-world/token-list/blob/main/cadence/transactions/bin/set-nft-reviewer-verified.cdc

```
import "NFTList"

transaction(
    reviewer: Address,
    verified: Bool,
) {
    prepare(acct: auth(Storage) &Account) {
        let registry = acct.storage
            .borrow<auth(NFTList.SuperAdmin) &NFTList.Registry>(from: NFTList.registryStoragePath)
            ?? panic("Missing or mis-typed TokenList")
        registry.updateReviewerVerified(reviewer, verified)
    }
}

```