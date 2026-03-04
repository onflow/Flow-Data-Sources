# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/bbxb/scripts/global_account_caps.cdc

```
// DEPRECATED
import "NonFungibleToken"
import "FungibleToken"
import "MetadataViews"


access(all) fun main(addr: Address): {String: AnyStruct} {
  let acct: &Account = getAccount(addr)
  let ret: {String: AnyStruct} = {}
  ret["capacity"] = acct.storage.capacity
  ret["used"] = acct.storage.used
  ret["available"]  = 0
  if acct.storage.capacity>acct.storage.used{
    ret["available"] = acct.storage.capacity - acct.storage.used
  }
    var s : [Path] = []
    var pu : [Path] = []
    var pr : [Path] = []
    var nft : [{String:AnyStruct}] = []
    var ft : [{String:AnyStruct}] = []

    getAuthAccount(addr).forEachStored(fun (path: StoragePath, type: Type): Bool {
      for banned in ["MusicBlockCollection", "FantastecNFTCollection","ZayTraderCollection","jambbLaunchCollectiblesCollection","LibraryPassCollection","RaribleNFTCollection"]{
      if path==StoragePath(identifier: banned){
          return true
      }}
      
      if type.isSubtype(of: Type<@{NonFungibleToken.Collection}>()){
        var collection = getAuthAccount(addr).borrow<&NonFungibleToken.Collection>(from:path)!
        nft.append({"path":path, "count":collection.getIDs().length})
      }
      else if type.isSubtype(of: Type<@{FungibleToken.Vault}>()){
        var vault = getAuthAccount(addr).borrow<&FungibleToken.Vault>(from:path)!
        ft.append({"path":path, "balance":vault.balance})
      }
      else{
        s.append(path)
      }
      return true
    })
    getAuthAccount(addr).forEachPublic(fun (path: PublicPath, type: Type): Bool {
      pu.append(path)
      return true
    })
    getAuthAccount(addr).forEachPrivate(fun (path: PrivatePath, type: Type): Bool {
      pr.append(path)
      return true
    })
  ret["paths"] = s
  ret["public"] = pu
  ret["private"] = pr
  ret["nft"] = nft
  ret["ft"] = ft

  //find profile
  var findProfile = getAuthAccount(addr).borrow<&AnyResource>(from:/storage/findProfile)
  ret["find"] = findProfile

  return ret
}
```