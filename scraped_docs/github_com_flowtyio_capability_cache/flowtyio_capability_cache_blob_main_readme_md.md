# Source: https://github.com/Flowtyio/capability-cache/blob/main/README.md

[![codecov](https://codecov.io/gh/Flowtyio/capability-cache/graph/badge.svg?token=8ZuYnUDlQD)](https://codecov.io/gh/Flowtyio/capability-cache)

# Capability Cache

## Overview

CapabilityCache is a contract that allows the storing and retrieval of capabilities.
Private paths are/were removed from Cadence with the launch of Crescendo, which presents
a challenge for platforms that want to keep the number of capabilities they issue
for their users to a minimum.

These platforms could choose to iterate over all controllers on a storage path they want
to have access to and choose one that matches their desired type, but that has a few challengnes:

- How do you know the capability you are using isn't slated to be removed by another platform
    when they no longer need it?
- What if there are so many capabilities issued to an existing storage path that iteration over it isn't possible?
- How does a platform know which capabilities they issued without having to build complex indexing?

Some of these can be fixed without a contract solution like this one. For instance, a platform could choose to
store a controller id or the issued Capability itself into storage in a way that can be looked up as needed.
This can work, but is overhead that can be offloaded to a contract.

The @CapabilityCache.Cache resource is given a namespace which it should be stored in (though there is no way to guarantee this),
which allows every platform to make their own cache and manage the capabilities that they issue for their users. This also makes it fairly easy
to tell what capabilities belong to what platform. If the cache is used, all a user or ecosystem tool would need to do is look at each
stored @Cache resource and iterate through the types and capabilities that they've stored.

## Usage

### Initialize Cache

In order to make a cache, you need to give it a namespace. This is done to encourage each platform to maintain their
own cache.

**NOTE: There is no way to ensure that someone else won't take a platform's typical cache namespace**

```cadence
import "CapabilityCache"

transaction(namespace: String) {
    prepare(acct: auth(Storage) &Account) {
        let s = CapabilityCache.getPathForCache(namespace)
        if acct.storage.borrow<&CapabilityCache.Cache>(from: s) == nil {
            let c <- CapabilityCache.createCache(namespace: namespace)
            acct.storage.save(<-c, to: s)
        }
    }
}
```

### Add Capability to Cache

```cadence
import "CapabilityCache"

transaction(namespace: String, resourceType: Type, capabilityBorrowType: Type, path: StoragePath) {
    prepare(acct: auth(SaveValue, BorrowValue, IssueStorageCapabilityController) &Account) {
        let s = CapabilityCache.getPathForCache(namespace)
        if acct.storage.borrow<&CapabilityCache.Cache>(from: s) == nil {
            let c <- CapabilityCache.createCache(namespace: namespace)
            acct.storage.save(<-c, to: s)
        }

        let cache = acct.storage.borrow<auth(CapabilityCache.Add) &CapabilityCache.Cache>(from: s)
            ?? panic("capability cache was not found")

        let cap = acct.capabilities.storage.issueWithType(path, type: capabilityBorrowType)
        cache.addCapability(resourceType: resourceType, cap: cap)
    }
}
```

### Retrieve FT Provider Capability from Cache
```cadence
import "CapabilityCache"
import "FungibleToken"
import "FlowToken"

transaction(namespace: String) {
    prepare(acct: auth(BorrowValue) &Account) {
        let capType = Type<auth(FungibleToken.Withdraw) &{FungibleToken.Provider}>()

        let s = CapabilityCache.getPathForCache(namespace)
        let cache = acct.storage.borrow<auth(CapabilityCache.Get) &CapabilityCache.Cache>(from: s)
            ?? panic("cache not found in storage")
        let cap = cache.getCapabilityByType(resourceType: Type<@FlowToken.Vault>(), capabilityType: CapabilityType(capType)!)
            ?? panic("capability not found with provided type")
        let casted = cap as! Capability<auth(FungibleToken.Withdraw) &{FungibleToken.Provider}>
        casted.borrow() ?? panic("failed to borrow provider capability")
    }
}
```

### Remove Capability from Cache

```cadence
import "CapabilityCache"

transaction(namespace: String, resourceType: Type, capabilityBorrowType: Type) {
    prepare(acct: auth(BorrowValue) &Account) {
        let s = CapabilityCache.getPathForCache(namespace)
        let cache = acct.storage.borrow<auth(CapabilityCache.Delete) &CapabilityCache.Cache>(from: s)
            ?? panic("cache not found in storage")

        cache.removeCapabilityByType(resourceType: resourceType, capabilityType: CapabilityType(capabilityBorrowType)!)
    }
}
```