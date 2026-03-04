# Source: https://github.com/Flowtyio/fantastec/blob/main/contracts/FantastecPackNFT.cdc

```
import Crypto
import "NonFungibleToken"
import "FantastecNFT"
import "IFantastecPackNFT"
import "MetadataViews"
import "ViewResolver"
import "Burner"

access(all) contract FantastecPackNFT: NonFungibleToken, IFantastecPackNFT {

    access(all) var totalSupply: UInt64
    access(all) let CollectionStoragePath: StoragePath
    access(all) let CollectionPublicPath: PublicPath
    access(all) let CollectionIFantastecPackNFTPublicPath: PublicPath
    access(all) let OperatorStoragePath: StoragePath

    access(contract) let packs: @{UInt64: Pack}

    // from IFantastecPackNFT
    access(all) event Burned(id: UInt64)
    // from NonFungibleToken
    access(all) event ContractInitialized()
    access(all) event Withdraw(id: UInt64, from: Address?)
    access(all) event Deposit(id: UInt64, to: Address?)
    // contract specific
    access(all) event Minted(id: UInt64)

    access(all) resource FantastecPackNFTOperator: IFantastecPackNFT.IOperator {
        access(IFantastecPackNFT.Owner) fun mint(packId: UInt64, productId: UInt64): @{IFantastecPackNFT.NFT}{
            let packNFT <- create NFT(packId: packId, productId: productId)
            FantastecPackNFT.totalSupply = FantastecPackNFT.totalSupply + 1
            emit Minted(id: packNFT.id)
            let pack <- create Pack()
            FantastecPackNFT.packs[packNFT.id] <-! pack
            return <- packNFT
        }

        access(IFantastecPackNFT.Owner) fun open(id: UInt64, recipient: Address) {
            let pack <- FantastecPackNFT.packs.remove(key: id) ?? panic("cannot find pack with ID ".concat(id.toString()))
            pack.open(recipient: recipient)
            FantastecPackNFT.packs[id] <-! pack
        }

        access(IFantastecPackNFT.Owner) fun addFantastecNFT(id: UInt64, nft: @FantastecNFT.NFT) {
            let pack <- FantastecPackNFT.packs.remove(key: id) ?? panic("cannot find pack with ID ".concat(id.toString()))
            pack.addFantastecNFT(nft: <- nft)
            FantastecPackNFT.packs[id] <-! pack
        }

        init(){}
    }

    access(all) resource Pack: IFantastecPackNFT.IFantastecPack {
        access(all) var ownedNFTs: @{UInt64: FantastecNFT.NFT}

        access(IFantastecPackNFT.Owner) fun open(recipient: Address) {
            let receiver = getAccount(recipient)
                .capabilities.get<&{NonFungibleToken.CollectionPublic}>(FantastecNFT.CollectionPublicPath)
                .borrow()
                ?? panic("Could not get receiver reference to the NFT Collection - ".concat(recipient.toString()))
            for key in self.ownedNFTs.keys {
                let nft <-! self.ownedNFTs.remove(key: key)
                receiver.deposit(token: <- nft!)
            }
        }

        access(all) fun addFantastecNFT(nft: @FantastecNFT.NFT) {
            let id = nft.id
            self.ownedNFTs[id] <-! nft
        }

        init() {
            self.ownedNFTs <- {}
        }
    }

    access(all) resource NFT: IFantastecPackNFT.NFT, Burner.Burnable, ViewResolver.Resolver {
        access(all) let id: UInt64
        access(all) let productId: UInt64

        access(contract) fun burnCallback() {
            FantastecPackNFT.totalSupply = FantastecPackNFT.totalSupply - (1 as UInt64)
            let pack <- FantastecPackNFT.packs.remove(key: self.id)
                ?? panic("cannot find pack with ID ".concat(self.id.toString()))
            destroy pack
            emit Burned(id: self.id)
        }

        init(packId: UInt64, productId: UInt64) {
            self.id = packId
            self.productId = productId
        }

        // from MetadataViews.Resolver
        access(all) view fun getViews(): [Type] {
            return [
                Type<MetadataViews.Display>()
            ]
        }

        // from MetadataViews.Resolver
        access(all) view fun resolveView(_ view: Type): AnyStruct? {
            switch view {
                case Type<MetadataViews.Display>():
                    return MetadataViews.Display(
                        name: "Fantastec Pack",
                        description: "Reveals Fantstec NFTs when opened",
                        thumbnail: MetadataViews.HTTPFile(url: self.getThumbnailPath())
                    )
            }
            return nil
        }

        access(all) view fun getThumbnailPath(): String {
            return "path/to/thumbnail/".concat(self.id.toString())
        }

        access(all) fun createEmptyCollection(): @{NonFungibleToken.Collection} { 
            return <- create Collection()
        }
    }

    access(all) resource Collection: IFantastecPackNFT.IFantastecPackNFTCollectionPublic {
        // dictionary of NFT conforming tokens
        // NFT is a resource type with an `UInt64` ID field
        access(all) var ownedNFTs: @{UInt64: {NonFungibleToken.NFT}}

        init () {
            self.ownedNFTs <- {}
        }

        // withdraw removes an NFT from the collection and moves it to the caller
        access(NonFungibleToken.Withdraw) fun withdraw(withdrawID: UInt64): @{NonFungibleToken.NFT} {
            let token <- self.ownedNFTs.remove(key: withdrawID) ?? panic("missing NFT")
            emit Withdraw(id: token.id, from: self.owner?.address)
            return <- token
        }

        // deposit takes a NFT and adds it to the collections dictionary
        // and adds the ID to the id array
        access(all) fun deposit(token: @{NonFungibleToken.NFT}) {
            let token <- token as! @FantastecPackNFT.NFT

            let id: UInt64 = token.id

            // add the new token to the dictionary which removes the old one
            let oldToken <- self.ownedNFTs[id] <- token
            emit Deposit(id: id, to: self.owner?.address)

            destroy oldToken
        }

        // getIDs returns an array of the IDs that are in the collection
        access(all) view fun getIDs(): [UInt64] {
            return self.ownedNFTs.keys
        }

        // borrowNFT gets a reference to an NFT in the collection
        // so that the caller can read its metadata and call its methods
        access(all) view fun borrowNFT(_ id: UInt64): &{NonFungibleToken.NFT}? {
            return &self.ownedNFTs[id]
        }

        access(all) fun createEmptyCollection(): @{NonFungibleToken.Collection} { 
            return <- create Collection()
        }

        access(all) view fun getSupportedNFTTypes(): {Type: Bool} {
            return {
                Type<@NFT>(): true
            }
        }

        access(all) view fun isSupportedNFTType(type: Type): Bool {
            return type == Type<@NFT>()
        }
    }

    access(all) fun createEmptyCollection(nftType: Type): @{NonFungibleToken.Collection} {
        return <- create Collection()
    }

    access(all) view fun getContractViews(resourceType: Type?): [Type] {
        return []
    }

    access(all) fun resolveContractView(resourceType: Type?, viewType: Type): AnyStruct? {
        return nil
    }

    init(){
        self.totalSupply = 0
        self.packs <- {}
        // Set our named paths
        self.CollectionStoragePath = /storage/FantastecPackNFTCollection
        self.CollectionPublicPath = /public/FantastecPackNFTCollection
        self.CollectionIFantastecPackNFTPublicPath = /public/FantastecPackNFTCollection
        self.OperatorStoragePath = /storage/FantastecPackNFTOperatorCollection

        // Create a collection to receive Pack NFTs
        let collection <- create Collection()
        self.account.storage.save(<-collection, to: self.CollectionStoragePath)

        let cap = self.account.capabilities.storage.issue<&{NonFungibleToken.CollectionPublic, IFantastecPackNFT.IFantastecPackNFTCollectionPublic}>(self.CollectionStoragePath)
        self.account.capabilities.publish(cap, at: self.CollectionPublicPath)

        // Create a operator to share mint capability with proxy
        let operator <- create FantastecPackNFTOperator()
        self.account.storage.save(<-operator, to: self.OperatorStoragePath)

        self.account.capabilities.storage.issue<&{IFantastecPackNFT.IOperator}>(self.OperatorStoragePath)
    }
}

```