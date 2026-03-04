# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/hw_v2/scripts/hw_v2_get_redeemable_cards_by_address.cdc

```
import "NonFungibleToken"
import "MetadataViews"
import "FungibleToken"
import "FlowToken"
import "HWGarageCardV2"

access(all) fun main(address: Address): [{String: AnyStruct}] {
    let account = getAccount(address)
    let cardPubPath = HWGarageCardV2.CollectionPublicPath
    let cardCollection = account.capabilities.get<&HWGarageCardV2.Collection>(cardPubPath).borrow()
    let redeemableCards: [{String: AnyStruct}] = []
    if (cardCollection == nil) {
        return redeemableCards
    }
    for id in cardCollection!.getIDs() {
        let map: {String: AnyStruct} = {}

        let card = cardCollection!.borrowCard(id: id)

        if (card!.redeemable.toLower() == "true"){
            let packMetadataViews = cardCollection!.borrowViewResolver(id: id)           
            let displayView = packMetadataViews?.resolveView(Type<MetadataViews.Display>())
            let externalURLView = packMetadataViews?.resolveView(Type<MetadataViews.ExternalURL>())
            let nftCollectionDisplayView = packMetadataViews?.resolveView(Type<MetadataViews.NFTCollectionDisplay>())
            let royaltiesView = packMetadataViews?.resolveView(Type<MetadataViews.Royalties>())
            let traitsView = packMetadataViews?.resolveView(Type<MetadataViews.Traits>())

            map["uuid"] = card!.uuid
            map["id"] = card!.id
            map["isRedeemable"] = card!.redeemable
            map["packSeriesID"] = card!.packSeriesID
            map["cardEditionID"] = card!.cardEditionID
            map["packHash"] = card!.packHash
            map["nftCollectionDisplayView"] = nftCollectionDisplayView
            map["royaltiesView"] = royaltiesView
            map["displayView"] = displayView
            map["traitsView"] = traitsView

            redeemableCards.append(map)
        }


        
    }
    return redeemableCards
}
 
 
```