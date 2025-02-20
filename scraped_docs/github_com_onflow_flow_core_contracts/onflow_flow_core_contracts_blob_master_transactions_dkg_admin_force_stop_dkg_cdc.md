# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/dkg/admin/force_stop_dkg.cdc

```
import "FlowDKG"

transaction {

    let dkgAdmin: &FlowDKG.Admin

    prepare(signer: auth(BorrowValue) &Account) {
        self.dkgAdmin = signer.storage.borrow<&FlowDKG.Admin>(from: FlowDKG.AdminStoragePath)
            ?? panic("Could not borrow DKG Admin reference")
    }

    execute {
        self.dkgAdmin.forceEndDKG()
    }
}

```