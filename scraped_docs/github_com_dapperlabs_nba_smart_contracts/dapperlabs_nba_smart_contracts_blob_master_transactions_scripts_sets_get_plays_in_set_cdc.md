# Source: https://github.com/dapperlabs/nba-smart-contracts/blob/master/transactions/scripts/sets/get_plays_in_set.cdc

```
import TopShot from 0xTOPSHOTADDRESS

// This script returns an array of the play IDs that are
// in the specified set

// Parameters:
//
// setID: The unique ID for the set whose data needs to be read

// Returns: [UInt32]
// Array of play IDs in specified set

access(all) fun main(setID: UInt32): [UInt32] {

    let plays = TopShot.getPlaysInSet(setID: setID)!

    return plays
}
```