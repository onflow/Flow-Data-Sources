# Source: https://github.com/IncrementFi/Liquid-Staking/blob/main/cadence/transactions/system/set_approved_list_in_system_kick.cdc

```
import FlowIDTableStaking from "../../contracts/standard/mainnet/FlowIDTableStaking.cdc"

transaction() {

    prepare(acct: auth(BorrowValue) &Account) {
        // borrow a reference to the admin object
        let adminRef = acct.storage.borrow<&FlowIDTableStaking.Admin>(from: FlowIDTableStaking.StakingAdminStoragePath)
            ?? panic("Could not borrow reference to staking admin")
        
        let nodeIDs = {
            "node-1-1": true,
            "node-1-2": true,
            "node-1-3": true,
            "node-1-4": true
        }
        adminRef.setApprovedList(nodeIDs)
    }
}
```