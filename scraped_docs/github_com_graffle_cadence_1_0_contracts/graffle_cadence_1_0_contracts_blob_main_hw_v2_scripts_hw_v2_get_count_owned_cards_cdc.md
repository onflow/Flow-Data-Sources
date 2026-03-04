# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/hw_v2/scripts/hw_v2_get_count_owned_cards.cdc

```
import "NonFungibleToken"
import "MetadataViews"
import "FungibleToken"
import "FlowToken"
import "HWGarageCardV2"

access(all) fun main(address: Address): AnyStruct {
    let account: &Account = getAccount(address)
    let cardPubPath: PublicPath = HWGarageCardV2.CollectionPublicPath
    let HWGarageCardV2sCollection: &HWGarageCardV2.Collection? = account.capabilities.get<&HWGarageCardV2.Collection>(cardPubPath).borrow()
    let ownedCards: [{String: AnyStruct}] = []
    if (HWGarageCardV2sCollection == nil) {
        return ownedCards
    }
    return HWGarageCardV2sCollection!.getIDs().length
}

```