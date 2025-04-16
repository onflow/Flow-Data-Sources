# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/idTableStaking/delegation/del_request_unstaking.cdc

```
import "FlowIDTableStaking"


transaction(amount: UFix64) {

    // Local variable for a reference to the Delegator object
    let delegatorRef: auth(FlowIDTableStaking.DelegatorOwner) &FlowIDTableStaking.NodeDelegator

    prepare(acct: auth(BorrowValue) &Account) {
        // borrow a reference to the delegator object
        self.delegatorRef = acct.storage.borrow<auth(FlowIDTableStaking.DelegatorOwner) &FlowIDTableStaking.NodeDelegator>(from: FlowIDTableStaking.DelegatorStoragePath)
            ?? panic("Could not borrow reference to delegator")

    }

    execute {

        self.delegatorRef.requestUnstaking(amount: amount)

    }
}
```