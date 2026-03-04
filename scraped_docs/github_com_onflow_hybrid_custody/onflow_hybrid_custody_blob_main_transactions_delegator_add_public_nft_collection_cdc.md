# Source: https://github.com/onflow/hybrid-custody/blob/main/transactions/delegator/add_public_nft_collection.cdc

```
import "CapabilityDelegator"

import "NonFungibleToken"
import "ExampleNFT"

transaction {
    prepare(acct: auth(BorrowValue) &Account) {
        let delegator = acct.storage.borrow<auth(CapabilityDelegator.Add) &CapabilityDelegator.Delegator>(from: CapabilityDelegator.StoragePath)
            ?? panic("delegator not found")

        let sharedCap 
            = acct.capabilities.get<&{ExampleNFT.ExampleNFTCollectionPublic, NonFungibleToken.CollectionPublic}>(ExampleNFT.CollectionPublicPath)
        delegator.addCapability(cap: sharedCap, isPublic: true)
    }
}
```