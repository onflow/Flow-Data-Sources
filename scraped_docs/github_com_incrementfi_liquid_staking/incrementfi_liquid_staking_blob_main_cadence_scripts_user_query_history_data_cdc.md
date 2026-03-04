# Source: https://github.com/IncrementFi/Liquid-Staking/blob/main/cadence/scripts/user/query_history_data.cdc

```
import DelegatorManager from "../../contracts/DelegatorManager.cdc"
import LiquidStakingConfig from "../../contracts/LiquidStakingConfig.cdc"

access(all) fun main(): AnyStruct {
    let currentEpoch = DelegatorManager.quoteEpochCounter
    let lastEpoch = DelegatorManager.quoteEpochCounter
    var indexEpoch: UInt64 = 45
    let res: [AnyStruct] = []

    let currSnapshot = DelegatorManager.borrowEpochSnapshot(at: currentEpoch)
    let rewardReceivedNext = LiquidStakingConfig.calcEstimatedStakingPayout(stakedAmount: currSnapshot.allDelegatorStaked)
    let currentTotalStaked = DelegatorManager.getTotalValidStakingAmount()
    let currentApr = rewardReceivedNext / currentTotalStaked / 7.0 * 365.0

    while indexEpoch <= lastEpoch {
        let data = DelegatorManager.borrowEpochSnapshot(at: indexEpoch)

        var totalStaked = data.allDelegatorStaked+data.allDelegatorCommitted-data.allDelegatorRequestedToUnstake
        var apr = data.receivedReward / totalStaked / 7.0 * 365.0
        if indexEpoch == currentEpoch {
            apr = currentApr
            totalStaked = currentTotalStaked
        }
        res.append({
            "epoch": indexEpoch,
            "price": data.scaledQuoteStFlowFlow,
            "totalStaked": totalStaked,
            "apr": apr
        })
        indexEpoch = indexEpoch + 1
    }
    return res
}
```