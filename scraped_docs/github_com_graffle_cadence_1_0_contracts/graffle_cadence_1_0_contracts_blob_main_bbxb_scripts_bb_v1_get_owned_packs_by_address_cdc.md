# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/bbxb/scripts/bb_v1_get_owned_packs_by_address.cdc

```
import "NonFungibleToken"
import "MetadataViews"
import "FungibleToken"
import "FlowToken"
import "BBxBarbiePack"

access(all) fun main(address: Address): [{String: AnyStruct}] {
    let account: &Account = getAccount(address)
    let packPubPath: PublicPath = BBxBarbiePack.CollectionPublicPath
    let packsCollection: &BBxBarbiePack.Collection? = account.capabilities.get<&BBxBarbiePack.Collection>(packPubPath).borrow()
    let ownedPacks: [{String: AnyStruct}] = []
    if (packsCollection == nil) {
        return ownedPacks
    }
    for id in packsCollection!.getIDs() {
        let pack: &BBxBarbiePack.NFT? = packsCollection!.borrowPack(id: id)

        let map: {String: AnyStruct} = {}
        map["uuid"] = pack!.uuid
        map["id"] = pack!.id
        map["packSeriesID"] = pack!.packSeriesID
        map["packEditionID"] = pack!.packEditionID
        map["metadata"] = pack!.metadata

        ownedPacks.append(map)
    }
    return ownedPacks
}
```