# Source: https://github.com/blocto/revv-contracts/blob/master/scripts/getTeleportFees.cdc

```
import "TeleportCustody"

access(all)
fun main(teleportAdmin: Address): [UFix64] {
    let teleportUserRef = getAccount(teleportAdmin).capabilities.borrow<&{TeleportCustody.TeleportUser}>(TeleportCustody.TeleportUserPublicPath)
        ?? panic("Could not borrow a reference to TeleportUser")
    return [teleportUserRef.outwardFee, teleportUserRef.inwardFee]
}
```