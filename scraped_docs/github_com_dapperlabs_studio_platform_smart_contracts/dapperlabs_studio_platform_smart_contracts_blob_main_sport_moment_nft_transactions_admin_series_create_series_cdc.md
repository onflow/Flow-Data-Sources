# Source: https://github.com/dapperlabs/studio-platform-smart-contracts/blob/main/sport-moment-nft/transactions/admin/series/create_series.cdc

```
import DapperSport from "../../../contracts/DapperSport.cdc"

transaction(name: String) {
    // local variable for the admin reference
    let admin: &DapperSport.Admin

    prepare(signer: AuthAccount) {
        // borrow a reference to the Admin resource
        self.admin = signer.borrow<&DapperSport.Admin>(from: DapperSport.AdminStoragePath)
            ?? panic("Could not borrow a reference to the DapperSport Admin capability")
    }

    execute {
        let id = self.admin.createSeries(
            name: name,
        )

        log("====================================")
        log("New Series: ".concat(name))
        log("SeriesID: ".concat(id.toString()))
        log("====================================")
    }
}


```