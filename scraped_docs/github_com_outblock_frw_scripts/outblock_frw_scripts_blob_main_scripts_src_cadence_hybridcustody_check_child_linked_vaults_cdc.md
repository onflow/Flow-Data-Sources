# Source: https://github.com/Outblock/FRW-scripts/blob/main/scripts/src/cadence/hybridCustody/check_child_linked_vaults.cdc

```
import HybridCustody from 0xHybridCustody
import CapabilityFilter from 0xCapabilityFilter
import FungibleToken from 0xFungibleToken

access(all) fun main(parent: Address, child: Address, path: String): Bool {
  let account = getAuthAccount<auth(Storage) &Account>(parent)
  let manager = getAuthAccount<auth(Storage) &Account>(parent).storage.borrow<auth(HybridCustody.Manage) &HybridCustody.Manager>(from: HybridCustody.ManagerStoragePath) ?? panic ("manager does not exist")
  
  let providerType = Type<auth(FungibleToken.Withdraw) &{FungibleToken.Provider}>()

  let addr = getAuthAccount<auth(Storage, Capabilities) &Account>(child)
  
  let childAcct = manager.borrowAccount(addr: child) ?? panic("child account not found")

  let controllers = addr.capabilities.storage.getControllers(forPath: StoragePath(identifier: path)!)
  var flag = false

  for c in controllers {
    if !c.borrowType.isSubtype(of: providerType) {
      continue
    }

    if let cap = childAcct.getCapability(controllerID: c.capabilityID, type: providerType) {
      let providerCap = cap as! Capability<&{FungibleToken.Provider}> 

      if !providerCap.check(){
        continue
      }

      flag = true
      break
    }
  }

  return flag
} 
    
```