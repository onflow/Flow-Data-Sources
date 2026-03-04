# Source: https://github.com/IncrementFi/Liquid-Staking/blob/main/cadence/transactions/user/unstake_cashing.cdc

```
import LiquidStaking from "../../contracts/LiquidStaking.cdc"
import FlowToken from "../../contracts/standard/FlowToken.cdc"
import FungibleToken from "../../contracts/standard/FungibleToken.cdc"

transaction(uuid: UInt64) {
    prepare(userAccount: auth(BorrowValue) &Account) {
        let voucherCollection = userAccount.storage.borrow<auth(FungibleToken.Withdraw) &LiquidStaking.WithdrawVoucherCollection>(from: LiquidStaking.WithdrawVoucherCollectionPath)
            ?? panic("cannot borrow reference to WithdrawVoucherCollection")
        let voucher <-voucherCollection.withdraw(uuid: uuid)
        let flowVault <- LiquidStaking.cashoutWithdrawVoucher(voucher: <-voucher)

        userAccount.storage.borrow<&FlowToken.Vault>(from: /storage/flowTokenVault)!.deposit(from: <-flowVault)
    }
}
```