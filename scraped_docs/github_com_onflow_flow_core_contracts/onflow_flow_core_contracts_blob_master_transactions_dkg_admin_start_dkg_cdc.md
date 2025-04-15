# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/dkg/admin/start_dkg.cdc

```
import "FlowDKG"

transaction(nodeIDs: [String]) {

    let dkgAdmin: &FlowDKG.Admin

    prepare(signer: auth(BorrowValue) &Account) {
        self.dkgAdmin = signer.storage.borrow<&FlowDKG.Admin>(from: FlowDKG.AdminStoragePath)
            ?? panic("Could not borrow DKG Admin reference")
    }

    execute {
        self.dkgAdmin.startDKG(nodeIDs: nodeIDs)
    }
}

```