# Source: https://github.com/IncrementFi/Liquid-Staking/blob/main/cadence/transactions/user/unstake_slowly.cdc

```
import LiquidStaking from "../../contracts/LiquidStaking.cdc"
import stFlowToken from "../../contracts/stFlowToken.cdc"
import FungibleToken from "../../contracts/standard/FungibleToken.cdc"

transaction(stFlowAmount: UFix64) {
    prepare(userAccount: auth(Storage, Capabilities) &Account) {
        let stFlowVault = userAccount.storage.borrow<auth(FungibleToken.Withdraw) &stFlowToken.Vault>(from: stFlowToken.tokenVaultPath)!
        let inVault <- stFlowVault.withdraw(amount: stFlowAmount) as! @stFlowToken.Vault

        let voucher <- LiquidStaking.unstake(stFlowVault: <-inVault)

        var voucherCollectionRef = userAccount.storage.borrow<&LiquidStaking.WithdrawVoucherCollection>(from: LiquidStaking.WithdrawVoucherCollectionPath)
        if voucherCollectionRef == nil {
            destroy <- userAccount.storage.load<@AnyResource>(from: LiquidStaking.WithdrawVoucherCollectionPath)
            userAccount.storage.save(<-LiquidStaking.createEmptyWithdrawVoucherCollection(), to: LiquidStaking.WithdrawVoucherCollectionPath)
            userAccount.capabilities.unpublish(LiquidStaking.WithdrawVoucherCollectionPublicPath)
            userAccount.capabilities.publish(
                userAccount.capabilities.storage.issue<&{LiquidStaking.WithdrawVoucherCollectionPublic}>(LiquidStaking.WithdrawVoucherCollectionPath),
                at: LiquidStaking.WithdrawVoucherCollectionPublicPath
            )
            voucherCollectionRef = userAccount.storage.borrow<&LiquidStaking.WithdrawVoucherCollection>(from: LiquidStaking.WithdrawVoucherCollectionPath)
        }
        voucherCollectionRef!.deposit(voucher: <-voucher)
    }
}
```