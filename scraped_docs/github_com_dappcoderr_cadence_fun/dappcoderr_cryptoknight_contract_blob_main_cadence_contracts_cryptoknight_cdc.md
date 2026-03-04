# Source: https://github.com/DappCoderr/CryptoKnight-Contract/blob/main/cadence/contracts/CryptoKnight.cdc

```
import NonFungibleToken from "./NonFungibleToken.cdc"
import MetadataViews from "./MetadataViews.cdc"

/// The CryptoKnight contract defines a custom NFT with gameplay mechanics.
access(all) contract CryptoKnight: NonFungibleToken {

    // Events
    access(all) event ContractInitialized()
    access(all) event Withdraw(id: UInt64, from: Address?)
    access(all) event Deposit(id: UInt64, to: Address?)
    access(all) event KinigtMinted(id: UInt64, name: String, type: UInt8)

    // Collection storage and public path declarations
    access(all) let CollectionStoragePath: StoragePath
    access(all) let CollectionPublicPath: PublicPath

    // Tracks total NFTs minted
    access(all) var totalSupply: UInt64

    /// Enum defining types of offensive power a knight can have
    access(all) enum OffencivePower: UInt8 {
        access(all) case Rock
        access(all) case Fire
        access(all) case Water
        access(all) case Electric
    }

    /// Metadata struct for a Knight NFT
    access(all) struct KnightDetails {
        access(all) var name: String
        access(all) var dob: UFix64
        access(all) var type: OffencivePower?

        init(name: String, dob: UFix64, type: UInt8) {
            self.name = name
            self.dob = dob
            self.type = CryptoKnight.OffencivePower(rawValue: type)
        }
    }

    /// Main NFT resource that implements NonFungibleToken
    access(all) resource NFT: NonFungibleToken.NFT {
        access(all) let id: UInt64
        access(all) let details: CryptoKnight.KnightDetails
        access(all) var xp: UInt64
        access(all) var winCount: UInt64

        init(_name: String, _type: UInt8) {
            let currntTime: UFix64 = getCurrentBlock().timestamp
            self.id = self.uuid
            self.details = CryptoKnight.KnightDetails(
                name: _name,
                dob: currntTime,
                type: _type
            )
            self.xp = CryptoKnight.getRandomKNightXP()
            self.winCount = 0
            CryptoKnight.totalSupply = CryptoKnight.totalSupply + 1
        }

        /// Declares supported metadata views
        access(all) view fun getViews(): [Type] {
            return [
                Type<MetadataViews.Display>(),
                Type<MetadataViews.NFTCollectionData>(),
                Type<MetadataViews.NFTCollectionDisplay>(),
                Type<MetadataViews.ExternalURL>(),
                Type<MetadataViews.Traits>(),
                Type<MetadataViews.Edition>(),
                Type<MetadataViews.Royalties>(),
                Type<MetadataViews.Serial>()
            ]
        }

        /// Adds XP to the knight randomly between 1 and 5, and adds extra XP based on its type
        access(contract) fun updateXP() {
            let randomNumber: UInt64 = revertibleRandom<UInt64>(modulo: UInt64.max)
            self.xp = self.xp + (randomNumber % 5) + 1
            let power = self.details.type!.rawValue
            switch power {
                case 0: self.xp = self.xp + 5
                case 1: self.xp = self.xp + 4
                case 2: self.xp = self.xp + 3
                case 3: self.xp = self.xp + 2
            }
        }

        /// Reduces XP by 1
        access(contract) fun deprecateXP() {
            self.xp = self.xp - 1
        }

        /// Resolves metadata views for marketplaces and wallets
        access(all) fun resolveView(_ view: Type): AnyStruct? {
            switch view {
                case Type<MetadataViews.ExternalURL>():
                    return MetadataViews.ExternalURL("https://flow.com/")
                case Type<MetadataViews.NFTCollectionData>():
                    return MetadataViews.NFTCollectionData(
                        storagePath: CryptoKnight.CollectionStoragePath,
                        publicPath: CryptoKnight.CollectionPublicPath,
                        publicCollection: Type<&CryptoKnight.Collection>(),
                        publicLinkedType: Type<&CryptoKnight.Collection>(),
                        createEmptyCollectionFunction: fun (): @{NonFungibleToken.Collection} {
                            return <-CryptoKnight.createEmptyCollection(nftType: Type<@CryptoKnight.Collection>())
                        }
                    )
                case Type<MetadataViews.NFTCollectionDisplay>():
                    let bannerMedia = MetadataViews.Media(
                        file: MetadataViews.HTTPFile(url: "https://banner_2023.png"),
                        mediaType: "image/png"
                    )
                    let logoFull = MetadataViews.Media(
                        file: MetadataViews.HTTPFile(url: "https://logo_full.png"),
                        mediaType: "image/png"
                    )
                    return MetadataViews.NFTCollectionDisplay(
                        name: "CryptoKnight",
                        description: "CryptoKnight Is A Fun And Interactive Cadence Tutorial...",
                        externalURL: MetadataViews.ExternalURL("https://flow.io/"),
                        squareImage: logoFull,
                        bannerImage: bannerMedia,
                        socials: {
                            "twitter": MetadataViews.ExternalURL("https://twitter.com/flunks_nft")
                        }
                    )
            }
            return nil
        }

        /// Increments win count
        access(all) fun winner() {
            self.winCount = self.winCount + 1
        }

        /// Factory method for collection view compatibility
        access(all) fun createEmptyCollection(): @{NonFungibleToken.Collection} {
            return <-CryptoKnight.createEmptyCollection(nftType: Type<@CryptoKnight.NFT>())
        }
    }

    /// Public-facing interface for knight collections
    access(all) resource interface CryptoKnightCollectinPublic {
        access(all) fun deposit(token: @{NonFungibleToken.NFT})
        access(all) fun getIDs(): [UInt64]
        access(all) fun borrowNFT(_ id: UInt64): &{NonFungibleToken.NFT}?

        /// Specialized borrow function for CryptoKnight
        access(all) fun borrowCryptoknight(id: UInt64): &CryptoKnight.NFT? {
            post {
                result == nil || result?.id == id:
                    "Cannot borrow CryptoKnight reference: ID mismatch"
            }
        }
    }

    /// Resource representing a collection of knights
    access(all) resource Collection:
        CryptoKnightCollectinPublic,
        NonFungibleToken.Provider,
        NonFungibleToken.Receiver,
        NonFungibleToken.Collection,
        NonFungibleToken.CollectionPublic {

        access(all) var ownedNFTs: @{UInt64: {NonFungibleToken.NFT}}

        init() {
            self.ownedNFTs <- {}
        }

        access(all) fun createEmptyCollection(): @{NonFungibleToken.Collection} {
            return <-CryptoKnight.createEmptyCollection(nftType: Type<@CryptoKnight.NFT>())
        }

        // Placeholder for supported types
        access(all) view fun getSupportedNFTTypes(): {Type: Bool} {
            panic("implement me")
        }

        access(all) view fun isSupportedNFTType(type: Type): Bool {
            panic("implement me")
        }

        /// Withdraws NFT by ID
        access(NonFungibleToken.Withdraw) fun withdraw(withdrawID: UInt64): @{NonFungibleToken.NFT} {
            let token <- self.ownedNFTs.remove(key: withdrawID)
                ?? panic("Could not withdraw NFT with provided ID")
            emit Withdraw(id: token.id, from: self.owner?.address)
            return <- token
        }

        /// Deposits NFT into collection
        access(all) fun deposit(token: @{NonFungibleToken.NFT}) {
            let token <- token as! @CryptoKnight.NFT
            let id = token.id
            let oldToken <- self.ownedNFTs[id] <- token
            destroy oldToken
            emit Deposit(id: id, to: self.owner?.address)
        }

        /// Borrows any NFT interface by ID
        access(all) view fun borrowNFT(_ id: UInt64): &{NonFungibleToken.NFT}? {
            return &self.ownedNFTs[id]
        }

        /// Borrows full CryptoKnight NFT reference
        access(all) fun borrowCryptoknight(id: UInt64): &CryptoKnight.NFT? {
            if self.ownedNFTs[id] != nil {
                let ref = (&self.ownedNFTs[id] as &{NonFungibleToken.NFT}?)
                return ref as! &CryptoKnight.NFT
            } else {
                return nil
            }
        }

        /// Returns list of owned NFT IDs
        access(all) view fun getIDs(): [UInt64] {
            return self.ownedNFTs.keys
        }

        /// Returns number of NFTs in collection
        access(all) view fun getLength(): Int {
            return self.ownedNFTs.length
        }
    }

    /// Factory for empty collection
    access(all) fun createEmptyCollection(nftType: Type): @{NonFungibleToken.Collection} {
        return <- create Collection()
    }

    /// Mints new knight NFT
    access(all) fun mintKnight(name: String, type: UInt8): @NFT {
        pre {
            name.length > 0: "Name cannot be empty"
        }
        let nftId = CryptoKnight.totalSupply
        var newNFT <- create NFT(_name: name, _type: type)
        emit KinigtMinted(id: nftId, name: name, type: type)
        return <- newNFT
    }

    /// Generates initial XP between 1 and 100
    access(all) fun getRandomKNightXP(): UInt64 {
        let randomNumber: UInt64 = revertibleRandom<UInt64>(modulo: UInt64.max)
        return (randomNumber % 100) + 1
    }

    /// Compares XP between two knights and determines a winner
    access(all) fun battle(userA: Address, userAKnight: UInt64, userB: Address, userBKnight: UInt64) {
        let accountA = getAccount(userA)
        let accountB = getAccount(userB)

        let borrowCap_A = accountA.capabilities.borrow<&CryptoKnight.Collection>(CryptoKnight.CollectionPublicPath)!
        let borrowKnight_A = borrowCap_A.borrowCryptoknight(id: userAKnight)!

        let knightA_XP = borrowKnight_A.xp

        let borrowCap_B = accountB.capabilities.borrow<&CryptoKnight.Collection>(CryptoKnight.CollectionPublicPath)!
        let borrowKnight_B = borrowCap_B.borrowCryptoknight(id: userBKnight)!

        let knightB_XP = borrowKnight_B.xp

        if (knightA_XP > knightB_XP) {
            borrowKnight_A.winner()
            borrowKnight_A.updateXP()
            borrowKnight_B.deprecateXP()
        } else {
            borrowKnight_B.winner()
            borrowKnight_B.updateXP()
            borrowKnight_A.deprecateXP()
        }
    }

    // View resolution placeholders
    access(all) view fun getContractViews(resourceType: Type?): [Type] {
        panic("implement me")
    }

    access(all) fun resolveContractView(resourceType: Type?, viewType: Type): AnyStruct? {
        return nil
    }

    /// Initializes contract storage paths and total supply
    init() {
        let identifier = "KnightCollection".concat(self.account.address.toString())
        self.CollectionPublicPath = PublicPath(identifier: identifier)!
        self.CollectionStoragePath = StoragePath(identifier: identifier)!
        self.totalSupply = 0
        emit ContractInitialized()
    }
}

```