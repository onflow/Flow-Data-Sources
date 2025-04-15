# Source: https://github.com/Outblock/FRW-scripts/blob/main/scripts/src/cadence/hybridCustody/get_accessible_collection_and_ids_display.cdc

```
import HybridCustody from 0xHybridCustody
import MetadataViews from 0xMetadataViews
import ViewResolver from 0xMetadataViews
import FungibleToken from 0xFungibleToken
import NonFungibleToken from 0xNonFungibleToken


access(all) struct CollectionDisplay {
  access(all) let name: String
  access(all) let squareImage: MetadataViews.Media

  init(name: String, squareImage: MetadataViews.Media) {
    self.name = name
    self.squareImage = squareImage
  }
}

access(all) struct NFTCollection {
  access(all) let id: String
  access(all) let display: CollectionDisplay?
  access(all) let idList: [UInt64]

  init(id:String, display: CollectionDisplay?, idList: [UInt64]) {
    self.id = id
    self.display = display
    self.idList = idList
  }
}

access(all) fun getDisplay(address: Address, path: StoragePath): CollectionDisplay? {
  let account = getAuthAccount<auth(Storage, Capabilities) &Account>(address)

  let resourceType = Type<@AnyResource>()
  // let vaultType = Type<@{FungibleToken.Vault}>()
  let collectionType = Type<@{NonFungibleToken.Collection}>()
  let metadataViewType = Type<&{ViewResolver.ResolverCollection}>()
  var item: CollectionDisplay? =  nil

    if let type = account.storage.type(at: path) {
      let isResource = type.isSubtype(of: resourceType)
      let isNFTCollection = type.isSubtype(of: collectionType)
      let conformedMetadataViews = type.isSubtype(of: metadataViewType)

      var tokenIDs: [UInt64] = []
      if isNFTCollection && conformedMetadataViews {
        if let collectionRef = account.storage.borrow<&{ViewResolver.ResolverCollection, NonFungibleToken.CollectionPublic}>(from: path) {
          tokenIDs = collectionRef.getIDs()

          // TODO: move to a list
          if tokenIDs.length > 0 
          && path != /storage/RaribleNFTCollection 
          && path != /storage/ARTIFACTPackV3Collection
          && path != /storage/ArleeScene {
            let resolver = collectionRef.borrowViewResolver(id: tokenIDs[0])!
            if let display = MetadataViews.getNFTCollectionDisplay(resolver) {
              item = CollectionDisplay(
                name: display.name,
                squareImage: display.squareImage
              )
            }
          }
        }
      }
    }

  return item
}

access(all) fun main(parent: Address, childAccount: Address): [NFTCollection] {
    let manager =  getAuthAccount<auth(Storage) &Account>(parent).storage.borrow<auth(HybridCustody.Manage) &HybridCustody.Manager>(from: HybridCustody.ManagerStoragePath) ?? panic ("manager does not exist")

    // Address -> Collection Type -> ownedNFTs

    let providerType = Type<Capability<&{NonFungibleToken.Provider}>>()
    let collectionType: Type = Type<@{NonFungibleToken.CollectionPublic}>()

    // Iterate through child accounts

    let acct = getAuthAccount<auth(Storage, Capabilities) &Account>(childAccount)
    let foundTypes: [Type] = []
    let nfts: {String: [UInt64]} = {}
    let collectionList: [NFTCollection] = []
    let childAcct = manager.borrowAccount(addr: childAccount) ?? panic("child account not found")
    
    // get all private paths
    acct.storage.forEachStored(fun (path: StoragePath, type: Type): Bool {
        // Check which private paths have NFT Provider AND can be borrowed
        // if !type.isSubtype(of: providerType){
        //     return true
        // }
        // if let cap = childAcct.getCapability(path: path, type: Type<&{NonFungibleToken.Provider}>()) {
        //     let providerCap = cap as! Capability<&{NonFungibleToken.Provider}> 

        //     if !providerCap.check(){
        //         // if this isn't a provider capability, exit the account iteration function for this path
        //         return true
        //     }
        //     foundTypes.append(cap.borrow<&AnyResource>()!.getType())
        // }

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
            foundTypes.append(cap.borrow<&AnyResource>()!.getType())
          }
        }
        return true
    })

    // iterate storage, check if typeIdsWithProvider contains the typeId, if so, add to nfts
    acct.storage.forEachStored(fun (path: StoragePath, type: Type): Bool {

        if foundTypes == nil {
            return true
        }

        for idx, value in foundTypes {
            let value = foundTypes!

            if value[idx] != type {
                continue
            } else {
                if type.isInstance(collectionType) {
                    continue
                }
                if let collection = acct.storage.borrow<&{NonFungibleToken.CollectionPublic}>(from: path) { 
                    nfts.insert(key: type.identifier, collection.getIDs())
                    collectionList.append(
                      NFTCollection(
                        id: type.identifier,
                        display: getDisplay(address: childAccount, path: path),
                        idList: collection.getIDs()
                      )
                    )
                }
                continue
            }
        }
        return true
    })

    return collectionList
}
```