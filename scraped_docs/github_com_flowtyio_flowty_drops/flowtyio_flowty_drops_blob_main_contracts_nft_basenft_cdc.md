# Source: https://github.com/Flowtyio/flowty-drops/blob/main/contracts/nft/BaseNFT.cdc

```
import "NonFungibleToken"
import "StringUtils"
import "AddressUtils"
import "ViewResolver"
import "MetadataViews"
import "BaseCollection"
import "FlowtyDrops"
import "NFTMetadata"
import "UniversalCollection"

// A few primary challenges that have come up in thinking about how to define base-level interfaces
// for collections and NFTs:
// 
// - How do we resolve contract-level interfaces?
// - How do we track total supply/serial numbers for NFTs?
// - How do we store traits and medias?
//
// For some of these, mainly contract-level interfaces, we might be able to simply consolidate
// all of these into one contract interface and require that collection display (banner, thumbnail, name, description, etc.)
// be stored at the top-level of the contract so that they can be easily referenced later. This could make things easier in that we can
// make a base definition for anyone to use, but since it isn't a concrete definition, anyone can later override the pre-generated
// pieces to and modify the code to their liking. This could achieve the best of both worlds where there is minimal work to get something
// off the ground, but doesn't close the door to customization in the future. This could come at the cost of duplicated resource definitions,
// or could have the risk of circular imports depending on how we resolve certain pieces of information about a collection.
access(all) contract interface BaseNFT: ViewResolver {
    access(all) resource interface NFT: NonFungibleToken.NFT {
        // This is the id entry that corresponds to an NFTs NFTMetadata.Container entry.
        // Some NFTs might share the same data, so we want to permit reusing storage where possible
        access(all) metadataID: UInt64

        access(all) view fun getViews(): [Type] {
            return [
                Type<MetadataViews.Display>(),
                Type<MetadataViews.Serial>(),
                Type<MetadataViews.Traits>(),
                Type<MetadataViews.Editions>(),
                Type<MetadataViews.ExternalURL>(),
                Type<MetadataViews.NFTCollectionData>(),
                Type<MetadataViews.NFTCollectionDisplay>()
            ]
        }

        // In case the implementor of `NFT` wants to override resolved views,
        // the actual logic to perform view resolution is done in another method,
        // with this one calling directly into it.
        access(all) fun resolveView(_ view: Type): AnyStruct? {
            return self._resolveView(view)
        }

        access(all) fun _resolveView(_ view: Type): AnyStruct? {
            if view == Type<MetadataViews.Serial>() {
                return MetadataViews.Serial(self.id)
            }

            let rt = self.getType()
            let segments = rt.identifier.split(separator: ".")
            let addr = AddressUtils.parseAddress(rt)!
            let tmp = getAccount(addr).contracts.borrow<&{BaseCollection}>(name: segments[2])
            if tmp == nil {
                return nil
            }
            
            let c = tmp!
            let tmpMd = c.MetadataCap.borrow()
            if tmpMd == nil {
                return nil
            }

            let md = tmpMd!
            switch view {
                case Type<MetadataViews.NFTCollectionData>():
                    let pathIdentifier = StringUtils.join([segments[2], segments[1]], "_")
                    return MetadataViews.NFTCollectionData(
                        storagePath: StoragePath(identifier: pathIdentifier)!,
                        publicPath: PublicPath(identifier: pathIdentifier)!,
                        publicCollection: Type<&{NonFungibleToken.Collection}>(),
                        publicLinkedType: Type<&{NonFungibleToken.Collection}>(),
                        createEmptyCollectionFunction: fun(): @{NonFungibleToken.Collection} {
                            let addr = AddressUtils.parseAddress(rt)!
                            let c = getAccount(addr).contracts.borrow<&{BaseCollection}>(name: segments[2])!
                            return <- c.createEmptyCollection(nftType: rt)
                        }
                    )
                case Type<MetadataViews.NFTCollectionDisplay>():
                    return md.collectionInfo.getDisplay()
            }

            if let entry = md.borrowMetadata(id: self.metadataID) {
                switch view {
                    case Type<MetadataViews.Traits>():
                        return entry.getTraits()
                    case Type<MetadataViews.Editions>():
                        return entry.getEditions()
                    case Type<MetadataViews.Display>():
                        let num = (entry.editions?.infoList?.length ?? 0) > 0 ? entry.editions!.infoList[0].number : self.id

                        return MetadataViews.Display(
                            name: entry.name.concat(" #").concat(num.toString()),
                            description: entry.description,
                            thumbnail: entry.getThumbnail()
                        )
                    case Type<MetadataViews.ExternalURL>():
                        return entry.getExternalURL()
                    case Type<MetadataViews.Royalties>():
                        return entry.getRoyalties()
                }
            }

            return nil
        }

        access(all) fun createEmptyCollection(): @{NonFungibleToken.Collection} {
            return <- UniversalCollection.createCollection(nftType: self.getType())
        }
    }
}
```