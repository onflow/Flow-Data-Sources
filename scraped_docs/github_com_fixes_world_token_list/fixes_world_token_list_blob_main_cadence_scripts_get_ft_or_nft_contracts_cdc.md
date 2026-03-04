# Source: https://github.com/fixes-world/token-list/blob/main/cadence/scripts/get-ft-or-nft-contracts.cdc

```
import "ViewResolver"
import "FungibleToken"
import "NonFungibleToken"
import "MetadataViews"
import "FungibleTokenMetadataViews"
import "FlowEVMBridgeConfig"
import "ViewResolvers"
import "FTViewUtils"
import "TokenList"
import "NFTViewUtils"
import "NFTList"

access(all)
fun main(
    addr: Address
): [TokenAssetStatus] {
    let acct = getAuthAccount<auth(Storage, Capabilities) &Account>(addr)
    let contractNames = acct.contracts.names
    if contractNames.length == 0 {
        return []
    }

    let addrNo0x = addr.toString().slice(from: 2, upTo: addr.toString().length)

    let tokensDic: {Type: String} = {}
    let viewResolverDic: {Type: &{ViewResolver}} = {}
    for contractName in contractNames {
        log("Loading Contract: ".concat(contractName))
        if let ftReff = acct.contracts.borrow<&{FungibleToken}>(name: contractName) {
            let ftType = CompositeType("A.".concat(addrNo0x)
                .concat(".").concat(contractName)
                .concat(".Vault"))
            if ftType != nil && !ftType!.isRecovered {
                tokensDic[ftType!] = contractName
                // Borrow the view resolver for the contract
                if let viewResolver = ViewResolvers.borrowContractViewResolver(addr, contractName) {
                    log("ViewResolver for ".concat(contractName).concat("is borrowed"))
                    viewResolverDic[ftType!] = viewResolver
                }
            }
        } else if let nftRef = acct.contracts.borrow<&{NonFungibleToken}>(name: contractName) {
            let collectionType = CompositeType("A.".concat(addrNo0x)
                .concat(".").concat(contractName)
                .concat(".Collection"))
            if collectionType != nil && !collectionType!.isRecovered {
                tokensDic[collectionType!] = contractName
                // Borrow the view resolver for the contract
                if let viewResolver = ViewResolvers.borrowContractViewResolver(addr, contractName) {
                    log("ViewResolver for ".concat(contractName).concat("is borrowed"))
                    viewResolverDic[collectionType!] = viewResolver
                }
            }
        }
    }

    let pathsDic: {Type: String} = {}
    let pathToType: {String: Type} = {}
    acct.storage.forEachStored(fun (path: StoragePath, type: Type): Bool {
        if type.isRecovered {
            return true
        }
        if type.isSubtype(of: Type<@{FungibleToken.Vault}>()) {
            pathsDic[type] = path.toString()
            pathToType[path.toString()] = type
        } else if type.isSubtype(of: Type<@{NonFungibleToken.Collection}>()) {
            pathsDic[type] = path.toString()
            pathToType[path.toString()] = type
        }
        return true
    })
    let publicPathsDic: {Type: {String: String}} = {}
    acct.storage.forEachPublic(fun (path: PublicPath, type: Type): Bool {
        let capExists = acct.capabilities.exists(path)
        if capExists {
            let cap = acct.capabilities.get<&AnyResource>(path)
            if let controler = acct.capabilities.storage.getController(byCapabilityID: cap.id) {
                let storagePath = controler.target()

                if let tokenType = pathToType[storagePath.toString()] {
                    if publicPathsDic[tokenType] == nil {
                        publicPathsDic[tokenType] = {}
                    }
                    let ref = (&publicPathsDic[tokenType] as auth(Mutate) &{String: String}?)!
                    ref[type.identifier] = path.toString()
                }
            }
        }
        return true
    })

    let ret: [TokenAssetStatus] = []
    for tokenType in tokensDic.keys {
        let contractName = tokensDic[tokenType]!
        let supportedViews = viewResolverDic[tokenType]?.getContractViews(resourceType: nil) ?? []
        let isNFT = tokenType.isSubtype(of: Type<@{NonFungibleToken.Collection}>())
        let publicPaths = publicPathsDic[tokenType] ?? {}
        let isRegistered = isNFT
            ? NFTList.isNFTCollectionRegistered(addr, contractName)
            : TokenList.isFungibleTokenRegistered(addr, contractName)
        let bridgedType = !isNFT
            ? tokenType
            : CompositeType("A.".concat(addrNo0x).concat(".").concat(contractName).concat(".NFT"))
        let status = TokenAssetStatus(
            address: addr,
            contractName: contractName,
            isNFT: isNFT,
            isBridged: FlowEVMBridgeConfig.getEVMAddressAssociated(with: bridgedType!) != nil,
            isRegistered: isRegistered,
            isRegisteredWithNativeViewResolver: isRegistered && viewResolverDic[tokenType] != nil,
            isWithDisplay: isNFT
                ? supportedViews.contains(Type<MetadataViews.NFTCollectionDisplay>())
                : supportedViews.contains(Type<FungibleTokenMetadataViews.FTDisplay>()),
            isWithVaultData: isNFT
                ? supportedViews.contains(Type<MetadataViews.NFTCollectionData>())
                : supportedViews.contains(Type<FungibleTokenMetadataViews.FTVaultData>()),
            storagePath: pathsDic[tokenType],
            publicPath: publicPaths[publicPaths.keys[0]],
            publicPaths: publicPaths
        )
        ret.append(status)
    }
    return ret
}

access(all) struct TokenAssetStatus {
    access(all)
    let address: Address
    access(all)
    let contractName: String
    access(all)
    let isNFT: Bool
    access(all)
    let isBridged: Bool
    access(all)
    let isRegistered: Bool
    access(all)
    let isRegisteredWithNativeViewResolver: Bool
    access(all)
    let isWithDisplay: Bool
    access(all)
    let isWithVaultData: Bool
    access(all)
    let storagePath: String?
    access(all)
    let publicPath: String?
    access(all)
    let publicPaths: {String: String}

    init(
        address: Address,
        contractName: String,
        isNFT: Bool,
        isBridged: Bool,
        isRegistered: Bool,
        isRegisteredWithNativeViewResolver: Bool,
        isWithDisplay: Bool,
        isWithVaultData: Bool,
        storagePath: String?,
        publicPath: String?,
        publicPaths: {String: String}
    ) {
        self.address = address
        self.contractName = contractName
        self.isNFT = isNFT
        self.isBridged = isBridged
        self.isRegistered = isRegistered
        self.isRegisteredWithNativeViewResolver = isRegisteredWithNativeViewResolver
        self.isWithDisplay = isWithDisplay
        self.isWithVaultData = isWithVaultData
        self.storagePath = storagePath
        self.publicPath = publicPath
        self.publicPaths = publicPaths
    }
}

```