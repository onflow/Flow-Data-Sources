# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/nodeVersionBeacon/scripts/get_next_version_update_sequence.cdc

```
import NodeVersionBeacon from "NodeVersionBeacon"

/// Gets the next sequence number for the table updated event
access(all) fun main(): UInt64 {
    return NodeVersionBeacon.getNextVersionBeaconSequence()
}
```