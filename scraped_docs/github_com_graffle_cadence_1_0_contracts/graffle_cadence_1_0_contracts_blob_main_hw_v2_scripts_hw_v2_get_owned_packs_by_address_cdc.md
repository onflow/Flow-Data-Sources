# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/hw_v2/scripts/hw_v2_get_owned_packs_by_address.cdc

```
import "NonFungibleToken"
import "MetadataViews"
import "FungibleToken"
import "FlowToken"
import "HWGaragePackV2"

access(all) fun main(address: Address): [{String: AnyStruct}] {

    let account: &Account = getAccount(address)
    let packPubPath: PublicPath = HWGaragePackV2.CollectionPublicPath
    let packsCollection: &HWGaragePackV2.Collection? = account.capabilities.get<&HWGaragePackV2.Collection>(packPubPath).borrow()
    let ownedPacks: [{String: AnyStruct}] = []

    if (packsCollection == nil) {
        return ownedPacks
    }

    for id in packsCollection!.getIDs() {
        let cardPack: &HWGaragePackV2.NFT? = packsCollection!.borrowPack(id: id)
        // let metadataViews = packsCollection!.borrowViewResolver(id: id)
        // let displayView = metadataViews.resolveView(Type<MetadataViews.Display>())
        // let externalURLView = metadataViews.resolveView(Type<MetadataViews.ExternalURL>())
        // let nftCollectionDisplayView = metadataViews.resolveView(Type<MetadataViews.NFTCollectionDisplay>())
        // let royaltiesView = metadataViews.resolveView(Type<MetadataViews.Royalties>())
        // let traitsView = metadataViews.resolveView(Type<MetadataViews.Traits>())

        let map: {String: AnyStruct} = {}

        map["uuid"] = cardPack!.uuid
        map["id"] = cardPack!.id
        map["packID"] = cardPack!.packSeriesID
        map["packEditionID"] = cardPack!.packEditionID
        map["editionMetadata"] = cardPack!.metadata
        // map["packHash"] = cardPack!.packHash
        // map["displayView"] = displayView
        // map["externalURLView"] = externalURLView
        // map["nftCollectionDisplayView"] = nftCollectionDisplayView
        // map["royaltiesView"] = royaltiesView
        // map["traitsView"] = traitsView

        ownedPacks.append(map)
    }
    return ownedPacks
}

```