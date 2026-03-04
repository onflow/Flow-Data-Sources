# Source: https://github.com/emerald-dao/project-toucans-v2/blob/master/frontend/src/flow/cadence/scripts/can_receive_project_token.cdc

```
import ExampleToken from "../ExampleToken.cdc"
import FungibleToken from "../utility/FungibleToken.cdc"

access(all) fun main(user: Address): Bool {
  // otherwise check the projects token
  let vault = getAccount(user).capabilities.borrow<&{FungibleToken.Receiver}>(ExampleToken.ReceiverPublicPath)

  return vault != nil
}
```