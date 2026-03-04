# Source: https://github.com/IncrementFi/Liquid-Staking/blob/main/cadence/scripts/user/query_user_info.cdc

```
import FungibleToken from "../../contracts/standard/FungibleToken.cdc"
import stFlowToken from "../../contracts/stFlowToken.cdc"
import LiquidStaking from "../../contracts/LiquidStaking.cdc"
import FlowStakingCollection from "../../contracts/standard/mainnet/FlowStakingCollection.cdc"

access(all) fun main(userAddr: Address): {String: AnyStruct} {
    
    let flowBalance = getAccount(userAddr).capabilities.borrow<&{FungibleToken.Balance}>(/public/flowTokenBalance)!.balance
    let stFlowBalance = getAccount(userAddr).capabilities.borrow<&{FungibleToken.Balance}>(/public/stFlowTokenBalance)!.balance

    let voucherCollectionRef = getAccount(userAddr).capabilities.borrow<&{LiquidStaking.WithdrawVoucherCollectionPublic}>(LiquidStaking.WithdrawVoucherCollectionPublicPath)
    var voucherInfos: [AnyStruct]? = nil
    if voucherCollectionRef != nil {
        voucherInfos = voucherCollectionRef!.getVoucherInfos()
    }

    var lockedTokensUsed = 0.0
    var unlockedTokensUsed = 0.0
    var migratedInfos: [AnyStruct]? = nil
    let stakingCollectionRef = getAccount(userAddr).capabilities.borrow<&{FlowStakingCollection.StakingCollectionPublic}>(FlowStakingCollection.StakingCollectionPublicPath)
    if stakingCollectionRef != nil {
        migratedInfos = stakingCollectionRef!.getAllDelegatorInfo()
        lockedTokensUsed = stakingCollectionRef!.lockedTokensUsed
        unlockedTokensUsed = stakingCollectionRef!.unlockedTokensUsed
    }

    return {
        "Flow": flowBalance,
        "stFlow": stFlowBalance,
        "UnstakingVouchers": voucherInfos,
        "MigratedInfos": {
            "lockedTokensUsed": lockedTokensUsed,
            "unlockedTokensUsed": unlockedTokensUsed,
            "migratedInfos": migratedInfos
        }
    }
}
```