# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/epoch/admin/update_clusters.cdc

```
import "FlowEpoch"

transaction(newNumClusters: UInt16) {
    prepare(signer: auth(BorrowValue) &Account) {

        let epochAdmin = signer.storage.borrow<&FlowEpoch.Admin>(from: FlowEpoch.adminStoragePath)
            ?? panic("Could not borrow admin from storage path")

        epochAdmin.updateNumCollectorClusters(newNumClusters)
    }
}
```