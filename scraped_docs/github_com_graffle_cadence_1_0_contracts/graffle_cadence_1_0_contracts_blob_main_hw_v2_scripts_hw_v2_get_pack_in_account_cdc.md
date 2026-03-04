# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/hw_v2/scripts/hw_v2_get_pack_in_account.cdc

```
import "NonFungibleToken"
import "MetadataViews"
import "FungibleToken"
import "FlowToken"
import "HWGaragePackV2"

access(all) fun main(address: Address, tokenID: UInt64): {String: AnyStruct} {
    let account = getAccount(address)
    let packPubPath = HWGaragePackV2.CollectionPublicPath
    let cardsCollection = account.capabilities.get<&HWGaragePackV2.Collection>(packPubPath).borrow()
    if (cardsCollection == nil) {
        return {"response":"HWGaragePackV2 Collection Does not exist"}
    }
    if !cardsCollection!.getIDs().contains(tokenID) {
        return {"response":tokenID.toString().concat(" does not exist in address provided")}
    } else {
        let token: &HWGaragePackV2.NFT? = cardsCollection!.borrowPack(id: tokenID)
        let cardMetadataViews = cardsCollection!.borrowViewResolver(id: tokenID)
        let displayView = cardMetadataViews?.resolveView(Type<MetadataViews.Display>())
        let externalURLView = cardMetadataViews?.resolveView(Type<MetadataViews.ExternalURL>())
        // let nftCollectionDataView = cardMetadataViews.resolveView(Type<MetadataViews.NFTCollectionData>())
        let nftCollectionDisplayView = cardMetadataViews?.resolveView(Type<MetadataViews.NFTCollectionDisplay>())
        let royaltiesView = cardMetadataViews?.resolveView(Type<MetadataViews.Royalties>())
        let traitsView = cardMetadataViews?.resolveView(Type<MetadataViews.Traits>())
        return({
            "uuid": token!.uuid
            // ,"id": token!.id
            // ,"packID": token!.packSeriesID
            // ,"packEditionID": token!.packEditionID
            // ,"packHash": token!.packHash
            // ,"editionMetadata": token!.metadata
            ,"displayView": displayView
            // ,"externalURLView": externalURLView
            //         // ,"nftCollectionDataView":nftCollectionDataView
            ,"nftCollectionDisplayView":nftCollectionDisplayView
            // ,"royaltiesView": royaltiesView
            // ,"traitsView": traitsView
        })
    }
}
 
```