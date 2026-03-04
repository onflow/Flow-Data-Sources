# Source: https://github.com/Flowtyio/nft-catalog/blob/main/cadence/scripts/get_nft_catalog_proposals_count.cdc

```
import "NFTCatalog"

access(all) fun main(): Int {
    let proposals = NFTCatalog.getCatalogProposalKeys()
    return proposals.length
}
```