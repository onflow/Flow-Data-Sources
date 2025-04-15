# Source: https://github.com/onflow/nft-storefront/blob/main/contracts/hybrid-custody/factories/NFTProviderFactory.cdc

```
import "CapabilityFactory"
import "NonFungibleToken"

pub contract NFTProviderFactory {
    pub struct Factory: CapabilityFactory.Factory {
        pub fun getCapability(acct: &AuthAccount, path: CapabilityPath): Capability {
            return acct.getCapability<&{NonFungibleToken.Provider}>(path)
        }
    }
}
```