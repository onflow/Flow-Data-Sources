# Source: https://github.com/Flowtyio/fantastec/blob/main/contracts/IFantastecPackNFT.cdc

```
import Crypto
import "NonFungibleToken"
import "FantastecNFT"

access(all) contract interface IFantastecPackNFT {

    access(all) entitlement Owner

    /// StoragePath for Collection Resource
    access(all) let CollectionStoragePath: StoragePath

    /// PublicPath expected for deposit
    access(all) let CollectionPublicPath: PublicPath

    /// PublicPath for receiving NFT
    access(all) let CollectionIFantastecPackNFTPublicPath: PublicPath

    /// StoragePath for the NFT Operator Resource (issuer owns this)
    access(all) let OperatorStoragePath: StoragePath

    /// Burned
    /// Emitted when a NFT has been burned
    access(all) event Burned(id: UInt64 )

    access(all) resource interface IOperator {
        access(Owner) fun mint(packId: UInt64, productId: UInt64): @{NFT}
        access(Owner) fun addFantastecNFT(id: UInt64, nft: @FantastecNFT.NFT)
        access(Owner) fun open(id: UInt64, recipient: Address)
    }

    access(all) resource interface FantastecPackNFTOperator: IOperator {
        access(Owner) fun mint(packId: UInt64, productId: UInt64): @{NFT}
        access(Owner) fun addFantastecNFT(id: UInt64, nft: @FantastecNFT.NFT)
        access(Owner) fun open(id: UInt64, recipient: Address)
    }

    access(all) resource interface IFantastecPack {
        access(all) var ownedNFTs: @{UInt64: FantastecNFT.NFT}

        access(all) fun addFantastecNFT(nft: @FantastecNFT.NFT)
        access(Owner) fun open(recipient: Address)
    }

    access(all) resource interface NFT: NonFungibleToken.NFT {
        access(all) let id: UInt64
    }

    access(all) resource interface IFantastecPackNFTCollectionPublic: NonFungibleToken.Collection {
        access(all) fun deposit(token: @{NonFungibleToken.NFT})
    }
}
```