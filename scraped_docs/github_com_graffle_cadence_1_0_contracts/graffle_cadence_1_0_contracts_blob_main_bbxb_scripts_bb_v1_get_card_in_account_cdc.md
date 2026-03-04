# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/bbxb/scripts/bb_v1_get_card_in_account.cdc

```
import "NonFungibleToken"
import "MetadataViews"
import "FungibleToken"
import "FlowToken"
import "BBxBarbieCard"

access(all) fun main(address: Address, tokenID: UInt64): {String: AnyStruct} {
    let account: &Account = getAccount(address)
    let cardPubPath: PublicPath = BBxBarbieCard.CollectionPublicPath
    let cardsCollection: &BBxBarbieCard.Collection? = account.capabilities.get<&BBxBarbieCard.Collection>(cardPubPath).borrow()
    if (cardsCollection == nil) {
        return {"response":"BBxBarbieCard Collection Does not exist"}
    }
    if !cardsCollection!.getIDs().contains(tokenID) {
        return {"response":tokenID.toString().concat(" does not exist in address provided")}
    } else {
        let token: &BBxBarbieCard.NFT? = cardsCollection!.borrowCard(id: tokenID)
        return({
            "uuid": token!.uuid
            ,"id": token!.id
            ,"packSeriesID": token!.packSeriesID
            ,"metadata": token!.metadata
        })
    }
}
 
```