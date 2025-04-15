# Source: https://github.com/Outblock/FRW-scripts/blob/main/scripts/src/cadence/basic/is_locked_flow_enable.cdc

```
import LockedTokens from 0xLockedTokens

access(all) fun main(address: Address): Bool {
    let account = getAccount(address)
    return account.capabilities.exists(LockedTokens.LockedAccountInfoPublicPath)
}
```