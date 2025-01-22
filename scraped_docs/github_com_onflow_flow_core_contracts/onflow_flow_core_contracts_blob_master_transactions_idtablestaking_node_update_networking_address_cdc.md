# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/idTableStaking/node/update_networking_address.cdc

```
import FlowIDTableStaking from "FlowIDTableStaking"

transaction(newAddress: String) {

    // Local variable for a reference to the node object
    let stakerRef: auth(FlowIDTableStaking.NodeOperator) &FlowIDTableStaking.NodeStaker

    prepare(acct: auth(BorrowValue) &Account) {
        // borrow a reference to the node object
        self.stakerRef = acct.storage.borrow<auth(FlowIDTableStaking.NodeOperator) &FlowIDTableStaking.NodeStaker>(from: FlowIDTableStaking.NodeStakerStoragePath)
            ?? panic("Could not borrow reference to staking admin")
    }

    execute {
        self.stakerRef.updateNetworkingAddress(newAddress)
    }
}

```