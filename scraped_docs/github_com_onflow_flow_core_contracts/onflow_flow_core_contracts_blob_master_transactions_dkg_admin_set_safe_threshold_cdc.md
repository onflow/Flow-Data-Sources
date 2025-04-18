# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/dkg/admin/set_safe_threshold.cdc

```
import "FlowDKG"

transaction(newThresholdPercentage: UFix64?) {

    let dkgAdmin: &FlowDKG.Admin

    prepare(signer: auth(BorrowValue) &Account) {
        self.dkgAdmin = signer.storage.borrow<&FlowDKG.Admin>(from: FlowDKG.AdminStoragePath)
            ?? panic("Could not borrow DKG Admin reference")
    }

    execute {
        self.dkgAdmin.setSafeSuccessThreshold(newThresholdPercentage: newThresholdPercentage)
    }
}

```