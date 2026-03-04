# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/hw_v2/scripts/hw_v2_get_count_owned_tokens.cdc

```
import "NonFungibleToken"
import "MetadataViews"
import "FungibleToken"
import "FlowToken"
import "HWGarageTokenV2"

access(all) fun main(address: Address): AnyStruct {
    let account: &Account = getAccount(address)
    let tokenPubPath: PublicPath = HWGarageTokenV2.CollectionPublicPath
    let HWGarageTokenV2sCollection: &HWGarageTokenV2.Collection? = account.capabilities.get<&HWGarageTokenV2.Collection>(tokenPubPath).borrow()
    let ownedCards: [{String: AnyStruct}] = []
    if (HWGarageTokenV2sCollection == nil) {
        return ownedCards
    }
    return HWGarageTokenV2sCollection!.getIDs().length
}

```