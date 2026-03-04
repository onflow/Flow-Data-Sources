# Source: https://github.com/Flowtyio/capability-cache/blob/main/transactions/remove_cached_capability.cdc

```
import "CapabilityCache"

transaction(namespace: String, resourceType: Type, capabilityType: Type) {
    prepare(acct: auth(BorrowValue) &Account) {
        let s = CapabilityCache.getPathForCache(namespace)
        let cache = acct.storage.borrow<auth(CapabilityCache.Delete) &CapabilityCache.Cache>(from: s)
            ?? panic("cache not found in storage")

        cache.removeCapabilityByType(resourceType: resourceType, capabilityType: capabilityType)
    }
}
```