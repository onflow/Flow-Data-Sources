# Source: https://github.com/fixes-world/token-list/blob/main/cadence/contracts/EVMTokenList.cdc

```
/**
> Author: Fixes World <https://fixes.world/>

# EVMTokenList - A on-chain list of all the EVM compatible tokens on the Flow blockchain.

This contract is a list of all the bridged ERC20 / ERC721 tokens for Flow(EVM) on the Flow blockchain.

*/
import "FungibleToken"
import "NonFungibleToken"
import "MetadataViews"
import "ViewResolver"
import "FungibleTokenMetadataViews"
// EVM and VMBridge related contracts
import "EVM"
import "FlowEVMBridge"
import "FlowEVMBridgeConfig"
import "FlowEVMBridgeUtils"
// TokenList contract
import "TokenList"
import "NFTList"
import "FTViewUtils"
import "NFTViewUtils"

/// The EVMTokenList contract
/// The List only contains the basic EVM Address information for the registered tokens.
///
access(all) contract EVMTokenList {
    /* --- Entitlement --- */

    access(all) entitlement SuperAdmin

    /* --- Events --- */

    /// Event emitted when the contract is initialized
    access(all) event ContractInitialized()

    /// Event emitted when a new EVM compatible token is registered
    access(all) event EVMBridgedAssetRegistered(
        _ evmAddress: String,
        _ isERC721: Bool,
        _ bridgedAssetAddress: Address,
        _ bridgedAssetContractName: String,
    )
    /// Event emitted when a EVM compatible token is removed
    access(all) event EVMBridgedAssetRemoved(
        _ evmAddress: String,
        _ isERC721: Bool,
        _ bridgedAssetAddress: Address,
        _ bridgedAssetContractName: String,
    )
        /* --- Variable, Enums and Structs --- */

    access(all) let registryStoragePath: StoragePath
    access(all) let registryPublicPath: PublicPath

    /* --- Interfaces & Resources --- */

    /// Interface for the Token List Viewer
    ///
    access(all) resource interface IListViewer {
        // --- Read functions ---

        /// Check if the EVM Address is registered
        access(all)
        view fun isEVMAddressRegistered(_ evmContractAddressHex: String): Bool

        // --- ERC20 functions ---

        /// Get the total number of registered ERC20 tokens
        access(all)
        view fun getERC20Amount(): Int
        /// Get the ERC20 addresses with pagination
        /// The method will copy the addresses to the result array
        access(all)
        fun getERC20Addresses(_ page: Int, _ size: Int): [EVM.EVMAddress]
        /// Get the ERC20 addresses with pagination
        /// The method will copy the addresses to the result array
        access(all)
        fun getERC20AddressesHex(_ page: Int, _ size: Int): [String]
        /// Get the ERC20 addresses by for each
        /// The method will call the function for each address
        access(all)
        fun forEachERC20Address(_ f: fun (EVM.EVMAddress): Bool)
        /// Get the ERC20 addresses(String) by for each
        access(all)
        fun forEachERC20AddressString(_ f: fun (String): Bool)
        /// Borrow the Bridged Token's TokenList Entry
        access(all)
        view fun borrowFungibleTokenEntry(_ evmContractAddressHex: String): &{TokenList.FTEntryInterface}?

        // --- ERC721 functions ---

        /// Get the total number of registered ERC721 tokens
        access(all)
        view fun getERC721Amount(): Int
        /// Get the ERC721 addresses with pagination
        /// The method will copy the addresses to the result array
        access(all)
        fun getERC721Addresses(_ page: Int, _ size: Int): [EVM.EVMAddress]
        /// Get the ERC721 addresses with pagination
        /// The method will copy the addresses to the result array
        access(all)
        fun getERC721AddressesHex(_ page: Int, _ size: Int): [String]
        /// Get the ERC721 addresses by for each
        /// The method will call the function for each address
        access(all)
        fun forEachERC721Address(_ f: fun (EVM.EVMAddress): Bool)
        /// Get the ERC721 addresses(String) by for each
        access(all)
        fun forEachERC721AddressString(_ f: fun (String): Bool)
        /// Borrow the Bridged Token's TokenList Entry
        access(all)
        view fun borrowNonFungibleTokenEntry(_ evmContractAddressHex: String): &NFTList.NFTCollectionEntry?

        // --- Register functions ---

        /// Register and onboard a new EVM compatible token (ERC20 or ERC721) to the EVM Token List
        access(all)
        fun registerEVMAsset(_ evmContractAddressHex: String, feeProvider: auth(FungibleToken.Withdraw) &{FungibleToken.Provider}?)

        /// Register and onboard a new Cadence Asset to the EVM Token List
        access(all)
        fun registerCadenceAsset(_ ftOrNftType: Type, feeProvider: auth(FungibleToken.Withdraw) &{FungibleToken.Provider}?)
    }

    /// Resource for the Token List Registry
    ///
    access(all) resource Registry: IListViewer {
        // EVM Address Hex => Bridged Token Identity
        access(self)
        let regsiteredErc20s: {String: FTViewUtils.FTIdentity}
        // EVM Address Hex => Bridged Token Identity
        access(self)
        let regsiteredErc721s: {String: NFTViewUtils.NFTIdentity}

        init() {
            self.regsiteredErc20s = {}
            self.regsiteredErc721s = {}
        }

        /* --- Implement the IListViewer interface ---  */

        /// Check if the EVM Address is registered
        access(all)
        view fun isEVMAddressRegistered(_ evmContractAddressHex: String): Bool {
            return self.regsiteredErc20s[evmContractAddressHex] != nil
                || self.regsiteredErc721s[evmContractAddressHex] != nil
        }

        /// Get the total number of registered ERC20 tokens
        access(all)
        view fun getERC20Amount(): Int {
            return self.regsiteredErc20s.keys.length
        }

        /// Get the ERC20 addresses with pagination
        /// The method will copy the addresses to the result array
        access(all)
        fun getERC20Addresses(_ page: Int, _ size: Int): [EVM.EVMAddress] {
            return self.getERC20AddressesHex(page, size)
                .map(fun (key: String): EVM.EVMAddress { return EVM.addressFromString(key) })
        }

        /// Get the ERC20 addresses with pagination
        /// The method will copy the addresses to the result array
        access(all)
        fun getERC20AddressesHex(_ page: Int, _ size: Int): [String] {
            pre {
                page >= 0: "Invalid page"
                size > 0: "Invalid size"
            }
            let max = self.getERC20Amount()
            let start = page * size
            if start > max {
                return []
            }
            var end = start + size
            if end > max {
                end = max
            }
            return self.regsiteredErc20s.keys.slice(from: start, upTo: end)
        }

        /// Get the ERC20 addresses by for each
        /// The method will call the function for each address
        access(all)
        fun forEachERC20Address(_ f: fun (EVM.EVMAddress): Bool) {
            self.regsiteredErc20s.forEachKey(fun (key: String): Bool {
                return f(EVM.addressFromString(key))
            })
        }

        /// Get the ERC20 addresses(String) by for each
        access(all)
        fun forEachERC20AddressString(_ f: fun (String): Bool) {
            self.regsiteredErc20s.forEachKey(f)
        }

        /// Borrow the Bridged Token's TokenList Entry
        access(all)
        view fun borrowFungibleTokenEntry(_ evmContractAddressHex: String): &{TokenList.FTEntryInterface}? {
            if let item = self.regsiteredErc20s[evmContractAddressHex] {
                let ftRegistry = TokenList.borrowRegistry()
                let ftType = item.buildType()
                return ftRegistry.borrowFungibleTokenEntry(ftType)
            }
            return nil
        }

        /// Get the total number of registered ERC721 tokens
        access(all)
        view fun getERC721Amount(): Int {
            return self.regsiteredErc721s.keys.length
        }

        /// Get the ERC721 addresses with pagination
        /// The method will copy the addresses to the result array
        access(all)
        fun getERC721Addresses(_ page: Int, _ size: Int): [EVM.EVMAddress] {
            return self.getERC721AddressesHex(page, size)
                .map(fun (key: String): EVM.EVMAddress { return EVM.addressFromString(key) })
        }

        /// Get the ERC721 addresses with pagination
        /// The method will copy the addresses to the result array
        access(all)
        fun getERC721AddressesHex(_ page: Int, _ size: Int): [String] {
            pre {
                page >= 0: "Invalid page"
                size > 0: "Invalid size"
            }
            let max = self.getERC721Amount()
            let start = page * size
            if start > max {
                return []
            }
            var end = start + size
            if end > max {
                end = max
            }
            return self.regsiteredErc721s.keys.slice(from: start, upTo: end)
        }

        /// Get the ERC721 addresses by for each
        /// The method will call the function for each address
        access(all)
        fun forEachERC721Address(_ f: fun (EVM.EVMAddress): Bool) {
            self.regsiteredErc721s.forEachKey(fun (key: String): Bool {
                return f(EVM.addressFromString(key))
            })
        }

        /// Get the ERC721 addresses(String) by for each
        access(all)
        fun forEachERC721AddressString(_ f: fun (String): Bool) {
            self.regsiteredErc721s.forEachKey(f)
        }

        /// Borrow the Bridged Token's TokenList Entry
        access(all)
        view fun borrowNonFungibleTokenEntry(_ evmContractAddressHex: String): &NFTList.NFTCollectionEntry? {
            if let item = self.regsiteredErc721s[evmContractAddressHex] {
                let nftRegistry = NFTList.borrowRegistry()
                let nftType = item.buildNFTType()
                return nftRegistry.borrowNFTEntry(nftType)
            }
            return nil
        }

        /* --- Register functions --- */

        /// Register and onboard a new EVM compatible token (ERC20 or ERC721) to the EVM Token List
        ///
        access(all)
        fun registerEVMAsset(_ evmContractAddressHex: String, feeProvider: auth(FungibleToken.Withdraw) &{FungibleToken.Provider}?) {
            var contractAddr: Address? = nil
            var contractName: String? = nil
            var isNFT: Bool = false

            let address = EVM.addressFromString(evmContractAddressHex)
            let isRequires = FlowEVMBridge.evmAddressRequiresOnboarding(address)
            if isRequires == false {
                // Now just need to look up the type of the token and register it to the Token List
                let assetType = FlowEVMBridgeConfig.getTypeAssociated(with: address)
                    ?? panic("Could not find the asset type")
                contractAddr = FlowEVMBridgeUtils.getContractAddress(fromType: assetType)
                contractName = FlowEVMBridgeUtils.getContractName(fromType: assetType)
                isNFT = assetType.isSubtype(of: Type<@{NonFungibleToken.NFT}>())
            } else if isRequires == true {
                // Onboard the token to the bridge
                assert(feeProvider != nil, message: "Fee provider is required for onboarding")
                FlowEVMBridge.onboardByEVMAddress(address, feeProvider: feeProvider!)
                // FIXME: Because the new deployed Cadence contracts can not be found in the same transaction
                // So we just build the contract address and name here
                let identifierSplit = FlowEVMBridge.getType().identifier.split(separator: ".")
                contractAddr = Address.fromString("0x".concat(identifierSplit[1]))
                let evmOnboardingValues = FlowEVMBridgeUtils.getEVMOnboardingValues(evmContractAddress: address)
                contractName = evmOnboardingValues.cadenceContractName
                isNFT = evmOnboardingValues.isERC721
            } else {
                // This address is not a valid EVM asset
                panic("Invalid EVM Asset for the Address: 0x".concat(evmContractAddressHex))
            }

            // register the asset to the Token List
            self._tryRegisterAsset(
                address.toString(),
                contractAddr ?? panic("Contract address is required to register"),
                contractName ?? panic("Contract name is required to register"),
                isNFT
            )
        }

        /// Register and onboard a new Cadence Asset to the EVM Token List
        access(all)
        fun registerCadenceAsset(_ ftOrNftType: Type, feeProvider: auth(FungibleToken.Withdraw) &{FungibleToken.Provider}?) {
            let contractAddr = FlowEVMBridgeUtils.getContractAddress(fromType: ftOrNftType) ?? panic("Could not find the contract address")
            let contractName = FlowEVMBridgeUtils.getContractName(fromType: ftOrNftType) ?? panic("Could not find the contract name")
            let isNFT: Bool = ftOrNftType.isSubtype(of: Type<@{NonFungibleToken.NFT}>())
            var evmAddress: EVM.EVMAddress? = nil

            let isRequires = FlowEVMBridge.typeRequiresOnboarding(ftOrNftType)
            if isRequires == false {
                // Now just need to look up the type of the token and register it to the Token List
                evmAddress = FlowEVMBridgeConfig.getEVMAddressAssociated(with: ftOrNftType)
            } else if isRequires == true {
                // Onboard the token to the bridge
                assert(feeProvider != nil, message: "Fee provider is required for onboarding")
                FlowEVMBridge.onboardByType(ftOrNftType, feeProvider: feeProvider!)
                // EVM Contract deployment can be found in the same transaction
                evmAddress = FlowEVMBridgeConfig.getEVMAddressAssociated(with: ftOrNftType)
            } else {
                panic("Invalid Cadence Asset Type for the Type: ".concat(ftOrNftType.identifier))
            }

            self._tryRegisterAsset(
                evmAddress?.toString() ?? panic("EVM Address is required to register"),
                contractAddr,
                contractName,
                isNFT
            )
        }

        /* --- Internal functions --- */

        /// Register the EVM compatible asset to the Token List
        ///
        access(self)
        fun _tryRegisterAsset(_ evmContractAddressHex: String, _ address: Address, _ contractName: String, _ isNFT: Bool) {
            var isRegistered = false
            if isNFT {
                if self.regsiteredErc721s[evmContractAddressHex] != nil {
                    return
                }
                NFTList.ensureNFTCollectionRegistered(address, contractName)
                if NFTList.isNFTCollectionRegistered(address, contractName) {
                    isRegistered = true
                    self.regsiteredErc721s[evmContractAddressHex] = NFTViewUtils.NFTIdentity(address, contractName)
                }
            } else {
                if self.regsiteredErc20s[evmContractAddressHex] != nil {
                    return
                }
                TokenList.ensureFungibleTokenRegistered(address, contractName)
                if TokenList.isFungibleTokenRegistered(address, contractName) {
                    isRegistered = true
                    self.regsiteredErc20s[evmContractAddressHex] = FTViewUtils.FTIdentity(address, contractName)
                }
            }

            if isRegistered {
                emit EVMBridgedAssetRegistered(
                    "0x".concat(evmContractAddressHex),
                    isNFT,
                    address,
                    contractName
                )
            }
        }
    }

    /* --- Public functions --- */

    /// Borrow the public capability of Token List Registry
    ///
    access(all)
    view fun borrowRegistry(): &Registry {
        return getAccount(self.account.address)
            .capabilities.get<&Registry>(self.registryPublicPath)
            .borrow()
            ?? panic("Could not borrow the Registry reference")
    }

    /// Whether the EVM Address is registered
    ///
    access(all)
    view fun isEVMAddressRegistered(_ evmContractAddressHex: String): Bool {
        let registry = self.borrowRegistry()
        return registry.isEVMAddressRegistered(evmContractAddressHex)
    }

    /// Whether the EVM Address is valid to register
    ///
    access(all)
    fun isValidToRegisterEVMAddress(_ evmContractAddressHex: String): Bool {
        let addr = EVM.addressFromString(evmContractAddressHex)
        let isRegistered = self.isEVMAddressRegistered(addr.toString())
        if isRegistered {
            return false
        }
        let isRequires = FlowEVMBridge.evmAddressRequiresOnboarding(addr)
        return isRequires != nil
    }

    /// Whether the Cadence Type is valid to register
    ///
    access(all)
    view fun isValidToRegisterCadenceType(_ ftOrNftType: Type): Bool {
        let registry = self.borrowRegistry()
        let isRequires = FlowEVMBridge.typeRequiresOnboarding(ftOrNftType)
        if isRequires == nil {
            return false
        }
        let evmAddress = FlowEVMBridgeConfig.getEVMAddressAssociated(with: ftOrNftType)
        return evmAddress == nil || !registry.isEVMAddressRegistered(evmAddress!.toString())
    }

    /// Ensure the Cadence Asset is registered
    ///
    access(all)
    fun ensureCadenceAssetRegistered(
        _ address: Address,
        _ contractName: String,
        feeProvider: auth(FungibleToken.Withdraw) &{FungibleToken.Provider}?
    ) {
        var isNFT: Bool? = nil
        var ftOrNftType = FTViewUtils.buildFTVaultType(address, contractName)
        if ftOrNftType != nil {
            if TokenList.isValidToRegister(address, contractName) {
                isNFT = false
            }
        } else {
            ftOrNftType = NFTViewUtils.buildNFTType(address, contractName)
            if ftOrNftType != nil && NFTList.isValidToRegister(address, contractName) {
                isNFT = true
            }
        }
        if isNFT != nil && ftOrNftType != nil && ftOrNftType!.isRecovered == false {
            if self.isValidToRegisterCadenceType(ftOrNftType!) {
                let registry = self.borrowRegistry()
                registry.registerCadenceAsset(ftOrNftType!, feeProvider: feeProvider)
            }
        }
    }

    /// Ensure the EVM Asset is registered
    ///
    access(all)
    fun ensureEVMAssetRegistered(
        _ evmContractAddressHex: String,
        feeProvider: auth(FungibleToken.Withdraw) &{FungibleToken.Provider}?
    ) {
        let addrHex = EVM.addressFromString(evmContractAddressHex).toString()
        if self.isValidToRegisterEVMAddress(addrHex) {
            let registry = self.borrowRegistry()
            registry.registerEVMAsset(addrHex, feeProvider: feeProvider)
        }
    }

    /// The prefix for the paths
    ///
    access(all)
    view fun getPathPrefix(): String {
        return "EVMTokenList_".concat(self.account.address.toString()).concat("_")
    }

    /// Initialize the contract
    init() {
        // Identifiers
        let identifier = NFTList.getPathPrefix()
        self.registryStoragePath = StoragePath(identifier: identifier.concat("Registry"))!
        self.registryPublicPath = PublicPath(identifier: identifier.concat("Registry"))!

        // Create the Token List Registry
        let registry <- create Registry()
        self.account.storage.save(<- registry, to: self.registryStoragePath)
        // link the public capability
        let cap = self.account.capabilities
            .storage.issue<&Registry>(self.registryStoragePath)
        self.account.capabilities.publish(cap, at: self.registryPublicPath)

        // Emit the initialized event
        emit ContractInitialized()
    }
}

```