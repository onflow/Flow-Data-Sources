# Source: https://github.com/fixes-world/token-list/blob/main/cadence/scripts/migration/get-valid-nft-collections-in-catalog.cdc

```
import "NFTCatalog"

access(all)
fun main(): [String] {
    let ret: [String] = []

    NFTCatalog.forEachCatalogKey(fun (key: String): Bool {
        if let metadata = NFTCatalog.getCatalogEntry(collectionIdentifier: key) {
            if !metadata.nftType.isRecovered {
                ret.append(metadata.nftType.identifier)
            }
        }
        return true
    })
    return ret
}

```