# Source: https://github.com/Flowtyio/flowty-wrapped/blob/main/scripts/raffle/borrow_raffle_manager.cdc

```
import "FlowtyRaffles"

access(all) fun main(addr: Address) {
    getAccount(addr).capabilities.get<&FlowtyRaffles.Manager>(FlowtyRaffles.ManagerPublicPath).borrow()
        ?? panic("unable to borrow manager")
}
```