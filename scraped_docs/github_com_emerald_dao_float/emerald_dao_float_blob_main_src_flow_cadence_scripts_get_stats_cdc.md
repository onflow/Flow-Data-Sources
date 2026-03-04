# Source: https://github.com/emerald-dao/float/blob/main/src/flow/cadence/scripts/get_stats.cdc

```
import "FLOAT"

access(all) fun main(): Result {
    return Result(FLOAT.totalSupply, FLOAT.totalFLOATEvents)
}

access(all) struct Result {
    access(all) let floatTotalSupply: UInt64
    access(all) let eventsCreated: UInt64

    init(_ f: UInt64, _ e: UInt64) {
        self.floatTotalSupply = f
        self.eventsCreated = e
    }
}
```