# Source: https://github.com/dapperlabs/nba-smart-contracts/blob/master/transactions/scripts/collections/get_locked_nfts_length.cdc

```
import TopShotLocking from 0xTOPSHOTLOCKINGADDRESS

// This script determines how many NFTs are locked in the Top Shot Locking contract

// Returns: Int
// The number of locked NFTs

access(all) fun main(): Int {
    return TopShotLocking.getLockedNFTsLength()
}

```