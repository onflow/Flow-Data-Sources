# Source: https://github.com/emerald-dao/project-toucans-v2/blob/master/frontend/src/flow/cadence/scripts/can_receive_nft_collection.cdc

```
import NFTCatalog from "../utility/NFTCatalog.cdc"
import NonFungibleToken from "../utility/NonFungibleToken.cdc"

access(all) fun main(user: Address, collectionIdentifier: String): Bool {

  // if the token symbol is for payments
  if let catalogEntry = NFTCatalog.getCatalogEntry(collectionIdentifier: collectionIdentifier) {
    let publicPath: PublicPath = catalogEntry.collectionData.publicPath
    if let collectionReceiver = getAccount(user).capabilities.borrow<&{NonFungibleToken.Receiver}>(publicPath) {
      return true
    }
    if let collectionPublic = getAccount(user).capabilities.borrow<&{NonFungibleToken.CollectionPublic}>(publicPath) {
      return true
    }
  }

  return false
}
```