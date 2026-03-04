# Source: https://github.com/blocto/blt-contracts/blob/master/scripts/token/TeleportedTetherToken/getTotalSupply.cdc

```
import "TeleportedTetherToken"

access(all) fun main(): UFix64 {
  return TeleportedTetherToken.totalSupply
}

```