# Source: https://github.com/Outblock/FRW-scripts/blob/main/cadence/basic/query/query_flow_balance.cdc

```
import FungibleToken from 0xFungibleToken
import FlowToken from 0xFlowToken

access(all) fun checkFlowTokenBalance(address: Address) : UFix64 {
  let account = getAccount(address)
  let vaultRef = account.capabilities.borrow<&{FungibleToken.Balance}>(/public/flowTokenBalance)
    ?? nil
  
  if vaultRef != nil {
    return vaultRef!.balance
  }
  
  return 0.0
}

access(all) fun main(addrs: [Address]): [UFix64] {
  let bals: [UFix64] = []

  for addr in addrs {
    let bal = checkFlowTokenBalance(address: addr)
    bals.append(bal)
  }
  
  return bals
}
```