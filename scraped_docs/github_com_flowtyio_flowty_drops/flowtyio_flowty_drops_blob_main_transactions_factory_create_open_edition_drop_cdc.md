# Source: https://github.com/Flowtyio/flowty-drops/blob/main/transactions/factory/create_open_edition_drop.cdc

```
import "ContractFactoryTemplate"
import "ContractFactory"
import "OpenEditionTemplate"
import "MetadataViews"
import "OpenEditionInitializer"
import "ContractManager"
import "FungibleToken"
import "FlowToken"
import "FlowtyDrops"
import "NFTMetadata"
import "FlowtyActiveCheckers"
import "FlowtyPricers"
import "FlowtyAddressVerifiers"
    
transaction(contractName: String, managerInitialTokenBalance: UFix64, start: UInt64?, end: UInt64?, price: UFix64, paymentTokenType: String, phaseArgs: {String: String}, metadataArgs: {String: String}, collectionInfoArgs: {String: String}, dropDetailArgs: {String: String}) {
    prepare(acct: auth(Storage, Capabilities) &Account) {
        if acct.storage.type(at: ContractManager.StoragePath) == nil {
            let v = acct.storage.borrow<auth(FungibleToken.Withdraw) &FlowToken.Vault>(from: /storage/flowTokenVault)!
            let tokens <- v.withdraw(amount: managerInitialTokenBalance) as! @FlowToken.Vault

            acct.storage.save(<- ContractManager.createManager(tokens: <-tokens, defaultRouterAddress: acct.address), to: ContractManager.StoragePath)
            acct.storage.borrow<auth(ContractManager.Manage) &ContractManager.Manager>(from: ContractManager.StoragePath)!.onSave()

            acct.capabilities.publish(
                acct.capabilities.storage.issue<&ContractManager.Manager>(ContractManager.StoragePath),
                at: ContractManager.PublicPath
            )
        }

        let manager: auth(ContractManager.Manage) &ContractManager.Manager = acct.storage.borrow<auth(ContractManager.Manage) &ContractManager.Manager>(from: ContractManager.StoragePath)
            ?? panic("manager was not borrowed successfully")

        let data: {String: AnyStruct} = {}
        let nftMetadata: NFTMetadata.Metadata = NFTMetadata.Metadata(
            name: metadataArgs["name"]!,
            description: metadataArgs["description"]!,
            thumbnail: MetadataViews.IPFSFile(cid: metadataArgs["cid"]!, path: metadataArgs["path"]),
            traits: nil,
            editions: nil,
            externalURL: metadataArgs["externalURL"] != nil ? MetadataViews.ExternalURL(metadataArgs["externalURL"]!) : nil,
            royalties: nil,
            data: data
        )

        let socials: {String: MetadataViews.ExternalURL} = {}
        let keys = ["twitter", "x", "discord", "instagram"]
        for k in keys {
            if let v = collectionInfoArgs[k] {
                socials[k] = MetadataViews.ExternalURL(v)
            }
        }

        let collectionDisplay = MetadataViews.NFTCollectionDisplay(
            name: collectionInfoArgs["name"]!,
            description: collectionInfoArgs["description"]!,
            externalURL: MetadataViews.ExternalURL(collectionInfoArgs["externalURL"]!),
            squareImage: MetadataViews.Media(
                file: MetadataViews.IPFSFile(cid: collectionInfoArgs["squareImageCid"]!, path: collectionInfoArgs["squareImagePath"]),
                mediaType: collectionInfoArgs["squareImageMediaType"]!
            ),
            bannerImage: MetadataViews.Media(
                file: MetadataViews.IPFSFile(cid: collectionInfoArgs["bannerImageCid"]!, path: collectionInfoArgs["bannerImagePath"]),
                mediaType: collectionInfoArgs["bannerImageMediaType"]!
            ),
            socials: socials
        )

        let addrStr = manager.getAccount().address.toString()
        let nftType = "A.".concat(addrStr.slice(from: 2, upTo: addrStr.length)).concat(".").concat(contractName).concat(".NFT")

        let dropDetails = FlowtyDrops.DropDetails(
            display: MetadataViews.Display(
                name: dropDetailArgs["name"]!,
                description: dropDetailArgs["description"]!,
                thumbnail: MetadataViews.IPFSFile(cid: dropDetailArgs["thumbnailCid"]!, path: dropDetailArgs["thumbnailPath"])
            ),
            medias: nil,
            commissionRate: 0.05,
            nftType: nftType,
            paymentTokenTypes: {paymentTokenType: true}
        )

        let phaseDetails = FlowtyDrops.PhaseDetails(
            activeChecker: FlowtyActiveCheckers.TimestampChecker(start: start, end: end),
            display: phaseArgs["displayName"] != nil ? MetadataViews.Display(
                name: phaseArgs["displayName"]!,
                description: phaseArgs["displayDescription"]!,
                thumbnail: MetadataViews.IPFSFile(cid: phaseArgs["displayCid"]!, path: phaseArgs["displayPath"])
            ) : nil,
            pricer: FlowtyPricers.FlatPrice(price: price, paymentTokenType: CompositeType(paymentTokenType)!),
            addressVerifier: FlowtyAddressVerifiers.AllowAll(maxPerMint: 10)
        )

        // The Open edition initializer requires at least two keys:
        // - data: NFTMetadata.Metadata
        // - collectionInfo: NFTMetadata.CollectionInfo
        // 
        // You can also specify some optional paramters:
        // - dropDetails: FlowtyDrops.DropDetails
        // - phaseDetails: [FlowtyDrops.PhaseDetails]
        // - minterController: This is supplied in the initialization of the contract itself
        let arr: [FlowtyDrops.PhaseDetails] = [phaseDetails]
        let params: {String: AnyStruct} = {
            "data": nftMetadata,
            "collectionInfo": NFTMetadata.CollectionInfo(collectionDisplay: collectionDisplay),
            "dropDetails": dropDetails,
            "phaseDetails": arr
        }

        ContractFactory.createContract(templateType: Type<OpenEditionTemplate>(), acct: manager.borrowContractAccount(), name: contractName, params: params, initializeIdentifier: Type<OpenEditionInitializer>().identifier)
    }
}
```