# Source: https://github.com/blocto/blt-contracts/blob/master/scripts/teleport/getTeleportLengths.cdc

```
import TeleportCustody from "../../contracts/flow/teleport/TeleportCustody.cdc"

pub fun main(): [Int] {
    return [TeleportCustody.teleportAddressLength, TeleportCustody.teleportTxHashLength]
}

```