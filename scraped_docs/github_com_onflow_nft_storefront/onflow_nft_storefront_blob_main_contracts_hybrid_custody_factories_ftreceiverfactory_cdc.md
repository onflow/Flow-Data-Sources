# Source: https://github.com/onflow/nft-storefront/blob/main/contracts/hybrid-custody/factories/FTReceiverFactory.cdc

```
import "CapabilityFactory"
import "FungibleToken"

pub contract FTReceiverFactory {
    pub struct Factory: CapabilityFactory.Factory {
        pub fun getCapability(acct: &AuthAccount, path: CapabilityPath): Capability {
            return acct.getCapability<&{FungibleToken.Receiver}>(path)
        }
    }
}
```