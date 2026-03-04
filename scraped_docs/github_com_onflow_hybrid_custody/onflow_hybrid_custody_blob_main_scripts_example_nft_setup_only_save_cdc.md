# Source: https://github.com/onflow/hybrid-custody/blob/main/scripts/example-nft/setup_only_save.cdc

```
import "NonFungibleToken"
import "MetadataViews"

import "ExampleNFT"

transaction {
    prepare(acct: auth(BorrowValue, SaveValue) &Account) {
        if acct.storage.borrow<&ExampleNFT.Collection>(from: ExampleNFT.CollectionStoragePath) == nil {
            acct.storage.save(<- ExampleNFT.createEmptyCollection(nftType: Type<@ExampleNFT.NFT>()), to: ExampleNFT.CollectionStoragePath)
        }
    }
}

```