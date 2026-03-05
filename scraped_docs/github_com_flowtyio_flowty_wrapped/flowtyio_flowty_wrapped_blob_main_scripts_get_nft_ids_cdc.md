# Source: https://github.com/Flowtyio/flowty-wrapped/blob/main/scripts/get_nft_ids.cdc

```
import "NonFungibleToken"

import "FlowtyWrapped"

access(all) fun main(addr: Address): [UInt64] {
    let cp = getAccount(addr).capabilities.get<&{NonFungibleToken.CollectionPublic}>(FlowtyWrapped.CollectionPublicPath).borrow()
        ?? panic("collection not found")

    let nftIDs = cp.getIDs()
    return  nftIDs
}
```