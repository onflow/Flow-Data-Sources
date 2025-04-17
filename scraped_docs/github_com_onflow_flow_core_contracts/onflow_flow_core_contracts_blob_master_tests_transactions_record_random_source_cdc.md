# Source: https://github.com/onflow/flow-core-contracts/blob/master/tests/transactions/record_random_source.cdc

```
import "RandomBeaconHistory"

transaction(randomSource: [UInt8]) {
    prepare(acct: auth(BorrowValue) &Account) {
        let heartbeat = acct.storage.borrow<&RandomBeaconHistory.Heartbeat>(
            from: RandomBeaconHistory.HeartbeatStoragePath
        ) ?? panic("Could not borrow heartbeat resource")

        heartbeat.heartbeat(randomSourceHistory: randomSource)
    }
}

```