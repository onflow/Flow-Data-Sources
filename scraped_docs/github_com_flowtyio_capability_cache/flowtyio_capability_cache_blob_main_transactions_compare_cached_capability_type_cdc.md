# Source: https://github.com/Flowtyio/capability-cache/blob/main/transactions/compare_cached_capability_type.cdc

```
import "CapabilityCache"
import "FungibleToken"

transaction(namespace: String, resourceType: Type, capabilityType: Type) {
    prepare(acct: auth(BorrowValue) &Account) {
        let s = CapabilityCache.getPathForCache(namespace)
        let cache = acct.storage.borrow<auth(CapabilityCache.Get) &CapabilityCache.Cache>(from: s)
            ?? panic("cache not found in storage")
        let cap = cache.getCapabilityByType(resourceType: resourceType, capabilityType: capabilityType)
            ?? panic("capability not found with provided type")
        assert(cap.getType() == capabilityType, message: "capability type is not exepected value")
    }
}
```