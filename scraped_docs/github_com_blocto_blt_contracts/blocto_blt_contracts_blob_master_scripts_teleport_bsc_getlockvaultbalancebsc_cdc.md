# Source: https://github.com/blocto/blt-contracts/blob/master/scripts/teleport/BSC/getLockVaultBalanceBSC.cdc

```
import TeleportCustodyBSC from "../../contracts/flow/teleport/TeleportCustodyBSC.cdc"

pub fun main(): UFix64 {
    return TeleportCustodyBSC.getLockVaultBalance()
}

```