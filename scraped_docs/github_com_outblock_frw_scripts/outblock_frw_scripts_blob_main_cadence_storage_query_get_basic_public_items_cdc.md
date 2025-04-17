# Source: https://github.com/Outblock/FRW-scripts/blob/main/cadence/storage/query/get_basic_public_items.cdc

```
access(all)struct Item {
  access(all)let address: Address
  access(all)let path: String
  access(all)let targetPath: String?

  init(address: Address, path: String, targetPath: String?) {
    self.address = address
    self.path = path
    self.targetPath = targetPath
  }
}

access(all)fun main(address: Address): [Item] {
  let account = getAccount(address)
  let items: [Item] = []


  fun eachPath(path: PublicPath, capType: Type): Bool {
    // todo
    let cap = account.capabilities.get<&AnyStruct>(path)
    var targetPath = ""

    if cap != nil {
      targetPath = "12" 
    }
    let item = Item(address: address, path: path.toString(), targetPath: targetPath)
    items.append(item)
    return true
  }
  account.storage.forEachPublic(eachPath)

  return items
}
```