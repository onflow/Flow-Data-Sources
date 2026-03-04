# Source: https://github.com/Flowtyio/capability-cache/blob/main/scripts/get_cached_capability_type.cdc

```
import "CapabilityCache"

access(all) fun main(addr: Address, namespace: String, resourceType: Type, capabilityType: Type): Type? {
    let s = CapabilityCache.getPathForCache(namespace)
    let acct = getAuthAccount<auth(BorrowValue) &Account>(addr)
    let cache = acct.storage.borrow<auth(CapabilityCache.Get) &CapabilityCache.Cache>(from: s)
        ?? panic("cache not found in storage")
    if let cap = cache.getCapabilityByType(resourceType: resourceType, capabilityType: capabilityType) {
        return cap.getType()
    }
    return nil
}
```