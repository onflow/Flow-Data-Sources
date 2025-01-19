# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/lockedTokens/user/get_locked_account_balance.cdc

```
import LockedTokens from "LockedTokens"

access(all) fun main(account: Address): UFix64 {

    let lockedAccountInfoRef = getAccount(account)
        .capabilities.borrow<&LockedTokens.TokenHolder>(
            LockedTokens.LockedAccountInfoPublicPath
        )
        ?? panic("Could not borrow a reference to public LockedAccountInfo")

    return lockedAccountInfoRef.getLockedAccountBalance()
}

```