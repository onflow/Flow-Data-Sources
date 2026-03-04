# Source: https://github.com/Flowtyio/lost-and-found/blob/main/transactions/example-nft/destroy_example_nft_storage.cdc

```
import "FlowToken"
import "FungibleToken"
import "ExampleNFT"

transaction {
    prepare(signer: auth(Storage, Capabilities) &Account) {
        let r <- signer.storage.load<@AnyResource>(from: ExampleNFT.CollectionStoragePath)
        destroy r
        signer.capabilities.unpublish(ExampleNFT.CollectionPublicPath)
    }
}
```