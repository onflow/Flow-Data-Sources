# Source: https://github.com/Flowtyio/flowty-wrapped/blob/main/transactions/setup_flowty_wrapped.cdc

```
import "NonFungibleToken"
import "FlowtyWrapped"
import "MetadataViews"

transaction {
    prepare(signer: auth(Storage, Capabilities) &Account) {
        // Return early if the account already stores a FlowtyWrapped Collection
        if signer.storage.borrow<&FlowtyWrapped.Collection>(from: FlowtyWrapped.CollectionStoragePath) == nil {
            // Create a new FlowtyWrapped Collection and put it in storage
            signer.storage.save(
                <-FlowtyWrapped.createEmptyCollection(nftType: Type<@FlowtyWrapped.NFT>()),
                to: FlowtyWrapped.CollectionStoragePath
            )

            // Create a public capability to the Collection that only exposes
            // the balance field through the Balance interface
            signer.capabilities.publish(
                signer.capabilities.storage.issue<&FlowtyWrapped.Collection>(FlowtyWrapped.CollectionStoragePath),
                at: FlowtyWrapped.CollectionPublicPath
            )
        }
    }
}
```