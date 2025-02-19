# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/idTableStaking/admin/transfer_fees_admin.cdc

```
import "FlowFees"

transaction {

    prepare(owner: auth(LoadValue) &Account, receiver: auth(SaveValue) &Account) {

        // Link the staking admin capability to a private place
        let feesAdmin <- owner.storage.load<@FlowFees.Administrator>(from: /storage/flowFeesAdmin)!

        // Save the capability to the receiver's account storage
        receiver.storage.save(<-feesAdmin, to: /storage/flowFeesAdmin)
    }

}
 

```