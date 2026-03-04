# Source: https://github.com/Flowtyio/flow-raffle/blob/main/scripts/borrow_manager.cdc

```
import "FlowtyRaffles"

access(all) fun main(addr: Address) {
    getAccount(addr).capabilities.get<&{FlowtyRaffles.ManagerPublic}>(FlowtyRaffles.ManagerPublicPath).borrow()
        ?? panic("unable to borrow manager")
}
```