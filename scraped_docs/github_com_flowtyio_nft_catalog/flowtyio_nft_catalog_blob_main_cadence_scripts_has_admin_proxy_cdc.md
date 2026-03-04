# Source: https://github.com/Flowtyio/nft-catalog/blob/main/cadence/scripts/has_admin_proxy.cdc

```
import "NFTCatalogAdmin"

access(all) fun main(ownerAddress: Address) : Bool {
    let owner = getAccount(ownerAddress)
    let proxyCap = owner.capabilities.get<&NFTCatalogAdmin.AdminProxy>(NFTCatalogAdmin.AdminProxyPublicPath)
    return proxyCap.check()
}
```