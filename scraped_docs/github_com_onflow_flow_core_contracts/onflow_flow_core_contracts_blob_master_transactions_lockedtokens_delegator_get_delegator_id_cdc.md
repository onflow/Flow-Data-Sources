# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/lockedTokens/delegator/get_delegator_id.cdc

```
import LockedTokens from "LockedTokens"

access(all) fun main(account: Address): UInt32 {

    let lockedAccountInfoRef = getAccount(account)
        .capabilities.borrow<&LockedTokens.TokenHolder>(
            LockedTokens.LockedAccountInfoPublicPath
        )
        ?? panic("Could not borrow a reference to public LockedAccountInfo")

    return lockedAccountInfoRef.getDelegatorID()!
}

```