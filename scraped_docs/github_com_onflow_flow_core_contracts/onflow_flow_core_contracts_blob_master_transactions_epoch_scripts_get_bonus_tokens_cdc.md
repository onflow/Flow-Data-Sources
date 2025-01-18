# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/epoch/scripts/get_bonus_tokens.cdc

```
import FlowEpoch from "FlowEpoch"

access(all) fun main(): UFix64 {
    return FlowEpoch.getBonusTokens()
}

```