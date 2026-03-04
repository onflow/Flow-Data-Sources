# Source: https://github.com/IncrementFi/Money-Market/blob/main/cadence/transactions/User/user_repay_template.cdc

```
import FlowToken from "../../contracts/tokens/FlowToken.cdc"
import FungibleToken from "../../contracts/tokens/FungibleToken.cdc"
import LendingPool from "../../contracts/LendingPool.cdc"
import LendingInterfaces from "../../contracts/LendingInterfaces.cdc"
import LendingConfig from "../../contracts/LendingConfig.cdc"

transaction(amount: UFix64) {
    let flowTokenVault: auth(FungibleToken.Withdraw) &FlowToken.Vault
    let borrowerAddress: Address

    prepare(signer: auth(Storage, Capabilities) &Account) {
        let flowTokenStoragePath = /storage/flowTokenVault
        if (signer.storage.borrow<&FlowToken.Vault>(from: flowTokenStoragePath) == nil) {
            signer.storage.save(<-FlowToken.createEmptyVault(vaultType: Type<@FlowToken.Vault>()), to: flowTokenStoragePath)
            signer.capabilities.publish(
                signer.capabilities.storage.issue<&{FungibleToken.Receiver}>(flowTokenStoragePath),
                at: /public/flowTokenReceiver
            )
            signer.capabilities.publish(
                signer.capabilities.storage.issue<&{FungibleToken.Balance}>(flowTokenStoragePath),
                at: /public/flowTokenBalance
            )
        }
        self.flowTokenVault = signer.storage.borrow<auth(FungibleToken.Withdraw) &FlowToken.Vault>(from: flowTokenStoragePath)
            ?? panic("cannot borrow auth(FT.Withdraw) reference to FlowToken Vault")
        self.borrowerAddress = signer.address
    }

    execute {
        var amountRepay = amount
        if amountRepay == UFix64.max {
            // accrueInterest() to update with latest pool states used to calculate borrowBalance
            LendingPool.accrueInterest()
            let totalRepayScaled = LendingPool.borrowBalanceSnapshotScaled(borrowerAddress: self.borrowerAddress)
            amountRepay = LendingConfig.ScaledUInt256ToUFix64(totalRepayScaled) + 1.0/LendingConfig.ufixScale
        }

        let inUnderlyingVault <- self.flowTokenVault.withdraw(amount: amountRepay)
        let leftVault <- LendingPool.repayBorrow(borrower: self.borrowerAddress, repayUnderlyingVault: <-inUnderlyingVault)
        if leftVault != nil {
            self.flowTokenVault.deposit(from: <-leftVault!)
        } else {
            destroy leftVault
        }
    }
}
```