# Source: https://github.com/Flowtyio/capability-cache/blob/main/scripts/check_for_cache.cdc

```
import "CapabilityCache"

access(all) fun main(addr: Address, namespace: String): Bool {
    let s = CapabilityCache.getPathForCache(namespace)

    let acct = getAuthAccount<auth(BorrowValue) &Account>(addr)
    return acct.storage.borrow<&CapabilityCache.Cache>(from: s) != nil
}
```