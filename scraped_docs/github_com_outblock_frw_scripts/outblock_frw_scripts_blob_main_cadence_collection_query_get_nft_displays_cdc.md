# Source: https://github.com/Outblock/FRW-scripts/blob/main/cadence/collection/query/get_nft_displays.cdc

```
import NonFungibleToken from 0xNonFungibleToken
import MetadataViews from 0xMetadataViews
import ViewResolver from 0xMetadataViews

access(all) struct ViewInfo {
  access(all) let name: String
  access(all) let description: String
  access(all) let thumbnail: {MetadataViews.File}
  access(all) let rarity: String?
  access(all) let collectionDisplay: MetadataViews.NFTCollectionDisplay?

  init(name: String, description: String, thumbnail: {MetadataViews.File}, rarity: String?, collectionDisplay: MetadataViews.NFTCollectionDisplay?) {
    self.name = name
    self.description = description
    self.thumbnail = thumbnail
    self.rarity = rarity
    self.collectionDisplay = collectionDisplay
  }
}

access(all) fun main(address: Address, pathID: String, tokenIDs: [UInt64]): {UInt64: ViewInfo} {
  let account = getAccount(address)
  let res: {UInt64: ViewInfo} = {}
  var collectionDisplayFetched = false

  if tokenIDs.length == 0 {
    return res
  }

  let storagePath = StoragePath(identifier: pathID)!
  let publicPath = PublicPath(identifier: pathID)!
  let type = account.storage.type(at: storagePath)
  if type == nil {
    return res
  }

  let metadataViewType = Type<@{ViewResolver.ResolverCollection}>()

  let conformedMetadataViews = type!.isSubtype(of: metadataViewType)
  if !conformedMetadataViews {
    for tokenID in tokenIDs {
      res[tokenID] = ViewInfo(
        name: pathID,
        description: "",
        thumbnail: MetadataViews.HTTPFile(url: ""),
        rarity: nil,
        collectionDisplay: nil
      )
    }
    return res
  }

  let collectionRef = account.capabilities.borrow<&{ViewResolver.ResolverCollection, NonFungibleToken.Receiver}>(publicPath)
  for tokenID in tokenIDs {
    let resolver = collectionRef!.borrowViewResolver(id: tokenID)
    if resolver != nil {
      if let display = MetadataViews.getDisplay(resolver!) {
        var rarityDesc: String? = nil
        if let rarityView = MetadataViews.getRarity(resolver!) {
          rarityDesc = rarityView.description
        }

        var collectionDisplay: MetadataViews.NFTCollectionDisplay? = nil
        if (!collectionDisplayFetched) {
          if let cDisplay = MetadataViews.getNFTCollectionDisplay(resolver!) {
            collectionDisplay = cDisplay
            collectionDisplayFetched = true
          }
        }

        res[tokenID] = ViewInfo(
          name: display.name,
          description: display.description,
          thumbnail: display.thumbnail,
          rarity: rarityDesc,
          collectionDisplay: collectionDisplay
        )
      }
    } else {
      res[tokenID] = ViewInfo(
        name: pathID,
        description: "",
        thumbnail: MetadataViews.HTTPFile(url: ""),
        rarity: nil,
        collectionDisplay: nil
      )
    }
  }
  return res
}
```