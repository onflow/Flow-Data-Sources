# Source: https://github.com/Outblock/FRW-scripts/blob/main/scripts/src/cadence/hybridCustody/check_child_recieve_vaults.cdc

```
import HybridCustody from 0xHybridCustody
import CapabilityFilter from 0xHybridCustody
import FungibleToken from 0xFungibleToken

access(all) fun main(parent: Address, child: Address, path: String): Bool {
  let account = getAuthAccount<auth(Storage) &Account>(parent)
  let manager = getAuthAccount<auth(Storage) &Account>(parent).storage.borrow<auth(HybridCustody.Manage) &HybridCustody.Manager>(from: HybridCustody.ManagerStoragePath) ?? panic ("manager does not exist")
  
  let receiverType = Type<&{FungibleToken.Receiver}>()

  let addr = getAuthAccount<auth(Storage, Capabilities) &Account>(child)
  
  let childAcct = manager.borrowAccount(addr: child) ?? panic("child account not found")

  let controllers = addr.capabilities.storage.getControllers(forPath: StoragePath(identifier: path)!)
  var flag = false

  for c in controllers {
    if !c.borrowType.isSubtype(of: receiverType) {
      continue
    }

    if let cap = childAcct.getCapability(controllerID: c.capabilityID, type: receiverType) {
      let providerCap = cap as! Capability<&{FungibleToken.Receiver}> 

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