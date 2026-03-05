# Source: https://github.com/Flowtyio/flowty-wrapped/blob/main/scripts/borrow_nft.cdc

```
import "NonFungibleToken"
import "MetadataViews"

import "FlowtyWrapped"

access(all) fun main(addr: Address, nftID: UInt64): Bool{
  let cp = getAccount(addr).capabilities.get<&{NonFungibleToken.CollectionPublic}>(FlowtyWrapped.CollectionPublicPath).borrow()
    ?? panic("collection not found")

  let nft = cp.borrowNFT(nftID) 
  return nft != nil
}
```