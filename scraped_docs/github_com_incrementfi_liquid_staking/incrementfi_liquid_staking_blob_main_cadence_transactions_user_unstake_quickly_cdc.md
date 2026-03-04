# Source: https://github.com/IncrementFi/Liquid-Staking/blob/main/cadence/transactions/user/unstake_quickly.cdc

```
import LiquidStaking from "../../contracts/LiquidStaking.cdc"
import stFlowToken from "../../contracts/stFlowToken.cdc"
import FlowToken from "../../contracts/standard/FlowToken.cdc"
import FungibleToken from "../../contracts/standard/FungibleToken.cdc"

transaction(stFlowAmount: UFix64) {
    prepare(userAccount: auth(BorrowValue) &Account) {
        let flowVault = userAccount.storage.borrow<&FlowToken.Vault>(from: /storage/flowTokenVault)!
        let stFlowVault = userAccount.storage.borrow<auth(FungibleToken.Withdraw) &stFlowToken.Vault>(from: stFlowToken.tokenVaultPath)!

        let inVault <- stFlowVault.withdraw(amount: stFlowAmount) as! @stFlowToken.Vault
        let outVault <- LiquidStaking.unstakeQuickly(stFlowVault: <-inVault)

        flowVault.deposit(from: <-outVault)
    }
}
```