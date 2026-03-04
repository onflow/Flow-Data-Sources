# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/bbxb/scripts/bb_v1_get_count_owned_packs.cdc

```
import "NonFungibleToken"
import "MetadataViews"
import "FungibleToken"
import "FlowToken"
import "BBxBarbiePack"

access(all) fun main(address: Address): AnyStruct {
    let account: &Account = getAccount(address)
    let packPubPath: PublicPath = BBxBarbiePack.CollectionPublicPath
    let BBxBarbiePackCollection: &BBxBarbiePack.Collection? = account.capabilities.get<&BBxBarbiePack.Collection>(packPubPath).borrow()
    let ownedPacks: [{String: AnyStruct}] = []
    if (BBxBarbiePackCollection == nil) {
        return ownedPacks
    }
    return BBxBarbiePackCollection!.getIDs().length

}
 
```