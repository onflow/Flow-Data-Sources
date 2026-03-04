# Source: https://github.com/emerald-dao/project-toucans-v2/blob/master/frontend/test.cdc

```
import NonFungibleToken from "./src/flow/cadence/utility/NonFungibleToken.cdc"
import AllDay from "./src/flow/cadence/utility/AllDay.cdc"

access(all) fun main(): Int {
  let type = Type<@AllDay.NFT>()
  let nftTreasury: @{Type: {NonFungibleToken.Collection}} <- {type: <- AllDay.createEmptyCollection(nftType: type)}
  let additions: @{String: {Type: {NonFungibleToken.Collection}}} <- {"nftTreasury": <- nftTreasury}
  
  let nftTreasuryRef: auth(NonFungibleToken.Withdraw) &{Type: {NonFungibleToken.Collection}} = (&additions["nftTreasury"])!
  let working: auth(NonFungibleToken.Withdraw) &{NonFungibleToken.Collection}? = nftTreasuryRef[Type<@AllDay.NFT>()]
  
  destroy additions
  return 1
}
```