# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/quorumCertificate/admin/publish_voter.cdc

```
import "FlowClusterQC"

// Test transaction for the QC admin to publish a reference
// that allows accounts to register for QC voting

transaction {

    prepare(signer: auth(Capabilities) &Account) {
        let adminCap = signer.capabilities.storage.issue<&FlowClusterQC.Admin>(FlowClusterQC.AdminStoragePath)
        signer.capabilities.publish(adminCap, at: /public/voterCreator)
    }
}

```