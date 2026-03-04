# Source: https://github.com/Flowtyio/capability-cache/blob/main/contracts/CapabilityCache.cdc

```
/*
https://github.com/Flowtyio/capability-cache

CapabilityCache helps manage capabilities which are issued but are not in public paths.
Rather than looping through all capabilities under a storage path and finding one that 
matches the Capability type you want, the cache can be used to retrieve them
*/
access(all) contract CapabilityCache {

    access(all) let basePathIdentifier: String

    access(all) event CapabilityAdded(owner: Address?, cacheUuid: UInt64, namespace: String, resourceType: Type, capabilityType: Type, capabilityID: UInt64)
    access(all) event CapabilityRemoved(owner: Address?, cacheUuid: UInt64, namespace: String, resourceType: Type, capabilityType: Type, capabilityID: UInt64)

    // Add to a namespace
    access(all) entitlement Add

    // Remove from a namespace
    access(all) entitlement Delete

    // Retrieve a cap from the namespace
    access(all) entitlement Get

    // Resource that manages capabilities for a provided namespace. Only one capability is permitted per type.
    access(all) resource Cache {
        // A dictionary of resourceType -> CapabilityType -> Capability
        // For example, one might store a Capability<auth(NonFungibleToken.Withdraw) &{NonFungibleToken.Collection}> for the @TopShot.NFT resource.
        // Note that the resource type is not necessarily the type that the borrowed capability is an instance of. This is because some resource definitions
        // might be reused.
        access(self) let caps: {Type: {Type: Capability}}

        // who is this capability cache maintained by? e.g. flowty, dapper, find? 
        access(all) let namespace: String

        // Remove a capability, if it exists, 
        access(Delete) fun removeCapabilityByType(resourceType: Type, capabilityType: Type): Capability? {
            if let ref = &self.caps[resourceType] as auth(Mutate) &{Type: Capability}? {
                let cap = ref.remove(key: capabilityType)
                if cap != nil {
                    emit CapabilityRemoved(owner: self.owner?.address, cacheUuid: self.uuid, namespace: self.namespace, resourceType: resourceType, capabilityType: capabilityType, capabilityID: cap!.id)
                }
            }

            return nil
        }

        // Adds a capability to the cache. If there is already an entry for the given type,
        // it will be returned
        access(Add) fun addCapability(resourceType: Type, cap: Capability): Capability? {
            pre {
                cap.id != 0: "cannot add a capability with id 0"
            }

            let capType = cap.getType()
            emit CapabilityAdded(owner: self.owner?.address, cacheUuid: self.uuid, namespace: self.namespace, resourceType: resourceType, capabilityType: capType, capabilityID: cap.id)
            if let ref = &self.caps[resourceType] as auth(Mutate) &{Type: Capability}? {
                return ref.insert(key: capType, cap)
            }

            self.caps[resourceType] = {
                capType: cap
            }

            return nil
        }

        // Retrieve a capability key'd by a given type.
        access(Get) fun getCapabilityByType(resourceType: Type, capabilityType: Type): Capability? {
            if let tmp = self.caps[resourceType] {
                return tmp[capabilityType]
            }

            return nil
        }

        init(namespace: String) {
            self.caps = {}

            self.namespace = namespace
        }
    }

    // There is no uniform storage path for the Capability Cache. Instead, each platform which issues capabilities
    // should manage their own cache, and can generate the storage path to store it in with this helper method
    access(all) fun getPathForCache(_ namespace: String): StoragePath {
        return StoragePath(identifier: self.basePathIdentifier.concat(namespace))
            ?? panic("invalid namespace value")
    }

    access(all) fun createCache(namespace: String): @Cache {
        return <- create Cache(namespace: namespace)
    }

    init() {
        self.basePathIdentifier = "CapabilityCache_".concat(self.account.address.toString()).concat("_")
    }
}
```