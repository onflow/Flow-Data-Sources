# Source: https://github.com/blocto/blt-contracts/blob/master/scripts/teleport/Solana/getTeleportFeesSolana.cdc

```
import "TeleportCustodySolana"

access(all)
fun main(teleportAdmin: Address): [UFix64] {
    let teleportUserRef = getAccount(teleportAdmin).capabilities.borrow<&{TeleportCustodySolana.TeleportUser}>(TeleportCustodySolana.TeleportAdminTeleportUserPath)
        ?? panic("Could not borrow a reference to TeleportUser")
    return [teleportUserRef.lockFee, teleportUserRef.unlockFee]
}
```