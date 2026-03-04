# Source: https://github.com/IncrementFi/Liquid-Staking/blob/main/cadence/transactions/admin/withdraw_protocol_fees.cdc

```
import DelegatorManager from "../../contracts/DelegatorManager.cdc"
import FungibleToken from "../../contracts/standard/FungibleToken.cdc"

transaction(feeTo: Address) {
    prepare(admin: auth(BorrowValue) &Account) {
        let flowReceiverRef = getAccount(feeTo).capabilities.borrow<&{FungibleToken.Receiver}>(/public/flowTokenReceiver)
            ?? panic("cannot borrow receiver reference to the recipient's Vault")
        let adminRef = admin.storage.borrow<&DelegatorManager.Admin>(from: DelegatorManager.adminPath)
            ?? panic("cannot borrow reference to Liquid Staking Admin")
        let protocolFeeVault <- adminRef.borrowProtocolFeeVault().withdraw(amount: DelegatorManager.getProtocolFeeBalance())
        flowReceiverRef.deposit(from: <-protocolFeeVault)
    }
}
```