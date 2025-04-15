# Source: https://github.com/dapperlabs/nba-smart-contracts/blob/master/transactions/admin/unlock_all_moments.cdc

```
import TopShotLocking from 0xTOPSHOTLOCKINGADDRESS

transaction() {
    let adminRef: &TopShotLocking.Admin

    prepare(acct: auth(BorrowValue) &Account) {
        // Set TopShotLocking admin ref
        self.adminRef = acct.storage.borrow<&TopShotLocking.Admin>(from: /storage/TopShotLockingAdmin)
            ?? panic("Could not find reference to TopShotLocking Admin resource")
    }

    execute {
        self.adminRef.unlockAll()
    }
}

```