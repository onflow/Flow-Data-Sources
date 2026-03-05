# Source: https://github.com/Flowtyio/flowty-wrapped/blob/main/scripts/get_medias.cdc

```
import "FlowtyWrapped"
import "MetadataViews"
import "NonFungibleToken"

access(all) fun main(addr: Address, nftID: UInt64): MetadataViews.Medias {
    let acct = getAuthAccount<auth(Storage) &Account> (addr)
    let col = acct.storage.borrow<&FlowtyWrapped.Collection>(from: FlowtyWrapped.CollectionStoragePath)
        ?? panic("collection not found")
    let nft = col.borrowFlowtyWrapped(nftID) ?? panic("nft not found")
    return nft.resolveView(Type<MetadataViews.Medias>())! as! MetadataViews.Medias
}
```