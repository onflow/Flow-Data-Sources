# Source: https://github.com/IncrementFi/Liquid-Staking/blob/main/cadence/scripts/user/query_locked_account.cdc

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

    // voucher
    var voucherInfos: [AnyStruct]? = nil
    if userAddr != nil {
        let voucherCollectionRef = getAccount(userAddr!).capabilities.borrow<&{LiquidStaking.WithdrawVoucherCollectionPublic}>(LiquidStaking.WithdrawVoucherCollectionPublicPath)
        if voucherCollectionRef != nil {
            voucherInfos = voucherCollectionRef!.getVoucherInfos()
        }
    }

    // migrate
    var lockedTokensUsed = 0.0
    var unlockedTokensUsed = 0.0
    var migratedInfos: [AnyStruct] = []
    var lockedAccountBalance = 0.0
    var lockedAccountUnlockLimit = 0.0
    var lockedAccountDelegatorID: UInt32? = nil
    var lockedAccountDelegatorNodeID: String? = nil
    if userAddr != nil {
        // check locked account delegator
        let lockedAccountInfoRef = getAccount(userAddr!).capabilities.borrow<&{LockedTokens.LockedAccountInfo}>(LockedTokens.LockedAccountInfoPublicPath)
        if lockedAccountInfoRef != nil {
            lockedAccountBalance = lockedAccountInfoRef!.getLockedAccountBalance()
            lockedAccountUnlockLimit = lockedAccountInfoRef!.getUnlockLimit()
            lockedAccountDelegatorNodeID = lockedAccountInfoRef!.getDelegatorNodeID()
            lockedAccountDelegatorID = lockedAccountInfoRef!.getDelegatorID()
        }

        let stakingCollectionRef = getAccount(userAddr!).capabilities.borrow<&{FlowStakingCollection.StakingCollectionPublic}>(FlowStakingCollection.StakingCollectionPublicPath)
        if stakingCollectionRef != nil {
            let delegatorInfos = stakingCollectionRef!.getAllDelegatorInfo()
            lockedTokensUsed = stakingCollectionRef!.lockedTokensUsed
            unlockedTokensUsed = stakingCollectionRef!.unlockedTokensUsed
            
            for delegatorInfo in delegatorInfos {
                var migratable = true
                var isLockedAccount = false
                var isLockedTokenUsed = false
                if delegatorInfo.nodeID == lockedAccountDelegatorNodeID && delegatorInfo.id == lockedAccountDelegatorID {
                    migratable = false
                    isLockedAccount = true
                }
                if lockedTokensUsed > 0.0 {
                    migratable = false
                    isLockedTokenUsed = true
                }
                if delegatorInfo.tokensUnstaking > 0.0 {
                    migratable = false
                }
                if delegatorInfo.tokensCommitted + delegatorInfo.tokensStaked + delegatorInfo.tokensUnstaking + delegatorInfo.tokensRewarded + delegatorInfo.tokensUnstaked > 0.0 {
                    migratedInfos.append({
                        "migratable": migratable,
                        "isLockedAccount": isLockedAccount,
                        "isLockedTokenUsed": isLockedTokenUsed,
                        
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
        } else if lockedAccountDelegatorID != nil && lockedAccountDelegatorNodeID != nil {
            let delegatorInfo = FlowIDTableStaking.DelegatorInfo(nodeID: lockedAccountDelegatorNodeID!, delegatorID: lockedAccountDelegatorID!)
            migratedInfos.append({
                "migratable": false,
                "isLockedAccount": true,
                "isLockedTokenUsed": 0.0,
                
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
    
    return {
        "CurrentEpoch": DelegatorManager.quoteEpochCounter,
        "CurrentUnstakeEpoch": unlockEpoch,

        "stFlowFlow": currentProtocolSnapshot.scaledQuoteStFlowFlow,
        "FlowStFlow": currentProtocolSnapshot.scaledQuoteFlowStFlow,

        "TotalStaked": DelegatorManager.getTotalValidStakingAmount(),
        "APR": FlowIDTableStaking.getEpochTokenPayout() / FlowIDTableStaking.getTotalStaked() / 7.0 * 365.0 * (1.0 - FlowIDTableStaking.getRewardCutPercentage() * (1.0 - LiquidStakingConfig.protocolFee)),

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
                "lockedTokensUsed": lockedTokensUsed,
                "unlockedTokensUsed": unlockedTokensUsed,
                "lockedAccountUnlockLimit": lockedAccountUnlockLimit,
                "migratedInfos": migratedInfos
            }
        },

        "MinStakingAmount": LiquidStakingConfig.minStakingAmount
    }
}
```