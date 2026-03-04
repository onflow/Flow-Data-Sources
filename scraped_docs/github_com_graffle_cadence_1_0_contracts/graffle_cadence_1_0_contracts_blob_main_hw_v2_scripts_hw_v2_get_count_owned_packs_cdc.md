# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/hw_v2/scripts/hw_v2_get_count_owned_packs.cdc

```
import "NonFungibleToken"
import "MetadataViews"
import "FungibleToken"
import "FlowToken"
import "HWGaragePackV2"

access(all) fun main(address: Address): AnyStruct {
    let account: &Account = getAccount(address)
    let packPubPath: PublicPath = HWGaragePackV2.CollectionPublicPath
    let HWGaragePackV2Collection: &HWGaragePackV2.Collection? = account.capabilities.get<&HWGaragePackV2.Collection>(packPubPath).borrow()
    let ownedPacks: [{String: AnyStruct}] = []
    if (HWGaragePackV2Collection == nil) {
        return ownedPacks
    }
    return HWGaragePackV2Collection!.getIDs().length
}

```