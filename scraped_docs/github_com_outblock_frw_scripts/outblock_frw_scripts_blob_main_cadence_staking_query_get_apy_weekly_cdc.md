# Source: https://github.com/Outblock/FRW-scripts/blob/main/cadence/staking/query/get_apy_weekly.cdc

```
import FlowIDTableStaking from 0xFlowIDTableStaking

access(all) fun main(): UFix64 {
  let apr = FlowIDTableStaking.getEpochTokenPayout() / FlowIDTableStaking.getTotalStaked() * 54.0 * (1.0 - FlowIDTableStaking.getRewardCutPercentage())
  return apr
}
```