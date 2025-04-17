# Source: https://github.com/Outblock/FRW-scripts/blob/main/cadence/staking/query/get_delegates_info_array.cdc

```

import FlowStakingCollection from 0xFlowStakingCollection
import FlowIDTableStaking from 0xFlowIDTableStaking
import LockedTokens from 0xLockedTokens
        
access(all) fun main(address: Address): [FlowIDTableStaking.DelegatorInfo] {
  return FlowStakingCollection.getAllDelegatorInfo(address: address)
}
```