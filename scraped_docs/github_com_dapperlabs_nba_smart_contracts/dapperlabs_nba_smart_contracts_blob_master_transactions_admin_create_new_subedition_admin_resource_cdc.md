# Source: https://github.com/dapperlabs/nba-smart-contracts/blob/master/transactions/admin/create_new_subedition_admin_resource.cdc

```
import TopShot from 0xTOPSHOTADDRESS

// This transaction is for the admin to create a new subedition admin resource
// and store it in the top shot smart contract

transaction() {

    // Local variable for the topshot Admin object
    let adminRef: &TopShot.Admin

    prepare(acct: auth(BorrowValue) &Account) {

        // borrow a reference to the Admin resource in storage
        self.adminRef = acct.storage.borrow<&TopShot.Admin>(from: /storage/TopShotAdmin)
            ?? panic("Could not borrow a reference to the Admin resource")
    }

    execute {
        self.adminRef.createSubeditionAdminResource()
    }
}
```