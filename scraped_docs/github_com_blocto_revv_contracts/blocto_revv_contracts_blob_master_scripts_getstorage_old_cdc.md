# Source: https://github.com/blocto/revv-contracts/blob/master/scripts/getStorage-old.cdc

```
import "TeleportCustody"
import "REVV"
import "FungibleToken"

pub fun main(teleportAdmin: Address, user: Address): [UFix64] {
    let teleportUserRef = getAccount(teleportAdmin).getCapability<&{TeleportCustody.TeleportUser}>(TeleportCustody.TeleportUserPublicPath).borrow()
        ?? panic("Could not borrow a reference to TeleportUser")

    let userRef = getAccount(user).getCapability<&{FungibleToken.Balance}>(REVV.RevvBalancePublicPath).borrow()
        ?? panic("Could not borrow a reference to the vault resource")

    return [teleportUserRef.allowedAmount, userRef.balance]
}
```