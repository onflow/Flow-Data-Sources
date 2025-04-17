# Source: https://github.com/Outblock/FRW-scripts/blob/main/cadence/staking/query/check_staking_enabled.cdc

```
import FlowIDTableStaking from 0xFlowIDTableStaking

access(all) fun main():Bool {
  return FlowIDTableStaking.stakingEnabled()
}
```