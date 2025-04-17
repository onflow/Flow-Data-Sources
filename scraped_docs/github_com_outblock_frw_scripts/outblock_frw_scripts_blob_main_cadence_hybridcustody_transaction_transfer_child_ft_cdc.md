# Source: https://github.com/Outblock/FRW-scripts/blob/main/cadence/hybridCustody/transaction/transfer_child_ft.cdc

```
import HybridCustody from 0xHybridCustody

// HC-owned imports
import CapabilityFactory from 0xHybridCustody
import CapabilityFilter from 0xHybridCustody

import FungibleToken from 0xFungibleToken
import <Token> from <TokenAddress>



transaction(address: Address, path: String, amount: UFix64 ) {

  prepare(signer: auth(Storage) &Account) {
    // signer is the parent account
    // get the manager resource and borrow childAccount
    let m = signer.storage.borrow<auth(HybridCustody.Manage) &HybridCustody.Manager>(from: HybridCustody.ManagerStoragePath)
        ?? panic("manager does not exist")
    let childAcct = m.borrowAccount(addr: address) ?? panic("child account not found")
    
    let vaultData = <Token>.resolveContractView(resourceType: nil, viewType: Type<FungibleTokenMetadataViews.FTVaultData>()) as! FungibleTokenMetadataViews.FTVaultData?
        ?? panic("Could not get the vault data view for <Token> ")

    //get Ft cap from child account
    let capType = Type<auth(FungibleToken.Withdraw) &{FungibleToken.Provider}>()
    let controllerID = childAcct.getControllerIDForType(type: capType, forPath: vaultData.storagePath)
        ?? panic("no controller found for capType")
    
    let cap = childAcct.getCapability(controllerID: controllerID, type: capType) ?? panic("no cap found")
    let providerCap = cap as! Capability<auth(FungibleToken.Withdraw) &{FungibleToken.Provider}>
    assert(providerCap.check(), message: "invalid provider capability")
    
    // Get a reference to the child's stored vault
    let vaultRef = providerCap.borrow()!

    // Withdraw tokens from the signer's stored vault
    let paymentVault <- vaultRef.withdraw(amount: amount)
    let receiverRef =  signer.capabilities.get<&{FungibleToken.Receiver}>(vaultData.receiverPath)!.borrow()
    ?? panic("Could not borrow receiver reference to the recipient's Vault")
    receiverRef.deposit(from: <-paymentVault)
  }
}
```