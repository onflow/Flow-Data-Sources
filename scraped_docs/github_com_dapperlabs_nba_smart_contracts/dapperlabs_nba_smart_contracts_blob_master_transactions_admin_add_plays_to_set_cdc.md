# Source: https://github.com/dapperlabs/nba-smart-contracts/blob/master/transactions/admin/add_plays_to_set.cdc

```
import TopShot from 0xTOPSHOTADDRESS

// This transaction adds multiple plays to a set
		
// Parameters:
//
// setID: the ID of the set to which multiple plays are added
// plays: an array of play IDs being added to the set

transaction(setID: UInt32, plays: [UInt32]) {

    // Local variable for the topshot Admin object
    let adminRef: &TopShot.Admin

    prepare(acct: auth(BorrowValue) &Account) {

        // borrow a reference to the Admin resource in storage
        self.adminRef = acct.storage.borrow<&TopShot.Admin>(from: /storage/TopShotAdmin)!
    }

    execute {

        // borrow a reference to the set to be added to
        let setRef = self.adminRef.borrowSet(setID: setID)

        // Add the specified play IDs
        setRef.addPlays(playIDs: plays)
    }
}
```