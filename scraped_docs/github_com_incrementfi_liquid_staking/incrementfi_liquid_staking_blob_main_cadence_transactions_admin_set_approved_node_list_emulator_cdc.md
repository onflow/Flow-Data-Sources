# Source: https://github.com/IncrementFi/Liquid-Staking/blob/main/cadence/transactions/admin/set_approved_node_list.emulator.cdc

```
import DelegatorManager from "../../contracts/DelegatorManager.cdc"
import FlowToken from "../../contracts/standard/FlowToken.cdc"
import FungibleToken from "../../contracts/standard/FungibleToken.cdc"

transaction(initialCommitment: UFix64) {
    prepare(nodeMgrAcct: auth(BorrowValue) &Account) {
        log("---------> node: set approved list")
        let vaultRef = nodeMgrAcct.storage.borrow<auth(FungibleToken.Withdraw) &FlowToken.Vault>(from: /storage/flowTokenVault)
            ?? panic("cannot borrow reference to Flow Vault")
        let adminRef = nodeMgrAcct.storage.borrow<&DelegatorManager.Admin>(from: DelegatorManager.adminPath)
            ?? panic("cannot borrow reference to Liquid Staking Admin")
        let ids: {String: UFix64} = {
            "node-1-1": 1.0,
            "node-1-2": 1.0,
            "node-1-3": 1.0,
            "node-1-4": 1.0,
            "node-1-5": 1.0
        }
        adminRef.initApprovedNodeIDList(nodeIDs: ids, defaultNodeIDToStake: "node-1-1")

        adminRef.registerApprovedDelegator(nodeID: "node-1-1", initialCommit: <- vaultRef.withdraw(amount: initialCommitment))
        adminRef.registerApprovedDelegator(nodeID: "node-1-2", initialCommit: <- vaultRef.withdraw(amount: initialCommitment))
        adminRef.registerApprovedDelegator(nodeID: "node-1-3", initialCommit: <- vaultRef.withdraw(amount: initialCommitment))
        adminRef.registerApprovedDelegator(nodeID: "node-1-4", initialCommit: <- vaultRef.withdraw(amount: initialCommitment))
        adminRef.registerApprovedDelegator(nodeID: "node-1-5", initialCommit: <- vaultRef.withdraw(amount: initialCommitment))
    }
}
```