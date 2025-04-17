# Source: https://github.com/Outblock/FRW-scripts/blob/main/cadence/storage/query/get_private_items.cdc

```
access(all)struct Item {
  access(all)let address: Address
  access(all)let path: String
  access(all)let type: Type
  access(all)let targetPath: String?

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

access(all)fun main(address: Address, pathMap: {String: Bool}): [Item] {
  let account = getAccount(address)

  let items: [Item] = []

  account.storage.forEachPrivate(fun (path: PrivatePath, type: Type): Bool {
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
    return true
  })

  return items
}
```