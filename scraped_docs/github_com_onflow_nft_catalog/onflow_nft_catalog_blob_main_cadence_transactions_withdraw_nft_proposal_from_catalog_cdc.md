# Source: https://github.com/onflow/nft-catalog/blob/main/cadence/transactions/withdraw_nft_proposal_from_catalog.cdc

```
import "NFTCatalog"

transaction(
    proposalID : UInt64
) {
    let nftCatalogProposalResourceRef : auth(NFTCatalog.ProposalActionOwner) &NFTCatalog.NFTCatalogProposalManager

    prepare(acct: auth(BorrowValue) &Account) {
        self.nftCatalogProposalResourceRef = acct.storage.borrow<auth(NFTCatalog.ProposalActionOwner) &NFTCatalog.NFTCatalogProposalManager>(from: NFTCatalog.ProposalManagerStoragePath)!
    }

    execute {
        let proposal = NFTCatalog.getCatalogProposalEntry(proposalID: proposalID)!
        
        self.nftCatalogProposalResourceRef.setCurrentProposalEntry(identifier : proposal.collectionIdentifier)
        NFTCatalog.withdrawNFTProposal(proposalID : proposalID)
        self.nftCatalogProposalResourceRef.setCurrentProposalEntry(identifier : nil)
    }
}
```