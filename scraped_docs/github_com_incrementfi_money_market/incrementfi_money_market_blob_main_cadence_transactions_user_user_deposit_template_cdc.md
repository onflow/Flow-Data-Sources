# Source: https://github.com/IncrementFi/Money-Market/blob/main/cadence/transactions/User/user_deposit_template.cdc

```
import FlowToken from "../../contracts/tokens/FlowToken.cdc"
import FungibleToken from "../../contracts/tokens/FungibleToken.cdc"
import LendingPool from "../../contracts/LendingPool.cdc"

transaction(amountDeposit: UFix64) {
    let flowTokenVault: auth(FungibleToken.Withdraw) &FlowToken.Vault
    let supplierAddress: Address

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
        self.supplierAddress = signer.address
    }

    execute {
        let inUnderlyingVault <- self.flowTokenVault.withdraw(amount: amountDeposit)
        LendingPool.supply(supplierAddr: self.supplierAddress, inUnderlyingVault: <-inUnderlyingVault)
    }
}
```