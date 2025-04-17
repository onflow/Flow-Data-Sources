# Source: https://github.com/Outblock/FRW-scripts/blob/main/cadence/basic/query/get_account_total_flow_balance.cdc

```
import FungibleToken from 0xFungibleToken
import FlowToken from 0xFlowToken
import LockedTokens from 0xLockedTokens

access(all) fun main(address: Address): UFix64 {
  let account = getAccount(address)
  let unlockedVault = account
    .capabilities.get<&{FungibleToken.Balance}>(/public/flowTokenBalance)!
    .borrow()
      ?? panic("Could not borrow Balance reference to the Vault")
  let unlockedBalance = unlockedVault.balance
      
  let lockedAccountInfoCap = account
    .capabilities.get
    <&LockedTokens.TokenHolder>
    (LockedTokens.LockedAccountInfoPublicPath)
  if lockedAccountInfoCap == nil || !(lockedAccountInfoCap!.check()) {
    return unlockedBalance
  }
  
  let lockedAccountInfoRef = lockedAccountInfoCap!.borrow()!
  let lockedBalance = lockedAccountInfoRef.getLockedAccountBalance()
  
  return lockedBalance + unlockedBalance
}
```