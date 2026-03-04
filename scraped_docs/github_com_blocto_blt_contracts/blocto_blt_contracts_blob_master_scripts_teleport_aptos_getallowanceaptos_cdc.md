# Source: https://github.com/blocto/blt-contracts/blob/master/scripts/teleport/Aptos/getAllowanceAptos.cdc

```
import "TeleportCustodyAptos"

access(all)
fun main(teleportAdmin: Address): UFix64 {
    let teleportUserRef = getAccount(teleportAdmin).capabilities.borrow<&{TeleportCustodyAptos.TeleportUser}>(TeleportCustodyAptos.TeleportAdminTeleportUserPath)
        ?? panic("Could not borrow a reference to TeleportUser")
    return teleportUserRef.allowedAmount
}
```