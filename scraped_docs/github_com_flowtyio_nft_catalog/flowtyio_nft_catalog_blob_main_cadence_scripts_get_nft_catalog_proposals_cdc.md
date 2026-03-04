# Source: https://github.com/Flowtyio/nft-catalog/blob/main/cadence/scripts/get_nft_catalog_proposals.cdc

```
import "NFTCatalog"

access(all) fun main(proposalIDs: [UInt64]): {UInt64 : NFTCatalog.NFTCatalogProposal} {
    var data : {UInt64 : NFTCatalog.NFTCatalogProposal}  = {}
    for proposalID in proposalIDs {
        assert(NFTCatalog.getCatalogProposalEntry(proposalID: proposalID) != nil, message: "Invalid Proposal ID")
         data.insert(key: proposalID, NFTCatalog.getCatalogProposalEntry(proposalID: proposalID)!)
    }

    return data
}
```