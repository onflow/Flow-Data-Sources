# Source: https://github.com/IncrementFi/Swap/blob/main/src/flashloan/TestExecutor.cdc

```
import FungibleToken from "../contracts/tokens/FungibleToken.cdc"
import FlowToken from "../contracts/tokens/FlowToken.cdc"
import SwapConfig from "../contracts/SwapConfig.cdc"
import SwapFactory from "../contracts/SwapFactory.cdc"
import SwapInterfaces from "../contracts/SwapInterfaces.cdc"

pub contract TestExecutor {
    pub let feeVault: @FlowToken.Vault
    pub resource FlashloanExecutor: SwapInterfaces.FlashLoanExecutor {
        pub fun executeAndRepay(loanedToken: @FungibleToken.Vault, params: {String: AnyStruct}): @FungibleToken.Vault {
            // TODO: implement example
            let amountIn = loanedToken.balance

            // TODO: implement example
            // amountOut = amountIn x (1 + fee%)
            let feeAmount = amountIn*(1.0+UFix64(SwapFactory.getFlashloanRateBps()) / 10000.0) - amountIn - 0.00000001
            loanedToken.deposit(from: <- TestExecutor.feeVault.withdraw(amount: feeAmount))

            // TODO: implement example
            return <-loanedToken
        }
    }

    init() {
        // Set up FlashLoanExecutor resource
        let pathStr = "swap_flashloan_executor1"
        let executorPrivatePath = PrivatePath(identifier: pathStr)!
        let executorStoragePath = StoragePath(identifier: pathStr)!
        destroy <-self.account.load<@AnyResource>(from: executorStoragePath)
        self.account.save(<- create FlashloanExecutor(), to: executorStoragePath)
        self.account.link<&{SwapInterfaces.FlashLoanExecutor}>(executorPrivatePath, target: executorStoragePath)

        //self.feeVault <- FlowToken.createEmptyVault() as! @FlowToken.Vault
        self.feeVault <- self.account.borrow<&FlowToken.Vault>(from: /storage/flowTokenVault)!.withdraw(amount: 1000.0) as! @FlowToken.Vault
    }
}
 
```