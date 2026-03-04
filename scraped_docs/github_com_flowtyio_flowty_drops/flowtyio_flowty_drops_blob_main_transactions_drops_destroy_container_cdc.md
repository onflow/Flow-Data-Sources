# Source: https://github.com/Flowtyio/flowty-drops/blob/main/transactions/drops/destroy_container.cdc

```
import "FlowtyDrops"

transaction {
    prepare(acct: auth(LoadValue) &Account) {
        destroy acct.storage.load<@AnyResource>(from: FlowtyDrops.ContainerStoragePath)
    }
}
```