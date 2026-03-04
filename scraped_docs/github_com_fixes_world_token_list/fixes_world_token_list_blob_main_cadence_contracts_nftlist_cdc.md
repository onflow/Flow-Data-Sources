# Source: https://github.com/fixes-world/token-list/blob/main/cadence/contracts/NFTList.cdc

```
/**
> Author: Fixes Lab <https://github.com/fixes-world/>

# NFT List - An on-chain list of Flow Standard Non-Fungible Tokens (NFTs).

This is the basic contract of the NFT List.
It will be used to store the list of all the Flow Standard Non-Fungible Tokens (NFTs) that are available on the Flow blockchain.

*/
import "NonFungibleToken"
import "MetadataViews"
import "ViewResolver"
// TokenList Imports
import "ViewResolvers"
import "FTViewUtils"
import "NFTViewUtils"

/// NFT List registry contract
///
access(all) contract NFTList {

    /* --- Entitlement --- */

    access(all) entitlement Maintainer
    access(all) entitlement SuperAdmin


    /* --- Events --- */

    /// Event emitted when the contract is initialized
    access(all) event ContractInitialized()

    /// Event emitted when a new Non-Fungible Token is registered
    access(all) event NFTCollectionRegistered(
        _ address: Address,
        _ contractName: String,
        _ type: Type,
    )
    /// Event emitted when a new Non-Fungible Token is removed
    access(all) event NFTCollectionRemoved(
        _ address: Address,
        _ contractName: String,
        _ type: Type,
    )
    /// Event emitted when Reviewer Metadata is updated
    access(all) event NFTListReviewerMetadataUpdated(
        _ reviewer: Address,
        name: String?,
        url: String?,
    )
    /// Event emitted when reviewer rank is updated
    access(all) event NFTListReviewerVerifiedUpdated(
        _ reviewer: Address,
        _ isVerified: Bool
    )
    /// Event emitted when reviewer rank is updated
    access(all) event NFTListReviewerRankUpdated(
        _ reviewer: Address,
        _ rank: UInt8
    )
    /// Evenit emitted when an Editable FTDisplay is created
    access(all) event NFTListReviewerEditableNFTCollectionDisplayCreated(
        _ address: Address,
        _ contractName: String,
        reviewer: Address
    )
    /// Event emitted when a new Non-Fungible Token is reviewed
    access(all) event NFTCollectionViewResolverUpdated(
        _ address: Address,
        _ contractName: String,
        _ newResolverIdentifier: String
    )
    /// Event emitted when a Non-Fungible Token is evaluated
    access(all) event NFTCollectionReviewEvaluated(
        _ address: Address,
        _ contractName: String,
        _ rank: UInt8,
        _ by: Address
    )
    /// Event emitted when a Non-Fungible Token is tagged
    access(all) event NFTCollectionTagsAdded(
        _ address: Address,
        _ contractName: String,
        _ tags: [String],
        _ by: Address
    )

    /* --- Variable, Enums and Structs --- */

    access(all) let registryStoragePath: StoragePath
    access(all) let registryPublicPath: PublicPath
    access(all) let reviewerStoragePath: StoragePath
    access(all) let reviewerPublicPath: PublicPath
    access(all) let maintainerStoragePath: StoragePath

    /* --- Interfaces & Resources --- */

    /// Interface for the FT Entry
    ///
    access(all) resource interface NFTEntryInterface {
        /// Create an empty collection for the NFT
        access(all)
        fun createEmptyCollection(): @{NonFungibleToken.Collection}
        // ----- View Methods -----
        access(all)
        view fun getIdentity(): NFTViewUtils.NFTIdentity
        /// Get the NFT Type
        access(all)
        view fun getNFTType(): Type
        /// Get the Collection Type
        access(all)
        view fun getCollectionType(): Type
        /// Check if the Non-Fungible Token is reviewed by some one
        access(all)
        view fun isReviewedBy(_ reviewer: Address): Bool
        /// Get the Non-Fungible Token Review
        access(all)
        view fun getReview(_ reviewer: Address): FTViewUtils.FTReview?
        /// Get the display metadata of the FT, fallback to the highest rank reviewer
        access(all)
        fun getDisplay(_ reviewer: Address?): NFTViewUtils.NFTCollectionViewWithSource?
        // ----- Quick Access For FTViews -----
        /// Get the evaluation rank of the Non-Fungible Token, no fallback
        access(all)
        view fun getEvaluatedRank(_ reviewer: Address?): FTViewUtils.Evaluation? {
            if let reviewerAddr = reviewer {
                if let reviewRef = self.borrowReviewRef(reviewerAddr) {
                    return reviewRef.getEvaluationRank()
                }
            }
            return nil
        }
        /// Get the tags of the Fungiuble Token, fallback to the highest rank reviewer
        access(all)
        fun getTags(_ reviewer: Address?): [String] {
            if let fallbackedReviewerAddr = self.tryGetReviewer(reviewer) {
                if let reviewRef = self.borrowReviewRef(fallbackedReviewerAddr) {
                    let returnTags = reviewRef.getTags()
                    // Add extra tags based on the evaluation rank if the reviewer is the fallbackedReviewer
                    if reviewer == fallbackedReviewerAddr {
                        if reviewRef.evalRank.rawValue == FTViewUtils.Evaluation.BLOCKED.rawValue {
                            returnTags.insert(at: 0, "Blocked")
                        } else if reviewRef.evalRank.rawValue == FTViewUtils.Evaluation.FEATURED.rawValue {
                            returnTags.insert(at: 0, "Featured")
                            returnTags.insert(at: 0, "Verified")
                        } else if reviewRef.evalRank.rawValue == FTViewUtils.Evaluation.VERIFIED.rawValue {
                            returnTags.insert(at: 0, "Verified")
                        } else if reviewRef.evalRank.rawValue == FTViewUtils.Evaluation.PENDING.rawValue {
                            returnTags.insert(at: 0, "Pending")
                        }
                    }
                    return returnTags
                }
            }
            return []
        }
        // ----- Internal Methods: Used by Reviewer -----
        /// Try to get a reviewer address
        access(contract)
        view fun tryGetReviewer(_ reviewer: Address?): Address? {
            var reviewerAddr = reviewer
            if reviewerAddr == nil {
                let registry = NFTList.borrowRegistry()
                reviewerAddr = registry.getHighestRankVerifiedCustomizedReviewer(self.getNFTType())
            }
            return reviewerAddr
        }
        access(contract)
        view fun borrowReviewRef(_ reviewer: Address): &FTViewUtils.FTReview?
        /// Add a new review to the FT
        access(contract)
        fun addReview(_ reviewer: Address, _ review: FTViewUtils.FTReview)
    }

    /// Resource for the Non-Fungible Token Entry
    ///
    access(all) resource NFTCollectionEntry: NFTEntryInterface {
        access(all)
        let identity: NFTViewUtils.NFTIdentity
        // Reviewer => FTReview
        access(self)
        let reviewers: {Address: FTViewUtils.FTReview}
        // view resolver
        access(all)
        var viewResolver: @{ViewResolver.Resolver}

        init(
            _ address: Address,
            _ contractName: String,
        ) {
            self.reviewers = {}
            self.identity = NFTViewUtils.NFTIdentity(address, contractName)
            self.viewResolver <- ViewResolvers.createContractViewResolver(address: address, contractName: contractName)
            // ensure display and vault exists
            self.getDisplay(nil)
            self.getCollectionData()
        }

        // ----- Implementing the FTMetadataInterface -----

        /// Create an empty vault for the FT
        ///
        access(all)
        fun createEmptyCollection(): @{NonFungibleToken.Collection} {
            let contractRef = self.borrowNFTContract()
            let nftType = self.identity.buildNFTType()
            return <- contractRef.createEmptyCollection(nftType: nftType)
        }

        /// Get the Non-Fungible Token Identity
        ///
        access(all)
        view fun getIdentity(): NFTViewUtils.NFTIdentity {
            return self.identity
        }

        /// Check if the Non-Fungible Token is reviewed by some one
        ///
        access(all)
        view fun isReviewedBy(_ reviewer: Address): Bool {
            return self.reviewers[reviewer] != nil
        }

        /// Get the Non-Fungible Token Review
        ///
        access(all)
        view fun getReview(_ reviewer: Address): FTViewUtils.FTReview? {
            return self.reviewers[reviewer]
        }

        /// Get the display metadata of the FT
        ///
        access(all)
        fun getDisplay(_ reviewer: Address?): NFTViewUtils.NFTCollectionViewWithSource? {
            var source: Address? = nil

            let viewResolver = self.borrowViewResolver()
            var retNFTDisplay = MetadataViews.getNFTCollectionDisplay(viewResolver)

            var reviewerAddr = self.tryGetReviewer(reviewer)
            if let addr = reviewerAddr {
                if let reviewerRef = NFTList.borrowReviewerPublic(addr) {
                    if let displayRef = reviewerRef.borrowNFTCollectionDisplayReader(self.identity.address, self.identity.contractName) {
                        let socials = retNFTDisplay?.socials ?? {}
                        let extraSocials = displayRef.getSocials()
                        for key in extraSocials.keys {
                            socials[key] = extraSocials[key]
                        }
                        source = addr
                        retNFTDisplay = MetadataViews.NFTCollectionDisplay(
                            name: displayRef.getName() ?? retNFTDisplay?.name ?? "Unkonwn",
                            description: displayRef.getDescription() ?? retNFTDisplay?.description ?? "No Description",
                            externalURL: displayRef.getExternalURL() ?? retNFTDisplay?.externalURL ?? MetadataViews.ExternalURL("https://fixes.world"),
                            squareImage: displayRef.getSquareImage() ?? retNFTDisplay?.squareImage ?? displayRef.getDefaultSquareImage(),
                            bannerImage: displayRef.getBannerImage() ?? retNFTDisplay?.bannerImage ?? displayRef.getDefaultBannerImage(),
                            socials: socials
                        )
                    }
                }
            }
            return retNFTDisplay != nil
                ? NFTViewUtils.NFTCollectionViewWithSource(source, retNFTDisplay!)
                : nil
        }

        /// Get the vault data of the FT
        ///
        access(all)
        fun getCollectionData(): MetadataViews.NFTCollectionData {
            return MetadataViews.getNFTCollectionData(self.borrowViewResolver())
                ?? panic("Failed to load the NFT Collection Data for ".concat(self.identity.toString()))
        }

        /// Get the FT Type
        access(all)
        view fun getNFTType(): Type {
            return self.identity.buildNFTType()
        }
        /// Get the Collection Type
        access(all)
        view fun getCollectionType(): Type {
            return self.identity.buildCollectionType()
        }

        // ----- Internal Methods -----

        /// Add a new review to the FT
        ///
        access(contract)
        fun addReview(_ reviewer: Address, _ review: FTViewUtils.FTReview) {
            pre {
                self.reviewers[reviewer] == nil:
                    "Reviewer already exists"
            }
            self.reviewers[reviewer] = review
        }

        /// Borrow the review reference
        ///
        access(contract)
        view fun borrowReviewRef(_ reviewer: Address): &FTViewUtils.FTReview? {
            return &self.reviewers[reviewer]
        }

        /// Borrow the View Resolver
        ///
        access(contract)
        view fun borrowViewResolver(): &{ViewResolver.Resolver} {
            return &self.viewResolver
        }

        /// Borrow the Non-Fungible Token Contract
        ///
        access(contract)
        fun borrowNFTContract(): &{NonFungibleToken} {
            return self.identity.borrowNFTContract()
        }
    }

    /// Interface for the Non-Fungible Token Reviewer
    ///
    access(all) resource interface NFTListReviewerInterface {
        access(all)
        view fun getAddress(): Address {
            return self.owner?.address ?? panic("Owner not found")
        }
        access(all)
        view fun getName(): String? {
            let metadata = self.getMetadata()
            return metadata["name"]
        }
        access(all)
        view fun getUrl(): String? {
            let metadata = self.getMetadata()
            return metadata["url"]
        }
        access(all)
        view fun getMetadata(): {String: String}
        access(all)
        view fun getReviewedNFTAmount(): Int
        access(all)
        view fun getCustomizedNFTAmount(): Int
        access(all)
        view fun getReviewedNFTTypes(): [Type]
        access(all)
        view fun getFeaturedNFTTypes(): [Type]
        access(all)
        view fun getVerifiedNFTTypes(): [Type]
        access(all)
        view fun getBlockedNFTTypes(): [Type]
        access(all)
        view fun borrowNFTCollectionDisplayReaderByNftType(_ nftType: Type): &NFTViewUtils.EditableNFTCollectionDisplay?
        access(all)
        view fun borrowNFTCollectionDisplayReader(
            _ address: Address,
            _ contractName: String,
        ): &NFTViewUtils.EditableNFTCollectionDisplay?
    }

    /// Maintainer interface for the Non-Fungible Token Reviewer
    ///
    access(all) resource interface NFTListReviewMaintainer {
        /// Update Reviewer Metadata
        access(Maintainer)
        fun updateMetadata(name: String?, url: String?)
        /// Review the Non-Fungible Token with Evaluation
        access(Maintainer)
        fun reviewNFTEvalute(
            _ address: Address,
            _ contractName: String,
            rank: FTViewUtils.Evaluation
        )
        /// Review the Non-Fungible Token, add tags
        access(Maintainer)
        fun reviewNFTAddTags(
            _ address: Address,
            _ contractName: String,
            tags: [String]
        )
        /// Register the Non-Fungible Token Display Patch
        access(Maintainer)
        fun registerNFTCollectionDisplayPatch(
            _ address: Address,
            _ contractName: String,
        )
        /// Borrow or create the FTDisplay editor
        access(Maintainer)
        view fun borrowNFTCollectionDisplayEditor(
            _ address: Address,
            _ contractName: String,
        ): auth(NFTViewUtils.Editable) &NFTViewUtils.EditableNFTCollectionDisplay?
    }

    /// The resource for the FT Reviewer
    ///
    access(all) resource NFTListReviewer: NFTListReviewMaintainer, NFTListReviewerInterface {
        access(self)
        let metadata: {String: String}
        access(self)
        let storedDisplayPatches: @{Type: NFTViewUtils.EditableNFTCollectionDisplay}
        access(self)
        let reviewed: {Type: FTViewUtils.Evaluation}

        init() {
            self.metadata = {}
            self.reviewed = {}
            self.storedDisplayPatches <- {}
        }

        // --- Implement the FungibleTokenReviewMaintainer ---

        /// Update Reviewer Metadata
        ///
        access(Maintainer)
        fun updateMetadata(name: String?, url: String?) {
            if name != nil {
                self.metadata["name"] = name!
            }

            if url != nil {
                self.metadata["url"] = url!
            }

            // emit the event
            emit NFTListReviewerMetadataUpdated(
                self.getAddress(),
                name: name,
                url: url,
            )
        }

        /// Review the Non-Fungible Token with Evaluation
        ///
        access(Maintainer)
        fun reviewNFTEvalute(
            _ address: Address,
            _ contractName: String,
            rank: FTViewUtils.Evaluation
        ) {
            let registery = NFTList.borrowRegistry()
            let entryRef = registery.borrowNFTEntryByContract(address, contractName)
                ?? panic("Failed to load the Non-Fungible Token Entry")

            let reviewerAddr = self.getAddress()
            var isUpdated = false
            if let reviewRef = entryRef.borrowReviewRef(reviewerAddr) {
                if reviewRef.evalRank.rawValue != rank.rawValue {
                    reviewRef.updateEvaluationRank(rank)
                    isUpdated = true
                }
            } else {
                entryRef.addReview(reviewerAddr, FTViewUtils.FTReview(rank))
                isUpdated = true
            }

            // If not updated, then return
            if !isUpdated {
                return
            }

            let identity = entryRef.getIdentity()
            let type = identity.buildNFTType()

            // update reviewed status locally
            self.reviewed[type] = rank

            // emit the event
            emit NFTCollectionReviewEvaluated(
                identity.address,
                identity.contractName,
                rank.rawValue,
                reviewerAddr
            )
        }

        /// Review the Non-Fungible Token, add tags
        ///
        access(Maintainer)
        fun reviewNFTAddTags(
            _ address: Address,
            _ contractName: String,
            tags: [String]
        ) {
            pre {
                tags.length > 0: "Tags should not be empty"
            }

            let registery = NFTList.borrowRegistry()
            let entryRef = registery.borrowNFTEntryByContract(address, contractName)
                ?? panic("Failed to load the Non-Fungible Token Entry")

            let reviewerAddr = self.getAddress()
            if entryRef.borrowReviewRef(reviewerAddr) == nil {
                // add the review with UNVERIFIED evaluation
                self.reviewNFTEvalute(address, contractName, rank: FTViewUtils.Evaluation.UNVERIFIED)
            }
            let ref = entryRef.borrowReviewRef(reviewerAddr)
                ?? panic("Failed to load the Non-Fungible Token Review")
            var isUpdated = false
            for tag in tags {
                // ingore the eval tags
                if tag == "Verified" || tag == "Featured" || tag == "Pending" || tag == "Blocked" {
                    continue
                }
                if ref.addTag(tag) {
                    isUpdated = true
                }
            }

            // If not updated, then return
            if !isUpdated {
                return
            }

            let identity = entryRef.getIdentity()
            // emit the event
            emit NFTCollectionTagsAdded(
                identity.address,
                identity.contractName,
                tags,
                reviewerAddr
            )
        }

        /// Register the Non-Fungible Token Display Patch
        ///
        access(Maintainer)
        fun registerNFTCollectionDisplayPatch(
            _ address: Address,
            _ contractName: String
        ) {
            let registery = NFTList.borrowRegistry()

            let entry = registery.borrowNFTEntryByContract(address, contractName)
                ?? panic("Token not registered")
            let nftType = entry.getNFTType()
            assert(
                self.storedDisplayPatches[nftType] == nil,
                message: "Editable FTDisplay already exists"
            )

            // create a Editable FTDisplay resource it the reviewer storage
            let editableFTDisplay <- NFTViewUtils.createEditableCollectionDisplay(address, contractName)
            let ftDisplayId = editableFTDisplay.uuid
            // save in the resource
            self.storedDisplayPatches[nftType] <-! editableFTDisplay

            registery.onReviewerNFTCollectionCustomized(self.getAddress(), nftType)

            // emit the event for editable FTDisplay
            emit NFTListReviewerEditableNFTCollectionDisplayCreated(
                address,
                contractName,
                reviewer: self.getAddress()
            )
        }

        /// Borrow or create the editor
        ///
        access(Maintainer)
        view fun borrowNFTCollectionDisplayEditor(
            _ address: Address,
            _ contractName: String,
        ): auth(NFTViewUtils.Editable) &NFTViewUtils.EditableNFTCollectionDisplay? {
            let nftType = NFTViewUtils.buildNFTType(address, contractName)
                ?? panic("Failed to build the NFT Type")
            return &self.storedDisplayPatches[nftType]
        }

        // --- Implement the FungibleTokenReviewerInterface ---

        access(all)
        view fun getMetadata(): {String: String} {
            return self.metadata
        }

        /// Return the amount of Non-Fungible Token which reviewed by the reviewer
        ///
        access(all)
        view fun getReviewedNFTAmount(): Int {
            return self.reviewed.keys.length
        }

        /// Return the amount of Non-Fungible Token which display customized by the reviewer
        ///
        access(all)
        view fun getCustomizedNFTAmount(): Int {
            return self.storedDisplayPatches.keys.length
        }

        /// Return all Non-Fungible Token Types reviewed by the reviewer
        ///
        access(all)
        view fun getReviewedNFTTypes(): [Type] {
            return self.reviewed.keys
        }

        /// Return all Non-Fungible Token Types with FEATURED evaluation
        ///
        access(all)
        view fun getFeaturedNFTTypes(): [Type] {
            let reviewedRef = &self.reviewed as &{Type: FTViewUtils.Evaluation}
            return self.reviewed.keys.filter(view fun(type: Type): Bool {
                return reviewedRef[type]?.rawValue == FTViewUtils.Evaluation.FEATURED.rawValue
            })
        }

        /// Return all Non-Fungible Token Types with VERIFIED or FEATURED evaluation
        ///
        access(all)
        view fun getVerifiedNFTTypes(): [Type] {
            let reviewedRef = &self.reviewed as &{Type: FTViewUtils.Evaluation}
            return self.reviewed.keys.filter(view fun(type: Type): Bool {
                return reviewedRef[type]?.rawValue == FTViewUtils.Evaluation.VERIFIED.rawValue
                    || reviewedRef[type]?.rawValue == FTViewUtils.Evaluation.FEATURED.rawValue
            })
        }

        /// Return all Non-Fungible Token Types with BLOCKED evaluation
        ///
        access(all)
        view fun getBlockedNFTTypes(): [Type] {
            let reviewedRef = &self.reviewed as &{Type: FTViewUtils.Evaluation}
            return self.reviewed.keys.filter(view fun(type: Type): Bool {
                return reviewedRef[type]?.rawValue == FTViewUtils.Evaluation.BLOCKED.rawValue
            })
        }

        /// Borrow the FTDisplay editor
        ///
        access(all)
        view fun borrowNFTCollectionDisplayReader(
            _ address: Address,
            _ contractName: String,
        ): &NFTViewUtils.EditableNFTCollectionDisplay? {
            return self.borrowNFTCollectionDisplayEditor(address, contractName)
        }

        /// Borrow the FTDisplay editor
        ///
        access(all)
        view fun borrowNFTCollectionDisplayReaderByNftType(_ nftType: Type): &NFTViewUtils.EditableNFTCollectionDisplay? {
            return &self.storedDisplayPatches[nftType]
        }

        // --- Internal Methods ---
    }

    /// The Maintainer for the Non-Fungible Token Reviewer
    ///
    access(all) resource ReviewMaintainer: NFTListReviewMaintainer {
        access(self)
        let reviewerCap: Capability<auth(Maintainer) &NFTListReviewer>

        init(
            _ cap: Capability<auth(Maintainer) &NFTListReviewer>
        ) {
            pre {
                cap.check(): "Invalid capability"
            }
            self.reviewerCap = cap
        }

        /// Get the reviewer address
        ///
        access(all)
        view fun getReviewerAddress(): Address {
            return self.reviewerCap.address
        }

        /// Update Reviewer Metadata
        ///
        access(Maintainer)
        fun updateMetadata(name: String?, url: String?) {
            self._borrowReviewer().updateMetadata(name: name, url: url)
        }

        /// Review the Non-Fungible Token with Evaluation
        ///
        access(Maintainer)
        fun reviewNFTEvalute(_ address: Address, _ contractName: String, rank: FTViewUtils.Evaluation) {
            self._borrowReviewer().reviewNFTEvalute(address, contractName, rank: rank)
        }

        /// Review the Non-Fungible Token, add tags
        ///
        access(Maintainer)
        fun reviewNFTAddTags(_ address: Address, _ contractName: String, tags: [String]) {
            self._borrowReviewer().reviewNFTAddTags(address, contractName, tags: tags)
        }

        /// Register the Non-Fungible Token Display Patch
        access(Maintainer)
        fun registerNFTCollectionDisplayPatch(
            _ address: Address,
            _ contractName: String
        ) {
            self._borrowReviewer().registerNFTCollectionDisplayPatch(address, contractName)
        }

        /// Borrow or create the FTDisplay editor
        access(Maintainer)
        view fun borrowNFTCollectionDisplayEditor(
            _ address: Address,
            _ contractName: String,
        ): auth(NFTViewUtils.Editable) &NFTViewUtils.EditableNFTCollectionDisplay? {
            return self._borrowReviewer().borrowNFTCollectionDisplayEditor(address, contractName)
        }

        /* ---- Internal Methods ---- */

        access(self)
        view fun _borrowReviewer(): auth(Maintainer) &NFTListReviewer {
            return self.reviewerCap.borrow() ?? panic("Failed to borrow the reviewer")
        }
    }

    /// Interface for the Token List Viewer
    ///
    access(all) resource interface NFTListViewer {
        // --- Read Methods ---
        /// Return all available reviewers
        access(all)
        view fun getReviewers(): [Address]
        /// Get the reviewer rank
        access(all)
        view fun getReviewerRank(_ reviewer: Address): ReviewerRank?
        /// Return all verified reviewers
        access(all)
        view fun getVerifiedReviewers(): [Address]
        /// Return if the reviewer is verified
        access(all)
        view fun isReviewerVerified(_ reviewer: Address): Bool
        /// Get the amount of Non-Fungible Token Entries
        access(all)
        view fun getNFTEntriesAmount(): Int
        /// Get all the Non-Fungible Token Entries
        access(all)
        view fun getAllNFTEntries(): [Type]
        /// Get the Non-Fungible Token Entry by the page and size
        access(all)
        view fun getNFTEntries(_ page: Int, _ size: Int): [Type]
        /// Get the Non-Fungible Token Entry by the address
        access(all)
        view fun getNFTEntriesByAddress(_ address: Address): [Type]
        /// Get the customized reviewers
        access(all)
        view fun getHighestRankVerifiedCustomizedReviewer(_ nftType: Type): Address?
        /// Borrow the NFT Entry by the type
        access(all)
        view fun borrowNFTEntry(_ nftType: Type): &NFTCollectionEntry?
        /// Borrow the NFT Entry by the contract address
        access(all)
        view fun borrowNFTEntryByContract(_ address: Address, _ contractName: String): &NFTCollectionEntry?
        // --- Write Methods ---
        /// Register a new standard Non-Fungible Token Entry to the registry
        access(contract)
        fun registerStandardNonFungibleToken(_ address: Address, _ contractName: String)
        /// Invoked when a new Non-Fungible Token is customized by the reviewer
        access(contract)
        fun onReviewerNFTCollectionCustomized(_ reviewer: Address, _ nftType: Type)
    }

    access(all) enum ReviewerRank: UInt8 {
        access(all) case NORMAL
        access(all) case ADVANCED
        access(all) case EXPERT
    }

    /// The Token List Registry
    ///
    access(all) resource Registry: NFTListViewer {
        // Address => isVerified
        access(self)
        let verifiedReviewers: {Address: Bool}
        access(self)
        let reviewerRanks: {Address: ReviewerRank}
        // NFT Type => NFT Collection Entry
        access(self)
        let entries: @{Type: NFTCollectionEntry}
        // Entry ID => NFT Type
        access(self)
        let entriesIdMapping: {UInt64: Type}
        // Address => [contractName]
        access(self)
        let addressMapping: {Address: [String]}
        // Customized NFT Views
        access(self)
        let customizedNFTViews: {Type: [Address]}

        init() {
            self.verifiedReviewers = {}
            self.reviewerRanks = {}
            self.entriesIdMapping = {}
            self.entries <- {}
            self.addressMapping = {}
            self.customizedNFTViews = {}
        }

        // ----- Read Methods -----

        /// Return all available reviewers
        ///
        access(all)
        view fun getReviewers(): [Address] {
            return self.reviewerRanks.keys
        }

        /// Get the reviewer rank
        ///
        access(all)
        view fun getReviewerRank(_ reviewer: Address): ReviewerRank? {
            return self.reviewerRanks[reviewer]
        }

        /// Return all verified reviewers
        ///
        access(all)
        view fun getVerifiedReviewers(): [Address] {
            return self.verifiedReviewers.keys
        }

        /// Return if the reviewer is verified
        ///
        access(all)
        view fun isReviewerVerified(_ reviewer: Address): Bool {
            return self.verifiedReviewers[reviewer] ?? false
        }

        /// Get the amount of Non-Fungible Token Entries
        access(all)
        view fun getNFTEntriesAmount(): Int {
            return self.entries.keys.length
        }

        /// Get all the Non-Fungible Token Entries
        ///
        access(all)
        view fun getAllNFTEntries(): [Type] {
            return self.entries.keys
        }

        /// Get the Non-Fungible Token Entry by the page and size
        ///
        access(all)
        view fun getNFTEntries(_ page: Int, _ size: Int): [Type] {
            pre {
                page >= 0: "Invalid page"
                size > 0: "Invalid size"
            }
            let max = self.getNFTEntriesAmount()
            let start = page * size
            if start > max {
                return []
            }
            var end = start + size
            if end > max {
                end = max
            }
            return self.entries.keys.slice(from: start, upTo: end)
        }

        /// Get the Non-Fungible Token Entry by the address
        ///
        access(all)
        view fun getNFTEntriesByAddress(_ address: Address): [Type] {
            if let contracts = self.borrowAddressContractsRef(address) {
                var types: [Type] = []
                for contractName in contracts {
                    if let type = NFTViewUtils.buildNFTType(address, contractName) {
                        types = types.concat([type])
                    }
                }
                return types
            }
            return []
        }

        /// Get the highest rank customized reviewers
        ///
        access(all)
        view fun getHighestRankVerifiedCustomizedReviewer(_ nftType: Type): Address? {
            if let reviewers = self.customizedNFTViews[nftType] {
                var highestRank: ReviewerRank? = nil
                var highestReviewer: Address? = nil
                for reviewer in reviewers {
                    if self.verifiedReviewers[reviewer] != true {
                        continue
                    }
                    if let rank = self.reviewerRanks[reviewer] {
                        if highestRank == nil || rank.rawValue > highestRank!.rawValue {
                            highestRank = rank
                            highestReviewer = reviewer
                            // break if the reviewer is verified
                            if self.verifiedReviewers[reviewer] == true {
                                break
                            }
                        }
                    }
                }
                return highestReviewer
            }
            return nil
        }

        /// Borrow the NFT Entry by the type
        access(all)
        view fun borrowNFTEntry(_ nftType: Type): &NFTCollectionEntry? {
            return &self.entries[nftType]
        }

        /// Borrow the NFT Entry by the contract address
        access(all)
        view fun borrowNFTEntryByContract(_ address: Address, _ contractName: String): &NFTCollectionEntry? {
            var entry: &NFTCollectionEntry? = nil
            if let collectionType = NFTViewUtils.buildCollectionType(address, contractName) {
                entry = self.borrowNFTEntry(collectionType)
            }
            if entry == nil {
                if let nftType = NFTViewUtils.buildNFTType(address, contractName) {
                    entry = self.borrowNFTEntry(nftType)
                }
            }
            return entry
        }

        // ----- Write Methods -----

        /// Update the reviewer verified status
        ///
        access(SuperAdmin)
        fun updateReviewerVerified(_ reviewer: Address, _ verified: Bool) {
            pre {
                NFTList.borrowReviewerPublic(reviewer) != nil: "FT Reviewer not found"
            }
            self.verifiedReviewers[reviewer] = verified

            // emit the event
            emit NFTListReviewerVerifiedUpdated(
                reviewer,
                verified
            )
        }

        /// Remove a Non-Fungible Token Entry from the registry
        ///
        access(SuperAdmin)
        fun removeNFTCollection(_ type: Type): Bool {
            return self._removeNFTCollection(type)
        }

        /// Register a new standard Non-Fungible Token Entry to the registry
        ///
        access(contract)
        fun registerStandardNonFungibleToken(_ address: Address, _ contractName: String) {
            pre {
                NFTList.isNFTCollectionRegistered(address, contractName) == false: "Fungible Token already registered"
            }
            self._register(<- create NFTCollectionEntry(address, contractName))
        }

        /// Invoked when a new Non-Fungible Token is customized by the reviewer
        ///
        access(contract)
        fun onReviewerNFTCollectionCustomized(_ reviewer: Address, _ nftType: Type) {
            pre {
                NFTList.borrowReviewerPublic(reviewer) != nil: "FT Reviewer not found"
            }
            // ensure the tokenType exists
            if self.customizedNFTViews[nftType] == nil {
                self.customizedNFTViews[nftType] = []
            }
            // add the reviewer to the list
            if let arrRef = &self.customizedNFTViews[nftType] as &[Address]? {
                if arrRef.firstIndex(of: reviewer) == nil {
                    self.customizedNFTViews[nftType]?.append(reviewer)
                }
            }
            // update the rank
            self._updateReviewerRank(reviewer)
        }

        // ----- Internal Methods -----

        access(self)
        fun _updateReviewerRank(_ reviewer: Address) {
            let reviewerRef = NFTList.borrowReviewerPublic(reviewer)
                ?? panic("Could not find the FT Reviewer")
            let oldRank = self.reviewerRanks[reviewer]
            var newRank: NFTList.ReviewerRank? = nil
            // ensure the reviewer rank exists
            if self.reviewerRanks[reviewer] == nil {
                newRank = ReviewerRank.NORMAL
            } else {
                // update the rank by the amount of customized FT
                let reviewedAmt = reviewerRef.getReviewedNFTAmount()
                let customizedAmt = reviewerRef.getCustomizedNFTAmount()
                let weight = customizedAmt * 5 + reviewedAmt
                if weight >= 1000 {
                    newRank = ReviewerRank.EXPERT
                } else if weight >= 200 {
                    newRank = ReviewerRank.ADVANCED
                }
            }

            if newRank != nil && oldRank != newRank {
                self.reviewerRanks[reviewer] = newRank!
                // emit the event
                emit NFTListReviewerRankUpdated(
                    reviewer,
                    newRank!.rawValue
                )
            }
        }

        /// Remove a Non-Fungible Token Entry from the registry
        ///
        access(self)
        fun _removeNFTCollection(_ nftType: Type): Bool {
            if self.entries[nftType] == nil {
                return false
            }
            let entry <- self.entries.remove(key: nftType)
                ?? panic("Could not remove the Non-Fungible Token Entry")
            self.entriesIdMapping.remove(key: entry.uuid)

            let identity = entry.getIdentity()
            if let addrRef = self.borrowAddressContractsRef(identity.address) {
                if let idx = addrRef.firstIndex(of: identity.contractName) {
                    addrRef.remove(at: idx)
                }
            }
            destroy entry

            // emit the event
            emit NFTCollectionRemoved(
                identity.address,
                identity.contractName,
                nftType
            )
            return true
        }

        /// Add a new Non-Fungible Token Entry to the registry
        ///
        access(self)
        fun _register(_ entry: @NFTCollectionEntry) {
            pre {
                self.entries[entry.getNFTType()] == nil:
                    "FungibleToken Entry already exists in the registry"
                self.entriesIdMapping[entry.uuid] == nil:
                    "FungibleToken Entry ID already exists in the registry"
            }
            let nftType = entry.getNFTType()
            self.entries[nftType] <-! entry

            let ref = &self.entries[nftType] as &NFTCollectionEntry?
                ?? panic("Could not borrow the FT Entry")
            // Add the ID mapping
            self.entriesIdMapping[ref.uuid] = nftType
            // Add the address mapping
            if let addrRef = self.borrowAddressContractsRef(ref.identity.address) {
                addrRef.append(ref.identity.contractName)
            } else {
                self.addressMapping[ref.identity.address] = [ref.identity.contractName]
            }

            // emit the event
            emit NFTCollectionRegistered(
                ref.identity.address,
                ref.identity.contractName,
                nftType
            )
        }

        access(self)
        view fun borrowAddressContractsRef(_ addr: Address): auth(Mutate) &[String]? {
            return &self.addressMapping[addr]
        }
    }

    /* --- Public Methods --- */

    /// Create a new NFT List Reviewer
    ///
    access(all)
    fun createNFTListReviewer(): @NFTListReviewer {
        return <- create NFTListReviewer()
    }

    /// Create a new Non-Fungible Token Review Maintainer
    ///
    access(all)
    fun createNFTListReviewMaintainer(
        _ cap: Capability<auth(Maintainer) &NFTListReviewer>
    ): @ReviewMaintainer {
        return <- create ReviewMaintainer(cap)
    }

    /// Get the Non-Fungible Token Reviewer capability
    ///
    access(all)
    view fun getReviewerCapability(_ addr: Address): Capability<&NFTListReviewer> {
        return getAccount(addr).capabilities
            .get<&NFTListReviewer>(self.reviewerPublicPath)
    }

    /// Borrow the public capability of the Non-Fungible Token Reviewer
    ///
    access(all)
    view fun borrowReviewerPublic(_ addr: Address): &NFTListReviewer? {
        return self.getReviewerCapability(addr).borrow()
    }

    /// Borrow the public capability of  Token List Registry
    ///
    access(all)
    view fun borrowRegistry(): &{NFTListViewer} {
        return getAccount(self.account.address)
            .capabilities.get<&{NFTListViewer}>(self.registryPublicPath)
            .borrow()
            ?? panic("Could not borrow the Registry reference")
    }

    /// Check if the NFT is registered
    ///
    access(all)
    view fun isNFTCollectionRegistered(_ address: Address, _ contractName: String): Bool {
        let registry: &{NFTList.NFTListViewer} = self.borrowRegistry()
        let entry = registry.borrowNFTEntryByContract(address, contractName)
        return entry != nil
    }

    /// Check if the NFT is valid to register
    access(all)
    fun isValidToRegister(_ address: Address, _ contractName: String): Bool {
        if let contractRef = ViewResolvers.borrowContractViewResolver(address, contractName) {
            let colDisplayType = Type<MetadataViews.NFTCollectionDisplay>()
            let colDataType = Type<MetadataViews.NFTCollectionData>()
            let contractViews = contractRef.getContractViews(resourceType: nil)
            if contractViews.contains(colDataType) == false || contractViews.contains(colDisplayType) == false {
                return false
            }
            var convertedDisplayView: MetadataViews.NFTCollectionDisplay? = nil
            var convertedDataView: MetadataViews.NFTCollectionData? = nil
            if let displayView = contractRef.resolveContractView(resourceType: nil, viewType: colDisplayType) {
                convertedDisplayView = displayView as? MetadataViews.NFTCollectionDisplay
            } else {
                return false
            }
            if let dataView = contractRef.resolveContractView(resourceType: nil, viewType: colDataType) {
                convertedDataView = dataView as? MetadataViews.NFTCollectionData
            } else {
                return false
            }
            if convertedDisplayView != nil && convertedDataView != nil {
                return true
            }
        }
        return false
    }

    /// Try to register a new NFT, if already registered, then do nothing
    ///
    access(all)
    fun ensureNFTCollectionRegistered(_ address: Address, _ contractName: String) {
        if !self.isNFTCollectionRegistered(address, contractName) && self.isValidToRegister(address, contractName) {
            let registry = self.borrowRegistry()
            registry.registerStandardNonFungibleToken(address, contractName)
        }
    }

    /// The prefix for the paths
    ///
    access(all)
    view fun getPathPrefix(): String {
        return "NFTList_".concat(self.account.address.toString()).concat("_")
    }

    /// Generate the review maintainer capability ID
    ///
    access(all)
    view fun generateReviewMaintainerCapabilityId(_ addr: Address): String {
        return NFTList.getPathPrefix().concat("PrivateIdentity_ReviewMaintainer_".concat(addr.toString()))
    }

    init() {
        // Identifiers
        let identifier = NFTList.getPathPrefix()
        self.registryStoragePath = StoragePath(identifier: identifier.concat("_Registry"))!
        self.registryPublicPath = PublicPath(identifier: identifier.concat("_Registry"))!

        self.reviewerStoragePath = StoragePath(identifier: identifier.concat("_Reviewer"))!
        self.reviewerPublicPath = PublicPath(identifier: identifier.concat("_Reviewer"))!

        self.maintainerStoragePath = StoragePath(identifier: identifier.concat("_Maintainer"))!

        // Create the Token List Registry
        let registry <- create Registry()
        self.account.storage.save(<- registry, to: self.registryStoragePath)
        // link the public capability
        let cap = self.account.capabilities
            .storage.issue<&{NFTListViewer}>(self.registryStoragePath)
        self.account.capabilities.publish(cap, at: self.registryPublicPath)

        // Emit the initialized event
        emit ContractInitialized()
    }
}

```