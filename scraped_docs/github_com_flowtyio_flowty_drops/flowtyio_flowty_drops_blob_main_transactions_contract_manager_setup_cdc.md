# Source: https://github.com/Flowtyio/flowty-drops/blob/main/transactions/contract-manager/setup.cdc

```
import "ContractManager"
import "FlowToken"
import "FungibleToken"
import "HybridCustody"
import "ViewResolver"

transaction(flowTokenAmount: UFix64) {
    prepare(acct: auth(Storage, Capabilities, Inbox) &Account) {
        let v = acct.storage.borrow<auth(FungibleToken.Withdraw) &FlowToken.Vault>(from: /storage/flowTokenVault)!
        let tokens <- v.withdraw(amount: flowTokenAmount) as! @FlowToken.Vault

        acct.storage.save(<- ContractManager.createManager(tokens: <-tokens, defaultRouterAddress: acct.address), to: ContractManager.StoragePath)
        let contractManager = acct.storage.borrow<auth(ContractManager.Manage) &ContractManager.Manager>(from: ContractManager.StoragePath)!
        contractManager.onSave()

        // there is a published hybrid custody capability to redeem
        if acct.storage.borrow<&HybridCustody.Manager>(from: HybridCustody.ManagerStoragePath) == nil {
            let m <- HybridCustody.createManager(filter: nil)
            acct.storage.save(<- m, to: HybridCustody.ManagerStoragePath)

            for c in acct.capabilities.storage.getControllers(forPath: HybridCustody.ManagerStoragePath) {
                c.delete()
            }

            acct.capabilities.unpublish(HybridCustody.ManagerPublicPath)

            acct.capabilities.publish(
                acct.capabilities.storage.issue<&{HybridCustody.ManagerPublic}>(HybridCustody.ManagerStoragePath),
                at: HybridCustody.ManagerPublicPath
            )

            acct.capabilities.storage.issue<auth(HybridCustody.Manage) &{HybridCustody.ManagerPrivate, HybridCustody.ManagerPublic}>(HybridCustody.ManagerStoragePath)
        }

        let inboxName = HybridCustody.getChildAccountIdentifier(acct.address)
        let cap = acct.inbox.claim<auth(HybridCustody.Child) &{HybridCustody.AccountPrivate, HybridCustody.AccountPublic, ViewResolver.Resolver}>(inboxName, provider: contractManager.getAccount().address)
            ?? panic("child account cap not found")

        let manager = acct.storage.borrow<auth(HybridCustody.Manage) &HybridCustody.Manager>(from: HybridCustody.ManagerStoragePath)
            ?? panic("manager no found")
        manager.addAccount(cap: cap)
    }
}
```