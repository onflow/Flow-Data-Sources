# Source: https://github.com/dapperlabs/studio-platform-smart-contracts/blob/main/sport-moment-nft/transactions/admin/sets/lock_set.cdc

```
import DapperSport from "../../../contracts/DapperSport.cdc"

transaction(setID: UInt64) {
    // local variable for the admin reference
    let admin: &DapperSport.Admin

    prepare(signer: AuthAccount) {
        // borrow a reference to the Admin resource
        self.admin = signer.borrow<&DapperSport.Admin>(from: DapperSport.AdminStoragePath)
            ?? panic("Could not borrow a reference to the DapperSport Admin capability")
    }

    execute {
        let id = self.admin.lockSet(id: setID)

        log("====================================")
        log("Locked Set:")
        log("SetID: ".concat(id.toString()))
        log("====================================")
    }
}


```