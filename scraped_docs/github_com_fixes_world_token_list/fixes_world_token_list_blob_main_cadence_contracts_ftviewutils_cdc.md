# Source: https://github.com/fixes-world/token-list/blob/main/cadence/contracts/FTViewUtils.cdc

```
/**
> Author: Fixes Lab <https://github.com/fixes-world/>

# Token List - A on-chain list of Flow Standard Fungible Tokens (FTs).

This is the Fungible Token view utilties contract of the Token List.

*/
import "MetadataViews"
import "ViewResolver"
import "FungibleToken"
import "FungibleTokenMetadataViews"

access(all) contract FTViewUtils {

    // ----- Entitlement -----

    // An entitlement for allowing edit the FT View Data
    access(all) entitlement Editable

    /*  ---- Events ---- */

    access(all) event FTViewStoragePathUpdated(
        address: Address,
        contractName: String,
        storagePath: StoragePath
    )

    access(all) event FTVaultDataUpdated(
        address: Address,
        contractName: String,
        storagePath: StoragePath,
        receiverPath: PublicPath,
        metadataPath: PublicPath,
        receiverType: Type,
        metadataType: Type
    )

    access(all) event FTDisplayUpdated(
        address: Address,
        contractName: String,
        name: String?,
        symbol: String?,
        description: String?,
        externalURL: String?,
        logo: String?,
        socials: {String: String}
    )

    /// The struct interface for the Fungible Token Identity
    ///
    access(all) struct interface TokenIdentity {
        /// Build type
        access(all)
        view fun buildType(): Type
        /// Get Type identifier
        access(all)
        view fun toString(): String {
            return self.buildType().identifier
        }
    }

    /// The struct for the Fungible Token Identity
    ///
    access(all) struct FTIdentity: TokenIdentity {
        access(all)
        let address: Address
        access(all)
        let contractName: String

        view init(
            _ address: Address,
            _ contractName: String
        ) {
            self.address = address
            self.contractName = contractName
        }

        access(all)
        view fun buildType(): Type {
            return FTViewUtils.buildFTVaultType(self.address, self.contractName)
                ?? panic("Could not build the FT Type")
        }

        /// Borrow the Fungible Token Contract
        ///
        access(all)
        fun borrowFungibleTokenContract(): &{FungibleToken} {
            return getAccount(self.address)
                .contracts.borrow<&{FungibleToken}>(name: self.contractName)
                ?? panic("Could not borrow the FungibleToken contract reference")
        }
    }

    /// The struct for the Fungible Token Vault Data with Source
    ///
    access(all) struct FTVaultDataWithSource {
        access(all)
        let source: Address?
        access(all)
        let vaultData: FungibleTokenMetadataViews.FTVaultData

        view init(
            _ source: Address?,
            _ vaultData: FungibleTokenMetadataViews.FTVaultData
        ) {
            self.source = source
            self.vaultData = vaultData
        }
    }

    /// The struct for the Fungible Token Display with Source
    ///
    access(all) struct FTDisplayWithSource {
        access(all)
        let source: Address?
        access(all)
        let display: FungibleTokenMetadataViews.FTDisplay

        view init(
            _ source: Address?,
            _ display: FungibleTokenMetadataViews.FTDisplay
        ) {
            self.source = source
            self.display = display
        }
    }

    /// The struct for the Fungible Token Paths
    ///
    access(all) struct StandardTokenPaths {
        access(all)
        let vaultPath: StoragePath
        access(all)
        let balancePath: PublicPath
        access(all)
        let receiverPath: PublicPath

        view init(
            vaultPath: StoragePath,
            balancePath: PublicPath,
            receiverPath: PublicPath,
        ) {
            self.vaultPath = vaultPath
            self.balancePath = balancePath
            self.receiverPath = receiverPath
        }
    }

    /// The struct interface for the Bridged Token View
    access(all) struct interface IBridgedTokenView {
        access(all)
        let evmAddress: String
    }

    /// The interface for the Token View
    access(all) struct interface ITokenView {
        access(all)
        let tags: [String]
        access(all)
        let dataSource: Address?

        access(all)
        view fun getIdentity(): {TokenIdentity}
    }

    /// The struct for the Fungible Token List View
    ///
    access(all) struct StandardTokenView: ITokenView {
        access(all)
        let identity: FTIdentity
        access(all)
        let decimals: UInt8
        access(all)
        let tags: [String]
        access(all)
        let dataSource: Address?
        access(all)
        let paths: StandardTokenPaths?
        access(all)
        let display: FTDisplayWithSource?

        view init(
            identity: FTIdentity,
            decimals: UInt8,
            tags: [String],
            dataSource: Address?,
            paths: StandardTokenPaths?,
            display: FTDisplayWithSource?,
        ) {
            self.identity = identity
            self.decimals = decimals
            self.tags = tags
            self.dataSource = dataSource
            self.paths = paths
            self.display = display
        }

        access(all)
        view fun getIdentity(): {TokenIdentity} {
            return self.identity
        }
    }

    /// The struct for the Bridged Token View
    ///
    access(all) struct BridgedTokenView: ITokenView, IBridgedTokenView {
        access(all)
        let identity: FTIdentity
        access(all)
        let evmAddress: String
        access(all)
        let decimals: UInt8
        access(all)
        let tags: [String]
        access(all)
        let dataSource: Address?
        access(all)
        let paths: StandardTokenPaths?
        access(all)
        let display: FTDisplayWithSource?

        view init(
            identity: FTIdentity,
            evmAddress: String,
            decimals: UInt8,
            tags: [String],
            dataSource: Address?,
            paths: StandardTokenPaths?,
            display: FTDisplayWithSource?,
        ) {
            self.identity = identity
            self.evmAddress = evmAddress
            self.decimals = decimals
            self.tags = tags
            self.dataSource = dataSource
            self.paths = paths
            self.display = display
        }

        access(all)
        view fun getIdentity(): {TokenIdentity} {
            return self.identity
        }
    }

    /// The enum for the Evaluation
    ///
    access(all) enum Evaluation: UInt8 {
        access(all) case UNVERIFIED
        access(all) case PENDING
        access(all) case VERIFIED
        access(all) case FEATURED
        access(all) case BLOCKED
    }

    /// The struct for the Review Comment
    ///
    access(all) struct ReviewComment {
        access(all)
        let comment: String
        access(all)
        let by: Address
        access(all)
        let at: UInt64

        view init(_ comment: String, _ by: Address) {
            self.comment = comment
            self.by = by
            self.at = UInt64(getCurrentBlock().timestamp)
        }
    }

    /// The struct for the FT Review
    ///
    access(all) struct FTReview {
        access(all)
        let comments: [ReviewComment]
        access(all)
        let tags: [String]
        access(all)
        var evalRank: Evaluation

        init(
            _ rank: Evaluation,
        ) {
            self.evalRank = rank
            self.tags = []
            self.comments = []
        }

        /// Get tags
        ///
        access(all)
        view fun getTags(): [String] {
            return self.tags
        }

        /// Get getEvaluationRank
        ///
        access(all)
        view fun getEvaluationRank(): Evaluation {
            return self.evalRank
        }

        /// Update the evaluation rank
        ///
        access(all)
        fun updateEvaluationRank(
            _ rank: Evaluation
        ) {
            self.evalRank = rank
        }

        /// Add a new comment to the review
        ///
        access(all)
        fun addComment(_ comment: String, _ by: Address) {
            self.comments.append(ReviewComment(comment, by))
        }

        /// Add a new tag to the review
        ///
        access(all)
        fun addTag(_ tag: String): Bool {
            if !self.tags.contains(tag) {
                self.tags.append(tag)
                return true
            }
            return false
        }
    }

    /// The struct for the Reviewer Info
    ///
    access(all) struct ReviewerInfo {
        access(all)
        let address: Address
        access(all)
        let verified: Bool
        access(all)
        let name: String?
        access(all)
        let url: String?
        access(all)
        let managedTokenAmt: Int
        access(all)
        let reviewedTokenAmt: Int
        access(all)
        let customziedTokenAmt: Int

        view init(
            address: Address,
            verified: Bool,
            name: String?,
            url: String?,
            _ managedTokenAmt: Int,
            _ reviewedTokenAmt: Int,
            _ customziedTokenAmt: Int,
        ) {
            self.address = address
            self.verified = verified
            self.name = name
            self.url = url
            self.managedTokenAmt = managedTokenAmt
            self.reviewedTokenAmt = reviewedTokenAmt
            self.customziedTokenAmt = customziedTokenAmt
        }
    }

    /** Editable FTView */

    /// The enum for the FT Capability Path
    ///
    access(all) enum FTCapPath: UInt8 {
        access(all) case receiver
        access(all) case metadata
        access(all) case provider
    }

    /// The interface for the Editable FT View Data
    ///
    access(all) resource interface EditableFTViewDataInterface {
        /// Identity of the FT
        access(all)
        let identity: FTIdentity
        // ----- FT Vault Data -----
        /// Get the Storage Path
        access(all)
        view fun getStoragePath(): StoragePath
        /// Get the Receiver Path
        access(all)
        view fun getReceiverPath(): PublicPath?
        /// Get the Metadata Path
        access(all)
        view fun getMetadataPath(): PublicPath?
        /// Get the Provider Path
        access(all)
        view fun getProviderPath(): PrivatePath?
        /// Get the Capability Path
        access(all)
        view fun getCapabilityType(_ capPath: FTCapPath): Type?
        // --- default implementation ---
        /// Check if the FT View Data is initialized
        ///
        access(all)
        view fun isInitialized(): Bool {
            return self.getReceiverPath() != nil &&
                self.getMetadataPath() != nil &&
                self.getProviderPath() != nil &&
                self.getCapabilityType(FTCapPath.receiver) != nil &&
                self.getCapabilityType(FTCapPath.metadata) != nil &&
                self.getCapabilityType(FTCapPath.provider) != nil
        }
        /// Get the FT Vault Data
        ///
        access(all)
        fun getFTVaultData(): FungibleTokenMetadataViews.FTVaultData {
            pre {
                self.isInitialized(): "FT View Data is not initialized"
            }
            let ftRef = self.identity.borrowFungibleTokenContract()
            let ftType = self.identity.buildType()
            return FungibleTokenMetadataViews.FTVaultData(
                storagePath: self.getStoragePath(),
                receiverPath: self.getReceiverPath()!,
                metadataPath: self.getMetadataPath()!,
                receiverLinkedType: Type<&{FungibleToken.Receiver}>(),
                metadataLinkedType: Type<&{FungibleToken.Vault}>(),
                createEmptyVaultFunction: (fun (): @{FungibleToken.Vault} {
                    return <- ftRef.createEmptyVault(vaultType: ftType)
                })
            )
        }
    }

    /// The interface for the Editable FT View Display
    ///
    access(all) resource interface EditableFTViewDisplayInterface: ViewResolver.Resolver {
        /// Identity of the FT
        access(all)
        let identity: FTIdentity
        // ----- FT Display -----
        access(all)
        view fun getSymbol(): String?
        access(all)
        view fun getName(): String?
        access(all)
        view fun getDescription(): String?
        access(all)
        view fun getExternalURL(): MetadataViews.ExternalURL?
        access(all)
        view fun getSocials(): {String: MetadataViews.ExternalURL}
        access(all)
        fun getLogos(): MetadataViews.Medias
        // --- default implementation ---
        /// Get the FT Display
        ///
        access(all)
        fun getFTDisplay(): FungibleTokenMetadataViews.FTDisplay {
            return FungibleTokenMetadataViews.FTDisplay(
                name: self.getName() ?? "Unknown Token",
                symbol: self.getSymbol() ?? "NONE",
                description: self.getDescription() ?? "No Description",
                externalURL: self.getExternalURL() ?? MetadataViews.ExternalURL("https://fixes.world"),
                logos: self.getLogos(),
                socials: self.getSocials()
            )
        }
    }

    /// The interface for the FT View Data Editor
    ///
    access(all) resource interface FTViewDataEditor: EditableFTViewDataInterface {
        /// Update the Storage Path
        access(Editable)
        fun updateStoragePath(_ storagePath: StoragePath)
        /// Set the FT Vault Data
        access(Editable)
        fun initializeVaultData(
            receiverPath: PublicPath,
            metadataPath: PublicPath,
            receiverType: Type,
            metadataType: Type,
        )
    }

    /// The interface for the FT View Display Editor
    ///
    access(all) resource interface FTViewDisplayEditor: EditableFTViewDisplayInterface {
        /// Set the FT Display
        access(Editable)
        fun setFTDisplay(
            name: String?,
            symbol: String?,
            description: String?,
            externalURL: String?,
            logo: String?,
            socials: {String: String}
        )
    }

    /// The Resource for the FT Display
    ///
    access(all) resource EditableFTDisplay: FTViewDisplayEditor, EditableFTViewDisplayInterface, ViewResolver.Resolver {
        access(all)
        let identity: FTIdentity
        access(contract)
        let metadata: {String: String}

        init(
            _ address: Address,
            _ contractName: String,
        ) {
            self.identity = FTIdentity(address, contractName)
            self.metadata = {}
        }

        /// Set the FT Display
        ///
        access(Editable)
        fun setFTDisplay(
            name: String?,
            symbol: String?,
            description: String?,
            externalURL: String?,
            logo: String?,
            socials: {String: String}
        ) {
            // set name
            if name != nil {
                self.metadata["name"] = name!
            }
            // set symbol
            if symbol != nil {
                self.metadata["symbol"] = symbol!
            }
            // set description
            if description != nil {
                self.metadata["description"] = description!
            }
            // set external URL
            if externalURL != nil {
                self.metadata["externalURL"] = externalURL!
            }
            // set logo
            if logo != nil {
                // the last 3 chars are file type, check the type
                let fileType = logo!.slice(from: logo!.length - 3, upTo: logo!.length)
                if fileType == "png" {
                    self.metadata["logo:png"] = logo!
                } else if fileType == "svg" {
                    self.metadata["logo:svg"] = logo!
                } else if fileType == "jpg" {
                    self.metadata["logo:jpg"] = logo!
                } else {
                    self.metadata["logo"] = logo!
                }
            }
            // set socials
            for key in socials.keys {
                self.metadata["social:".concat(key)] = socials[key]!
            }

            // Emit the event
            emit FTDisplayUpdated(
                address: self.identity.address,
                contractName: self.identity.contractName,
                name: name,
                symbol: symbol,
                description: description,
                externalURL: externalURL,
                logo: logo,
                socials: socials
            )
        }

        /** ---- Implement the EditableFTViewDisplayInterface ---- */

        access(all)
        view fun getSymbol(): String? {
            return self.metadata["symbol"]
        }

        access(all)
        view fun getName(): String? {
            return self.metadata["name"]
        }

        access(all)
        view fun getDescription(): String? {
            return self.metadata["description"]
        }

        access(all)
        view fun getExternalURL(): MetadataViews.ExternalURL? {
            let url = self.metadata["externalURL"]
            return url != nil ? MetadataViews.ExternalURL(url!) : nil
        }

        access(all)
        fun getLogos(): MetadataViews.Medias {
            let medias: [MetadataViews.Media] = []
            if self.metadata["logo:png"] != nil {
                medias.append(MetadataViews.Media(
                    file: MetadataViews.HTTPFile(url: self.metadata["logo:png"]!),
                    mediaType: "image/png" // default is png
                ))
            }
            if self.metadata["logo:svg"] != nil {
                medias.append(MetadataViews.Media(
                    file: MetadataViews.HTTPFile(url: self.metadata["logo:svg"]!),
                    mediaType: "image/svg+xml"
                ))
            }
            if self.metadata["logo:jpg"] != nil {
                medias.append(MetadataViews.Media(
                    file: MetadataViews.HTTPFile(url: self.metadata["logo:jpg"]!),
                    mediaType: "image/jpeg"
                ))
            }
            if self.metadata["logo"] != nil {
                medias.append(MetadataViews.Media(
                    file: MetadataViews.HTTPFile(url: self.metadata["logo"]!),
                    mediaType: "image/*"
                ))
            }
            // add default icon
            if medias.length == 0 {
                let ticker = self.getSymbol() ?? self.getName() ?? "NONE"
                let tickNameSize = 80 + (10 - ticker.length > 0 ? 10 - ticker.length : 0) * 12
                let svgStr = "data:image/svg+xml;utf8,"
                    .concat("%3Csvg%20xmlns%3D%5C%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%5C%22%20viewBox%3D%5C%22-256%20-256%20512%20512%5C%22%20width%3D%5C%22512%5C%22%20height%3D%5C%22512%5C%22%3E")
                    .concat("%3Cdefs%3E%3ClinearGradient%20gradientUnits%3D%5C%22userSpaceOnUse%5C%22%20x1%3D%5C%220%5C%22%20y1%3D%5C%22-240%5C%22%20x2%3D%5C%220%5C%22%20y2%3D%5C%22240%5C%22%20id%3D%5C%22gradient-0%5C%22%20gradientTransform%3D%5C%22matrix(0.908427%2C%20-0.41805%2C%200.320369%2C%200.696163%2C%20-69.267567%2C%20-90.441103)%5C%22%3E%3Cstop%20offset%3D%5C%220%5C%22%20style%3D%5C%22stop-color%3A%20rgb(244%2C%20246%2C%20246)%3B%5C%22%3E%3C%2Fstop%3E%3Cstop%20offset%3D%5C%221%5C%22%20style%3D%5C%22stop-color%3A%20rgb(35%2C%20133%2C%2091)%3B%5C%22%3E%3C%2Fstop%3E%3C%2FlinearGradient%3E%3C%2Fdefs%3E")
                    .concat("%3Cellipse%20style%3D%5C%22fill%3A%20rgb(149%2C%20225%2C%20192)%3B%20stroke-width%3A%201rem%3B%20paint-order%3A%20fill%3B%20stroke%3A%20url(%23gradient-0)%3B%5C%22%20ry%3D%5C%22240%5C%22%20rx%3D%5C%22240%5C%22%3E%3C%2Fellipse%3E")
                    .concat("%3Ctext%20style%3D%5C%22dominant-baseline%3A%20middle%3B%20fill%3A%20rgb(80%2C%20213%2C%20155)%3B%20font-family%3A%20system-ui%2C%20sans-serif%3B%20text-anchor%3A%20middle%3B%5C%22%20fill-opacity%3D%5C%220.2%5C%22%20y%3D%5C%22-12%5C%22%20font-size%3D%5C%22420%5C%22%3E%F0%9D%94%89%3C%2Ftext%3E")
                    .concat("%3Ctext%20style%3D%5C%22dominant-baseline%3A%20middle%3B%20fill%3A%20rgb(244%2C%20246%2C%20246)%3B%20font-family%3A%20system-ui%2C%20sans-serif%3B%20text-anchor%3A%20middle%3B%20font-style%3A%20italic%3B%20font-weight%3A%20700%3B%5C%22%20y%3D%5C%2212%5C%22%20font-size%3D%5C%22").concat(tickNameSize.toString()).concat("%5C%22%3E")
                    .concat(ticker).concat("%3C%2Ftext%3E%3C%2Fsvg%3E")
                medias.append(MetadataViews.Media(
                    file: MetadataViews.HTTPFile(url: svgStr),
                    mediaType: "image/svg+xml"
                ))
            }
            return MetadataViews.Medias(medias)
        }

        access(all)
        view fun getSocials(): {String: MetadataViews.ExternalURL} {
            let ret: {String: MetadataViews.ExternalURL} = {}
            let socialKey = "social:"
            let socialKeyLen = socialKey.length
            for key in self.metadata.keys {
                if key.length >= socialKeyLen && key.slice(from: 0, upTo: socialKey.length) == socialKey {
                    let socialName = key.slice(from: socialKey.length, upTo: key.length)
                    ret[socialName] = MetadataViews.ExternalURL(self.metadata[key]!)
                }
            }
            return ret
        }

        /* --- Implement the MetadataViews.Resolver --- */

        access(all)
        view fun getViews(): [Type] {
            return [
                Type<FungibleTokenMetadataViews.FTDisplay>()
            ]
        }

        access(all)
        fun resolveView(_ view: Type): AnyStruct? {
            switch view {
                case Type<FungibleTokenMetadataViews.FTDisplay>():
                    return self.getFTDisplay()
            }
            return nil
        }
    }

    /// Create the FT View Data
    ///
    access(all)
    fun createEditableFTDisplay(
        _ address: Address,
        _ contractName: String,
    ): @EditableFTDisplay {
        return <- create EditableFTDisplay(address, contractName)
    }

    /// The Resource for the FT View
    ///
    access(all) resource EditableFTView: FTViewDataEditor, EditableFTViewDataInterface, FTViewDisplayEditor, EditableFTViewDisplayInterface, ViewResolver.Resolver {
        access(self)
        let display: @EditableFTDisplay
        access(all)
        let identity: FTIdentity
        access(contract)
        var storagePath: StoragePath
        access(contract)
        let capabilityPaths: {FTCapPath: CapabilityPath}
        access(contract)
        let capabilityTypes: {FTCapPath: Type}

        init(
            _ address: Address,
            _ contractName: String,
            _ storagePath: StoragePath,
        ) {
            self.identity = FTIdentity(address, contractName)
            self.display <- create EditableFTDisplay(address, contractName)
            self.capabilityPaths = {}
            self.capabilityTypes = {}
            self.storagePath = storagePath
        }

        // ---- Writable Functions ----

        /// Update the Storage Path
        ///
        access(Editable)
        fun updateStoragePath(_ storagePath: StoragePath) {
            self.storagePath = storagePath

            emit FTViewStoragePathUpdated(
                address: self.identity.address,
                contractName: self.identity.contractName,
                storagePath: storagePath
            )
        }

        /// Initialize the FT View Data
        ///
        access(Editable)
        fun initializeVaultData(
            receiverPath: PublicPath,
            metadataPath: PublicPath,
            receiverType: Type,
            metadataType: Type,
        ) {
            self.capabilityPaths[FTCapPath.receiver] = receiverPath
            self.capabilityPaths[FTCapPath.metadata] = metadataPath
            self.capabilityTypes[FTCapPath.receiver] = receiverType
            self.capabilityTypes[FTCapPath.metadata] = metadataType

            // Emit the event
            emit FTVaultDataUpdated(
                address: self.identity.address,
                contractName: self.identity.contractName,
                storagePath: self.storagePath,
                receiverPath: receiverPath,
                metadataPath: metadataPath,
                receiverType: receiverType,
                metadataType: metadataType
            )
        }

        /** ---- Implement the EditableFTViewDataInterface ---- */

        access(all)
        view fun getStoragePath(): StoragePath {
            return self.storagePath
        }

        /// Get the Receiver Path
        access(all)
        view fun getReceiverPath(): PublicPath? {
            return self.capabilityPaths[FTCapPath.receiver] as! PublicPath?
        }

        /// Get the Metadata Path
        access(all)
        view fun getMetadataPath(): PublicPath? {
            return self.capabilityPaths[FTCapPath.metadata] as! PublicPath?
        }

        /// Get the Provider Path
        access(all)
        view fun getProviderPath(): PrivatePath? {
            return self.capabilityPaths[FTCapPath.provider] as! PrivatePath?
        }

        /// Get the Capability Path
        access(all)
        view fun getCapabilityType(_ capPath: FTCapPath): Type? {
            return self.capabilityTypes[capPath]
        }

        /** ---- Implement the FTViewDataEditor ---- */

        /// Set the FT Display
        ///
        access(Editable)
        fun setFTDisplay(
            name: String?,
            symbol: String?,
            description: String?,
            externalURL: String?,
            logo: String?,
            socials: {String: String}
        ) {
            self.display.setFTDisplay(
                name: name,
                symbol: symbol,
                description: description,
                externalURL: externalURL,
                logo: logo,
                socials: socials
            )
        }

        /** ---- Implement the FTViewDisplayInterface ---- */

        access(all)
        view fun getSymbol(): String? {
            return self.display.getSymbol()
        }

        access(all)
        view fun getName(): String? {
            return self.display.getName()
        }

        access(all)
        view fun getDescription(): String? {
            return self.display.getDescription()
        }

        access(all)
        view fun getExternalURL(): MetadataViews.ExternalURL? {
            return self.display.getExternalURL()
        }

        access(all)
        fun getLogos(): MetadataViews.Medias {
            return self.display.getLogos()
        }

        access(all)
        view fun getSocials(): {String: MetadataViews.ExternalURL} {
            return self.display.getSocials()
        }

        /* --- Implement the MetadataViews.Resolver --- */

        access(all)
        view fun getViews(): [Type] {
            return [
                Type<MetadataViews.ExternalURL>(),
                Type<FungibleTokenMetadataViews.FTView>(),
                Type<FungibleTokenMetadataViews.FTDisplay>(),
                Type<FungibleTokenMetadataViews.FTVaultData>()
            ]
        }

        access(all)
        fun resolveView(_ view: Type): AnyStruct? {
            switch view {
                case Type<MetadataViews.ExternalURL>():
                    return self.getExternalURL()
                case Type<FungibleTokenMetadataViews.FTView>():
                    return FungibleTokenMetadataViews.FTView(
                        ftDisplay: self.getFTDisplay(),
                        ftVaultData: self.getFTVaultData()
                    )
                case Type<FungibleTokenMetadataViews.FTDisplay>():
                    return self.getFTDisplay()
                case Type<FungibleTokenMetadataViews.FTVaultData>():
                    return self.getFTVaultData()
            }
            return nil
        }
    }

    /// Create the FT View Data
    ///
    access(all)
    fun createEditableFTView(
        _ address: Address,
        _ contractName: String,
        _ storagePath: StoragePath,
    ): @EditableFTView {
        return <- create EditableFTView(address, contractName, storagePath)
    }

    /// Build the FT Vault Type
    ///
    access(all)
    view fun buildFTVaultType(_ address: Address, _ contractName: String): Type? {
        let addrStr = address.toString()
        let addrStrNo0x = addrStr.slice(from: 2, upTo: addrStr.length)
        return CompositeType("A.".concat(addrStrNo0x).concat(".").concat(contractName).concat(".Vault"))
    }
}

```