# Source: https://github.com/onflow/nft-storefront/blob/main/contracts/hybrid-custody/factories/NFTProviderAndCollectionFactory.cdc

```
import "CapabilityFactory"
import "NonFungibleToken"

pub contract NFTProviderAndCollectionFactory {
    pub struct Factory: CapabilityFactory.Factory {
        pub fun getCapability(acct: &AuthAccount, path: CapabilityPath): Capability {
            return acct.getCapability<&{NonFungibleToken.Provider, NonFungibleToken.CollectionPublic}>(path)
        }
    }
}
```