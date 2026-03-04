# Source: https://github.com/onflow/nft-catalog/blob/main/cadence/scripts/get_nft_metadata_for_collection_identifier.cdc

```
import "NFTCatalog"

access(all) fun main(collectionIdentifier: String): NFTCatalog.NFTCatalogMetadata? {
    return NFTCatalog.getCatalogEntry(collectionIdentifier: collectionIdentifier)
}
```