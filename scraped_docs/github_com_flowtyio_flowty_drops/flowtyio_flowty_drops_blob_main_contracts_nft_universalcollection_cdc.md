# Source: https://github.com/Flowtyio/flowty-drops/blob/main/contracts/nft/UniversalCollection.cdc

```
import "NonFungibleToken"
import "MetadataViews"
import "BaseCollection"

access(all) contract UniversalCollection {
    access(all) resource Collection: BaseCollection.Collection {
        access(all) var ownedNFTs: @{UInt64: {NonFungibleToken.NFT}}
        access(all) var nftType: Type

        access(all) let data: {String: AnyStruct}
        access(all) let resources: @{String: AnyResource}

        access(all) fun createEmptyCollection(): @{NonFungibleToken.Collection} {
            return <- create Collection(nftType: self.nftType)
        }

        access(all) fun deposit(token: @{NonFungibleToken.NFT}) {
            pre {
                token.getType() == self.nftType: "unexpected nft type being deposited"
            }

            destroy self.ownedNFTs.insert(key: token.id, <-token)
        }

        access(all) view fun borrowNFT(_ id: UInt64): &{NonFungibleToken.NFT}? {
            return &self.ownedNFTs[id]
        }

        access(NonFungibleToken.Withdraw) fun withdraw(withdrawID: UInt64): @{NonFungibleToken.NFT} {
            return <- self.ownedNFTs.remove(key: withdrawID)!
        }

        init (nftType: Type) {
            self.ownedNFTs <- {}
            self.nftType = nftType

            self.data = {}
            self.resources <- {}
        }
    }

    access(all) fun createCollection(nftType: Type): @Collection {
        return <- create Collection(nftType: nftType)
    }
}
```