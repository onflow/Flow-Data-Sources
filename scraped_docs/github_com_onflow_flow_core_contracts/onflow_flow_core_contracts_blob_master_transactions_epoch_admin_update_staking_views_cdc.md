# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/epoch/admin/update_staking_views.cdc

```
import FlowEpoch from "FlowEpoch"

transaction(newStakingViews: UInt64) {
    prepare(signer: auth(BorrowValue) &Account) {
        let epochAdmin = signer.storage.borrow<&FlowEpoch.Admin>(from: FlowEpoch.adminStoragePath)
            ?? panic("Could not borrow admin from storage path")

        epochAdmin.updateAuctionViews(newStakingViews)
    }
}
```