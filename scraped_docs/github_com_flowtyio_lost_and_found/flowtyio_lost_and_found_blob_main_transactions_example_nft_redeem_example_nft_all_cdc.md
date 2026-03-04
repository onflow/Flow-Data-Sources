# Source: https://github.com/Flowtyio/lost-and-found/blob/main/transactions/example-nft/redeem_example_nft_all.cdc

```
import "ExampleNFT"
import "NonFungibleToken"

import "LostAndFound"

transaction {
    prepare(acct: auth(Storage, Capabilities) &Account) {
        let cap = acct.capabilities.storage.issue<&ExampleNFT.Collection>(ExampleNFT.CollectionStoragePath)
        LostAndFound.redeemAll(type: Type<@ExampleNFT.NFT>(), max: nil, receiver: cap)

        acct.capabilities.storage.getController(byCapabilityID: cap.id)!.delete()
    }
}

```