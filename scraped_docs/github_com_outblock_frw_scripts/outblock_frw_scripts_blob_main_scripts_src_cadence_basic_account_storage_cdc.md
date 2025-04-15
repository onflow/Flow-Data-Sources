# Source: https://github.com/Outblock/FRW-scripts/blob/main/scripts/src/cadence/basic/account_storage.cdc

```
 access(all) struct StorageInfo {
    access(all)  let capacity: UInt64
    access(all)  let used: UInt64
    access(all)  let available: UInt64

    init(capacity: UInt64, used: UInt64, available: UInt64) {
        self.capacity = capacity
        self.used = used
        self.available = available
    }
}

access(all) fun main(addr: Address): StorageInfo {
    let acct = getAccount(addr)
    var available: UInt64 = 0
    if acct.storage.capacity > 0 {
        available = acct.storage.capacity - acct.storage.used
    }
    return StorageInfo(capacity: acct.storage.capacity,
            used: acct.storage.used,
            available: available)
}
```