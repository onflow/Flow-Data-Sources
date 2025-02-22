# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/idTableStaking/admin/change_cut.cdc

```
import "FlowIDTableStaking"

// This transaction changes the flow token reward cut that nodes take from delegators

transaction(newCutPercentage: UFix64) {

    // Local variable for a reference to the ID Table Admin object
    let adminRef: &FlowIDTableStaking.Admin

    prepare(acct: auth(BorrowValue) &Account) {
        // borrow a reference to the admin object
        self.adminRef = acct.storage.borrow<&FlowIDTableStaking.Admin>(from: FlowIDTableStaking.StakingAdminStoragePath)
            ?? panic("Could not borrow reference to staking admin")
    }

    execute {
        self.adminRef.setCutPercentage(newCutPercentage)
    }
}
```