# Source: https://github.com/IncrementFi/Liquid-Staking/blob/main/cadence/transactions/admin/remove_approved_node.cdc

```
import DelegatorManager from "../../contracts/DelegatorManager.cdc"

transaction(nodeID: String) {
    prepare(nodeMgrAcct: auth(BorrowValue) &Account) {
        let adminRef = nodeMgrAcct.storage.borrow<&DelegatorManager.Admin>(from: DelegatorManager.adminPath)
            ?? panic("cannot borrow reference to Liquid Staking Admin")
        adminRef.removeApprovedNodeID(nodeID: nodeID)
    }
}
```