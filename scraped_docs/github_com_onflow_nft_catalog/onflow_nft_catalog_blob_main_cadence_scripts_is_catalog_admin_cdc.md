# Source: https://github.com/onflow/nft-catalog/blob/main/cadence/scripts/is_catalog_admin.cdc

```
import "NFTCatalogAdmin"

access(all) fun main(ownerAddress: Address) : Bool {
    let owner = getAccount(ownerAddress)
    let proxyCap = owner.capabilities.get<&NFTCatalogAdmin.AdminProxy>(NFTCatalogAdmin.AdminProxyPublicPath)
    if !proxyCap.check() {
        return false
    }
    let proxyRef = proxyCap!.borrow()!
    return proxyRef.hasCapability()
}
```