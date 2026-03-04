# Source: https://github.com/fixes-world/token-list/blob/main/cadence/transactions/bin/remove-asset.cdc

```
import "FTViewUtils"
import "TokenList"
import "NFTViewUtils"
import "NFTList"

transaction(
    address: Address,
    contractName: String,
) {

    prepare(acct: auth(BorrowValue) &Account) {
        if TokenList.isFungibleTokenRegistered(address, contractName) {
            let ftRegistry = acct.storage.borrow<auth(TokenList.SuperAdmin) &TokenList.Registry>(from: TokenList.registryStoragePath)
                ?? panic("Missing or mis-typed TokenList")
            if let type = FTViewUtils.buildFTVaultType(address, contractName) {
                ftRegistry.removeFungibleToken(type)
            }
        } else if NFTList.isNFTCollectionRegistered(address, contractName) {
            let nftRegistry = acct.storage.borrow<auth(NFTList.SuperAdmin) &NFTList.Registry>(from: NFTList.registryStoragePath)
                ?? panic("Missing or mis-typed NFTList")
            if let type = NFTViewUtils.buildNFTType(address, contractName) {
                nftRegistry.removeNFTCollection(type)
            }
        }
    }
}

```