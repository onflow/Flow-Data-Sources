# Source: https://github.com/Outblock/FRW-scripts/blob/main/cadence/storage/query/get_stored_struct.cdc

```
pub fun main(address: Address, pathStr: String): &AnyStruct? {
  let account = getAuthAccount(address)
  let path = StoragePath(identifier: pathStr)!
  return account.borrow<&AnyStruct>(from: path)
}
```