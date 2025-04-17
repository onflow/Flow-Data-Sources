# Source: https://github.com/Outblock/FRW-scripts/blob/main/cadence/basic/query/get_storage_info.cdc

```
 access(all) fun main(addr: Address): {String: UInt64} {
  let acct = getAccount(addr)
  let ret: {String: UInt64} = {}
  ret["capacity"] = acct.storage.capacity
  ret["used"] = acct.storage.used
  if acct.storage.capacity > 0 {
      ret["available"] = acct.storage.capacity -  acct.storage.used
  } else {
      ret["available"] = 0
  }

  return ret
}
```