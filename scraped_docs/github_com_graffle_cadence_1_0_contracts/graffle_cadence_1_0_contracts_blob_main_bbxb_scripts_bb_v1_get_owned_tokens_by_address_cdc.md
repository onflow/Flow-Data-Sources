# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/bbxb/scripts/bb_v1_get_owned_tokens_by_address.cdc

```
import "NonFungibleToken"
import "MetadataViews"
import "FungibleToken"
import "FlowToken"
import "BBxBarbieToken"

access(all) fun main(address: Address): [{String: AnyStruct}] {
    let account: &Account = getAccount(address)
    let tokenPubPath: PublicPath = BBxBarbieToken.CollectionPublicPath
    let tokenCollection: &BBxBarbieToken.Collection? = account.capabilities.get<&BBxBarbieToken.Collection>(tokenPubPath).borrow()
    let ownedTokens: [{String: AnyStruct}] = []
    if (tokenCollection == nil) {
        return ownedTokens
    }
    for id in tokenCollection!.getIDs() {
        let token: &BBxBarbieToken.NFT? = tokenCollection!.borrowToken(id: id)

        let map: {String: AnyStruct} = {}
        map["uuid"] = token!.uuid
        map["id"] = token!.id
        map["packSeriesID"] = token!.packSeriesID
        map["tokenEditionID"] = token!.tokenEditionID
        map["redeemable"] = token!.redeemable
        map["metadata"] = token!.metadata

        ownedTokens.append(map)
    }
    return ownedTokens
}
 
 
```