# Source: https://github.com/dapperlabs/nba-smart-contracts/blob/master/transactions/scripts/collections/get_moment_lockExpiry.cdc

```
import TopShot from 0xTOPSHOTADDRESS
import TopShotLocking from 0xTOPSHOTLOCKINGADDRESS

// This script gets the time at which a moment will be eligible for unlocking

// Parameters:
//
// account: The Flow Address of the account who owns the moment
// id: The unique ID for the moment

// Returns: UFix64
// The unix timestamp when the moment is unlockable

access(all) fun main(account: Address, id: UInt64): UFix64 {

    let collectionRef = getAccount(account).capabilities.borrow<&{TopShot.MomentCollectionPublic}>(/public/MomentCollection)
        ?? panic("Could not get public moment collection reference")

    let nftRef = collectionRef.borrowNFT(id)!

    return TopShotLocking.getLockExpiry(nftRef: nftRef)
}

```