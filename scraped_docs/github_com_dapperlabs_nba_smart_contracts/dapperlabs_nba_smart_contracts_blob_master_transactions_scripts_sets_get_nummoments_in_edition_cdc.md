# Source: https://github.com/dapperlabs/nba-smart-contracts/blob/master/transactions/scripts/sets/get_numMoments_in_edition.cdc

```
import TopShot from 0xTOPSHOTADDRESS

// This script returns the number of specified moments that have been
// minted for the specified edition

// Parameters:
//
// setID: The unique ID for the set whose data needs to be read
// playID: The unique ID for the play whose data needs to be read

// Returns: UInt32
// number of moments with specified playID minted for a set with specified setID

access(all) fun main(setID: UInt32, playID: UInt32): UInt32 {

    let numMoments = TopShot.getNumMomentsInEdition(setID: setID, playID: playID)
        ?? panic("Could not find the specified edition")

    return numMoments
}
```