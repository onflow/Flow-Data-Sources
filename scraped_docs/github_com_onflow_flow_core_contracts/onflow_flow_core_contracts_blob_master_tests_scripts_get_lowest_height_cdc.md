# Source: https://github.com/onflow/flow-core-contracts/blob/master/tests/scripts/get_lowest_height.cdc

```
import "RandomBeaconHistory"

access(all) fun main(): UInt64 {
    return RandomBeaconHistory.getLowestHeight()
}

```