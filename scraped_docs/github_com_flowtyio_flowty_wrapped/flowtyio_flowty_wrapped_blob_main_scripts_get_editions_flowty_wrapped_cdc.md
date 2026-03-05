# Source: https://github.com/Flowtyio/flowty-wrapped/blob/main/scripts/get_editions_flowty_wrapped.cdc

```
import "NonFungibleToken"
import "MetadataViews"

import "FlowtyWrapped"

access(all) fun main(addr: Address, nftID: UInt64): AnyStruct {
    let cp = getAccount(addr).capabilities.get<&{NonFungibleToken.CollectionPublic}>(FlowtyWrapped.CollectionPublicPath).borrow()
        ?? panic("collection not found")

    let nft = cp.borrowNFT(nftID)!
    return nft.resolveView(Type<MetadataViews.Editions>())!
}
```