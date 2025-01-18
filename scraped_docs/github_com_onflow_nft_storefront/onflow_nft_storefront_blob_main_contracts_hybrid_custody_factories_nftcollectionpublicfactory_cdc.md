# Source: https://github.com/onflow/nft-storefront/blob/main/contracts/hybrid-custody/factories/NFTCollectionPublicFactory.cdc

```
import "CapabilityFactory"
import "NonFungibleToken"

pub contract NFTCollectionPublicFactory {
    pub struct Factory: CapabilityFactory.Factory {
        pub fun getCapability(acct: &AuthAccount, path: CapabilityPath): Capability {
            return acct.getCapability<&{NonFungibleToken.CollectionPublic}>(path)
        }
    }
}
```