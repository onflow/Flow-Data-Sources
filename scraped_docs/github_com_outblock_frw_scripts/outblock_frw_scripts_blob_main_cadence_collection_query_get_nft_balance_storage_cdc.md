# Source: https://github.com/Outblock/FRW-scripts/blob/main/cadence/collection/query/get_nft_balance_storage.cdc

```
import NonFungibleToken from 0xNonFungibleToken


access(all) fun main(_ address: Address): {String: Int} {
  let account = getAuthAccount<auth(BorrowValue) &Account>(address)
  let data: {String: Int} = {}
  let collectionType: Type = Type<@{NonFungibleToken.Collection}>()

  // Iterate over each public path
  account.storage.forEachStored(fun (path: StoragePath, type: Type): Bool {
    // Return early if the collection is broken or is not the type we're looking for
    if type.isRecovered || (!type.isInstance(collectionType) && !type.isSubtype(of: collectionType)) {
      return true
    }
    if let collectionRef = account.storage.borrow<&{NonFungibleToken.Collection}>(from: path) {
      // Return early if no Resolver found in the Collection
      let ids: [UInt64]= collectionRef.getIDs()
      data.insert(key: type.identifier, ids.length)
    }
    return true
  })
  return data
}
```