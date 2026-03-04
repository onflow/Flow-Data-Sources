# Source: https://github.com/Flowtyio/nft-catalog/blob/main/cadence/scripts/get_full_nft_catalog.cdc

```
import "NFTCatalog"

// NOT RECOMMENDED FOR USE.
// This is used for automated testing of the
// expected to be deprecated getCatalog.
access(all) fun main(): {String : NFTCatalog.NFTCatalogMetadata} {
    return NFTCatalog.getCatalog()
}

```