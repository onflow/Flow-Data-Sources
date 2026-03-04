# Source: https://github.com/emerald-dao/project-toucans-v2/blob/master/frontend/src/flow/cadence/scripts/get_flow_balance.cdc

```
import FlowToken from "../utility/FlowToken.cdc"
import FungibleToken from "../utility/FungibleToken.cdc"

access(all) fun main(user: Address): UFix64 {
  let vault = getAccount(user).capabilities.borrow<&FlowToken.Vault>(/public/flowTokenBalance)
  return vault?.balance ?? 0.0
}
```