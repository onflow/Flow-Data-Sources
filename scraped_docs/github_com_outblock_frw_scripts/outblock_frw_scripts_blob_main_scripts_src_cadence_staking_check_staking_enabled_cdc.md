# Source: https://github.com/Outblock/FRW-scripts/blob/main/scripts/src/cadence/staking/check_staking_enabled.cdc

```
import FlowIDTableStaking from 0xFlowIDTableStaking

access(all) fun main():Bool {
    return FlowIDTableStaking.stakingEnabled()
}
```