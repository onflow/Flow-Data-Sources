# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/epoch/admin/advance_view.cdc

```
import "FlowEpoch"

transaction(phase: String) {
    prepare(signer: auth(BorrowValue) &Account) {
        let heartbeat = signer.storage.borrow<&FlowEpoch.Heartbeat>(from: FlowEpoch.heartbeatStoragePath)
            ?? panic("Could not borrow heartbeat from storage path")

        if phase == "EPOCHSETUP" {
            heartbeat.endStakingAuction()
        } else if phase == "EPOCHCOMMIT" {
            heartbeat.startEpochCommit()
        } else if phase == "ENDEPOCH" {
            heartbeat.endEpoch()
        } else if phase == "BLOCK" {
            heartbeat.advanceBlock()
        }
    }
}
```