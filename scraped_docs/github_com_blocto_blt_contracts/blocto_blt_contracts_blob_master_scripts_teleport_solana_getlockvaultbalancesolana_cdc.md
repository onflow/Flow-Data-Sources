# Source: https://github.com/blocto/blt-contracts/blob/master/scripts/teleport/Solana/getLockVaultBalanceSolana.cdc

```
import "TeleportCustodySolana"

pub fun main(): UFix64 {
    return TeleportCustodySolana.getLockVaultBalance()
}

```