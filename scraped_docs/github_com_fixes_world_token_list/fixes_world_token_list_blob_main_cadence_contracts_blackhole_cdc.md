# Source: https://github.com/fixes-world/token-list/blob/main/cadence/contracts/BlackHole.cdc

```
/**
> Author: Fixes Lab <https://github.com/fixes-world/>

# Black Hole is the utility contract for burning fungible tokens on the Flow blockchain.

## Features:

- You can register a BlackHole Resource from the BlackHole contract.
- Users can burn fungible tokens by sending them to the random BlackHole Resource.
- Users can get the balance of vanished fungible tokens by the type of the Fungible Token in the BlackHole Resource.

*/
import "FungibleToken"
import "NonFungibleToken"
import "ViewResolver"
import "StringUtils"
// IncrementFi Swap
import "SwapConfig"
import "SwapInterfaces"

/// BlackHole contract
///
access(all) contract BlackHole {

    /* --- Entitlement --- */

    // NOTHING

    /* --- Events --- */

    /// Event emitted when a new BlackHole Resource is registered
    access(all) event NewBlackHoleRegistered(
        blackHoleAddr: Address,
        blackHoleId: UInt64,
    )

    /// Event emitted when a new Fungible Token is registered
    access(all) event FungibleTokenVanished(
        blackHoleAddr: Address,
        blackHoleId: UInt64,
        vaultIdentifier: Type,
        amount: UFix64,
    )

    /// Event emitted when a new NonFungible Token is registered
    access(all) event NonFungibleTokenVanished(
        blackHoleAddr: Address,
        blackHoleId: UInt64,
        nftIdentifier: Type,
        nftID: UInt64,
    )

    /* --- Variable, Enums and Structs --- */

    /// BlackHole Resource
    access(all) let storagePath: StoragePath
    /// BlackHoles Registry
    access(contract) let blackHoles: {Address: Bool}

    /* --- Interfaces & Resources --- */

    /// The public interface for the BlackHole Resource
    ///
    access(all) resource interface BlackHolePublic {
        /// Check if the BlackHole Resource is valid
        /// Valid means that the owner's account should have all keys revoked
        ///
        access(all)
        view fun isValid(): Bool {
            /// The Keys in the owner's account should be all revoked
            if let ownerAddr = self.owner?.address {
                let ownerAcct = getAccount(ownerAddr)
                // Check if all keys are revoked
                var isAllKeyRevoked = true
                let totalKeyAmount = Int(ownerAcct.keys.count)
                var i = 0
                while i < totalKeyAmount {
                    if let key = ownerAcct.keys.get(keyIndex: i) {
                        isAllKeyRevoked = isAllKeyRevoked && key.isRevoked
                    }
                    i = i + 1
                }
                // TODO: Check no owned account (Hybrid custodial account)

                return isAllKeyRevoked
            }
            return false
        }
    }

    /// The resource of BlackHole Fungible Token Receiver
    ///
    access(all) resource Receiver: FungibleToken.Receiver, BlackHolePublic {
        /// The dictionary of Fungible Token Pools
        access(self) let pools: @{Type: {FungibleToken.Vault}}

        init() {
            self.pools <- {}
        }

        /** ---- FungibleToken Receiver Interface ---- */

        /// Takes a Vault and deposits it into the implementing resource type
        ///
        /// @param from: The Vault resource containing the funds that will be deposited
        ///
        access(all)
        fun deposit(from: @{FungibleToken.Vault}) {
            pre {
                self.isValid(): "The BlackHole Resource should be valid"
                from.balance > 0.0: "The balance should be greater than zero"
            }
            let blackHoleAddr = self.owner?.address ?? panic("Invalid BlackHole Address")

            // get basic information
            let fromType = from.getType()
            let vanishedAmount = from.balance

            // should be A.{address}.{contractName}.Vault
            let fromIdentifierArr = StringUtils.split(fromType.identifier, ".")
            // check if the from vault is an IncrementFi LP
            if fromIdentifierArr[2] == "SwapPair" {
                let pairAddr = Address.fromString("0x".concat(fromIdentifierArr[1]))!
                // @deprecated in Cadence 1.0
                if let pairPubRef = getAccount(pairAddr)
                    .capabilities
                    .borrow<&{SwapInterfaces.PairPublic}>(SwapConfig.PairPublicPath) {
                    if pairPubRef.getLpTokenVaultType() == fromType {
                        // Now we can confirm that the from vault is an IncrementFi LP
                        // check if there is a LP Collection in the BlackHole Account
                        if let lpTokenCollectionRef = getAccount(blackHoleAddr)
                            .capabilities
                            .borrow<&{SwapInterfaces.LpTokenCollectionPublic}>(SwapConfig.LpTokenCollectionPublicPath) {
                            // Deposit the LP Token into the LP Collection
                            lpTokenCollectionRef.deposit(pairAddr: pairAddr, lpTokenVault: <- from)

                            emit BlackHole.FungibleTokenVanished(
                                blackHoleAddr: blackHoleAddr,
                                blackHoleId: self.uuid,
                                vaultIdentifier: fromType,
                                amount: vanishedAmount
                            )
                            return
                        }
                    }
                }
            }
            // Deposit the Fungible Token into the BlackHole Vault
            let receiverRef = self._borrowOrCreateBlackHoleVault(fromType)
            receiverRef.deposit(from: <- from)

            emit BlackHole.FungibleTokenVanished(
                blackHoleAddr: blackHoleAddr,
                blackHoleId: self.uuid,
                vaultIdentifier: fromType,
                amount: vanishedAmount
            )
        }

        /// getSupportedVaultTypes returns a dictionary of Vault types
        /// and whether the type is currently supported by this Receiver
        access(all) view fun getSupportedVaultTypes(): {Type: Bool} {
            // All Vault types are supported by default, so return an empty dictionary
            return {}
        }

        /// Returns whether or not the given type is accepted by the Receiver
        /// A vault that can accept any type should just return true by default
        access(all) view fun isSupportedVaultType(type: Type): Bool {
            return true
        }

        /** ---- BlackHolePublic Interface ---- */

        /// Get the balance by the type of the Fungible Token
        ///
        access(all)
        view fun getVanishedBalance(_ type: Type): UFix64 {
            return self.pools[type]?.balance ?? 0.0
        }

        /** ---- Internal Methods ---- */

        /// Borrow the FungibleToken Vault
        ///
        access(self)
        fun _borrowOrCreateBlackHoleVault(_ type: Type): &{FungibleToken.Vault} {
            pre {
                type.isSubtype(of: Type<@{FungibleToken.Vault}>()): "The type should be a subtype of FungibleToken.Vault"
            }
            if let ref = &self.pools[type] as &{FungibleToken.Vault}? {
                return ref
            } else {
                let ftArr = StringUtils.split(type.identifier, ".")
                let ftAddress = Address.fromString("0x".concat(ftArr[1])) ?? panic("Invalid Fungible Token Address")
                let ftContractName = ftArr[2]
                let ftContract = getAccount(ftAddress)
                    .contracts.borrow<&{FungibleToken}>(name: ftContractName)
                    ?? panic("Could not borrow the FungibleToken contract reference")
                // @deprecated in Cadence 1.0
                self.pools[type] <-! ftContract.createEmptyVault(vaultType: type)
                return &self.pools[type] as &{FungibleToken.Vault}? ?? panic("Invalid Fungible Token Vault")
            }
        }
    }

    /// The resource of BlackHole NonFungible Token Collection
    ///
    access(all) resource Collection: NonFungibleToken.Collection, BlackHolePublic {
        access(all) var ownedNFTs: @{UInt64: {NonFungibleToken.NFT}}
        /// The dictionary of NonFungible Token Pools
        /// NFT Type -> [NFT ID]
        access(self) let nftOriginIds: {Type: [UInt64]}
        access(self) let nftIdPrefix: {Type: UInt64}
        access(self) let supportedNftTypes: {Type: Bool}

        init() {
            self.ownedNFTs <- {}
            self.nftOriginIds = {}
            self.nftIdPrefix = {}
            self.supportedNftTypes = {}
        }

        /// --- NonFungibleToken Collection Interface ---

        access(NonFungibleToken.Withdraw)
        fun withdraw(withdrawID: UInt64): @{NonFungibleToken.NFT} {
            panic("This function is invalid for the BlackHole Collection")
        }

        /// getSupportedNFTTypes returns a dictionary of NFT types
        /// It returns all types of the vanished NFTs
        access(all)
        view fun getSupportedNFTTypes(): {Type: Bool} {
            return self.supportedNftTypes
        }

        /// All NFT types are supported by default, so return true by default
        ///
        access(all)
        view fun isSupportedNFTType(type: Type): Bool {
            return true
        }

        /// deposit takes a NFT as an argument and stores it in the collection
        /// @param token: The NFT to deposit into the collection
        access(all)
        fun deposit(token: @{NonFungibleToken.NFT}) {
            pre {
                self.isValid(): "The BlackHole Resource should be valid"
            }

            let nftType = token.getType()
            var nftIdPrefix: UInt64 = 0
            if self.nftIdPrefix[nftType] != nil {
                nftIdPrefix = self.nftIdPrefix[nftType]!
            } else {
                nftIdPrefix = (UInt64(self.nftIdPrefix.keys.length) + 1) << 32
                self.nftIdPrefix[nftType] = nftIdPrefix
            }

            if self.nftOriginIds[nftType] == nil {
                self.nftOriginIds[nftType] = []
            }
            let nftIds = &self.nftOriginIds[nftType] as auth(Mutate) &[UInt64]? ?? panic("Invalid NFT Origin IDs")
            let nftIdToVanish: UInt64 = token.id
            // Add the NFT ID to the NFT Origin IDs
            nftIds.append(nftIdToVanish)

            // Store the NFT in the collection
            let newNFTid = nftIdPrefix + nftIdToVanish
            let toDestory <- self.ownedNFTs[newNFTid] <- token
            destroy toDestory

            // Set the NFTType as supported
            if self.supportedNftTypes[nftType] == nil {
                self.supportedNftTypes[nftType] = true
            }

            emit BlackHole.NonFungibleTokenVanished(
                blackHoleAddr: self.owner?.address ?? panic("Invalid BlackHole Address"),
                blackHoleId: self.uuid,
                nftIdentifier: nftType,
                nftID: nftIdToVanish
            )
        }

        access(all)
        view fun getLength(): Int {
            return self.ownedNFTs.length
        }

        access(all)
        view fun getIDs(): [UInt64] {
            return self.ownedNFTs.keys
        }

        access(all)
        view fun borrowNFT(_ id: UInt64): &{NonFungibleToken.NFT}? {
            return &self.ownedNFTs[id]
        }

        /// Borrow the view resolver for the specified NFT ID
        access(all)
        view fun borrowViewResolver(id: UInt64): &{ViewResolver.Resolver}? {
            if let nft = &self.ownedNFTs[id] as &{NonFungibleToken.NFT}? {
                return nft as &{ViewResolver.Resolver}
            }
            return nil
        }

        access(all)
        fun createEmptyCollection(): @{NonFungibleToken.Collection} {
            return <- create Collection()
        }

        /// --- BlackHolePublic Interface ---

        /// Get the balance by the type of the Fungible Token
        ///
        access(all)
        view fun getVanishedAmount(_ type: Type): Int {
            return self.nftOriginIds[type]?.length ?? 0
        }
    }

    /** --- Methods --- */

    /// Get the receiver path for the BlackHole Resource
    ///
    /// @return The PublicPath for the generic BlackHole receiver
    ///
    access(all)
    view fun getBlackHoleReceiverPublicPath(): PublicPath {
        return /public/BlackHoleFTReceiver
    }

    /// Get the storage path for the BlackHole Resource
    ///
    /// @return The StoragePath for the generic BlackHole receiver
    ///
    access(all)
    view fun getBlackHoleReceiverStoragePath(): StoragePath {
        return self.storagePath
    }

    /// Create a new BlackHole Resource
    ///
    access(all)
    fun createNewBlackHole(): @Receiver {
        return <- create Receiver()
    }

    /// Register an address as a new BlackHole
    ///
    access(all)
    fun registerAsBlackHole(_ addr: Address) {
        if self.blackHoles[addr] == nil {
            let ref = self.borrowBlackHoleReceiver(addr)
                ?? panic("Could not borrow the BlackHole Resource")
            assert(
                ref.isValid(),
                message: "The BlackHole Resource should be valid"
            )
            self.blackHoles[addr] = true

            // emit the event
            emit NewBlackHoleRegistered(
                blackHoleAddr: addr,
                blackHoleId: ref.uuid
            )
        }
    }

    /// Borrow a BlackHole Resource by the address
    ///
    access(all)
    view fun borrowBlackHoleReceiver(_ addr: Address): &{FungibleToken.Receiver, BlackHolePublic}? {
        return getAccount(addr)
            .capabilities.borrow<&Receiver>(self.getBlackHoleReceiverPublicPath())
    }

    /// Check if is the address a valid BlackHole address
    ///
    access(all)
    view fun isValidBlackHole(_ addr: Address): Bool {
        return self.borrowBlackHoleReceiver(addr)?.isValid() == true
    }

    /// Register a BlackHole Resource
    ///
    access(all)
    fun borrowRandomBlackHoleReceiver(): &{FungibleToken.Receiver, BlackHolePublic} {
        let max = UInt64(self.blackHoles.keys.length)
        assert(max > 0, message: "There is no BlackHole Resource")
        let rand = revertibleRandom<UInt64>()
        let blackHoleAddr = self.blackHoles.keys[rand % max]
        return self.borrowBlackHoleReceiver(blackHoleAddr) ?? panic("Could not borrow the BlackHole Resource")
    }

    /// Get the registered BlackHoles addresses
    ///
    access(all)
    view fun getRegisteredBlackHoles(): [Address] {
        return self.blackHoles.keys
    }

    /// Check if there is any BlackHole Resource available
    ///
    access(all)
    view fun isAnyBlackHoleAvailable(): Bool {
        return self.blackHoles.keys.length > 0
    }

    /// Burn the Fungible Token by sending it to the BlackHole Resource
    ///
    access(all)
    fun vanish(_ vault: @{FungibleToken.Vault}) {
        let blackHole = self.borrowRandomBlackHoleReceiver()
        blackHole.deposit(from: <- vault)
    }

    /// ----- For BlackHole NFT Collection -----

    /// Get the public path for the BlackHole Collection
    ///
    /// @return The PublicPath for the BlackHole Collection
    ///
    access(all)
    view fun getBlackHoleCollectionPublicPath(): PublicPath {
        return /public/BlackHoleNFTCollection
    }

    /// Get the storage path for the BlackHole Collection
    ///
    /// @return The StoragePath for the BlackHole Collection
    ///
    access(all)
    view fun getBlackHoleCollectionStoragePath(): StoragePath {
        return /storage/BlackHoleNFTCollection
    }

    /// Create a new BlackHole Resource
    ///
    access(all)
    fun createNewBlackHoleCollection(): @Collection {
        return <- create Collection()
    }

    /// Borrow a BlackHole Resource by the address
    ///
    access(all)
    view fun borrowBlackHoleCollection(_ addr: Address): &Collection? {
        return getAccount(addr)
            .capabilities
            .borrow<&Collection>(self.getBlackHoleCollectionPublicPath())
    }

    /// Check if is the address a valid BlackHole address
    ///
    access(all)
    view fun hasValidBlackHoleCollection(_ addr: Address): Bool {
        return self.borrowBlackHoleCollection(addr)?.isValid() == true
    }

    init() {
        let identifier = "BlackHole_".concat(self.account.address.toString()).concat("_receiver")
        self.storagePath = StoragePath(identifier: identifier)!

        self.blackHoles = {}
    }
}

```