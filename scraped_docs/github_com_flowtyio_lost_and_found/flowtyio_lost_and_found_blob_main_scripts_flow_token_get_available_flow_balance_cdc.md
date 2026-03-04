# Source: https://github.com/Flowtyio/lost-and-found/blob/main/scripts/flow-token/get_available_flow_balance.cdc

```
import FlowStorageFees from "../../contracts/FlowStorageFees.cdc"

pub fun main(addr: Address): UFix64 {
    return FlowStorageFees.defaultTokenAvailableBalance(addr)
}

```