# Source: https://github.com/Flowtyio/capability-cache/blob/main/transactions/setup.cdc

```
import "CapabilityCache"

transaction(namespace: String) {
    prepare(acct: auth(Storage) &Account) {
        let s = CapabilityCache.getPathForCache(namespace)
        if acct.storage.borrow<&CapabilityCache.Cache>(from: s) == nil {
            let c <- CapabilityCache.createCache(namespace: namespace)
            acct.storage.save(<-c, to: s)
        }
    }
}
```