# Source: https://github.com/dapperlabs/studio-platform-smart-contracts/blob/main/epl-nft/scripts/wallet_inventory.cdc

```
import NonFungibleToken from "./NonFungibleToken.cdc"
import EnglishPremierLeague from "./EnglishPremierLeague.cdc"

pub fun main(acctAddress: Address): [UInt64] {
  let nftOwner = getAccount(acctAddress)
  let capability = nftOwner.getCapability<&{NonFungibleToken.CollectionPublic}>(EnglishPremierLeague.CollectionPublicPath)
  let borrowed = capability.borrow() ?? panic("Could not borrow receiver reference")
  return borrowed.getIDs()
}
```