# Source: https://github.com/emerald-dao/project-toucans-v2/blob/master/frontend/src/flow/cadence/scripts/can_receive_toucans_token.cdc

```
import FungibleToken from "../utility/FungibleToken.cdc"
import ToucansTokens from "../ToucansTokens.cdc"

access(all) fun main(user: Address, tokenSymbol: String): Bool {

  // if the token symbol is for payments
  if let tokenInfo = ToucansTokens.getTokenInfoFromSymbol(symbol: tokenSymbol) {
    let vault = getAccount(user).capabilities.borrow<&{FungibleToken.Receiver}>(tokenInfo.receiverPath)

    return vault != nil
  }

  return false
}
```