# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/epoch/admin/update_dkg_phase_views.cdc

```
import "FlowEpoch"

transaction(newPhaseViews: UInt64) {
    prepare(signer: auth(BorrowValue) &Account) {
        let epochAdmin = signer.storage.borrow<&FlowEpoch.Admin>(from: FlowEpoch.adminStoragePath)
            ?? panic("Could not borrow admin from storage path")

        epochAdmin.updateDKGPhaseViews(newPhaseViews)
    }
}
```