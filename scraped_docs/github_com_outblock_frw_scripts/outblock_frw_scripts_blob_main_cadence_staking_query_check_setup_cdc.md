# Source: https://github.com/Outblock/FRW-scripts/blob/main/cadence/staking/query/check_setup.cdc

```
import FlowStakingCollection from 0xFlowStakingCollection

access(all) fun main(address: Address): Bool {
  return FlowStakingCollection.doesAccountHaveStakingCollection(address: address)
}
```