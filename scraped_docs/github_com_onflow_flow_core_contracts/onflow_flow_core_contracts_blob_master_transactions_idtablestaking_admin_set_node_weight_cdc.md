# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/idTableStaking/admin/set_node_weight.cdc

```
import "FlowIDTableStaking"

// This transaction sets the initialWeight of an existing node
transaction(id: String, weight: UInt64) {

    // Local variable for a reference to the ID Table Admin object
    let adminRef: &FlowIDTableStaking.Admin

    prepare(acct: auth(BorrowValue) &Account) {
        // borrow a reference to the admin object
        self.adminRef = acct.storage.borrow<&FlowIDTableStaking.Admin>(from: FlowIDTableStaking.StakingAdminStoragePath)
            ?? panic("Could not borrow reference to staking admin")
    }

    execute {
        self.adminRef.setNodeWeight(nodeID: id, weight: weight)
    }
}
```