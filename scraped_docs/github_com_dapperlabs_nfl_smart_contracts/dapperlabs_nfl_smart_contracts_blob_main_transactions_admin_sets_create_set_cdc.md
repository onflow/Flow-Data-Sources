# Source: https://github.com/dapperlabs/nfl-smart-contracts/blob/main/transactions/admin/sets/create_set.cdc

```
import AllDay from "AllDay"

transaction(name: String) {
    // local variable for the admin reference
    let admin: auth(AllDay.Operate) &AllDay.Admin

    prepare(signer: auth(BorrowValue) &Account) {
        // borrow a reference to the Admin resource
        self.admin = signer.storage.borrow<auth(AllDay.Operate) &AllDay.Admin>(from: AllDay.AdminStoragePath)
            ?? panic("Could not borrow a reference to the AllDay Admin capability")
    }

    execute {
        let id = self.admin.createSet(
            name: name,
        )

        log("====================================")
        log("New Set: ".concat(name))
        log("SetID: ".concat(id.toString()))
        log("====================================")
    }
}


```