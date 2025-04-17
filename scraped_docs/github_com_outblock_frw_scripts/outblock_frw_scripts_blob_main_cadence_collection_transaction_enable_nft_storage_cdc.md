# Source: https://github.com/Outblock/FRW-scripts/blob/main/cadence/collection/transaction/enable_nft_storage.cdc

```
import NonFungibleToken from 0xNonFungibleToken
import MetadataViews from 0xMetadataViews
import <NFT> from <NFTAddress>

transaction {
  prepare(signer: auth(Capabilities, SaveValue) &Account) {
    if signer.capabilities.borrow<&<NFT>.Collection>(<CollectionPublicPath>) == nil {
      let collection <- <NFT>.createEmptyCollection(nftType: Type<@<NFT>.NFT>())
      signer.storage.save(<-collection, to: <CollectionStoragePath>)
    }
    if (signer.capabilities.borrow<&<NFT>.Collection>(<CollectionPublicPath>) == nil) {
      signer.capabilities.unpublish(<CollectionPublicPath>)
      let cap = signer.capabilities.storage.issue<&<NFT>.Collection>(<CollectionStoragePath>)            
      signer.capabilities.publish(cap, at: <CollectionPublicPath>)
    }
  }
}
```