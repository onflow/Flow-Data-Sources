# Source: https://github.com/Outblock/FRW-scripts/blob/main/cadence/storage/query/get_public_item.cdc

```
// A workaround method
import FungibleToken from 0xFungibleToken
import NonFungibleToken from 0xNonFungibleToken
  
access(all) struct Item {
  access(all) let address: Address
  access(all) let path: String
  access(all) let type: Type

  access(all) let targetPath: String?

  init(
    address: Address, 
    path: String, 
    type: Type, 
    targetPath: String?
  ) {
    self.address = address
    self.path = path
    self.type = type
    self.targetPath = targetPath
  }
}

access(all) fun main(address: Address, pathMap: {String: Bool}): [Item] {
  let account = getAuthAccount(address)

  let items: [Item] = []
  account.forEachPublic(fun (path: PublicPath, type: Type): Bool {
    if !pathMap.containsKey(path.toString()) {
      return true
    }

    var targetPath: String? = nil

    if let target = account.getLinkTarget(path) {
      targetPath = target.toString()
    }

    let item = Item(
      address: address,
      path: path.toString(),
      type: type,
      targetPath: targetPath
    )

    items.append(item)
    return false
  })

  return items
}
```