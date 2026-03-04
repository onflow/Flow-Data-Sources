# Source: https://github.com/emerald-dao/float/blob/main/src/flow/cadence/scripts/validate_address_existance.cdc

```
import "FungibleToken"

access(all) fun main(address: Address): Bool {
  return getAccount(address).capabilities.borrow<&{FungibleToken.Balance}>(/public/flowTokenBalance) != nil
}
```