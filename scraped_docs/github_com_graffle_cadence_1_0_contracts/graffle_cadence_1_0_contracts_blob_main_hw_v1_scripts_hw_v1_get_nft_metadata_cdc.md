# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/hw_v1/scripts/hw_v1_get_NFT_metadata.cdc

```
import "NonFungibleToken"
import "MetadataViews"
import "FungibleToken"
import "FlowToken"
import "HWGarageCard"

access(all) fun main(address: Address, tokenID: UInt64): {String: AnyStruct} {
    let account = getAccount(address)
    let tokenPubPath = HWGarageCard.CollectionPublicPath
    let HWGarageCardsCollection = account.capabilities.get<&HWGarageCard.Collection>(tokenPubPath).borrow()
    if (HWGarageCardsCollection == nil) {
        return {"response":"HWGarageCard Collection Does not exist"}
    }
    if !HWGarageCardsCollection!.getIDs().contains(tokenID) {
        return {"response":tokenID.toString().concat(" does not exist in address provided")}
    } else {
        let token = HWGarageCardsCollection!.borrowHWGarageCard(id: tokenID)
        return token!.getMetadata()
    }
}
 
```