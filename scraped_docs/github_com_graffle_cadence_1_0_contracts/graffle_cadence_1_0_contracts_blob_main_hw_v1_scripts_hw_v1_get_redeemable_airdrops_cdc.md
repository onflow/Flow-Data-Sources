# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/hw_v1/scripts/hw_v1_get_redeemable_airdrops.cdc

```
/*
 * Note: This transaction will fail due to the size of the dictionary that we used to store metadata.
 */
import "NonFungibleToken"
import "MetadataViews"
import "FungibleToken"
import "FlowToken"
import "HWGaragePack"
import "ViewResolver"

access(all) fun main(address: Address): [{String: AnyStruct}] {
    let account: &Account = getAccount(address)
    let packPubPath: PublicPath = HWGaragePack.CollectionPublicPath
    let airdropPacksCollection: &HWGaragePack.Collection? = account.capabilities.get<&HWGaragePack.Collection>(packPubPath).borrow()
    let ownedAirdropPacks: [{String: AnyStruct}] = []
    if (airdropPacksCollection == nil) {
        return ownedAirdropPacks
    }
    for id in airdropPacksCollection!.getIDs() {
        let airdropPack: &HWGaragePack.NFT? = airdropPacksCollection!.borrowPack(id: id)
        let metadataViews: &{ViewResolver.Resolver}? = airdropPacksCollection!.borrowViewResolver(id: id)
        let displayView: AnyStruct?? = metadataViews?.resolveView(Type<MetadataViews.Display>())

        if (airdropPack!.packID == 2) {
            let map: {String: AnyStruct} = {}
            map["uuid"] = airdropPack!.uuid
            map["id"] = id
            map["edition"] = id
            map["packID"] = airdropPack!.packID
            map["packEditionID"] = airdropPack!.packEditionID
            map["displayView"] = displayView
            ownedAirdropPacks.append(map)
        }
    }
    return ownedAirdropPacks
}
 
```