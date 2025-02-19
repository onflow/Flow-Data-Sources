# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/epoch/admin/update_epoch_timing_config.cdc

```
import "FlowEpoch"

transaction(duration: UInt64, refCounter: UInt64, refTimestamp: UInt64) {
    prepare(signer: auth(BorrowValue) &Account) {
        let epochAdmin = signer.storage.borrow<&FlowEpoch.Admin>(from: FlowEpoch.adminStoragePath)
            ?? panic("Could not borrow admin from storage path")

        let config = FlowEpoch.EpochTimingConfig(duration: duration, refCounter: refCounter, refTimestamp: refTimestamp)
        epochAdmin.updateEpochTimingConfig(config)
    }
}
```