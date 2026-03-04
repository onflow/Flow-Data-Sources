# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/hw_v1/scripts/hw_v1_get_count_NFTs.cdc

```
import "NonFungibleToken"
import "MetadataViews"
import "FungibleToken"
import "FlowToken"
import "HWGarageCard"

access(all) fun main(address: Address): AnyStruct {
    let account: &Account = getAccount(address)
    let tokenPubPath: PublicPath = HWGarageCard.CollectionPublicPath
    let HWGarageCardsCollection: &HWGarageCard.Collection? = account.capabilities.get<&HWGarageCard.Collection>(tokenPubPath).borrow()
    let ownedCards: [{String: AnyStruct}] = []
    if (HWGarageCardsCollection == nil) {
        return ownedCards
    }
    return HWGarageCardsCollection!.getIDs().length
}

```