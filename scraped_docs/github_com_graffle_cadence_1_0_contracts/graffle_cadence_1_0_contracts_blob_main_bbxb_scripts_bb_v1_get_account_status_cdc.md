# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/bbxb/scripts/bb_v1_get_account_status.cdc

```
import "NonFungibleToken"
import "MetadataViews"
import "FungibleToken"
import "FlowToken"
import "BBxBarbieToken"
import "BBxBarbieCard"
import "BBxBarbiePack"
import "NFTStorefrontV2"


access(all) fun main(address: Address): {String: Bool} {
    let account = getAccount(address)

    let accountStatus: {String: Bool} = {}

    let v2_tokenPubPath: PublicPath = BBxBarbieToken.CollectionPublicPath
    let tokenCollection: &BBxBarbieToken.Collection? = account.capabilities.get<&BBxBarbieToken.Collection>(v2_tokenPubPath).borrow()

    let v2_cardPubPath: PublicPath = BBxBarbieCard.CollectionPublicPath
    let cardCollection: &BBxBarbieCard.Collection? = account.capabilities.get<&BBxBarbieCard.Collection>(v2_cardPubPath).borrow()

    let v2_packPubPath: PublicPath = BBxBarbiePack.CollectionPublicPath
    let packCollection: &BBxBarbiePack.Collection? = account.capabilities.get<&BBxBarbiePack.Collection>(v2_packPubPath).borrow()

    let StorefrontV2: &{NFTStorefrontV2.StorefrontPublic}? = account.capabilities.borrow<&{NFTStorefrontV2.StorefrontPublic}>(NFTStorefrontV2.StorefrontPublicPath)


    if tokenCollection != nil {
        accountStatus.insert(key: "BBxBarbieToken", true)
    } else {
        accountStatus.insert(key: "BBxBarbieToken", false)
    }

    if cardCollection != nil {
        accountStatus.insert(key: "BBxBarbieCard", true)
    } else {
        accountStatus.insert(key: "BBxBarbieCard", false)
    }
    
    if packCollection != nil {
        accountStatus.insert(key: "BBxBarbiePack", true)
    } else {
        accountStatus.insert(key: "BBxBarbiePack", false)
    }

    if StorefrontV2 != nil {
        accountStatus.insert(key: "StorefrontV2", true)
    } else {
        accountStatus.insert(key: "StorefrontV2", false)
    }


    return accountStatus
}
 
```