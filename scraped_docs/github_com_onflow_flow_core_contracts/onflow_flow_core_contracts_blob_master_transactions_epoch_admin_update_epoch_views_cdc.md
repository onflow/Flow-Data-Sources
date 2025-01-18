# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/epoch/admin/update_epoch_views.cdc

```
import FlowEpoch from "FlowEpoch"

transaction(newAuctionViews: UInt64) {
    prepare(signer: auth(BorrowValue) &Account) {
        let epochAdmin = signer.storage.borrow<&FlowEpoch.Admin>(from: FlowEpoch.adminStoragePath)
            ?? panic("Could not borrow admin from storage path")

        epochAdmin.updateEpochViews(newAuctionViews)
    }
}
```