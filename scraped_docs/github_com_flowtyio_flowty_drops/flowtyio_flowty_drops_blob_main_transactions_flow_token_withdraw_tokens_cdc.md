# Source: https://github.com/Flowtyio/flowty-drops/blob/main/transactions/flow-token/withdraw_tokens.cdc

```
import "FlowToken"
import "FungibleToken"
import "HybridCustody"
import "ContractManager"
import "FungibleTokenMetadataViews"

transaction(amount: UFix64, childAddr: Address, controllerID: UInt64) {
    prepare(acct: auth(Storage, Capabilities) &Account) {
        let manager = acct.storage.borrow<auth(HybridCustody.Manage) &HybridCustody.Manager>(from: HybridCustody.ManagerStoragePath)
            ?? panic("hybrid custody manager not found")

        let child = manager.borrowAccount(addr: childAddr)
            ?? panic("child account not found")

        let cap = child.getCapability(controllerID: controllerID, type: Type<auth(FungibleToken.Withdraw) &{FungibleToken.Provider}>()) ?? panic("capability count not be borrowed")
        let providerCap = cap as! Capability<auth(FungibleToken.Withdraw) &{FungibleToken.Provider}>
        let vault = providerCap.borrow() ?? panic("vault count not be borrowed")
        let tokens <- vault.withdraw(amount: amount)

        let ftVaultData = tokens.resolveView(Type<FungibleTokenMetadataViews.FTVaultData>())! as! FungibleTokenMetadataViews.FTVaultData
        
        if acct.storage.type(at: ftVaultData.storagePath) == nil {
            acct.storage.save(<- ftVaultData.createEmptyVault(), to: ftVaultData.storagePath)
        }

        acct.storage.borrow<&{FungibleToken.Vault}>(from: ftVaultData.storagePath)!.deposit(from: <-tokens)
    }
}
```