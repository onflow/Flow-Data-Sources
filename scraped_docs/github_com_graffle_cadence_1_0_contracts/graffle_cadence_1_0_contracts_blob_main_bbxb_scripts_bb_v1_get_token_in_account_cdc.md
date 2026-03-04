# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/bbxb/scripts/bb_v1_get_token_in_account.cdc

```
import "NonFungibleToken"
import "MetadataViews"
import "FungibleToken"
import "FlowToken"
import "BBxBarbieToken"

access(all) fun main(address: Address, tokenID: UInt64): {String: AnyStruct} {
    let account: &Account = getAccount(address)
    let tokenPubPath: PublicPath = BBxBarbieToken.CollectionPublicPath
    let tokensCollection: &BBxBarbieToken.Collection? = account.capabilities.get<&BBxBarbieToken.Collection>(tokenPubPath).borrow()
    if (tokensCollection == nil) {
        return {"response":"BBxBarbieToken Collection Does not exist"}
    }
    if !tokensCollection!.getIDs().contains(tokenID) {
        return {"response":tokenID.toString().concat(" does not exist in address provided")}
    } else {
        let token: &BBxBarbieToken.NFT? = tokensCollection!.borrowToken(id: tokenID)

        return({
            "uuid": token!.uuid
            ,"id": token!.id
            ,"packSeriesID": token!.packSeriesID
            ,"metadata": token!.metadata
        })
    }
}
 
```