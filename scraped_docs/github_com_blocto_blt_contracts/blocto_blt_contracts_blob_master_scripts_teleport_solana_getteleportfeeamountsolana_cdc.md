# Source: https://github.com/blocto/blt-contracts/blob/master/scripts/teleport/Solana/getTeleportFeeAmountSolana.cdc

```
import "TeleportCustodySolana"

access(all)
fun main(teleportAdmin: Address): UFix64 {
    let teleportUserRef = getAccount(teleportAdmin).storage.borrow<&TeleportCustodySolana.TeleportAdmin>(TeleportCustodySolana.TeleportAdminTeleportUserPath)
        ?? panic("Could not borrow a reference to TeleportUser")
    return teleportUserRef.feeCollector.balance
}
```