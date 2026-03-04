# Source: https://github.com/fixes-world/token-list/blob/main/cadence/contracts/TokenListHelper.cdc

```
/**
> Author: Fixes Lab <https://github.com/fixes-world/>

# TokenList Helper

The utility contract to help query the FTs and NFTs from the TokenList and NFTList contracts.

*/
import "MetadataViews"
import "ViewResolver"
import "FungibleToken"
import "NonFungibleToken"
import "FungibleTokenMetadataViews"
import "EVM"
import "FlowEVMBridgeConfig"
import "FlowEVMBridgeUtils"
import "FlowToken"
// TokenList Imports
import "TokenList"
import "NFTList"
import "FTViewUtils"
import "NFTViewUtils"
import "EVMTokenList"

access(all) contract TokenListHelper {

    /// Query result
    ///
    access(all) struct QueryResult {
        access(all)
        let total: Int
        access(all)
        let list: [{FTViewUtils.ITokenView}]

        init(total: Int, list: [{FTViewUtils.ITokenView}]) {
            self.total = total
            self.list = list
        }
    }

    /// Query FTs with pagination and filter
    ///
    access(all)
    fun queryFTs(
        page: Int,
        size: Int,
        reviewer: Address?,
        filterType: UInt8?,
    ): QueryResult {
        // If filterType is not in the range of 0-4, return empty list
        if filterType != nil && filterType! > 4 {
            return QueryResult(total: 0, list: [])
        }

        let registry = TokenList.borrowRegistry()

        var totalAmt = 0
        var ftTypes: [Type] = []
        if reviewer != nil && filterType != 0 {
            if let reviewerRef = TokenList.borrowReviewerPublic(reviewer!) {
                var all: [Type] = []
                let start = page * size
                var end = start + size
                if filterType == 1 {
                    // Reviewed by Reviewer
                    all = reviewerRef.getReviewedFTTypes()
                } else if filterType == 2 {
                    // Managed by Reviewer
                    all = reviewerRef.getManagedFTTypes()
                } else if filterType == 3 {
                    // Verified by Reviewer
                    all = reviewerRef.getVerifiedFTTypes()
                } else if filterType == 4 {
                    // Featured by Reviewer
                    all = reviewerRef.getFeaturedFTTypes()
                } else if filterType == 5 {
                    // Blocked by Reviewer
                    all = reviewerRef.getBlockedFTTypes()
                }
                totalAmt = all.length
                if totalAmt == 0 || start >= totalAmt {
                    return QueryResult(total: 0, list: [])
                }
                if end > totalAmt {
                    end = totalAmt
                }
                ftTypes = all.slice(from: start, upTo: end)
            }
        } else {
            totalAmt = registry.getFTEntriesAmount()
            ftTypes = registry.getFTEntries(page, size)
        }
        log("Page:".concat(page.toString()).concat(" Size:").concat(size.toString()).concat(" Reviewer:").concat(reviewer?.toString() ?? "").concat(" Total:").concat(totalAmt.toString()))

        return QueryResult(
            total: totalAmt,
            list: self.buildTheFTList(ftTypes, reviewer)
        )
    }

    /// Query FTs by address
    ///
    access(all)
    fun queryFTsByAddress(
        ftAddress: Address,
        reviewer: Address?,
    ): QueryResult {
        let registry = TokenList.borrowRegistry()
        let ftTypes: [Type] = registry.getFTEntriesByAddress(ftAddress)
        return QueryResult(
            total: ftTypes.length,
            list: self.buildTheFTList(ftTypes, reviewer)
        )
    }

    /// Query NFTs with pagination and filter
    ///
    access(self)
    fun buildTheFTList(_ types: [Type], _ reviewer: Address?): [{FTViewUtils.ITokenView}] {
        if types.length == 0 {
            return []
        }

        let registry = TokenList.borrowRegistry()
        var list: [{FTViewUtils.ITokenView}] = []

        // load token view
        for ftType in types {
            if let ftEntry = registry.borrowFungibleTokenEntry(ftType) {
                list.append(self.buildFTView(ftEntry, reviewer, false))
            }
        }
        return list
    }

    access(self)
    fun buildFTView(
        _ ftEntry: &{TokenList.FTEntryInterface},
        _ reviewer: Address?,
        _ prioritizeEVMData: Bool,
    ): {FTViewUtils.ITokenView} {
        let identity = ftEntry.getIdentity()
        var paths: FTViewUtils.StandardTokenPaths? = nil
        var source: Address? = nil
        if let data = ftEntry.getVaultData(reviewer) {
            source = data.source
            paths = FTViewUtils.StandardTokenPaths(
                vaultPath: data.vaultData.storagePath,
                balancePath: data.vaultData.metadataPath,
                receiverPath: data.vaultData.receiverPath,
            )
        }
        let tokenType = identity.buildType()
        if let evmAddr = FlowEVMBridgeConfig.getEVMAddressAssociated(with: tokenType) {
            var decimals: UInt8 = 8
            if prioritizeEVMData || FlowEVMBridgeUtils.isCadenceNative(type: tokenType) == false {
                if prioritizeEVMData && FlowEVMBridgeUtils.isERC20(evmContractAddress: evmAddr) {
                    decimals = FlowEVMBridgeUtils.getTokenDecimals(evmContractAddress: evmAddr)
                }
            }
            return FTViewUtils.BridgedTokenView(
                identity: identity,
                evmAddress: "0x".concat(evmAddr.toString()),
                decimals: decimals,
                tags: ftEntry.getTags(reviewer),
                dataSource: source,
                paths: paths,
                display: ftEntry.getDisplay(reviewer),
            )
        } else {
            return FTViewUtils.StandardTokenView(
                identity: identity,
                decimals: 8,
                tags: ftEntry.getTags(reviewer),
                dataSource: source,
                paths: paths,
                display: ftEntry.getDisplay(reviewer),
            )
        }
    }

    /// Query NFTs with pagination and filter
    ///
    access(all)
    fun queryNFTs(
        page: Int,
        size: Int,
        reviewer: Address?,
        filterType: UInt8?,
    ): QueryResult {
        // If filterType is not in the range of 0-4, return empty list
        if filterType != nil && filterType! > 4 {
            return QueryResult(total: 0, list: [])
        }

        let registry = NFTList.borrowRegistry()

        var totalAmt = 0
        var nftTypes: [Type] = []
        if reviewer != nil && filterType != 0 {
            if let reviewerRef = NFTList.borrowReviewerPublic(reviewer!) {
                var all: [Type] = []
                let start = page * size
                var end = start + size
                if filterType == 1 {
                    // Reviewed by Reviewer
                    all = reviewerRef.getReviewedNFTTypes()
                } else if filterType == 2 {
                    // Managed by Reviewer
                    all = []
                } else if filterType == 3 {
                    // Verified by Reviewer
                    all = reviewerRef.getVerifiedNFTTypes()
                } else if filterType == 4 {
                    // Featured by Reviewer
                    all = reviewerRef.getFeaturedNFTTypes()
                } else if filterType == 5 {
                    // Blocked by Reviewer
                    all = reviewerRef.getBlockedNFTTypes()
                }
                totalAmt = all.length
                if totalAmt == 0 || start >= totalAmt {
                    return QueryResult(total: 0, list: [])
                }
                if end > totalAmt {
                    end = totalAmt
                }
                nftTypes = all.slice(from: start, upTo: end)
            }
        } else {
            totalAmt = registry.getNFTEntriesAmount()
            nftTypes = registry.getNFTEntries(page, size)
        }
        log("Page:".concat(page.toString()).concat(" Size:").concat(size.toString()).concat(" Reviewer:").concat(reviewer?.toString() ?? "").concat(" Total:").concat(totalAmt.toString()))

        return QueryResult(
            total: totalAmt,
            list: self.buildTheNFTList(nftTypes, reviewer)
        )
    }

    /// Query NFTs by address
    ///
    access(all)
    fun queryNFTsByAddress(
        address: Address,
        reviewer: Address?,
    ): QueryResult {
        let registry = NFTList.borrowRegistry()
        let types = registry.getNFTEntriesByAddress(address)
        return QueryResult(
            total: types.length,
            list: self.buildTheNFTList(types, reviewer)
        )
    }

    /// Build the NFT list
    ///
    access(self)
    fun buildTheNFTList(_ types: [Type], _ reviewer: Address?): [{FTViewUtils.ITokenView}] {
        if types.length == 0 {
            return []
        }
        let registry = NFTList.borrowRegistry()
        var list: [{FTViewUtils.ITokenView}] = []

        // load token view
        for nftType in types {
            if let entry = registry.borrowNFTEntry(nftType) {
                list.append(self.buildNFTView(entry: entry, reviewer: reviewer))
            }
        }
        return list
    }

    access(self)
    fun buildNFTView(
        entry: &NFTList.NFTCollectionEntry,
        reviewer: Address?,
    ): {FTViewUtils.ITokenView} {
        let identity = entry.getIdentity()
        let data = entry.getCollectionData()
        let paths = NFTViewUtils.StandardNFTPaths(
            data.storagePath,
            data.publicPath,
        )
        if let evmAddr = FlowEVMBridgeConfig.getEVMAddressAssociated(with: identity.buildNFTType()) {
            return NFTViewUtils.BridgedTokenView(
                identity: identity,
                evmAddress: "0x".concat(evmAddr.toString()),
                tags: entry.getTags(reviewer),
                dataSource: nil,
                paths: paths,
                display: entry.getDisplay(reviewer),
            )
        } else {
            return NFTViewUtils.StandardTokenView(
                identity: identity,
                tags: entry.getTags(reviewer),
                dataSource: nil,
                paths: paths,
                display: entry.getDisplay(reviewer)
            )
        }
    }

    /// Query EVM Bridged FTs with pagination
    ///
    access(all)
    fun queryEVMBridgedFTs(
        page: Int,
        size: Int,
        reviewer: Address?,
    ): QueryResult {
        let list: [{FTViewUtils.ITokenView}] = []
        let registry = EVMTokenList.borrowRegistry()

        let addrs = registry.getERC20AddressesHex(page, size)
        for addr in addrs {
            if let entry = registry.borrowFungibleTokenEntry(addr) {
                list.append(self.buildFTView(entry, reviewer, true))
            }
        }
        return QueryResult(
            total: registry.getERC20Amount(),
            list: list
        )
    }

    /// Query EVM Bridged NFTs with pagination
    ///
    access(all)
    fun queryEVMBridgedNFTs(
        page: Int,
        size: Int,
        reviewer: Address?,
    ): QueryResult {
        let list: [{FTViewUtils.ITokenView}] = []
        let registry = EVMTokenList.borrowRegistry()

        let addrs = registry.getERC721AddressesHex(page, size)
        for addr in addrs {
            if let entry = registry.borrowNonFungibleTokenEntry(addr) {
                list.append(self.buildNFTView(entry: entry, reviewer: reviewer))
            }
        }
        return QueryResult(
            total: registry.getERC721Amount(),
            list: list
        )
    }
}

```