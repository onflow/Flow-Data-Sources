# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/idTableStaking/scripts/get_stake_requirements.cdc

```
import FlowIDTableStaking from "FlowIDTableStaking"

// This script returns the balance of staked tokens of a node

access(all) fun main(role: UInt8): UFix64 {
    let req = FlowIDTableStaking.getMinimumStakeRequirements()

    return req[role]!
}
```