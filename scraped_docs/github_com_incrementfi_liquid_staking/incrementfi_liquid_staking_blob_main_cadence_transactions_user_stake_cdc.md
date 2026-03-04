# Source: https://github.com/IncrementFi/Liquid-Staking/blob/main/cadence/transactions/user/stake.cdc

```
import LiquidStaking from "../../contracts/LiquidStaking.cdc"
import stFlowToken from "../../contracts/stFlowToken.cdc"
import FlowToken from "../../contracts/standard/FlowToken.cdc"
import FungibleToken from "../../contracts/standard/FungibleToken.cdc"

transaction(flowAmount: UFix64) {
    prepare(userAccount: auth(Storage, Capabilities) &Account) {
        let flowVault = userAccount.storage.borrow<auth(FungibleToken.Withdraw) &FlowToken.Vault>(from: /storage/flowTokenVault)!
        let inVault <- flowVault.withdraw(amount: flowAmount) as! @FlowToken.Vault        
        let outVault <- LiquidStaking.stake(flowVault: <-inVault)

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

        stFlowVaultRef!.deposit(from: <-outVault)
    }
}
```