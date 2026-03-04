# Source: https://github.com/Flowtyio/lost-and-found/blob/main/scripts/Depositor/get_balance.cdc

```
import "LostAndFound"

pub fun main(addr: Address): UFix64 {
    let depositorPublic = getAccount(addr).getCapability<&LostAndFound.Depositor{LostAndFound.DepositorPublic}>(LostAndFound.DepositorPublicPath).borrow()!
    return depositorPublic.balance()
}

```