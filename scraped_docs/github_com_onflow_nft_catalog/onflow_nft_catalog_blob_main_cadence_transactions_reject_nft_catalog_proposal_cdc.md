# Source: https://github.com/onflow/nft-catalog/blob/main/cadence/transactions/reject_nft_catalog_proposal.cdc

```
import "NFTCatalogAdmin"

transaction(proposalID : UInt64) {
    let adminProxyRef : auth(NFTCatalogAdmin.CatalogActions) &NFTCatalogAdmin.AdminProxy

    prepare(acct: auth(BorrowValue) &Account) {
        self.adminProxyRef = acct.storage.borrow<auth(NFTCatalogAdmin.CatalogActions) &NFTCatalogAdmin.AdminProxy>(from : NFTCatalogAdmin.AdminProxyStoragePath)!
    }

    execute {
        self.adminProxyRef.getCapability()!.borrow()!.rejectCatalogProposal(proposalID : proposalID)
    }
}
```