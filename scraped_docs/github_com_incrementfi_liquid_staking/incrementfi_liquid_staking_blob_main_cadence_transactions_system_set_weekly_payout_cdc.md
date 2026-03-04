# Source: https://github.com/IncrementFi/Liquid-Staking/blob/main/cadence/transactions/system/set_weekly_payout.cdc

```
import FlowIDTableStaking from "../../contracts/standard/mainnet/FlowIDTableStaking.cdc"

transaction(payout: UFix64) {

    prepare(acct: auth(BorrowValue) &Account) {
        // borrow a reference to the admin object
        let adminRef = acct.storage.borrow<&FlowIDTableStaking.Admin>(from: FlowIDTableStaking.StakingAdminStoragePath)
            ?? panic("Could not borrow reference to staking admin")
        
        adminRef.setEpochTokenPayout(payout)
    }
}
```