# Source: https://github.com/blocto/blt-contracts/blob/master/scripts/teleport/Aptos/getLockVaultBalanceAptos.cdc

```
import TeleportCustodyAptos from "../../contracts/flow/teleport/TeleportCustodyAptos.cdc"

pub fun main(): UFix64 {
    return TeleportCustodyAptos.getLockVaultBalance()
}

```