# Source: https://github.com/Outblock/FRW-scripts/blob/main/scripts/src/cadence/basic/is_token_storage_enabled.cdc

```
import FungibleToken from 0xFungibleToken
import <Token> from <TokenAddress>

access(all) fun main(address: Address) : Bool {
    let account = getAccount(address)
   
    let receiver = account.capabilities.exists(<TokenReceiverPath>)
    let balance = account.capabilities.exists(<TokenBalancePath>)

    return receiver && balance
}
```