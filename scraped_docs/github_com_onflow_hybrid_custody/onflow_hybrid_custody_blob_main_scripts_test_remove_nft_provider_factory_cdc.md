# Source: https://github.com/onflow/hybrid-custody/blob/main/scripts/test/remove_nft_provider_factory.cdc

```
import "CapabilityFactory"
import "NFTProviderFactory"

import "NonFungibleToken"

access(all) fun main(address: Address): Bool {
    
    let managerRef = getAuthAccount<auth(Storage) &Account>(address).storage.borrow<auth(CapabilityFactory.Delete) &CapabilityFactory.Manager>(from: CapabilityFactory.StoragePath)
        ?? panic("CapabilityFactory Manager not found")
    
    let expectedType = Type<NFTProviderFactory.Factory>()
    
    if let removed = managerRef.removeFactory(Type<auth(NonFungibleToken.Withdraw) &{NonFungibleToken.Provider}>()) {
        return removed.getType() == expectedType
    }

    return false
}
```