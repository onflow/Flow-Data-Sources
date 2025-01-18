# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/stakingCollection/scripts/get_unlocked_tokens_used.cdc

```
import FlowStakingCollection from "FlowStakingCollection"

/// Tells how many unlocked tokens the account is using
/// For there staking collection nodes and delegators

access(all) fun main(account: Address): UFix64 {
    return FlowStakingCollection.getUnlockedTokensUsed(address: account)
}

```