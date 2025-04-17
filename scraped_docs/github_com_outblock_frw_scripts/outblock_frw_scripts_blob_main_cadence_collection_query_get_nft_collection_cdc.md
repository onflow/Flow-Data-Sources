# Source: https://github.com/Outblock/FRW-scripts/blob/main/cadence/collection/query/get_nft_collection.cdc

```
import NonFungibleToken from 0xNonFungibleToken
import MetadataViews from 0xMetadataViews
import ViewResolver from 0xMetadataViews


access(all) struct CollectionDisplay {
  access(all) let name: String
  access(all) let squareImage: String
  access(all) let mediaType: String

  init(name: String, squareImage: String, mediaType: String) {
    self.name = name
    self.squareImage = squareImage
    self.mediaType = mediaType
  }
}

access(all) struct NFTCollection {
  access(all) let id: String
  access(all) let path: String
  access(all) let display: CollectionDisplay?
  access(all) let idList: [UInt64]

  init(id:String, path: String, display: CollectionDisplay?, idList: [UInt64]) {
    self.id = id
    self.path = path
    self.display = display
    self.idList = idList
  }
}

access(all) fun getDisplay(address: Address, storagePath: StoragePath, publicPath: PublicPath): CollectionDisplay? {
  let account = getAccount(address)
  let resourceType = Type<@AnyResource>()
  let collectionType = Type<@{NonFungibleToken.Collection}>()
  let metadataViewType = Type<@{ViewResolver.ResolverCollection}>()
  var item: CollectionDisplay? = nil

  if let type = account.storage.type(at: storagePath) {
    let isResource = type.isSubtype(of: resourceType)
    let isNFTCollection = type.isSubtype(of: collectionType)
    let conformedMetadataViews = type.isSubtype(of: metadataViewType)

    var tokenIDs: [UInt64] = []
    if isNFTCollection && conformedMetadataViews {
      if let collectionRef = account.capabilities.borrow<&{ViewResolver.ResolverCollection, NonFungibleToken.Receiver}>(publicPath) {
        tokenIDs = collectionRef.getIDs()

        // TODO: move to a list
        if tokenIDs.length > 0 {
          let resolver = collectionRef.borrowViewResolver(id: tokenIDs[0])
          if resolver != nil {
            if let display = MetadataViews.getNFTCollectionDisplay(resolver!) {
              item = CollectionDisplay(
                name: display.name,
                squareImage: display.squareImage.file.uri(),
                mediaType: display.squareImage.mediaType
              )
            }
          }
        }
      }
    }
  }

  return item
}


access(all) fun main(address: Address, pathID: String): NFTCollection {
  let account = getAccount(address)
  let storagePath = StoragePath(identifier: pathID)!
  let publicPath = PublicPath(identifier: pathID)!
  let collection = account.capabilities.borrow<&{ViewResolver.ResolverCollection}>(publicPath)!
  return NFTCollection(
    id: account.storage.type(at: storagePath)!.identifier,
    path: storagePath.toString(),
    display: getDisplay(address: address, storagePath: storagePath, publicPath: publicPath),
    idList: collection.getIDs()
  )
}
```