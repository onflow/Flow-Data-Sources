# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/hw_v2/scripts/hw_v2_get_card_in_account.cdc

```
import "NonFungibleToken"
import "MetadataViews"
import "FungibleToken"
import "FlowToken"
import "HWGarageCardV2"

access(all) fun main(address: Address, tokenID: UInt64): {String: AnyStruct} {
    let account: &Account = getAccount(address)
    let cardPubPath: PublicPath = HWGarageCardV2.CollectionPublicPath
    let cardsCollection: &HWGarageCardV2.Collection? = account.capabilities.get<&HWGarageCardV2.Collection>(cardPubPath).borrow()
    if (cardsCollection == nil) {
        return {"response":"HWGarageCardV2 Collection Does not exist"}
    }
    if !cardsCollection!.getIDs().contains(tokenID) {
        return {"response":tokenID.toString().concat(" does not exist in address provided")}
    } else {
        let token: &HWGarageCardV2.NFT? = cardsCollection!.borrowCard(id: tokenID)
        // let cardMetadataViews = cardsCollection!.borrowViewResolver(id: tokenID)
        // let displayView = cardMetadataViews.resolveView(Type<MetadataViews.Display>())
        // let externalURLView = cardMetadataViews.resolveView(Type<MetadataViews.ExternalURL>())
                        // let nftCollectionDataView = cardMetadataViews.resolveView(Type<MetadataViews.NFTCollectionData>())
        // let nftCollectionDisplayView = cardMetadataViews.resolveView(Type<MetadataViews.NFTCollectionDisplay>())
        // let royaltiesView = cardMetadataViews.resolveView(Type<MetadataViews.Royalties>())
        // let traitsView = cardMetadataViews.resolveView(Type<MetadataViews.Traits>())
        return({
            "uuid": token!.uuid
            ,"id": token!.id
            ,"packSeriesID": token!.packSeriesID
            ,"cardEditionID": token!.cardEditionID
            ,"editionMetadata": token!.metadata
            // ,"displayView": displayView
            // ,"externalURLView": externalURLView
                        // ,"nftCollectionDataView":nftCollectionDataView
            // ,"nftCollectionDisplayView":nftCollectionDisplayView
            // ,"royaltiesView": royaltiesView
            // ,"traitsView": traitsView
        })
    }
}
 
```