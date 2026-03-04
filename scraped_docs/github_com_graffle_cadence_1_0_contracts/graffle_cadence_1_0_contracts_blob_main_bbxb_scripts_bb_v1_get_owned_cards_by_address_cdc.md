# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/bbxb/scripts/bb_v1_get_owned_cards_by_address.cdc

```
import "NonFungibleToken"
import "MetadataViews"
import "FungibleToken"
import "FlowToken"
import "BBxBarbieCard"

access(all) fun main(address: Address): [{String: AnyStruct}] {
    let account: &Account = getAccount(address)
    let cardPubPath: PublicPath = BBxBarbieCard.CollectionPublicPath
    let cardCollection: &BBxBarbieCard.Collection? = account.capabilities.get<&BBxBarbieCard.Collection>(cardPubPath).borrow()
    let ownedCards: [{String: AnyStruct}] = []
    if (cardCollection == nil) {
        return ownedCards
    }
    for id in cardCollection!.getIDs() {
        let card: &BBxBarbieCard.NFT? = cardCollection!.borrowCard(id: id)

        let map: {String: AnyStruct} = {}
        map["uuid"] = card!.uuid
        map["id"] = card!.id
        map["packSeriesID"] = card!.packSeriesID
        map["cardEditionID"] = card!.cardEditionID
        map["metadata"] = card!.metadata

        ownedCards.append(map)
    }
    return ownedCards
}
 
 
```