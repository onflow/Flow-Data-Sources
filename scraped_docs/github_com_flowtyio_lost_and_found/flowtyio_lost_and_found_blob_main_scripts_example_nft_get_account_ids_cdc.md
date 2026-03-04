# Source: https://github.com/Flowtyio/lost-and-found/blob/main/scripts/example-nft/get_account_ids.cdc

```
import "ExampleNFT"
import "NonFungibleToken"

pub fun main(addr: Address): [UInt64] {
    let account = getAccount(addr)
    let cap = account.getCapability<&{NonFungibleToken.CollectionPublic}>(ExampleNFT.CollectionPublicPath)
    return cap.borrow()!.getIDs()
}
```