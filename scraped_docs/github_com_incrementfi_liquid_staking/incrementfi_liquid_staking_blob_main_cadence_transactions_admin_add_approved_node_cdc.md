# Source: https://github.com/IncrementFi/Liquid-Staking/blob/main/cadence/transactions/admin/add_approved_node.cdc

```
import DelegatorManager from "../../contracts/DelegatorManager.cdc"
import FlowToken from "../../contracts/standard/FlowToken.cdc"
import FungibleToken from "../../contracts/standard/FungibleToken.cdc"

transaction(nodeID: String, initialCommitment: UFix64) {
    prepare(nodeMgrAcct: auth(BorrowValue) &Account) {
        let vaultRef = nodeMgrAcct.storage.borrow<auth(FungibleToken.Withdraw) &FlowToken.Vault>(from: /storage/flowTokenVault)
            ?? panic("cannot borrow reference to Flow Vault")
        let adminRef = nodeMgrAcct.storage.borrow<&DelegatorManager.Admin>(from: DelegatorManager.adminPath)
            ?? panic("cannot borrow reference to Liquid Staking Admin")
        adminRef.upsertApprovedNodeID(nodeID: nodeID, weight: 1.0)
        adminRef.registerApprovedDelegator(nodeID: nodeID, initialCommit: <- vaultRef.withdraw(amount: initialCommitment))
    }
}
```