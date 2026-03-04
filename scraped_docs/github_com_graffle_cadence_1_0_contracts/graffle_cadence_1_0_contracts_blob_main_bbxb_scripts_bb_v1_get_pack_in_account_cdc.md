# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/bbxb/scripts/bb_v1_get_pack_in_account.cdc

```
import "NonFungibleToken"
import "MetadataViews"
import "FungibleToken"
import "FlowToken"
import "BBxBarbiePack"

access(all) fun main(address: Address, tokenID: UInt64): {String: AnyStruct} {
    let account: &Account = getAccount(address)
    let packPubPath: PublicPath = BBxBarbiePack.CollectionPublicPath
    let cardsCollection = account.capabilities.get<&BBxBarbiePack.Collection>(packPubPath).borrow()
    if (cardsCollection == nil) {
        return {"response":"BBxBarbiePack Collection Does not exist"}
    }
    if !cardsCollection!.getIDs().contains(tokenID) {
        return {"response":tokenID.toString().concat(" does not exist in address provided")}
    } else {
        let token: &BBxBarbiePack.NFT? = cardsCollection!.borrowPack(id: tokenID)
        let cardMetadataViews = cardsCollection!.borrowViewResolver(id: tokenID)
        return({
            "uuid": token!.uuid
            ,"id": token!.id
            ,"packSeriesID": token!.packSeriesID
            , "metadata" : token!.metadata
        })
    }
}
 
```