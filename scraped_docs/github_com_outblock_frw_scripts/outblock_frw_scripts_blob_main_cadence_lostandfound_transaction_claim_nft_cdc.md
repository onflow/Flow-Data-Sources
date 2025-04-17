# Source: https://github.com/Outblock/FRW-scripts/blob/main/cadence/lostAndFound/transaction/claim_nft.cdc

```

import NonFungibleToken from 0xNonFungibleToken
import LostAndFound from 0xLostAndFound
import MetadataViews from 0xMetadataViews
import ViewResolver from 0xMetadataViews
import FlowEVMBridgeUtils from 0xFlowEVMBridge


transaction(nftIdentifier: String) {
  prepare(acct: auth(Storage, Capabilities) &Account) {
    let nftType = CompositeType(nftIdentifier)
      ?? panic("Could not construct NFT type from identifier: ".concat(nftIdentifier))
    let nftContractAddress = FlowEVMBridgeUtils.getContractAddress(fromType: nftType)
      ?? panic("Could not get contract address from identifier: ".concat(nftIdentifier))
    let nftContractName = FlowEVMBridgeUtils.getContractName(fromType: nftType)
      ?? panic("Could not get contract name from identifier: ".concat(nftIdentifier))

    let viewResolver = getAccount(nftContractAddress).contracts.borrow<&{ViewResolver}>(name: nftContractName)
      ?? panic("Could not borrow ViewResolver from NFT contract")
    let collectionData = viewResolver.resolveContractView(
        resourceType: nil,
        viewType: Type<MetadataViews.NFTCollectionData>()
      ) as! MetadataViews.NFTCollectionData? ?? panic("Could not resolve NFTCollectionData view")
    
    if acct.storage.borrow<&{NonFungibleToken.Collection}>(from: collectionData.storagePath) == nil {
      acct.storage.save(
        <- collectionData.createEmptyCollection(),
        to: collectionData.storagePath
      )
    }

    acct.capabilities.unpublish(collectionData.publicPath)
    acct.capabilities.publish(
      acct.capabilities.storage.issue<&{NonFungibleToken.Receiver, NonFungibleToken.CollectionPublic}>(collectionData.storagePath),
      at: collectionData.publicPath
    )
            
    let cap = acct.capabilities.get<&{NonFungibleToken.CollectionPublic}>(collectionData.publicPath)

    LostAndFound.redeemAll(type: nftType, max: nil, receiver: cap)
    acct.capabilities.storage.getController(byCapabilityID: cap.id)!.delete()
  }
}
```