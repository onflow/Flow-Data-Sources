# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/epoch/admin/set_automatic_rewards.cdc

```
import FlowEpoch from "FlowEpoch"

transaction(automaticRewardsEnabled: Bool) {
    prepare(signer: auth(BorrowValue) &Account) {
        let epochAdmin = signer.storage.borrow<&FlowEpoch.Admin>(from: FlowEpoch.adminStoragePath)
            ?? panic("Could not borrow admin from storage path")

        epochAdmin.updateAutomaticRewardsEnabled(automaticRewardsEnabled)
    }
}
```