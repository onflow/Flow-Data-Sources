# Source: https://github.com/Flowtyio/flowty-drops/blob/main/transactions/drops/remove_all_drops.cdc

```
import "FlowtyDrops"

transaction {
    prepare(acct: auth(BorrowValue) &Account) {
        if let container = acct.storage.borrow<auth(FlowtyDrops.Owner) &FlowtyDrops.Container>(from: FlowtyDrops.ContainerStoragePath) {
            for id in container.getIDs() {
                destroy container.removeDrop(id: id)
            }
        }
    }
}
```