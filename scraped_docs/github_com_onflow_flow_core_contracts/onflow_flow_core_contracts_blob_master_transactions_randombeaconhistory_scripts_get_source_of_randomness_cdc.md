# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/randomBeaconHistory/scripts/get_source_of_randomness.cdc

```
import "RandomBeaconHistory"

/// Retrieves the source of randomness for the requested block height from the RandomBeaconHistory contract.
///
access(all) fun main(atBlockHeight: UInt64): RandomBeaconHistory.RandomSource {
    return RandomBeaconHistory.sourceOfRandomness(atBlockHeight: atBlockHeight)
}

```