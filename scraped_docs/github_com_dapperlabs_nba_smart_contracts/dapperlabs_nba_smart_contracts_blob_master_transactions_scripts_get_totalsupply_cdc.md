# Source: https://github.com/dapperlabs/nba-smart-contracts/blob/master/transactions/scripts/get_totalSupply.cdc

```
import TopShot from 0xTOPSHOTADDRESS

// This script reads the current number of moments that have been minted
// from the TopShot contract and returns that number to the caller

// Returns: UInt64
// Number of moments minted from TopShot contract

access(all) fun main(): UInt64 {

    return TopShot.totalSupply
}
```