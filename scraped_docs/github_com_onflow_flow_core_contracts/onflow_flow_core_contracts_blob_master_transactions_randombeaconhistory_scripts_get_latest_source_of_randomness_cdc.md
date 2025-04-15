# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/randomBeaconHistory/scripts/get_latest_source_of_randomness.cdc

```
import "RandomBeaconHistory"

access(all) fun main(): RandomBeaconHistory.RandomSource {
    return RandomBeaconHistory.sourceOfRandomness(
        atBlockHeight: getCurrentBlock().height - 1
    )
}

```