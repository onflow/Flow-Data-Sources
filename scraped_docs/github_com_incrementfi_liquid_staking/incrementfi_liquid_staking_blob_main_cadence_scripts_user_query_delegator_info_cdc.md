# Source: https://github.com/IncrementFi/Liquid-Staking/blob/main/cadence/scripts/user/query_delegator_info.cdc

```
import FlowIDTableStaking from "../../contracts/standard/mainnet/FlowIDTableStaking.cdc"

access(all) fun main(nodeID: String, delegatorID: UInt32): FlowIDTableStaking.DelegatorInfo {
    return FlowIDTableStaking.DelegatorInfo(nodeID: nodeID, delegatorID: delegatorID)
}
```