# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/hw_v2/scripts/hw_v2_get_owned_tokens_by_address.cdc

```
import "NonFungibleToken"
import "MetadataViews"
import "FungibleToken"
import "FlowToken"
import "HWGarageTokenV2"

access(all) fun main(address: Address): [{String: AnyStruct}] {
    let account: &Account = getAccount(address)
    let tokenPubPath: PublicPath = HWGarageTokenV2.CollectionPublicPath
    let tokenCollection: &HWGarageTokenV2.Collection? = account.capabilities.get<&HWGarageTokenV2.Collection>(tokenPubPath).borrow()
    let ownedTokens: [{String: AnyStruct}] = []
    if (tokenCollection == nil) {
        return ownedTokens
    }
    for id in tokenCollection!.getIDs() {
        let token: &HWGarageTokenV2.NFT? = tokenCollection!.borrowToken(id: id)
        // let packMetadataViews = tokenCollection!.borrowViewResolver(id: id)
        // let displayView = packMetadataViews.resolveView(Type<MetadataViews.Display>())
        // let externalURLView = packMetadataViews.resolveView(Type<MetadataViews.ExternalURL>())
        // let nftCollectionDisplayView = packMetadataViews.resolveView(Type<MetadataViews.NFTCollectionDisplay>())
        // let royaltiesView = packMetadataViews.resolveView(Type<MetadataViews.Royalties>())
        // let traitsView = packMetadataViews.resolveView(Type<MetadataViews.Traits>())

        let map: {String: AnyStruct} = {}
        map["uuid"] = token!.uuid
        map["id"] = token!.id
        map["packSeriesID"] = token!.packSeriesID
        map["tokenEditionID"] = token!.tokenEditionID
        map["editionMetadata"] = token!.metadata
    
        // map["displayView"] = displayView
        // map["externalURLView"] = externalURLView
        // map["nftCollectionDisplayView"] = nftCollectionDisplayView
        // map["royaltiesView"] = royaltiesView
        // map["traitsView"] = traitsView
        ownedTokens.append(map)
    }
    return ownedTokens
}
 
 
```