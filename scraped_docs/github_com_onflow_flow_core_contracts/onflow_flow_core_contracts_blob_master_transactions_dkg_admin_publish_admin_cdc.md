# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/dkg/admin/publish_admin.cdc

```
import "FlowDKG"

// This transaction is only for testing!
transaction {

    prepare(signer: auth(Capabilities) &Account) {
        let adminCap = signer.capabilities.storage.issue<&FlowDKG.Admin>(FlowDKG.AdminStoragePath)
        signer.capabilities.publish(adminCap, at: /public/dkgAdmin)
    }
}

```