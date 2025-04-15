# Source: https://github.com/dapperlabs/nba-smart-contracts/blob/master/transactions/scripts/subeditions/get_nextSubeditionID.cdc

```
import TopShot from 0xTOPSHOTADDRESS

// This script reads the nextSubeditionID from the SubeditionAdmin resource and
// returns that number to the caller

// Returns: UInt32
// the next number in nextSubeditionID from the SubeditionAdmin resource

access(all) fun main(): UInt32 {

    return TopShot.getNextSubeditionID()
}
```