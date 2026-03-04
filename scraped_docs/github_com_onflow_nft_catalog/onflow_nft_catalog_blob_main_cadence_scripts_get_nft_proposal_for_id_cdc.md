# Source: https://github.com/onflow/nft-catalog/blob/main/cadence/scripts/get_nft_proposal_for_id.cdc

```
import "NFTCatalog"

access(all) fun main(proposalID: UInt64): NFTCatalog.NFTCatalogProposal? {
    return NFTCatalog.getCatalogProposalEntry(proposalID: proposalID)
}
```