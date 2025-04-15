# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/lockedTokens/delegator/get_delegator_node_id.cdc

```
import "LockedTokens"

access(all) fun main(account: Address): String {

    let lockedAccountInfoRef = getAccount(account)
        .capabilities.borrow<&LockedTokens.TokenHolder>(
            LockedTokens.LockedAccountInfoPublicPath
        )
        ?? panic("Could not borrow a reference to public LockedAccountInfo")

    return lockedAccountInfoRef.getDelegatorNodeID()!
}

```