# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/epoch/admin/calculate_rewards.cdc

```
import "FlowEpoch"
import "FlowIDTableStaking"

transaction() {
    prepare(signer: auth(BorrowValue) &Account) {
        let heartbeat = signer.storage.borrow<&FlowEpoch.Heartbeat>(from: FlowEpoch.heartbeatStoragePath)
            ?? panic("Could not borrow heartbeat from storage path")

        heartbeat.calculateAndSetRewards()
    }
}
```