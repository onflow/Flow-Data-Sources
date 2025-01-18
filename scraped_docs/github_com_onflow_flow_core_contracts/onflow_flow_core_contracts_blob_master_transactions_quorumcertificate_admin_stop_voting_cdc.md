# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/quorumCertificate/admin/stop_voting.cdc

```
import FlowClusterQC from "FlowClusterQC"

// Test transaction for the QC contract to stop the voting period

transaction {

    prepare(signer: auth(BorrowValue) &Account) {
        let adminRef = signer.storage.borrow<&FlowClusterQC.Admin>(from: FlowClusterQC.AdminStoragePath)
            ?? panic("Could not borrow reference to qc admin")

        adminRef.stopVoting()
    }
}
```