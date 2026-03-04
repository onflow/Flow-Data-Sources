# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/hw_v1/scripts/hw_v1_get_single_card_by_address.cdc

```
import "NonFungibleToken"
import "MetadataViews"
import "FungibleToken"
import "FlowToken"
import "HWGarageCard"

access(all) fun main(address: Address, cardEditionID: UInt64): {String: AnyStruct} {
    let account = getAccount(address)
    let cardPubPath = HWGarageCard.CollectionPublicPath
    let HWGarageCardsCollection = account.capabilities.get<&HWGarageCard.Collection>(cardPubPath).borrow()
    let ownedCards: {String: AnyStruct} = {}
    if (HWGarageCardsCollection == nil) {
        return {"response":"HWGarageCard Collection Does not exist"}
    }
    if !HWGarageCardsCollection!.getIDs().contains(cardEditionID){
        return {"response":cardEditionID.toString().concat(" does not exist in address provided")}
    } else {
        let card = HWGarageCardsCollection!.borrowHWGarageCard(id: cardEditionID)
        
            let map: {String: AnyStruct} = {}
            ownedCards.insert(key: "uuid", card!.uuid)
            ownedCards.insert(key:"cardEditionID", card!.id)
            ownedCards.insert(key:"editionMetadata", card!.getMetadata())
        return ownedCards
   
    }
}


```