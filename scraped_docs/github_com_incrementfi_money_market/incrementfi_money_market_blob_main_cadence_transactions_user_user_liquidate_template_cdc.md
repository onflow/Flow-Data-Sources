# Source: https://github.com/IncrementFi/Money-Market/blob/main/cadence/transactions/User/user_liquidate_template.cdc

```
import FlowToken from "../../contracts/tokens/FlowToken.cdc"
import FungibleToken from "../../contracts/tokens/FungibleToken.cdc"
import LendingPool from "../../contracts/LendingPool.cdc"

// Liquidation Inform:
//
// Liquidated Address: BORROWER
// Repaied LIQUIDATEAMOUNT LIQUIDATETOKEN on your behalf
//
transaction(amountLiquidate: UFix64, borrower: Address, seizePoolAddr: Address) {
    let flowTokenVault: auth(FungibleToken.Withdraw) &FlowToken.Vault
    let liquidatorAddr: Address
    let informVault: @{FungibleToken.Vault}

    prepare(signer: auth(Storage, StorageCapabilities) &Account) {
        let flowTokenStoragePath = /storage/flowTokenVault
        self.flowTokenVault  = signer.storage.borrow<auth(FungibleToken.Withdraw) &FlowToken.Vault>(from: flowTokenStoragePath)
            ?? panic("cannot borrow auth(FT.Withdraw) reference to FlowToken Vault")
        self.liquidatorAddr = signer.address

        self.informVault <- signer.storage.borrow<auth(FungibleToken.Withdraw) &{FungibleToken.Vault}>(from: /storage/flowTokenVault)!.withdraw(amount: 0.00000001)
    }

    execute {
        let inUnderlyingVault <- self.flowTokenVault.withdraw(amount: amountLiquidate)
        // liquidate
        let leftVault <- LendingPool.liquidate(
            liquidator: self.liquidatorAddr,
            borrower: borrower,
            poolCollateralizedToSeize: seizePoolAddr,
            repayUnderlyingVault: <-inUnderlyingVault
        )
        if leftVault != nil {
            self.flowTokenVault.deposit(from: <-leftVault!)
        } else {
            destroy leftVault
        }

        // inform
        let flowTokenReceiverRef = getAccount(borrower).capabilities.borrow<&{FungibleToken.Receiver}>(/public/flowTokenReceiver)!
        flowTokenReceiverRef.deposit(from: <-self.informVault)
    }
}
```