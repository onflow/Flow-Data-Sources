# Source: https://github.com/emerald-dao/project-toucans-v2/blob/master/frontend/src/flow/cadence/scripts/has_flow_vault.cdc

```
import FlowToken from "../utility/FlowToken.cdc"

access(all) fun main(address: Address): Bool {
  let testVault = getAuthAccount<auth(Storage) &Account>(address).storage.borrow<&FlowToken.Vault>(from: /storage/flowTokenVault)
  return testVault != nil
}
```