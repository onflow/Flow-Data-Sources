# Source: https://github.com/IncrementFi/Liquid-Staking/blob/main/cadence/transactions/admin/redelegate.cdc

```
import DelegatorManager from "../../contracts/DelegatorManager.cdc"

transaction(nodeID: String, delegatorID: UInt32, redelegateAmount: UFix64) {
    prepare(nodeMgrAcct: auth(BorrowValue) &Account) {
        let adminRef = nodeMgrAcct.storage.borrow<&DelegatorManager.Admin>(from: DelegatorManager.adminPath)
            ?? panic("cannot borrow reference to Liquid Staking Admin")
        adminRef.redelegate(nodeID: nodeID, delegatorID: delegatorID, amount: redelegateAmount)
    }
}
```