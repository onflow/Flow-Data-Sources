# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/hw_v2/scripts/hw_v2_get_owned_cards_by_address.cdc

```
import "NonFungibleToken"
import "MetadataViews"
import "FungibleToken"
import "FlowToken"
import "HWGarageCardV2"

access(all) fun main(address: Address): [{String: AnyStruct}] {
    let account: &Account = getAccount(address)
    let cardPubPath: PublicPath = HWGarageCardV2.CollectionPublicPath
    let cardCollection: &HWGarageCardV2.Collection? = account.capabilities.get<&HWGarageCardV2.Collection>(cardPubPath).borrow()
    let ownedCards: [{String: AnyStruct}] = []
    if (cardCollection == nil) {
        return ownedCards
    }
    for id in cardCollection!.getIDs() {
        let card: &HWGarageCardV2.NFT? = cardCollection!.borrowCard(id: id)
        // let packMetadataViews = cardCollection!.borrowViewResolver(id: id)
        // let displayView = packMetadataViews.resolveView(Type<MetadataViews.Display>())
        // let externalURLView = packMetadataViews.resolveView(Type<MetadataViews.ExternalURL>())
        // let nftCollectionDisplayView = packMetadataViews.resolveView(Type<MetadataViews.NFTCollectionDisplay>())
        // let royaltiesView = packMetadataViews.resolveView(Type<MetadataViews.Royalties>())
        // let traitsView = packMetadataViews.resolveView(Type<MetadataViews.Traits>())

        let map: {String: AnyStruct} = {}
        map["uuid"] = card!.uuid
        map["id"] = card!.id
        map["packSeriesID"] = card!.packSeriesID
        map["cardEditionID"] = card!.cardEditionID
        map["editionMetadata"] = card!.metadata
        // map["packHash"] = card!.packHash
        // map["displayView"] = displayView
        // map["externalURLView"] = externalURLView
        // map["nftCollectionDisplayView"] = nftCollectionDisplayView
        // map["royaltiesView"] = royaltiesView
        // map["traitsView"] = traitsView
        ownedCards.append(map)
    }
    return ownedCards
}
 
 
```