# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/idTableStaking/delegation/get_delegator_info_from_address.cdc

```
import "FlowIDTableStaking"

// This script gets all the info about a delegator and returns it

access(all) fun main(address: Address): FlowIDTableStaking.DelegatorInfo {

    let delegator = getAccount(address)
        .capabilities.borrow<&{FlowIDTableStaking.NodeDelegatorPublic}>(/public/flowStakingDelegator)
        ?? panic("Could not borrow reference to delegator object")

    return FlowIDTableStaking.DelegatorInfo(nodeID: delegator.nodeID, delegatorID: delegator.id)
}

```