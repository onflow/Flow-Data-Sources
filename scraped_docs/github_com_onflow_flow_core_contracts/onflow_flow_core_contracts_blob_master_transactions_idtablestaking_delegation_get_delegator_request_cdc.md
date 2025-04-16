# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/idTableStaking/delegation/get_delegator_request.cdc

```
import "FlowIDTableStaking"

// This script returns the requested unstaking balance of a delegator

access(all) fun main(nodeID: String, delegatorID: UInt32): UFix64 {
    let delInfo = FlowIDTableStaking.DelegatorInfo(nodeID: nodeID, delegatorID: delegatorID)
    return delInfo.tokensRequestedToUnstake
}
```