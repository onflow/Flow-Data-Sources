# Source: https://github.com/IncrementFi/Liquid-Staking/blob/main/cadence/scripts/user/query_bot_infos.cdc

```
import DelegatorManager from "../../contracts/DelegatorManager.cdc"
import LiquidStakingConfig from "../../contracts/LiquidStakingConfig.cdc"
import FlowIDTableStaking from "../../contracts/standard/mainnet/FlowIDTableStaking.cdc"
import FlowEpoch from "../../contracts/standard/mainnet/FlowEpoch.cdc"

access(all) fun main(): AnyStruct {
    let currentEpochMetadata = FlowEpoch.getEpochMetadata(FlowEpoch.currentEpochCounter)
    var stakingEndView: UInt64 = 0
    if currentEpochMetadata != nil {
        stakingEndView = currentEpochMetadata!.stakingEndView
    }

    return {
        "StakingEnable": FlowIDTableStaking.stakingEnabled(),
        "QuoteEpoch": DelegatorManager.quoteEpochCounter,
        "FlowEpoch": FlowEpoch.currentEpochCounter,
        "DelegatorLength": DelegatorManager.getDelegatorsLength(),
        "UnprocessedUnstakeRequests": DelegatorManager.requestedToUnstake,
        "WindowSizeBeforeStakingEnd": LiquidStakingConfig.windowSizeBeforeStakingEnd,
        "CurrentView": getCurrentBlock().view,
        "StakingEndView": stakingEndView,
        "DefaultNodeID": DelegatorManager.defaultNodeIDToStake,
        "DefaultDelegatorCommitted": DelegatorManager.getApprovedDelegatorInfoByNodeID(nodeID: DelegatorManager.defaultNodeIDToStake).tokensCommitted,
        "TotalCommitted": DelegatorManager.borrowCurrentQuoteEpochSnapshot().allDelegatorCommitted
    }
}
```