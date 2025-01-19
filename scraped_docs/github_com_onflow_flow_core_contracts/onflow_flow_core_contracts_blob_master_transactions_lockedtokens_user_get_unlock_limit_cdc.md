# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/lockedTokens/user/get_unlock_limit.cdc

```
import LockedTokens from "LockedTokens"

access(all) fun main(account: Address): UFix64 {

    let lockedAccountInfoRef = getAccount(account)
        .capabilities.borrow<&LockedTokens.TokenHolder>(
            LockedTokens.LockedAccountInfoPublicPath
        )
        ?? panic("Could not borrow a reference to public LockedAccountInfo")

    return lockedAccountInfoRef.getUnlockLimit()
}

```