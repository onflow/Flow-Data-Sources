# Source: https://github.com/Flowtyio/capability-cache/blob/main/transactions/add_type_to_cache.cdc

```
import "CapabilityCache"

transaction(namespace: String, resourceType: Type, capIssueType: Type, path: StoragePath) {
    prepare(acct: auth(SaveValue, BorrowValue, IssueStorageCapabilityController) &Account) {
        let s = CapabilityCache.getPathForCache(namespace)
        if acct.storage.borrow<&CapabilityCache.Cache>(from: s) == nil {
            let c <- CapabilityCache.createCache(namespace: namespace)
            acct.storage.save(<-c, to: s)
        }

        let cache = acct.storage.borrow<auth(CapabilityCache.Add) &CapabilityCache.Cache>(from: s)
            ?? panic("capability cache was not found")

        let cap = acct.capabilities.storage.issueWithType(path, type: capIssueType)
        cache.addCapability(resourceType: resourceType, cap: cap)
    }
}
```