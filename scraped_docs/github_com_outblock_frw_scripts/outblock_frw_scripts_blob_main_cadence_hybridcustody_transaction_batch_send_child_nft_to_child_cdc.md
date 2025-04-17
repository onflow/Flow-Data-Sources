# Source: https://github.com/Outblock/FRW-scripts/blob/main/cadence/hybridCustody/transaction/batch_send_child_nft_to_child.cdc

```
import HybridCustody from 0xHybridCustody
import CapabilityFilter from 0xHybridCustody
import NonFungibleToken from 0xNonFungibleToken
import MetadataViews from 0xMetadataViews
import <NFT> from <NFTAddress>


transaction(childAddr: Address, receiver: Address, identifier: String, ids: [UInt64]) {
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
    let collectionRef = providerCap.borrow()!


    let receiverChildAcct = m.borrowAccount(addr: receiver) ?? panic("child account not found")
    let receiverControllerId = receiverChildAcct.getControllerIDForType(type: capType, forPath: collectionData.storagePath)
        ?? panic("no controller found for capType")
    let receiverCap = receiverChildAcct.getCapability(controllerID: receiverControllerId, type: capType) ?? panic("no cap found") 
    let publicCap = receiverCap as! Capability<&{NonFungibleToken.CollectionPublic}>
    let receiverRef =  publicCap.borrow()!

    for id in ids {
      let nft <- collectionRef.withdraw(withdrawID: id)
      receiverRef.deposit(token: <- nft)
    }
  }
}
```