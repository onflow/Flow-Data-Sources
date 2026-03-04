# Source: https://github.com/IncrementFi/Liquid-Staking/blob/main/cadence/transactions/test/clear_account_resource.cdc

```
import LiquidStaking from "../../contracts/LiquidStaking.cdc"
import stFlowToken from "../../contracts/stFlowToken.cdc"
import FlowToken from "../../contracts/standard/FlowToken.cdc"
import FungibleToken from "../../contracts/standard/FungibleToken.cdc"

transaction(flowAmount: UFix64) {
    prepare(userAccount: auth(LoadValue) &Account) {
        destroy userAccount.storage.load<@AnyResource>(from: stFlowToken.tokenVaultPath)
        destroy userAccount.storage.load<@AnyResource>(from: LiquidStaking.WithdrawVoucherCollectionPath)
    }
}
```