# Source: https://github.com/dapperlabs/nba-smart-contracts/blob/master/transactions/scripts/sets/get_setName.cdc

```
import TopShot from 0xTOPSHOTADDRESS

// This script gets the setName of a set with specified setID

// Parameters:
//
// setID: The unique ID for the set whose data needs to be read

// Returns: String
// Name of set with specified setID

access(all) fun main(setID: UInt32): String {

    let name = TopShot.getSetName(setID: setID)
        ?? panic("Could not find the specified set")
        
    return name
}
```