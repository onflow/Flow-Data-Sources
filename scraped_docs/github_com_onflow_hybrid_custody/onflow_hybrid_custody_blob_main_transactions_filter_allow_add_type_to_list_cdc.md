# Source: https://github.com/onflow/hybrid-custody/blob/main/transactions/filter/allow/add_type_to_list.cdc

```
import "CapabilityFilter"

transaction(identifier: String) {
    prepare(acct: auth(Storage) &Account) {
        let filter = acct.storage.borrow<auth(CapabilityFilter.Add) &CapabilityFilter.AllowlistFilter>(from: CapabilityFilter.StoragePath)
            ?? panic("filter does not exist")

        let c = CompositeType(identifier)!
        filter.addType(c)
    }
}
```