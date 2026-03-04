# Source: https://github.com/onflow/nft-catalog/blob/main/cadence/scripts/get_nft_catalog_proposal_ids.cdc

```
import "NFTCatalog"

access(all) fun main(): [UInt64] {
    return NFTCatalog.getCatalogProposalKeys()
}
```