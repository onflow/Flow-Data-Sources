# Source: https://github.com/IncrementFi/Liquid-Staking/blob/main/cadence/scripts/user/query_total_infos.cdc

```
import FlowIDTableStaking from "../../contracts/standard/mainnet/FlowIDTableStaking.cdc"
import FlowEpoch from "../../contracts/standard/mainnet/FlowEpoch.cdc"
import FlowStakingCollection from "../../contracts/standard/mainnet/FlowStakingCollection.cdc"

import stFlowToken from "../../contracts/stFlowToken.cdc"
import LiquidStaking from "../../contracts/LiquidStaking.cdc"
import LiquidStakingConfig from "../../contracts/LiquidStakingConfig.cdc"
import DelegatorManager from "../../contracts/DelegatorManager.cdc"
import LockedTokens from "../../contracts/standard/mainnet/LockedTokens.cdc"

access(all) fun main(userAddr: Address?): {String: AnyStruct} {
    let currentProtocolSnapshot = DelegatorManager.borrowCurrentQuoteEpochSnapshot()
    let currentBlockView = getCurrentBlock().view
    // Chain-referenced EpochMetadata
    let currentEpochMetadata = FlowEpoch.getEpochMetadata(FlowEpoch.currentEpochCounter)!
    // Protocol-referenced EpochMetadata
    let showEpochMetadata = FlowEpoch.getEpochMetadata(DelegatorManager.quoteEpochCounter)!

    var unlockEpoch = FlowEpoch.currentEpochCounter + 2
    if FlowIDTableStaking.stakingEnabled() {
        if currentBlockView + LiquidStakingConfig.windowSizeBeforeStakingEnd >= currentEpochMetadata.stakingEndView {
            unlockEpoch = FlowEpoch.currentEpochCounter + 3
        }
    } else {
        unlockEpoch = FlowEpoch.currentEpochCounter + 3
    }

    //let lastProtocolSnapshot = DelegatorManager.borrowEpochSnapshot(at: DelegatorManager.quoteEpochCounter-1) 
    //let lastApr = lastProtocolSnapshot.receivedReward / (lastProtocolSnapshot.allDelegatorStaked + lastProtocolSnapshot.allDelegatorCommitted - lastProtocolSnapshot.allDelegatorRequestedToUnstake) / 7.0 * 365.0
    let rewardReceivedNext = LiquidStakingConfig.calcEstimatedStakingPayout(stakedAmount: currentProtocolSnapshot.allDelegatorStaked)
    let currentTotalStaked = DelegatorManager.getTotalValidStakingAmount()
    let currentApr = rewardReceivedNext / currentTotalStaked / 7.0 * 365.0


    // voucher
    var voucherInfos: [AnyStruct]? = nil
    if userAddr != nil {
        let voucherCollectionRef = getAccount(userAddr!).capabilities.borrow<&{LiquidStaking.WithdrawVoucherCollectionPublic}>(LiquidStaking.WithdrawVoucherCollectionPublicPath)
        if voucherCollectionRef != nil {
            voucherInfos = voucherCollectionRef!.getVoucherInfos()
        }
    }

    // migrate
    var linkedAccountTokenUsed = 0.0
    var unlockedAccountTokensUsed = 0.0
    var migratedInfos: [AnyStruct] = []
    var linkedAccountBalance = 0.0
    var linkedAccountUnlockLimit = 0.0
    var linkedAccountDelegatorID: UInt32? = nil
    var linkedAccountDelegatorNodeID: String? = nil
    if userAddr != nil {
        // check locked account delegator
        let linkedAccountInfoRef = getAccount(userAddr!).capabilities.borrow<&{LockedTokens.LockedAccountInfo}>(LockedTokens.LockedAccountInfoPublicPath)
        if linkedAccountInfoRef != nil {
            linkedAccountBalance = linkedAccountInfoRef!.getLockedAccountBalance()
            linkedAccountUnlockLimit = linkedAccountInfoRef!.getUnlockLimit()
            linkedAccountDelegatorNodeID = linkedAccountInfoRef!.getDelegatorNodeID()
            linkedAccountDelegatorID = linkedAccountInfoRef!.getDelegatorID()
        }

        let stakingCollectionRef = getAccount(userAddr!).capabilities.borrow<&{FlowStakingCollection.StakingCollectionPublic}>(FlowStakingCollection.StakingCollectionPublicPath)
        if stakingCollectionRef != nil {
            let delegatorInfos = stakingCollectionRef!.getAllDelegatorInfo()
            linkedAccountTokenUsed = stakingCollectionRef!.lockedTokensUsed
            unlockedAccountTokensUsed = stakingCollectionRef!.unlockedTokensUsed
            
            for delegatorInfo in delegatorInfos {
                if delegatorInfo.nodeID == linkedAccountDelegatorNodeID && delegatorInfo.id == linkedAccountDelegatorID {
                    continue
                }
                var tokenStakedMigratable = delegatorInfo.tokensStaked

                if delegatorInfo.tokensUnstaking > 0.0 {
                    tokenStakedMigratable = 0.0
                }
                if delegatorInfo.tokensCommitted + delegatorInfo.tokensStaked + delegatorInfo.tokensUnstaking + delegatorInfo.tokensRewarded + delegatorInfo.tokensUnstaked > 0.0 {
                    migratedInfos.append({
                        "isLockedAccount": false,
                        "lockedTokenAmount": linkedAccountTokenUsed,

                        "tokenStakedNeedToUnstake": 0.0,
                        "tokenStakedMigratable": tokenStakedMigratable,
                        "tokenStakedNonMigratable": delegatorInfo.tokensStaked - tokenStakedMigratable,
                        
                        "id": delegatorInfo.id,
                        "nodeID": delegatorInfo.nodeID,
                        "tokensCommitted": delegatorInfo.tokensCommitted,
                        "tokensStaked": delegatorInfo.tokensStaked,
                        "tokensUnstaking": delegatorInfo.tokensUnstaking,
                        "tokensRewarded": delegatorInfo.tokensRewarded,
                        "tokensUnstaked": delegatorInfo.tokensUnstaked,
                        "tokensRequestedToUnstake": delegatorInfo.tokensRequestedToUnstake
                    })
                }
            }
        }
        // delegator in linked account
        if linkedAccountDelegatorID != nil && linkedAccountDelegatorNodeID != nil {
            let delegatorInfo = FlowIDTableStaking.DelegatorInfo(nodeID: linkedAccountDelegatorNodeID!, delegatorID: linkedAccountDelegatorID!)
            let tokensInDelegator = delegatorInfo.tokensCommitted + delegatorInfo.tokensStaked + delegatorInfo.tokensUnstaking + delegatorInfo.tokensRewarded + delegatorInfo.tokensUnstaked
            if tokensInDelegator > 0.0 {
                var lockedTokenAmount = 0.0
                if tokensInDelegator - delegatorInfo.tokensRewarded + linkedAccountBalance + linkedAccountTokenUsed > linkedAccountUnlockLimit {
                    lockedTokenAmount = tokensInDelegator - delegatorInfo.tokensRewarded + linkedAccountBalance + linkedAccountTokenUsed - linkedAccountUnlockLimit
                }
                let tokenStakedNeedToUnstake = delegatorInfo.tokensStaked - delegatorInfo.tokensRequestedToUnstake
                let tokenStakedMigratable = 0.0
                let tokenStakedNonMigratable = 0.0
                
                migratedInfos.append({
                    "isLockedAccount": true,
                    "lockedTokenAmount": lockedTokenAmount,

                    "tokenStakedNeedToUnstake": tokenStakedNeedToUnstake,
                    "tokenStakedMigratable": 0.0,
                    "tokenStakedNonMigratable": delegatorInfo.tokensStaked,
                    
                    "id": delegatorInfo.id,
                    "nodeID": delegatorInfo.nodeID,
                    "tokensCommitted": delegatorInfo.tokensCommitted,
                    "tokensStaked": delegatorInfo.tokensStaked,
                    "tokensUnstaking": delegatorInfo.tokensUnstaking,
                    "tokensRewarded": delegatorInfo.tokensRewarded,
                    "tokensUnstaked": delegatorInfo.tokensUnstaked,
                    "tokensRequestedToUnstake": delegatorInfo.tokensRequestedToUnstake
                })
            }
        }
    }
    
    return {
        "stakingEnable": FlowIDTableStaking.stakingEnabled(),
        "CurrentEpoch": DelegatorManager.quoteEpochCounter,
        "CurrentUnstakeEpoch": unlockEpoch,

        "stFlowFlow": currentProtocolSnapshot.scaledQuoteStFlowFlow,
        "FlowStFlow": currentProtocolSnapshot.scaledQuoteFlowStFlow,

        "TotalStaked": currentTotalStaked,
        "UnderlyingAPR": FlowIDTableStaking.getEpochTokenPayout() / FlowIDTableStaking.getTotalStaked() / 7.0 * 365.0 * (1.0 - FlowIDTableStaking.getRewardCutPercentage() * (1.0 - LiquidStakingConfig.protocolFee)),
        "APR": currentApr,
        "EpochMetadata": {
            "StartView": showEpochMetadata.startView,
            "StartTimestamp": currentProtocolSnapshot.quoteEpochStartTimestamp,
            "EndView": showEpochMetadata.endView,
            "CurrentView": currentBlockView,
            "CurrentTimestamp": getCurrentBlock().timestamp,
            "StakingEndView": showEpochMetadata.stakingEndView
        },

        "User": {
            "UnstakingVouchers": voucherInfos,
            "MigratedInfos": {
                "lockedTokensUsed": linkedAccountTokenUsed,
                "unlockedTokensUsed": unlockedAccountTokensUsed,
                "linkedAccountUnlockLimit": linkedAccountUnlockLimit,
                "linkedAccountDelegatorNodeID": linkedAccountDelegatorNodeID,
                "linkedAccountDelegatorID": linkedAccountDelegatorID,
                "migratedInfos": migratedInfos
            }
        },

        "MinStakingAmount": LiquidStakingConfig.minStakingAmount
    }
}
```