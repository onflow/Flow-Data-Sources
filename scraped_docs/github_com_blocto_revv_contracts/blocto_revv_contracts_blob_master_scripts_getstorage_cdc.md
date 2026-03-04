# Source: https://github.com/blocto/revv-contracts/blob/master/scripts/getStorage.cdc

```
import "TeleportCustody"
import "REVV"
import "FungibleToken"

access(all)
fun main(teleportAdmin: Address, user: Address): [UFix64] {
    let teleportUserRef = getAccount(teleportAdmin).capabilities.borrow<&{TeleportCustody.TeleportUser}>(TeleportCustody.TeleportUserPublicPath)
        ?? panic("Could not borrow a reference to TeleportUser")

    let userRef = getAccount(user).capabilities.borrow<&{FungibleToken.Balance}>(REVV.RevvBalancePublicPath)
        ?? panic("Could not borrow a reference to the vault resource")

    return [teleportUserRef.allowedAmount, userRef.balance]
}
```