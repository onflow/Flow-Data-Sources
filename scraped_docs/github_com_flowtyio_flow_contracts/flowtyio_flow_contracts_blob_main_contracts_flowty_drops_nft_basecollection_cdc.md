# Source: https://github.com/Flowtyio/flow-contracts/blob/main/contracts/flowty-drops/nft/BaseCollection.cdc

```
import "NonFungibleToken"
import "ViewResolver"
import "MetadataViews"
import "NFTMetadata"
import "FlowtyDrops"
import "AddressUtils"
import "StringUtils"

access(all) contract interface BaseCollection: ViewResolver {
    access(all) var MetadataCap: Capability<&NFTMetadata.Container>
    access(all) var totalSupply: UInt64

    access(all) fun createEmptyCollection(nftType: Type): @{NonFungibleToken.Collection}

    // The base collection is an interface that attmepts to take more boilerplate
    // off of NFT-standard compliant definitions.
    access(all) resource interface Collection: NonFungibleToken.Collection {
        access(all) var ownedNFTs: @{UInt64: {NonFungibleToken.NFT}}
        access(all) var nftType: Type

        access(all) fun deposit(token: @{NonFungibleToken.NFT}) {
            pre {
                token.getType() == self.nftType: "unexpected nft type being deposited"
            }

            destroy self.ownedNFTs.insert(key: token.id, <-token)
        }

        access(all) view fun borrowNFT(_ id: UInt64): &{NonFungibleToken.NFT}? {
            return &self.ownedNFTs[id]
        }

        access(all) view fun getSupportedNFTTypes(): {Type: Bool} {
            return {
                self.nftType: true
            }
        }

        access(all) view fun isSupportedNFTType(type: Type): Bool {
            return type == self.nftType
        }

        access(NonFungibleToken.Withdraw) fun withdraw(withdrawID: UInt64): @{NonFungibleToken.NFT} {
            return <- self.ownedNFTs.remove(key: withdrawID)!
        }
    }

    access(all) view fun getContractViews(resourceType: Type?): [Type] {
        return [
            Type<MetadataViews.NFTCollectionData>(),
            Type<MetadataViews.NFTCollectionDisplay>()
        ]
    }

    access(all) fun resolveContractView(resourceType: Type?, viewType: Type): AnyStruct? {
        if resourceType == nil {
            return nil
        }

        let rt = resourceType!
        let segments = rt.identifier.split(separator: ".") 
        let pathIdentifier = StringUtils.join([segments[2], segments[1]], "_")

        let addr = AddressUtils.parseAddress(rt)!
        let acct = getAccount(addr)
        
        switch viewType {
            case Type<MetadataViews.NFTCollectionData>():
                let segments = rt.identifier.split(separator: ".") 
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
            case Type<FlowtyDrops.DropResolver>():
                return FlowtyDrops.DropResolver(cap: acct.capabilities.get<&{FlowtyDrops.ContainerPublic}>(FlowtyDrops.ContainerPublicPath))
        }

        // These views require the {BaseCollection} interface
        if let c = getAccount(addr).contracts.borrow<&{BaseCollection}>(name: segments[2]) {
            let tmp = c.MetadataCap.borrow()
            if tmp == nil {
                return nil
            }

            switch viewType {
                case Type<MetadataViews.NFTCollectionDisplay>():
                    return tmp!.collectionInfo.getDisplay()
                case Type<MetadataViews.Royalties>():
                    let keys = tmp!.metadata.keys
                    if keys.length == 0 || keys.length > 1 {
                        return nil
                    }
                    return tmp!.borrowMetadata(id: keys[0])!.getRoyalties()
            }
        }

        return nil
    }
}
```