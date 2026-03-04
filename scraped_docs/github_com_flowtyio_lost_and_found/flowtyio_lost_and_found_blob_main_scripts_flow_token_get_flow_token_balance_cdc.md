# Source: https://github.com/Flowtyio/lost-and-found/blob/main/scripts/flow-token/get_flow_token_balance.cdc

```
import "FungibleToken"

pub fun main(addr: Address): UFix64 {
    let cap = getAccount(addr).getCapability<&{FungibleToken.Balance}>(/public/flowTokenBalance)
    let balance = cap.borrow()!.balance

    return balance
}
```