# Source: https://github.com/Outblock/FRW-scripts/blob/main/scripts/src/cadence/hybridCustody/check_child_linked_collections.cdc

```
import HybridCustody from 0xHybridCustody
import CapabilityFilter from 0xHybridCustody
import NonFungibleToken from 0xNonFungibleToken

access(all) fun main(parent: Address, child: Address, identifier: String): Bool {
    let mgr = getAuthAccount(parent).borrow<&HybridCustody.Manager>(from: HybridCustody.ManagerStoragePath)
        ?? panic("Could not borrow manager from parent")
    let child = mgr.borrowAccount(addr: child) ?? panic("Child account not found")

    let cap = child.getCapability(
            path: PrivatePath(identifier: identifier)! as CapabilityPath,
            type: Type<&{NonFungibleToken.Provider, NonFungibleToken.CollectionPublic}>()
        ) as! Capability<&{NonFungibleToken.Provider, NonFungibleToken.CollectionPublic}>?

    
    return cap != nil
}   
    
```