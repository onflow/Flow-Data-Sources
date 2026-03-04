# Source: https://github.com/IncrementFi/Liquid-Staking/blob/main/cadence/transactions/user/migrate.cdc

```
import LiquidStaking from "../../contracts/LiquidStaking.cdc"
import LiquidStakingConfig from "../../contracts/LiquidStakingConfig.cdc"
import stFlowToken from "../../contracts/stFlowToken.cdc"
import FlowToken from "../../contracts/standard/FlowToken.cdc"
import FungibleToken from "../../contracts/standard/FungibleToken.cdc"
import FlowStakingCollection from "../../contracts/standard/mainnet/FlowStakingCollection.cdc"
import FlowIDTableStaking from "../../contracts/standard/mainnet/FlowIDTableStaking.cdc"
import LockedTokens from "../../contracts/standard/mainnet/LockedTokens.cdc"

transaction(nodeID: String, delegatorID: UInt32) {
    prepare(userAccount: auth(Storage, Capabilities) &Account) {
        let flowVault = userAccount.storage.borrow<&FlowToken.Vault>(from: /storage/flowTokenVault)!
        var delegatroInfo = FlowIDTableStaking.DelegatorInfo(nodeID: nodeID, delegatorID: delegatorID)
        var stFlowVaultRef = userAccount.storage.borrow<&stFlowToken.Vault>(from: stFlowToken.tokenVaultPath)
        if stFlowVaultRef == nil {
            userAccount.storage.save(<- stFlowToken.createEmptyVault(vaultType: Type<@stFlowToken.Vault>()), to: stFlowToken.tokenVaultPath)
            userAccount.capabilities.unpublish(stFlowToken.tokenReceiverPath)
            userAccount.capabilities.unpublish(stFlowToken.tokenBalancePath)
            userAccount.capabilities.publish(
                userAccount.capabilities.storage.issue<&{FungibleToken.Receiver}>(stFlowToken.tokenVaultPath),
                at: stFlowToken.tokenReceiverPath
            )
            userAccount.capabilities.publish(
                userAccount.capabilities.storage.issue<&{FungibleToken.Balance}>(stFlowToken.tokenVaultPath),
                at: stFlowToken.tokenBalancePath
            )
            stFlowVaultRef = userAccount.storage.borrow<&stFlowToken.Vault>(from: stFlowToken.tokenVaultPath)
        }

        // delegator in the locked account
        let linkedAccountInfoRef = userAccount.capabilities.borrow<&{LockedTokens.LockedAccountInfo}>(LockedTokens.LockedAccountInfoPublicPath)
        if linkedAccountInfoRef != nil {
            if nodeID == linkedAccountInfoRef!.getDelegatorNodeID() && delegatorID == linkedAccountInfoRef!.getDelegatorID() {
                let tokenHolderRef = userAccount.storage.borrow<auth(FungibleToken.Withdraw, LockedTokens.TokenOperations) &LockedTokens.TokenHolder>(from: LockedTokens.TokenHolderStoragePath)
                    ?? panic("Cannot borrow auth reference to TokenHolder")
                let delegatorProxy = tokenHolderRef.borrowDelegator()
                let flowVaultToStake <- FlowToken.createEmptyVault(vaultType: Type<@FlowToken.Vault>())

                if delegatroInfo.tokensCommitted > 0.0 {
                    let committedAmount = delegatroInfo.tokensCommitted
                    // cancel committed tokens
                    delegatorProxy.requestUnstaking(amount: committedAmount)
                    delegatorProxy.withdrawUnstakedTokens(amount: committedAmount)
                    flowVaultToStake.deposit(from: <- tokenHolderRef.withdraw(amount: committedAmount))
                }
                if delegatroInfo.tokensRewarded > 0.0 {
                    let rewardedAmount = delegatroInfo.tokensRewarded
                    delegatorProxy.withdrawRewardedTokens(amount: rewardedAmount)
                    flowVaultToStake.deposit(from: <- tokenHolderRef.withdraw(amount: rewardedAmount))
                }
                if delegatroInfo.tokensUnstaked > 0.0 {
                    let unstakedAmount = delegatroInfo.tokensUnstaked
                    delegatorProxy.withdrawUnstakedTokens(amount: unstakedAmount)
                    flowVaultToStake.deposit(from: <- tokenHolderRef.withdraw(amount: unstakedAmount))
                }

                if flowVaultToStake.balance >= LiquidStakingConfig.minStakingAmount {
                    let stFlowVault <- LiquidStaking.stake(flowVault: <-(flowVaultToStake as! @FlowToken.Vault))
                    stFlowVaultRef!.deposit(from: <-stFlowVault)
                } else {
                    // Deposit dust back to user account
                    flowVault.deposit(from: <-flowVaultToStake)
                }
                
                // unstake
                if delegatroInfo.tokensStaked > 0.0 {
                    let stakedAmount = delegatroInfo.tokensStaked - delegatroInfo.tokensRequestedToUnstake
                    delegatorProxy.requestUnstaking(amount: stakedAmount)
                }
                return
            }
        }

        // delegator in the user account
        let stakingCollectionRef = userAccount.storage.borrow<auth(FlowStakingCollection.CollectionOwner) &FlowStakingCollection.StakingCollection>(from: FlowStakingCollection.StakingCollectionStoragePath)
            ?? panic("Could not borrow auth ref to StakingCollection")
        let migratedDelegator <- stakingCollectionRef.removeDelegator(nodeID: nodeID, delegatorID: delegatorID)!
        let flowVaultToStake <- FlowToken.createEmptyVault(vaultType: Type<@FlowToken.Vault>())

        if delegatroInfo.tokensCommitted > 0.0 {
            migratedDelegator.requestUnstaking(amount: delegatroInfo.tokensCommitted)
            let committedVault <- migratedDelegator.withdrawUnstakedTokens(amount: delegatroInfo.tokensCommitted)
            flowVaultToStake.deposit(from: <-committedVault)
        }

        if delegatroInfo.tokensRequestedToUnstake > 0.0 {
            migratedDelegator.delegateUnstakedTokens(amount: delegatroInfo.tokensRequestedToUnstake)
        }
        if delegatroInfo.tokensRewarded > 0.0 {
            let rewardedVault <-migratedDelegator.withdrawRewardedTokens(amount: delegatroInfo.tokensRewarded)
            flowVaultToStake.deposit(from: <-rewardedVault)
        }
        if delegatroInfo.tokensUnstaked > 0.0 {
            let unstakedVault <-migratedDelegator.withdrawUnstakedTokens(amount: delegatroInfo.tokensUnstaked)
            flowVaultToStake.deposit(from: <-unstakedVault)
        }

        if flowVaultToStake.balance >= LiquidStakingConfig.minStakingAmount {
            let stFlowVault <- LiquidStaking.stake(flowVault: <-(flowVaultToStake as! @FlowToken.Vault))
            stFlowVaultRef!.deposit(from: <-stFlowVault)
        } else {
            // Deposit dust back to user account
            flowVault.deposit(from: <-flowVaultToStake)
        }

        if delegatroInfo.tokensUnstaking + delegatroInfo.tokensStaked == 0.0 {
            delegatroInfo = FlowIDTableStaking.DelegatorInfo(nodeID: migratedDelegator.nodeID, delegatorID: migratedDelegator.id)
            assert(
                delegatroInfo.tokensUnstaking
                + delegatroInfo.tokensRewarded
                + delegatroInfo.tokensUnstaked
                + delegatroInfo.tokensRequestedToUnstake
                + delegatroInfo.tokensCommitted
                + delegatroInfo.tokensStaked
                == 0.0, message: "Cannot destroy delegator"
            )
            destroy migratedDelegator
        } else {
            let outVault <- LiquidStaking.migrate(delegator: <-migratedDelegator)

            stFlowVaultRef!.deposit(from: <-outVault)
        }
    }
}
```