# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/hw_v2/scripts/hw_v2_get_account_status.cdc

```
import "NonFungibleToken"
import "MetadataViews"
import "FungibleToken"
import "FlowToken"
import "HWGarageCard"
import "HWGaragePack"
import "HWGarageTokenV2"
import "HWGarageCardV2"
import "HWGaragePackV2"
import "NFTStorefrontV2"


access(all) fun main(address: Address): {String: Bool} {
    let account: &Account = getAccount(address)

    let accountStatus: {String: Bool} = {}
    
    // V1
    let v1_cardPubPath: PublicPath = HWGarageCard.CollectionPublicPath
    let v1_cardCollection: &HWGarageCard.Collection? = account.capabilities.get<&HWGarageCard.Collection>(v1_cardPubPath).borrow()

    let v1_packPubPath: PublicPath = HWGaragePack.CollectionPublicPath
    let v1_packCollection: &HWGaragePack.Collection? = account.capabilities.get<&HWGaragePack.Collection>(v1_packPubPath).borrow()

    // V2
    let v2_tokenPubPath: PublicPath = HWGarageTokenV2.CollectionPublicPath
    let v2_tokenCollection: &HWGarageTokenV2.Collection? = account.capabilities.get<&HWGarageTokenV2.Collection>(v2_tokenPubPath).borrow()

    let v2_cardPubPath: PublicPath = HWGarageCardV2.CollectionPublicPath
    let v2_cardCollection: &HWGarageCardV2.Collection? = account.capabilities.get<&HWGarageCardV2.Collection>(v2_cardPubPath).borrow()

    let v2_packPubPath: PublicPath = HWGaragePackV2.CollectionPublicPath
    let v2_packCollection: &HWGaragePackV2.Collection? = account.capabilities.get<&HWGaragePackV2.Collection>(v2_packPubPath).borrow()

    let StorefrontV2: &{NFTStorefrontV2.StorefrontPublic}? = account.capabilities.borrow<&{NFTStorefrontV2.StorefrontPublic}>(NFTStorefrontV2.StorefrontPublicPath)


    if v1_cardCollection != nil {
        accountStatus.insert(key: "HWGarageCard", true)
    } else {
        accountStatus.insert(key: "HWGarageCard", false)
    }
    
    if v1_packCollection != nil {
        accountStatus.insert(key: "HWGaragePack", true)
    } else {
        accountStatus.insert(key: "HWGaragePack", false)
    }

    if v2_tokenCollection != nil {
        accountStatus.insert(key: "HWGarageTokenV2", true)
    } else {
        accountStatus.insert(key: "HWGarageTokenV2", false)
    }

    if v2_cardCollection != nil {
        accountStatus.insert(key: "HWGarageCardV2", true)
    } else {
        accountStatus.insert(key: "HWGarageCardV2", false)
    }
    
    if v2_packCollection != nil {
        accountStatus.insert(key: "HWGaragePackV2", true)
    } else {
        accountStatus.insert(key: "HWGaragePackV2", false)
    }

    if StorefrontV2 != nil {
        accountStatus.insert(key: "StorefrontV2", true)
    } else {
        accountStatus.insert(key: "StorefrontV2", false)
    }


    return accountStatus
}
 
```