# Source: https://github.com/dapperlabs/nba-smart-contracts/blob/master/transactions/admin/transfer_admin.cdc

```
import TopShot from 0xTOPSHOTADDRESS
import TopshotAdminReceiver from 0xADMINRECEIVERADDRESS

// this transaction takes a TopShot Admin resource and 
// saves it to the account storage of the account
// where the contract is deployed

transaction {

    // Local variable for the topshot Admin object
    let adminRef: @TopShot.Admin

    prepare(acct: auth(LoadValue) &Account) {

        self.adminRef <- acct.storage.load<@TopShot.Admin>(from: /storage/TopShotAdmin)
            ?? panic("No topshot admin in storage")
    }

    execute {

        TopshotAdminReceiver.storeAdmin(newAdmin: <-self.adminRef)
        
    }
}
```