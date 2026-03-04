# Source: https://github.com/onflow/hybrid-custody/blob/main/transactions/filter/allow/remove_all_types.cdc

```
import "CapabilityFilter"

transaction() {
    prepare(acct: auth(Storage) &Account) {
        let filter = acct.storage.borrow<auth(CapabilityFilter.Delete) &CapabilityFilter.AllowlistFilter>(from: CapabilityFilter.StoragePath)
            ?? panic("filter does not exist")

        filter.removeAllTypes()
    }
}

```