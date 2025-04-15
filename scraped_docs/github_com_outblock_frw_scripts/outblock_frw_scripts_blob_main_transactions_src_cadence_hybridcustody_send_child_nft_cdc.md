# Source: https://github.com/Outblock/FRW-scripts/blob/main/transactions/src/cadence/hybridCustody/send_child_nft.cdc

```
import HybridCustody from 0xHybridCustody
import CapabilityFilter from 0xHybridCustody
import NonFungibleToken from 0xNonFungibleToken
import MetadataViews from 0xMetadataViews

import <NFT> from <NFTAddress>


transaction(childAddr: Address, receiver: Address, identifier: String, id: UInt64) {
  prepare(signer: auth(Storage) &Account) {
    // signer is the parent account
    // get the manager resource and borrow childAccount
    let m = signer.storage.borrow<auth(HybridCustody.Manage) &HybridCustody.Manager>(from: HybridCustody.ManagerStoragePath)
        ?? panic("manager does not exist")
    let childAcct = m.borrowAccount(addr: childAddr) ?? panic("child account not found")
    
    let collectionData = <NFT>.resolveContractView(resourceType: nil, viewType: Type<MetadataViews.NFTCollectionData>()) as! MetadataViews.NFTCollectionData?
        ?? panic("Could not get the vault data view for <NFT> ")

    //get Ft cap from child account
    let capType = Type<auth(NonFungibleToken.Withdraw) &{NonFungibleToken.Provider}>()
    let controllerID = childAcct.getControllerIDForType(type: capType, forPath: collectionData.storagePath)
        ?? panic("no controller found for capType")
    
    let cap = childAcct.getCapability(controllerID: controllerID, type: capType) ?? panic("no cap found")
    let providerCap = cap as! Capability<auth(NonFungibleToken.Withdraw) &{NonFungibleToken.Provider}>
    assert(providerCap.check(), message: "invalid provider capability")
    
    // Get a reference to the child's stored vault
    let collectionRef = providerCap.borrow()!

    // Withdraw tokens from the signer's stored vault
    let nft <- collectionRef.withdraw(withdrawID: id)
    let receiverAcc = getAccount(receiver)
    let receiverRef =  receiverAcc.capabilities.get<&{NonFungibleToken.Receiver}>(collectionData.publicPath)!.borrow()
    ?? panic("Could not borrow receiver reference to the recipient's Vault")
    
    receiverRef.deposit(token: <- nft)
  }
}
```