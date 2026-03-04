# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/hw_v1/scripts/hw_v1_get_count_NFT_packs.cdc

```
import "NonFungibleToken"
import "MetadataViews"
import "FungibleToken"
import "FlowToken"
import "HWGaragePack"

access(all) fun main(address: Address): AnyStruct {
    let account = getAccount(address)
    let tokenPubPath = HWGaragePack.CollectionPublicPath
    let HWGarageCardsPackCollection = account.capabilities.get<&HWGaragePack.Collection>(tokenPubPath).borrow()
    let ownedPacks: [{String: AnyStruct}] = []
    if (HWGarageCardsPackCollection == nil) {
        return ownedPacks
    }
    return HWGarageCardsPackCollection!.getIDs().length
}

```