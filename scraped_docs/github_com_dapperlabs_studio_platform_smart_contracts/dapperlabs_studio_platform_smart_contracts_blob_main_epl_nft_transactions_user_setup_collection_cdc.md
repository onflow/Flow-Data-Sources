# Source: https://github.com/dapperlabs/studio-platform-smart-contracts/blob/main/epl-nft/transactions/user/setup_collection.cdc

```
import NonFungibleToken from "./NonFungibleToken.cdc"
import EnglishPremierLeague from "./EnglishPremierLeague.cdc"

transaction {
    prepare(signer: AuthAccount) {
        if signer.borrow<&EnglishPremierLeague.Collection>(from: EnglishPremierLeague.CollectionStoragePath) == nil {

            let collection <- EnglishPremierLeague.createEmptyCollection()
            signer.save(<-collection, to: EnglishPremierLeague.CollectionStoragePath)
            signer.link<&EnglishPremierLeague.Collection{NonFungibleToken.CollectionPublic, EnglishPremierLeague.MomentNFTCollectionPublic}>(
                EnglishPremierLeague.CollectionPublicPath,
                target: EnglishPremierLeague.CollectionStoragePath
            )
        }
    }
}
```