# Source: https://github.com/IncrementFi/Liquid-Staking/blob/main/cadence/scripts/flow-service/query_mini_stake_req.cdc

```
import FlowEpoch from "../../contracts/standard/mainnet/FlowEpoch.cdc"
import FlowIDTableStaking from "../../contracts/standard/mainnet/FlowIDTableStaking.cdc"

access(all) fun main(): AnyStruct {
    // current nodes can be staked
    let needs = FlowIDTableStaking.getMinimumStakeRequirements();
    return needs
}
```