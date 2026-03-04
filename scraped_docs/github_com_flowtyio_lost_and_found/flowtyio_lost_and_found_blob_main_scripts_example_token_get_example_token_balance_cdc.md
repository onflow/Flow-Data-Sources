# Source: https://github.com/Flowtyio/lost-and-found/blob/main/scripts/example-token/get_example_token_balance.cdc

```
import "FungibleToken"
import "ExampleToken"

pub fun main(addr: Address): UFix64 {
    let acct = getAccount(addr)
    return acct.getCapability<&{FungibleToken.Balance}>(/public/exampleTokenBalance).borrow()!.balance
}
```