# Source: https://github.com/dapperlabs/nba-smart-contracts/blob/master/transactions/scripts/subeditions/get_all_subeditions.cdc

```
import TopShot from 0xTOPSHOTADDRESS

// This script returns an array of all the plays
// that have ever been created for Top Shot

// Returns: [TopShot.Play]
// array of all plays created for Topshot

access(all) fun main(): &[TopShot.Subedition] {

    return TopShot.getAllSubeditions()
}
```