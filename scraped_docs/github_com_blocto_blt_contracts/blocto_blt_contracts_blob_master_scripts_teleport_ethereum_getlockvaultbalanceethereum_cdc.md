# Source: https://github.com/blocto/blt-contracts/blob/master/scripts/teleport/Ethereum/getLockVaultBalanceEthereum.cdc

```
import TeleportCustodyEthereum from "../../contracts/flow/teleport/TeleportCustodyEthereum.cdc"

pub fun main(): UFix64 {
    return TeleportCustodyEthereum.getLockVaultBalance()
}

```