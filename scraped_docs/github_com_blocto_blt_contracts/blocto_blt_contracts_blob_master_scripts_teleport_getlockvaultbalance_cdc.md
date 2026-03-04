# Source: https://github.com/blocto/blt-contracts/blob/master/scripts/teleport/getLockVaultBalance.cdc

```
import TeleportCustody from "../../contracts/flow/teleport/TeleportCustody.cdc"

pub fun main(): UFix64 {
    return TeleportCustody.getLockVaultBalance()
}

```