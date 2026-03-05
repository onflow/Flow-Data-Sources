# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/idTableStaking/scripts/get_node_info_from_address.cdc

```
import "FlowIDTableStaking"

// This script gets all the info about a node and returns it

access(all) fun main(address: Address): FlowIDTableStaking.NodeInfo {

    let authAccount = getAuthAccount<auth(Storage) &Account>(address)
    let nodeStakerRef = authAccount.storage.borrow<&FlowIDTableStaking.NodeStaker>(from: FlowIDTableStaking.NodeStakerStoragePath)
        ?? panic("Could not borrow reference to node staker object")

    return FlowIDTableStaking.NodeInfo(nodeID: nodeStakerRef.id)
}

```