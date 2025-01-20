# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/idTableStaking/delegation/get_delegator_info.cdc

```
import FlowIDTableStaking from "FlowIDTableStaking"

// This script returns all the info associated with a delegator

access(all) fun main(nodeID: String, delegatorID: UInt32): FlowIDTableStaking.DelegatorInfo {
    return FlowIDTableStaking.DelegatorInfo(nodeID: nodeID, delegatorID: delegatorID)
}
```