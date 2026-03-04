# Source: https://github.com/IncrementFi/Money-Market/blob/main/cadence/transactions/User/user_borrow_template.cdc

```
import FlowToken from "../../contracts/tokens/FlowToken.cdc"
import FungibleToken from "../../contracts/tokens/FungibleToken.cdc"
import LendingPool from "../../contracts/LendingPool.cdc"
import LendingComptroller from "../../contracts/LendingComptroller.cdc"
import LendingConfig from "../../contracts/LendingConfig.cdc"
import LendingInterfaces from "../../contracts/LendingInterfaces.cdc"


transaction(amountBorrow: UFix64) {
    let flowTokenVault: &FlowToken.Vault
    let userCertificate: &{LendingInterfaces.IdentityCertificate}

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
        self.flowTokenVault = signer.storage.borrow<&FlowToken.Vault>(from: flowTokenStoragePath) ?? panic("cannot borrow reference to FlowToken Vault")

        // Get protocol-issued user certificate
        if (signer.storage.borrow<&{LendingInterfaces.IdentityCertificate}>(from: LendingConfig.UserCertificateStoragePath) == nil) {
            destroy <-signer.storage.load<@AnyResource>(from: LendingConfig.UserCertificateStoragePath)
            let userCertificate <- LendingComptroller.IssueUserCertificate()
            signer.storage.save(<-userCertificate, to: LendingConfig.UserCertificateStoragePath)
        }
        self.userCertificate = signer.storage.borrow<&{LendingInterfaces.IdentityCertificate}>(from: LendingConfig.UserCertificateStoragePath)
            ?? panic("cannot borrow reference to UserCertificate")
    }

    execute {
        let borrowVault <- LendingPool.borrow(userCertificate: self.userCertificate, borrowAmount: amountBorrow)
        self.flowTokenVault.deposit(from: <-borrowVault)
    }
}
```