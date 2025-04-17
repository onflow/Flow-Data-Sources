# Source: https://github.com/Outblock/FRW-scripts/blob/main/cadence/basic/query/get_account_total_locked_flow_balance.cdc

```
import FungibleToken from 0xFungibleToken
import FlowToken from 0xFlowToken
import LockedTokens from 0xLockedTokens

access(all) fun main(address: Address): UFix64 {
  let account = getAccount(address)

  let lockedAccountInfoCap = account
    .capabilities.get
    <&LockedTokens.TokenHolder>
    (LockedTokens.LockedAccountInfoPublicPath)
  if lockedAccountInfoCap == nil || !(lockedAccountInfoCap!.check()) {
    return UFix64(0)
  }
  
  let lockedAccountInfoRef = lockedAccountInfoCap!.borrow()!
  let lockedBalance = lockedAccountInfoRef.getLockedAccountBalance()
  
  return lockedBalance
}
```