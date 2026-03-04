# Source: https://github.com/onflow/random-coin-toss/blob/main/scripts/test/next_uint64.cdc

```
import "Xorshift128plus"

/// Returns a random number from a Xorshift128plus.PRG struct constructed from the given seed and salt.
///
/// Note that if the PRG were stored onchain, this script would not advance the state of the PRG
///
access(all) fun main(sourceOfRandomness: [UInt8], salt: [UInt8]): UInt64 {
    return Xorshift128plus.PRG(sourceOfRandomness: sourceOfRandomness, salt: salt).nextUInt64()
}

```