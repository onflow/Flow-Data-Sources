# Source: https://github.com/blocto/blt-contracts/blob/master/scripts/token/TeleportedTetherToken/getIsFrozen.cdc

```
import "TeleportedTetherToken"

access(all) fun main(): Bool {
  return TeleportedTetherToken.isFrozen
}

```