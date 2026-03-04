# Source: https://github.com/onflow/hybrid-custody/blob/main/scripts/example-nft/get_ids.cdc

```
import "ExampleNFT"

access(all) fun main(addr: Address): [UInt64] {
    let acct = getAuthAccount<auth(Storage) &Account>(addr)
    let collection = acct.storage.borrow<&ExampleNFT.Collection>(from: ExampleNFT.CollectionStoragePath)
        ?? panic("collection not found")
    return collection.getIDs()
}
```