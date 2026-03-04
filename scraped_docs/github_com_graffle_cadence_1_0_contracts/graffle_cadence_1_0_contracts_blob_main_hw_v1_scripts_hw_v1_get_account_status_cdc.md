# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/hw_v1/scripts/hw_v1_get_account_status.cdc

```
import "NonFungibleToken"
import "MetadataViews"
import "FungibleToken"
import "FlowToken"
import "HWGarageCard"
import "HWGaragePack"
import "NFTStorefrontV2"


access(all) fun main(address: Address): {String: Bool} {
    let account: &Account = getAccount(address)

    let accountStatus: {String: Bool} = {}

    let nftPubPath: PublicPath = HWGarageCard.CollectionPublicPath
    let nftCollection: &HWGarageCard.Collection? = account.capabilities.get<&HWGarageCard.Collection>(nftPubPath).borrow()

    let packPubPath: PublicPath = HWGaragePack.CollectionPublicPath
    let packCollection: &HWGaragePack.Collection? = account.capabilities.get<&HWGaragePack.Collection>(packPubPath).borrow()


    let StorefrontV2: &{NFTStorefrontV2.StorefrontPublic}? = account.capabilities.borrow<&{NFTStorefrontV2.StorefrontPublic}>(NFTStorefrontV2.StorefrontPublicPath)

    if nftCollection != nil {
        accountStatus.insert(key: "HWGarageCard", true)
    } else {
        accountStatus.insert(key: "HWGarageCard", false)
    }
    
    if packCollection != nil {
        accountStatus.insert(key: "HWGaragePack", true)
    } else {
        accountStatus.insert(key: "HWGaragePack", false)
    }

    if StorefrontV2 != nil {
        accountStatus.insert(key: "StorefrontV2", true)
    } else {
        accountStatus.insert(key: "StorefrontV2", false)
    }


    return accountStatus
}
 
```