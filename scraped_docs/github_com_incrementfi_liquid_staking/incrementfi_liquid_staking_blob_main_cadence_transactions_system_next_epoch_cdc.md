# Source: https://github.com/IncrementFi/Liquid-Staking/blob/main/cadence/transactions/system/next_epoch.cdc

```
import FlowEpoch from "../../contracts/standard/mainnet/FlowEpoch.cdc"
import FlowIDTableStaking from "../../contracts/standard/mainnet/FlowIDTableStaking.cdc"

transaction(nextRewardAmount: UFix64) {

    prepare(acct: auth(BorrowValue) &Account) {
        let heatbeat = acct.storage.borrow<&FlowEpoch.Heartbeat>(from: FlowEpoch.heartbeatStoragePath)!
        //
        heatbeat.payRewardsForPreviousEpoch()
        //
        heatbeat.endStakingAuction()
        //
        heatbeat.calculateAndSetRewards()
        //
        heatbeat.startEpochCommit()
        //
        heatbeat.endEpoch()

        let adminRef = acct.storage.borrow<&FlowIDTableStaking.Admin>(from: FlowIDTableStaking.StakingAdminStoragePath)
            ?? panic("Could not borrow reference to staking admin")
        
        adminRef.setEpochTokenPayout(nextRewardAmount)
    }
}
```