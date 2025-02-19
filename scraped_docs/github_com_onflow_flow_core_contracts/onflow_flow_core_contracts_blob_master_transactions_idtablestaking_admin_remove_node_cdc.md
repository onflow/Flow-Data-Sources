# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/idTableStaking/admin/remove_node.cdc

```
import "FlowIDTableStaking"

// This transaction removes an existing node from the identity table

transaction(id: String) {

    // Local variable for a reference to the ID Table Admin object
    let adminRef: &FlowIDTableStaking.Admin

    prepare(acct: auth(BorrowValue) &Account) {
        // borrow a reference to the admin object
        self.adminRef = acct.storage.borrow<&FlowIDTableStaking.Admin>(from: FlowIDTableStaking.StakingAdminStoragePath)
            ?? panic("Could not borrow reference to staking admin")
    }

    execute {
        self.adminRef.removeAndRefundNodeRecord(id)
    }
}
```