# Source: https://github.com/Outblock/FRW-scripts/blob/main/cadence/hybridCustody/query/get_accessible_child_account_nfts.cdc

```
import HybridCustody from 0xHybridCustody
import NonFungibleToken from 0xNonFungibleToken
import MetadataViews from 0xMetadataViews
import ViewResolver from 0xMetadataViews


access(all) fun main(addr: Address): AnyStruct {
  let manager = getAuthAccount<auth(Storage) &Account>(addr).storage.borrow<auth(HybridCustody.Manage) &HybridCustody.Manager>(from: HybridCustody.ManagerStoragePath) ?? panic ("manager does not exist")

  var typeIdsWithProvider = {} as {Address: [String]}

  // Address -> nft UUID -> Display
  var nftViews = {} as {Address: {String: [UInt64]}} 

  
  let providerType = Type<auth(NonFungibleToken.Withdraw) &{NonFungibleToken.Provider}>()
  let collectionType: Type = Type<@{NonFungibleToken.CollectionPublic}>()

  // Iterate through child accounts
  for address in manager.getChildAddresses() {
    let acct = getAuthAccount<auth(Storage, Capabilities) &Account>(address)
    let foundTypes: [String] = []
    let views: {String: [UInt64]} = {}
    let childAcct = manager.borrowAccount(addr: address) ?? panic("child account not found")
     
    // typeIdsWithProvider[address] = foundTypes

    acct.storage.forEachStored(fun (path: StoragePath, type: Type): Bool {

      let controllers = acct.capabilities.storage.getControllers(forPath: path!)
      for c in controllers {
        if !c.borrowType.isSubtype(of: providerType) {
          continue
        }

        if let cap = childAcct.getCapability(controllerID: c.capabilityID, type: providerType) {
          let providerCap = cap as! Capability<&{NonFungibleToken.Provider}> 

          if !providerCap.check(){
            continue
          }
          foundTypes.append(cap.borrow<&AnyResource>()!.getType().identifier)
        }
      }
      return true
    })

    typeIdsWithProvider[address] = foundTypes
    

    // iterate storage, check if typeIdsWithProvider contains the typeId, if so, add to views
    acct.storage.forEachStored(fun (path: StoragePath, type: Type): Bool {
      
      if typeIdsWithProvider[address] == nil {
        return true
      }

      for key in typeIdsWithProvider.keys {
        for idx, value in typeIdsWithProvider[key]! {
          let value = typeIdsWithProvider[key]!

          if value[idx] != type.identifier {
            continue
          } else {
            if type.isInstance(collectionType) {
              continue
            }
            if let collection = acct.storage.borrow<&{NonFungibleToken.CollectionPublic, ViewResolver.ResolverCollection}>(from: path) { 
              // Iterate over IDs & resolve the view
             
              for id in collection.getIDs() {
                let nft = collection.borrowNFT(id)!

                views[nft.getType().identifier] = collection.getIDs()
                break;
              }
            }
            continue
          }
        }
      }
      return true
    })
    nftViews[address] = views
  }
  return nftViews
}
```