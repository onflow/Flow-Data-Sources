# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/stakingCollection/scripts/get_locked_tokens_used.cdc

```
import "FlowStakingCollection"

/// Tells how many locked tokens the account is using
/// For there staking collection nodes and delegators

access(all) fun main(account: Address): UFix64 {
    return FlowStakingCollection.getLockedTokensUsed(address: account)
}
```