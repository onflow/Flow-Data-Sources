# Source: https://github.com/fixes-world/token-list/blob/main/cadence/contracts/NFTViewUtils.cdc

```
/**
> Author: Fixes Lab <https://github.com/fixes-world/>

# NFT List - An on-chain list of Flow Standard Non-Fungible Tokens (NFTs).

This is the Non-Fungible Token view utilties contract of the Token List.

*/
import "MetadataViews"
import "ViewResolver"
import "NonFungibleToken"
// TokenList Imports
import "FTViewUtils"

access(all) contract NFTViewUtils {

    // ----- Entitlement -----

    // An entitlement for allowing edit the FT View Data
    access(all) entitlement Editable

    /*  ---- Events ---- */

    access(all) event NFTDisplayUpdated(
        address: Address,
        contractName: String,
        name: String?,
        description: String?,
        externalURL: String?,
        squareImage: String?,
        bannerImage: String?,
        socials: {String: String}
    )

    /// The struct for the Fungible Token Identity
    ///
    access(all) struct NFTIdentity: FTViewUtils.TokenIdentity {
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
            return self.buildCollectionType()
        }

        access(all)
        view fun buildCollectionType(): Type {
            return NFTViewUtils.buildCollectionType(self.address, self.contractName)
                ?? panic("Could not build the FT Type")
        }

        access(all)
        view fun buildNFTType(): Type {
            return NFTViewUtils.buildNFTType(self.address, self.contractName)
                ?? panic("Could not build the FT Type")
        }

        /// Borrow the Fungible Token Contract
        ///
        access(all)
        fun borrowNFTContract(): &{NonFungibleToken} {
            return getAccount(self.address)
                .contracts.borrow<&{NonFungibleToken}>(name: self.contractName)
                ?? panic("Could not borrow the FungibleToken contract reference")
        }
    }

    /// The struct for the Fungible Token Display with Source
    ///
    access(all) struct NFTCollectionViewWithSource {
        access(all)
        let source: Address?
        access(all)
        let display: MetadataViews.NFTCollectionDisplay

        view init(
            _ source: Address?,
            _ display: MetadataViews.NFTCollectionDisplay
        ) {
            self.source = source
            self.display = display
        }
    }

    /// The struct for the Fungible Token Paths
    ///
    access(all) struct StandardNFTPaths {
        access(all)
        let storagePath: StoragePath
        access(all)
        let publicPath: PublicPath

        view init(
            _ storagePath: StoragePath,
            _ publicPath: PublicPath,
        ) {
            self.storagePath = storagePath
            self.publicPath = publicPath
        }
    }

    /// The struct for the Fungible Token List View
    ///
    access(all) struct StandardTokenView: FTViewUtils.ITokenView {
        access(all)
        let identity: NFTIdentity
        access(all)
        let tags: [String]
        access(all)
        let dataSource: Address?
        access(all)
        let paths: StandardNFTPaths?
        access(all)
        let display: NFTCollectionViewWithSource?

        view init(
            identity: NFTIdentity,
            tags: [String],
            dataSource: Address?,
            paths: StandardNFTPaths?,
            display: NFTCollectionViewWithSource?,
        ) {
            self.identity = identity
            self.tags = tags
            self.dataSource = dataSource
            self.paths = paths
            self.display = display
        }

        access(all)
        view fun getIdentity(): {FTViewUtils.TokenIdentity} {
            return self.identity
        }
    }

    /// The struct for the Bridged Token List View
    ///
    access(all) struct BridgedTokenView: FTViewUtils.IBridgedTokenView, FTViewUtils.ITokenView {
        access(all)
        let identity: NFTIdentity
        access(all)
        let evmAddress: String
        access(all)
        let tags: [String]
        access(all)
        let dataSource: Address?
        access(all)
        let paths: StandardNFTPaths?
        access(all)
        let display: NFTCollectionViewWithSource?

        view init(
            identity: NFTIdentity,
            evmAddress: String,
            tags: [String],
            dataSource: Address?,
            paths: StandardNFTPaths?,
            display: NFTCollectionViewWithSource?,
        ) {
            self.identity = identity
            self.evmAddress = evmAddress
            self.tags = tags
            self.dataSource = dataSource
            self.paths = paths
            self.display = display
        }

        access(all)
        view fun getIdentity(): {FTViewUtils.TokenIdentity} {
            return self.identity
        }
    }

    /** Editable NFTView */

    /// The interface for the Editable FT View Display
    ///
    access(all) resource interface EditableNFTCollectionDisplayInterface: ViewResolver.Resolver {
        /// Identity of the FT
        access(all)
        let identity: NFTIdentity
        // ----- FT Display -----
        access(all)
        view fun getName(): String?
        access(all)
        view fun getDescription(): String?
        access(all)
        view fun getExternalURL(): MetadataViews.ExternalURL?
        access(all)
        view fun getSocials(): {String: MetadataViews.ExternalURL}
        // Square-sized image to represent this collection.
        access(all)
        view fun getSquareImage(): MetadataViews.Media?
        // Banner-sized image for this collection, recommended to have a size near 1200x630.
        access(all)
        view fun getBannerImage(): MetadataViews.Media?
        // Get all the images
        access(all)
        fun getImages(): MetadataViews.Medias
        // --- default implementation ---
        // Get the default square image
        access(all)
        view fun getDefaultSquareImage(): MetadataViews.Media {
            return MetadataViews.Media(
                file: MetadataViews.HTTPFile(url: "https://i.imgur.com/hs3U5CY.png"),
                mediaType: "image/png"
            )
        }
        // Get the default banner image
        //
        access(all)
        view fun getDefaultBannerImage(): MetadataViews.Media {
            return MetadataViews.Media(
                file: MetadataViews.HTTPFile(url: "https://i.imgur.com/4DOuqFf.jpeg"),
                mediaType: "image/jpeg"
            )
        }
        /// Get the FT Display
        ///
        access(all)
        fun getCollectionDisplay(): MetadataViews.NFTCollectionDisplay {
            return MetadataViews.NFTCollectionDisplay(
                name: self.getName() ?? "Unknown Token",
                description: self.getDescription() ?? "No Description",
                externalURL: self.getExternalURL() ?? MetadataViews.ExternalURL("https://fixes.world"),
                // Square-sized image to represent this collection.
                squareImage: self.getSquareImage() ?? self.getDefaultSquareImage(),
                // Banner-sized image for this collection, recommended to have a size near 1200x630.
                bannerImage: self.getBannerImage() ?? self.getDefaultBannerImage(),
                socials: self.getSocials()
            )
        }
    }

    /// The interface for the FT View Display Editor
    ///
    access(all) resource interface NFTCollectionDisplayEditor: EditableNFTCollectionDisplayInterface {
        /// Set the FT Display
        access(Editable)
        fun setDisplay(
            name: String?,
            description: String?,
            externalURL: String?,
            squareImage: String?,
            bannerImage: String?,
            socials: {String: String}
        )
    }

    /// The Resource for the FT Display
    ///
    access(all) resource EditableNFTCollectionDisplay: NFTCollectionDisplayEditor, EditableNFTCollectionDisplayInterface {
        access(all)
        let identity: NFTIdentity
        access(contract)
        let metadata: {String: String}

        init(
            _ address: Address,
            _ contractName: String,
        ) {
            self.identity = NFTIdentity(address, contractName)
            self.metadata = {}
            // ensure identity is valid
            self.identity.borrowNFTContract()
        }

        /// Set the FT Display
        ///
        access(Editable)
        fun setDisplay(
            name: String?,
            description: String?,
            externalURL: String?,
            squareImage: String?,
            bannerImage: String?,
            socials: {String: String}
        ) {
            // set name
            if name != nil {
                self.metadata["name"] = name!
            }
            // set description
            if description != nil {
                self.metadata["description"] = description!
            }
            // set external URL
            if externalURL != nil {
                self.metadata["externalURL"] = externalURL!
            }
            // set squareImage
            if squareImage != nil {
                // the last 3 chars are file type, check the type
                let fileType = squareImage!.slice(from: squareImage!.length - 3, upTo: squareImage!.length)
                if fileType == "png" {
                    self.metadata["image:square:png"] = squareImage!
                } else if fileType == "svg" {
                    self.metadata["image:square:svg"] = squareImage!
                } else if fileType == "jpg" {
                    self.metadata["image:square:jpg"] = squareImage!
                } else {
                    self.metadata["image:square"] = squareImage!
                }
            }
            // set bannerImage
            if bannerImage != nil {
                // the last 3 chars are file type, check the type
                let fileType = bannerImage!.slice(from: bannerImage!.length - 3, upTo: bannerImage!.length)
                if fileType == "png" {
                    self.metadata["image:banner:png"] = bannerImage!
                } else if fileType == "svg" {
                    self.metadata["image:banner:svg"] = bannerImage!
                } else if fileType == "jpg" {
                    self.metadata["image:banner:jpg"] = bannerImage!
                } else {
                    self.metadata["image:banner"] = bannerImage!
                }
            }
            // set socials
            for key in socials.keys {
                self.metadata["social:".concat(key)] = socials[key]!
            }

            // Emit the event
            emit NFTDisplayUpdated(
                address: self.identity.address,
                contractName: self.identity.contractName,
                name: name,
                description: description,
                externalURL: externalURL,
                squareImage: squareImage,
                bannerImage: bannerImage,
                socials: socials
            )
        }

        /** ---- Implement the EditableFTViewDisplayInterface ---- */

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

        access(self)
        view fun getImage(_ key: String, _ type: String?): MetadataViews.Media? {
            var keyName = "image:".concat(key)
            if type != nil && (type == "svg" || type == "png" || type == "jpg") {
                keyName = keyName.concat(":").concat(type!)
            }
            if self.metadata[keyName] != nil {
                let mediaType = type == "svg"
                    ? "image/svg+xml"
                    : type == "png"
                        ? "image/png"
                        : type == "jpg"
                            ? "image/jpeg"
                            : "image/*"
                return MetadataViews.Media(
                    file: MetadataViews.HTTPFile(url: self.metadata[keyName]!),
                    mediaType: mediaType
                )
            }
            return nil
        }

        access(all)
        view fun getBannerImage(): MetadataViews.Media? {
            return self.getImage("banner", "svg") ?? self.getImage("banner", "png") ?? self.getImage("banner", "jpg") ?? self.getImage("banner", nil)
        }

        access(all)
        view fun getSquareImage(): MetadataViews.Media? {
            return self.getImage("square", "svg") ?? self.getImage("square", "png") ?? self.getImage("square", "jpg") ?? self.getImage("square", nil)
        }

        /// Get all the images
        ///
        access(all)
        fun getImages(): MetadataViews.Medias {
            let medias: [MetadataViews.Media] = []
            if let bannerSvg = self.getImage("banner", "svg") {
                medias.append(bannerSvg)
            }
            if let bannerPng = self.getImage("banner", "png") {
                medias.append(bannerPng)
            }
            if let bannerJpg = self.getImage("banner", "jpg") {
                medias.append(bannerJpg)
            }
            if let squareSvg = self.getImage("square", "svg") {
                medias.append(squareSvg)
            }
            if let squarePng = self.getImage("square", "png") {
                medias.append(squarePng)
            }
            if let squareJpg = self.getImage("square", "jpg") {
                medias.append(squareJpg)
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
                Type<MetadataViews.NFTCollectionDisplay>(),
                Type<MetadataViews.Medias>()
            ]
        }

        access(all)
        fun resolveView(_ view: Type): AnyStruct? {
            switch view {
                case Type<MetadataViews.NFTCollectionDisplay>():
                    return self.getCollectionDisplay()
                case Type<MetadataViews.Medias>():
                    return self.getImages()
            }
            return nil
        }
    }

    /// Create the FT View Data
    ///
    access(all)
    fun createEditableCollectionDisplay(
        _ address: Address,
        _ contractName: String,
    ): @EditableNFTCollectionDisplay {
        return <- create EditableNFTCollectionDisplay(address, contractName)
    }

    /// Build the NFT Type
    ///
    access(all)
    view fun buildNFTType(_ address: Address, _ contractName: String): Type? {
        let addrStr = address.toString()
        let addrStrNo0x = addrStr.slice(from: 2, upTo: addrStr.length)
        return CompositeType("A.".concat(addrStrNo0x).concat(".").concat(contractName).concat(".NFT"))
    }

    /// Build the NFT Collection Type
    ///
    access(all)
    view fun buildCollectionType(_ address: Address, _ contractName: String): Type? {
        let addrStr = address.toString()
        let addrStrNo0x = addrStr.slice(from: 2, upTo: addrStr.length)
        return CompositeType("A.".concat(addrStrNo0x).concat(".").concat(contractName).concat(".Collection"))
    }
}

```